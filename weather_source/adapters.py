from __future__ import annotations

import base64
import ftplib
import hashlib
import json
import os
import re
import ssl
import subprocess
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

import requests


USER_AGENT = "weather-source/0.1 (+https://github.com/f2re/weather_source)"
ENV_RE = re.compile(r"\$\{([A-Z0-9_]+)\}")
UTC_RE = re.compile(r"\{utc:([^}]+)\}")


class FetchError(RuntimeError):
    pass


@dataclass
class FetchResult:
    source_id: str
    adapter: str
    url: str | None
    path: Path | None
    bytes_written: int
    metadata: dict[str, Any]


class _LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        for key, value in attrs:
            if key.lower() == "href" and value:
                self.hrefs.append(value)


def render(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: render(item) for key, item in value.items()}
    if isinstance(value, list):
        return [render(item) for item in value]
    if not isinstance(value, str):
        return value

    now = datetime.now(timezone.utc)
    value = UTC_RE.sub(lambda match: now.strftime(match.group(1)), value)

    def env_sub(match: re.Match[str]) -> str:
        name = match.group(1)
        if name not in os.environ:
            raise FetchError(f"Не задана переменная окружения {name}")
        return os.environ[name]

    return ENV_RE.sub(env_sub, value)


def _write_bytes(source_id: str, data: bytes, output: Path | None, suggested_name: str) -> Path:
    if output is None:
        output = Path("downloads") / source_id / suggested_name
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(data)
    return output


def _finalize(result: FetchResult) -> FetchResult:
    """Write a reproducibility sidecar for every payload that exists on disk."""
    path = result.path
    if path is None or not path.is_file():
        return result
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    metadata = {
        "source_id": result.source_id,
        "adapter": result.adapter,
        "url": result.url,
        "received_at": datetime.now(timezone.utc).isoformat(),
        "path": str(path),
        "bytes": path.stat().st_size,
        "sha256": digest,
        "transport_metadata": result.metadata,
    }
    sidecar = path.with_name(path.name + ".metadata.json")
    sidecar.write_text(json.dumps(metadata, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")
    result.bytes_written = path.stat().st_size
    result.metadata = {**result.metadata, "sha256": digest, "metadata_path": str(sidecar)}
    return result


def _bounded_get(
    url: str,
    *,
    params: dict[str, Any] | None = None,
    headers: dict[str, str] | None = None,
    timeout: float,
    max_bytes: int | None,
) -> requests.Response:
    merged_headers = {"User-Agent": USER_AGENT, "Accept-Encoding": "identity"}
    if headers:
        merged_headers.update(headers)
    response = requests.get(url, params=params, headers=merged_headers, timeout=timeout, stream=True)
    response.raise_for_status()
    if max_bytes is not None:
        length = response.headers.get("Content-Length")
        if length and int(length) > max_bytes:
            response.close()
            raise FetchError(
                f"Файл {length} байт превышает безопасный предел {max_bytes}. "
                "Повторите с --full, если действительно хотите скачать весь продукт."
            )
    return response


def fetch_http(source_id: str, recipe: dict[str, Any], output: Path | None, timeout: float, full: bool) -> FetchResult:
    req = render(recipe["request"])
    url = req["url"]
    max_bytes = None if full else int(req.get("max_bytes", 8 * 1024 * 1024))
    response = _bounded_get(
        url,
        params=req.get("params"),
        headers=req.get("headers"),
        timeout=timeout,
        max_bytes=max_bytes,
    )
    try:
        content = response.content
        final_url = response.url
        content_type = response.headers.get("Content-Type", "")
    finally:
        response.close()

    follow_field = req.get("follow_json_field")
    if follow_field:
        try:
            payload = json.loads(content)
            follow_url: Any = payload
            for part in follow_field.split("."):
                follow_url = follow_url[part]
            if not isinstance(follow_url, str):
                raise TypeError("field is not string")
        except Exception as exc:  # noqa: BLE001
            raise FetchError(f"Не удалось извлечь URL из JSON-поля {follow_field}: {exc}") from exc
        response = _bounded_get(follow_url, timeout=timeout, max_bytes=max_bytes)
        try:
            content = response.content
            final_url = response.url
            content_type = response.headers.get("Content-Type", "")
        finally:
            response.close()

    if max_bytes is not None and len(content) > max_bytes:
        raise FetchError(f"Ответ превысил безопасный предел {max_bytes}; используйте --full")

    suggested = req.get("filename") or Path(final_url.split("?", 1)[0]).name or "response.bin"
    if "json" in content_type and not suggested.endswith(".json"):
        suggested += ".json"
    path = _write_bytes(source_id, content, output, suggested)
    return FetchResult(source_id, "http", final_url, path, len(content), {"content_type": content_type})


def fetch_html_latest(source_id: str, recipe: dict[str, Any], output: Path | None, timeout: float, full: bool) -> FetchResult:
    req = render(recipe["request"])
    index_url = req["url"]
    response = requests.get(index_url, headers={"User-Agent": USER_AGENT}, timeout=timeout)
    response.raise_for_status()
    parser = _LinkParser()
    parser.feed(response.text)
    pattern = re.compile(req.get("pattern", ".*"))
    matches = sorted(href for href in parser.hrefs if pattern.search(href) and not href.endswith("/"))
    if not matches:
        raise FetchError(f"В каталоге {index_url} не найден файл по шаблону {pattern.pattern}")
    chosen = matches[-1]
    direct = urljoin(index_url.rstrip("/") + "/", chosen)
    nested = dict(recipe)
    nested["request"] = {"url": direct, "max_bytes": req.get("max_bytes", 8 * 1024 * 1024)}
    result = fetch_http(source_id, nested, output, timeout, full)
    result.adapter = "html_latest"
    result.metadata["index_url"] = index_url
    return result


def fetch_ftp(source_id: str, recipe: dict[str, Any], output: Path | None, timeout: float, full: bool) -> FetchResult:
    req = render(recipe["request"])
    host = req["host"]
    remote_path = req["path"]
    user = req.get("user", "anonymous")
    password = req.get("password", "weather-source@example.invalid")
    max_bytes = None if full else int(req.get("max_bytes", 8 * 1024 * 1024))
    chunks: list[bytes] = []
    total = 0

    with ftplib.FTP(host, timeout=timeout) as ftp:
        ftp.login(user=user, passwd=password)
        try:
            size = ftp.size(remote_path)
        except ftplib.all_errors:
            size = None
        if size and max_bytes is not None and size > max_bytes:
            raise FetchError(f"FTP-файл {size} байт превышает безопасный предел {max_bytes}; используйте --full")

        def collect(chunk: bytes) -> None:
            nonlocal total
            total += len(chunk)
            if max_bytes is not None and total > max_bytes:
                raise FetchError(f"FTP-поток превысил безопасный предел {max_bytes}; используйте --full")
            chunks.append(chunk)

        ftp.retrbinary(f"RETR {remote_path}", collect)

    data = b"".join(chunks)
    path = _write_bytes(source_id, data, output, Path(remote_path).name or "ftp.bin")
    return FetchResult(source_id, "ftp", f"ftp://{host}/{remote_path.lstrip('/')}", path, len(data), {"reported_size": size})


def _s3_list(bucket: str, prefix: str, timeout: float, endpoint: str | None = None) -> list[tuple[str, str, int]]:
    base = endpoint or f"https://{bucket}.s3.amazonaws.com"
    response = requests.get(
        base,
        params={"list-type": "2", "prefix": prefix, "max-keys": 1000},
        headers={"User-Agent": USER_AGENT},
        timeout=timeout,
    )
    response.raise_for_status()
    root = ET.fromstring(response.content)
    ns = {"s3": "http://s3.amazonaws.com/doc/2006-03-01/"}
    result: list[tuple[str, str, int]] = []
    for node in root.findall("s3:Contents", ns):
        key = node.findtext("s3:Key", default="", namespaces=ns)
        modified = node.findtext("s3:LastModified", default="", namespaces=ns)
        size = int(node.findtext("s3:Size", default="0", namespaces=ns))
        result.append((key, modified, size))
    return result


def fetch_s3_latest(source_id: str, recipe: dict[str, Any], output: Path | None, timeout: float, full: bool) -> FetchResult:
    req = render(recipe["request"])
    bucket = req["bucket"]
    prefix = req.get("prefix", "")
    endpoint = req.get("endpoint")
    suffix = req.get("suffix")
    objects = _s3_list(bucket, prefix, timeout, endpoint)
    if suffix:
        objects = [item for item in objects if item[0].endswith(suffix)]
    if not objects:
        raise FetchError(f"В s3://{bucket}/{prefix} не найден подходящий объект")
    key, modified, size = max(objects, key=lambda item: item[1])
    max_bytes = None if full else int(req.get("max_bytes", 8 * 1024 * 1024))
    if max_bytes is not None and size > max_bytes:
        raise FetchError(
            f"Последний объект s3://{bucket}/{key} имеет {size} байт; "
            "используйте --full для загрузки полного продукта."
        )
    base = endpoint or f"https://{bucket}.s3.amazonaws.com"
    direct = f"{base.rstrip('/')}/{key}"
    nested = dict(recipe)
    nested["request"] = {"url": direct, "max_bytes": max_bytes or size + 1}
    result = fetch_http(source_id, nested, output, timeout, full)
    result.adapter = "s3_latest"
    result.metadata.update({"bucket": bucket, "key": key, "last_modified": modified, "size": size})
    return result


def _decode_inline_wis2(content: dict[str, Any]) -> bytes | None:
    value = content.get("value")
    if value is None:
        return None
    if isinstance(value, bytes):
        return value
    if not isinstance(value, str):
        return json.dumps(value, ensure_ascii=False).encode("utf-8")
    encoding = str(content.get("encoding", "utf-8")).lower()
    if encoding in {"base64", "base64url"}:
        padding = "=" * (-len(value) % 4)
        try:
            if encoding == "base64url":
                return base64.urlsafe_b64decode(value + padding)
            return base64.b64decode(value + padding)
        except Exception as exc:  # noqa: BLE001
            raise FetchError(f"Не удалось декодировать inline WIS2 content.value: {exc}") from exc
    return value.encode("utf-8")


def fetch_wis2(source_id: str, recipe: dict[str, Any], output: Path | None, timeout: float, full: bool) -> FetchResult:
    try:
        import paho.mqtt.client as mqtt
    except ImportError as exc:
        raise FetchError("Для WIS2 установите paho-mqtt: pip install paho-mqtt") from exc

    req = render(recipe["request"])
    broker = req["broker"]
    port = int(req.get("port", 8883))
    topic = req["topic"]
    username = req.get("username", "everyone")
    password = req.get("password", "everyone")
    received: dict[str, Any] = {}

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.username_pw_set(username, password)
    client.tls_set(cert_reqs=ssl.CERT_REQUIRED)

    def on_connect(client: Any, userdata: Any, flags: Any, reason_code: Any, properties: Any) -> None:
        if int(reason_code) != 0:
            received["error"] = f"MQTT connect failed: {reason_code}"
            return
        client.subscribe(topic, qos=1)

    def on_message(client: Any, userdata: Any, message: Any) -> None:
        try:
            payload = json.loads(message.payload.decode("utf-8"))
            links = payload.get("links", [])
            href = next(
                (
                    item.get("href")
                    for item in links
                    if item.get("rel") in {"canonical", "update"} and str(item.get("href", "")).startswith("http")
                ),
                None,
            )
            inline = _decode_inline_wis2(payload.get("content", {}))
            if href or inline is not None:
                received.update({"href": href, "inline": inline, "notification": payload, "topic": message.topic})
                client.disconnect()
        except Exception as exc:  # noqa: BLE001
            received["error"] = str(exc)
            client.disconnect()

    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port, keepalive=max(30, int(timeout)))
    client.loop_start()
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline and not any(key in received for key in ("href", "inline", "error")):
        time.sleep(0.1)
    client.loop_stop()
    try:
        client.disconnect()
    except Exception:  # noqa: BLE001
        pass

    if "error" in received:
        raise FetchError(received["error"])
    if not any(key in received for key in ("href", "inline")):
        raise FetchError(f"За {timeout:g} с по теме {topic} не получено WIS2-уведомление с payload")

    max_bytes = None if full else int(req.get("max_bytes", 8 * 1024 * 1024))
    if received.get("inline") is not None:
        data = received["inline"]
        if max_bytes is not None and len(data) > max_bytes:
            raise FetchError(f"Inline WIS2 payload {len(data)} байт превышает предел {max_bytes}; используйте --full")
        path = _write_bytes(source_id, data, output, req.get("filename", "wis2-inline.bin"))
        return FetchResult(
            source_id,
            "wis2",
            None,
            path,
            len(data),
            {"broker": broker, "topic": received["topic"], "notification": received["notification"], "inline": True},
        )

    nested = dict(recipe)
    nested["request"] = {"url": received["href"], "max_bytes": req.get("max_bytes", 8 * 1024 * 1024)}
    result = fetch_http(source_id, nested, output, timeout, full)
    result.adapter = "wis2"
    result.metadata.update({"broker": broker, "topic": received["topic"], "notification": received["notification"], "inline": False})
    return result


def fetch_amqp(source_id: str, recipe: dict[str, Any], output: Path | None, timeout: float, full: bool) -> FetchResult:
    try:
        import pika
    except ImportError as exc:
        raise FetchError("Для AMQP установите pika: pip install pika") from exc

    req = render(recipe["request"])
    url = req["url"]
    exchange = req.get("exchange", "xpublic")
    topic = req["topic"]
    received: dict[str, Any] = {}

    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    queue = channel.queue_declare(queue="", exclusive=True, auto_delete=True)
    queue_name = queue.method.queue
    channel.queue_bind(exchange=exchange, queue=queue_name, routing_key=topic)

    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        method, properties, body = channel.basic_get(queue_name, auto_ack=True)
        if method:
            received = {"routing_key": method.routing_key, "body": body}
            break
        connection.process_data_events(time_limit=0.25)
    connection.close()

    if not received:
        raise FetchError(f"За {timeout:g} с по AMQP-теме {topic} сообщений не получено")

    body = received["body"]
    filename = req.get("filename", "amqp-message.bin")
    path = _write_bytes(source_id, body, output, filename)
    return FetchResult(source_id, "amqp", url, path, len(body), {"routing_key": received["routing_key"]})


def fetch_external(source_id: str, recipe: dict[str, Any], output: Path | None, timeout: float, full: bool, allow_external: bool) -> FetchResult:
    command = render(recipe["request"]["command"])
    if not allow_external:
        raise FetchError(
            "Источник использует официальный внешний клиент. Команда подготовлена, но её запуск требует "
            "--allow-external:\n" + command
        )
    env = os.environ.copy()
    if output is not None:
        env["WEATHER_SOURCE_OUTPUT"] = str(output)
    completed = subprocess.run(command, shell=True, env=env, timeout=timeout, check=False)
    if completed.returncode != 0:
        raise FetchError(f"Внешний клиент завершился с кодом {completed.returncode}")
    return FetchResult(source_id, "external", None, output, 0, {"command": command, "returncode": 0})


def fetch_unavailable(source_id: str, recipe: dict[str, Any]) -> FetchResult:
    reason = recipe.get("reason_ru") or "Публичный машиночитаемый канал для этого источника не подтверждён."
    fallback = recipe.get("fallback")
    if fallback:
        reason += f" Рекомендуемый резерв: {fallback}."
    raise FetchError(reason)


def fetch(
    source_id: str,
    recipe: dict[str, Any],
    *,
    output: Path | None = None,
    timeout: float = 30.0,
    full: bool = False,
    allow_external: bool = False,
) -> FetchResult:
    adapter = recipe["adapter"]
    if adapter == "http":
        result = fetch_http(source_id, recipe, output, timeout, full)
    elif adapter == "html_latest":
        result = fetch_html_latest(source_id, recipe, output, timeout, full)
    elif adapter == "ftp":
        result = fetch_ftp(source_id, recipe, output, timeout, full)
    elif adapter == "s3_latest":
        result = fetch_s3_latest(source_id, recipe, output, timeout, full)
    elif adapter == "wis2":
        result = fetch_wis2(source_id, recipe, output, timeout, full)
    elif adapter == "amqp":
        result = fetch_amqp(source_id, recipe, output, timeout, full)
    elif adapter == "external":
        result = fetch_external(source_id, recipe, output, timeout, full, allow_external)
    elif adapter == "unavailable":
        return fetch_unavailable(source_id, recipe)
    else:
        raise FetchError(f"Неизвестный adapter={adapter}")
    return _finalize(result)


def probe(recipe: dict[str, Any], timeout: float = 12.0) -> tuple[bool, str]:
    try:
        req = render(recipe.get("probe", {}))
    except FetchError:
        # A probe must remain possible even when the full retrieval needs a secret.
        req = recipe.get("probe", {})
    url = req.get("url")
    if not url:
        if recipe["adapter"] == "unavailable":
            return False, recipe.get("reason_ru", "нет публичного probe endpoint")
        return True, "probe не задан; runtime-рецепт проверяется статически"
    try:
        response = requests.get(
            url,
            params=req.get("params"),
            headers={"User-Agent": USER_AGENT, **req.get("headers", {})},
            timeout=timeout,
            stream=True,
            allow_redirects=True,
        )
        status = response.status_code
        response.close()
        ok_statuses = set(req.get("ok_statuses", [200, 201, 202, 204, 206]))
        return status in ok_statuses, f"HTTP {status} {url}"
    except requests.RequestException as exc:
        return False, f"{type(exc).__name__}: {exc}"
