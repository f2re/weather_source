#!/usr/bin/env python3
"""Generate human-readable and agent-readable catalogue artifacts.

The YAML files under catalog/ are the source of truth. This generator produces
committable documentation and machine indexes so that GitHub readers and AI
agents can use the repository without running any build step first.
"""
from __future__ import annotations

import argparse
import json
import shutil
import tempfile
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from catalog_lib import DEFAULT_CATALOG, REPO_ROOT, load_catalog, public_source

DOCS_SOURCES = REPO_ROOT / "docs" / "sources"
GENERATED_DIR = DOCS_SOURCES / "generated"
CATEGORIES_DIR = DOCS_SOURCES / "categories"

CATEGORY_RU = {
    "surface": "Наземные наблюдения",
    "upper-air": "Аэрология и верхняя атмосфера",
    "aircraft": "Авиационные наблюдения",
    "satellite": "Спутниковые данные",
    "radar": "Метеорологические радары",
    "nwp": "Численные модели прогноза",
    "metadata": "Метаданные",
    "climate": "Климат и архивы",
    "marine": "Морские наблюдения",
    "ocean": "Океанографические данные",
    "ensemble": "Ансамблевые прогнозы",
    "lightning": "Грозопеленгация и молнии",
    "gnss-ro": "GNSS radio occultation",
    "profilers": "Профайлеры",
    "reanalysis": "Реанализ",
    "precipitation": "Осадки",
    "api": "API и агрегаторы",
}

TIER_RU = {
    "primary": "основной",
    "secondary": "резервный/региональный",
    "specialized": "специализированный",
    "aggregator": "агрегатор",
}

ACCESS_RU = {
    "open": "открытый без регистрации",
    "registration": "бесплатный после регистрации",
    "free-tier": "бесплатный тариф с квотами",
    "restricted": "ограниченный доступ",
}

LEVEL_ICON = {
    "primary": "🟢",
    "secondary": "🟡",
    "specialized": "🔵",
    "aggregator": "⚪",
}

FORMAT_DECODER_HINTS = {
    "BUFR": "ecCodes / pybufrkit",
    "GRIB": "ecCodes / wgrib2 / cfgrib",
    "GRIB2": "ecCodes / wgrib2 / cfgrib",
    "NetCDF": "xarray / netCDF4",
    "HDF5": "h5py / xarray",
    "ODIM HDF5": "wradlib / h5py",
    "GeoTIFF": "GDAL / rasterio",
    "JSON": "requests + stdlib json",
    "GeoJSON": "requests / geopandas",
    "CSV": "pandas / csv",
    "XML": "lxml / ElementTree",
    "GML": "OWSLib / GDAL",
}


def md_link(label: str, url: str) -> str:
    return f"[{label}]({url})"


def esc_cell(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def localized_category(category: str) -> str:
    return CATEGORY_RU.get(category, category)


def endpoint_link(endpoint: dict[str, Any]) -> str:
    url = str(endpoint["url"])
    return md_link("открыть / open", url) if url.startswith(("http://", "https://")) else f"`{url}`"


def decoder_hints(formats: list[str]) -> list[str]:
    result: list[str] = []
    for fmt in formats:
        for prefix, tool in FORMAT_DECODER_HINTS.items():
            if fmt == prefix or fmt.startswith(prefix):
                if tool not in result:
                    result.append(tool)
    return result


def ingestion_recipe_ru(source: dict[str, Any]) -> list[str]:
    protocols = set(source["protocols"])
    steps: list[str] = []
    if "wis2" in protocols or "mqtt" in protocols:
        steps.append("Подписаться на нужную WIS2/MQTT-тему, принимать уведомления и скачивать payload по canonical/cache HTTPS-ссылке.")
    elif "amqp" in protocols:
        steps.append("Подключиться к AMQP-уведомлениям и получать новые файлы событийно, без постоянного polling.")
    elif "s3" in protocols:
        steps.append("Использовать S3/object-storage API: листинг по префиксу продукта и времени, затем скачивание только новых объектов.")
    elif protocols.intersection({"wfs", "wcs", "wms", "ogc-api"}):
        steps.append("Использовать OGC API/WFS/WCS для численных данных; WMS применять главным образом для визуализации.")
    elif protocols.intersection({"rest", "api"}):
        steps.append("Работать через официальный API с явными параметрами времени, области и продукта; соблюдать квоты и rate limit.")
    else:
        steps.append("Забирать данные напрямую с официального HTTPS/FTP-файлового дерева, не парся HTML-визуализатор.")

    steps.append("Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.")
    hints = decoder_hints(source["formats"])
    if hints:
        steps.append(f"Декодировать нативный формат стандартными средствами: {', '.join(hints)}.")
    else:
        steps.append("Декодировать нативный формат специализированным клиентом из раздела ПО; нормализацию выполнять поверх raw-данных.")
    steps.append("Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.")
    return steps


def ingestion_recipe_en(source: dict[str, Any]) -> list[str]:
    protocols = set(source["protocols"])
    steps: list[str] = []
    if "wis2" in protocols or "mqtt" in protocols:
        steps.append("Subscribe to the required WIS2/MQTT topic, consume notifications, then download payloads from canonical/cache HTTPS links.")
    elif "amqp" in protocols:
        steps.append("Consume AMQP notifications and fetch new products event-by-event instead of continuously polling directories.")
    elif "s3" in protocols:
        steps.append("Use the S3/object-storage API, list objects by product/time prefix and download only unseen objects.")
    elif protocols.intersection({"wfs", "wcs", "wms", "ogc-api"}):
        steps.append("Use OGC API/WFS/WCS for data values; treat WMS primarily as a presentation service.")
    elif protocols.intersection({"rest", "api"}):
        steps.append("Use the official API with explicit product/time/area parameters and respect quotas and rate limits.")
    else:
        steps.append("Fetch the official HTTPS/FTP file tree directly; do not scrape rendered product viewers.")

    steps.append("Preserve the raw payload together with receive time, source URL/product identifier and checksum.")
    hints = decoder_hints(source["formats"])
    if hints:
        steps.append(f"Decode native payloads with standards-aware tools such as {', '.join(hints)}.")
    else:
        steps.append("Use a provider-specific client from the software section and keep normalization additive to the raw archive.")
    steps.append("Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.")
    return steps


def render_source(source: dict[str, Any]) -> str:
    name = source["name"]
    categories_ru = ", ".join(localized_category(x) for x in source["categories"])
    categories_en = ", ".join(source["categories"])
    formats = ", ".join(f"`{x}`" for x in source["formats"])
    protocols = ", ".join(f"`{x}`" for x in source["protocols"])
    tier_ru = TIER_RU.get(source["tier"], source["tier"])
    access_ru = ACCESS_RU.get(source["access"]["level"], source["access"]["level"])

    lines = [
        f"# {name['ru']} / {name['en']}",
        "",
        "> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.",
        "",
        f"`{source['id']}` · {LEVEL_ICON.get(source['tier'], '')} **{tier_ru} / {source['tier']}** · "
        f"{'оперативный / operational' if source['operational'] else 'неоперативный / non-operational'} · "
        f"проверено / verified **{source['last_verified']}**",
        "",
        "---",
        "",
        "## 🇷🇺 Русский",
        "",
        "### Что это",
        "",
        source["summary"]["ru"],
        "",
        f"**Поставщик:** {source['provider']}  ",
        f"**Статус:** {'официальный источник' if source['official'] else 'неофициальный/агрегированный источник'}; приоритет — **{tier_ru}**.  ",
        f"**Категории:** {categories_ru}.  ",
        "",
        "### Что можно получить и когда использовать",
        "",
        source["notes"]["ru"],
        "",
        "Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. "
        "Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.",
        "",
        "### Операционные характеристики",
        "",
        "| Параметр | Значение |",
        "|---|---|",
        f"| Географическое покрытие | {esc_cell(source['coverage'])} |",
        f"| Периодичность/режим обновления | {esc_cell(source['update_cadence'])} |",
        f"| Типичная задержка | {esc_cell(source['typical_latency'])} |",
        f"| Архив | {esc_cell(source['archive'])} |",
        f"| Надёжность | `{source['reliability']}` |",
        f"| Удобство автоматизации | `{source['automation']}` |",
        f"| Протоколы | {protocols} |",
        f"| Форматы | {formats} |",
        "",
        "### Доступ и ограничения",
        "",
        f"- **Уровень доступа:** {access_ru} (`{source['access']['level']}`).",
        f"- **Авторизация:** {source['access']['auth']}.",
        f"- **Лицензия/условия:** {source['access']['terms']}.",
        "",
        "### Точки доступа",
        "",
        "| Endpoint | Протокол | Назначение | Health-check | URL |",
        "|---|---|---|---:|---|",
    ]
    for endpoint in source["endpoints"]:
        lines.append(
            f"| {esc_cell(endpoint['name'])} | `{endpoint['protocol']}` | {esc_cell(endpoint['role'])} | "
            f"{'да' if endpoint['healthcheck'] else 'нет'} | {endpoint_link(endpoint)} |"
        )

    lines += ["", "### ПО, библиотеки и декодеры", ""]
    if source["software"]:
        for item in source["software"]:
            lines.append(f"- {md_link(item['name'], item['url'])} — {item['role']}.")
    else:
        lines.append("- Специализированный клиент в каталоге пока не зафиксирован; использовать стандартный клиент протокола и декодер формата.")

    hints = decoder_hints(source["formats"])
    if hints:
        lines.append(f"- **Быстрый выбор декодера по формату:** {', '.join(hints)}.")

    lines += ["", "### Рекомендуемый алгоритм автоматического приёма", ""]
    for idx, step in enumerate(ingestion_recipe_ru(source), start=1):
        lines.append(f"{idx}. {step}")

    lines += [
        "",
        "### Официальная документация",
        "",
    ]
    for url in source["documentation"]:
        lines.append(f"- {md_link(url, url)}")

    lines += [
        "",
        "### Для ИИ-агента",
        "",
        f"- Источник истины для этой карточки: `{source.get('_catalog_file', '')}` → `id: {source['id']}`.",
        f"- Для оперативного контура учитывать: `tier={source['tier']}`, `operational={str(source['operational']).lower()}`, "
        f"`access.level={source['access']['level']}`, `automation={source['automation']}`, `reliability={source['reliability']}`.",
        "- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.",
        "",
        "---",
        "",
        "## 🇬🇧 English",
        "",
        "### What it is",
        "",
        source["summary"]["en"],
        "",
        f"**Provider:** {source['provider']}  ",
        f"**Status:** {'official' if source['official'] else 'non-official/aggregated'}; tier **{source['tier']}**.  ",
        f"**Categories:** {categories_en}.  ",
        "",
        "### What it provides and when to use it",
        "",
        source["notes"]["en"],
        "",
        "Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.",
        "",
        "### Operational characteristics",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Coverage | {esc_cell(source['coverage'])} |",
        f"| Update cadence | {esc_cell(source['update_cadence'])} |",
        f"| Typical latency | {esc_cell(source['typical_latency'])} |",
        f"| Archive | {esc_cell(source['archive'])} |",
        f"| Reliability | `{source['reliability']}` |",
        f"| Automation | `{source['automation']}` |",
        f"| Protocols | {protocols} |",
        f"| Formats | {formats} |",
        "",
        "### Access and restrictions",
        "",
        f"- **Access level:** `{source['access']['level']}`.",
        f"- **Authentication:** {source['access']['auth']}.",
        f"- **Terms/licensing:** {source['access']['terms']}.",
        "",
        "### Endpoints",
        "",
        "| Endpoint | Protocol | Role | Health check | URL |",
        "|---|---|---|---:|---|",
    ]
    for endpoint in source["endpoints"]:
        lines.append(
            f"| {esc_cell(endpoint['name'])} | `{endpoint['protocol']}` | {esc_cell(endpoint['role'])} | "
            f"{'yes' if endpoint['healthcheck'] else 'no'} | {endpoint_link(endpoint)} |"
        )

    lines += ["", "### Software and decoders", ""]
    if source["software"]:
        for item in source["software"]:
            lines.append(f"- {md_link(item['name'], item['url'])} — {item['role']}.")
    else:
        lines.append("- No dedicated client is recorded; use a standard protocol client plus a native-format decoder.")

    lines += ["", "### Recommended ingestion flow", ""]
    for idx, step in enumerate(ingestion_recipe_en(source), start=1):
        lines.append(f"{idx}. {step}")

    lines += ["", "### Official/reference documentation", ""]
    for url in source["documentation"]:
        lines.append(f"- {md_link(url, url)}")

    lines += [
        "",
        "### Agent note",
        "",
        f"Authoritative record: `{source.get('_catalog_file', '')}` → `id: {source['id']}`. "
        "Treat this Markdown as a generated view; never override the YAML record from prose.",
        "",
    ]
    return "\n".join(lines)


def source_table(sources: list[dict[str, Any]], lang: str) -> list[str]:
    if lang == "ru":
        lines = [
            "| Источник | Описание | Категории | Доступ | Протоколы | Форматы | Оперативный |",
            "|---|---|---|---|---|---|---:|",
        ]
        for source in sources:
            link = f"generated/{source['id']}.md"
            cats = ", ".join(localized_category(x) for x in source["categories"])
            lines.append(
                f"| {LEVEL_ICON.get(source['tier'], '')} [{esc_cell(source['name']['ru'])}]({link}) | "
                f"{esc_cell(source['summary']['ru'])} | {esc_cell(cats)} | "
                f"{esc_cell(ACCESS_RU.get(source['access']['level'], source['access']['level']))} | "
                f"{esc_cell(', '.join(source['protocols']))} | {esc_cell(', '.join(source['formats']))} | "
                f"{'да' if source['operational'] else 'нет'} |"
            )
    else:
        lines = [
            "| Source | Description | Categories | Access | Protocols | Formats | Operational |",
            "|---|---|---|---|---|---|---:|",
        ]
        for source in sources:
            link = f"generated/{source['id']}.md"
            lines.append(
                f"| {LEVEL_ICON.get(source['tier'], '')} [{esc_cell(source['name']['en'])}]({link}) | "
                f"{esc_cell(source['summary']['en'])} | {esc_cell(', '.join(source['categories']))} | "
                f"`{source['access']['level']}` | {esc_cell(', '.join(source['protocols']))} | "
                f"{esc_cell(', '.join(source['formats']))} | {'yes' if source['operational'] else 'no'} |"
            )
    return lines


def render_index(sources: list[dict[str, Any]], index: dict[str, Any], lang: str) -> str:
    ordered = sorted(sources, key=lambda x: (x["tier"], x["provider"].lower(), x["id"]))
    if lang == "ru":
        lines = [
            "# 🇷🇺 Каталог источников метеоинформации",
            "",
            f"**Источников:** {len(sources)} · **Версия каталога:** {index.get('catalog_version')} · "
            f"**Ревизия:** {index.get('last_reviewed')}",
            "",
            "Это полный человекочитаемый индекс всех записей `catalog/`. Каждая строка ведёт на подробную карточку с доступом, "
            "протоколами, форматами, декодерами и рекомендуемым алгоритмом автоматического приёма.",
            "",
            "[English catalogue](index.en.md) · [Двуязычная стартовая страница](index.md)",
            "",
        ]
    else:
        lines = [
            "# 🇬🇧 Meteorological source catalogue",
            "",
            f"**Sources:** {len(sources)} · **Catalogue version:** {index.get('catalog_version')} · "
            f"**Reviewed:** {index.get('last_reviewed')}",
            "",
            "This is the complete human-readable index generated from `catalog/`. Every row links to a detailed bilingual source card.",
            "",
            "[Русский каталог](index.ru.md) · [Bilingual landing page](index.md)",
            "",
        ]
    lines.extend(source_table(ordered, lang))
    lines.append("")
    return "\n".join(lines)


def render_landing(sources: list[dict[str, Any]], index: dict[str, Any]) -> str:
    tier_counts = Counter(source["tier"] for source in sources)
    categories = Counter(cat for source in sources for cat in source["categories"])
    lines = [
        "# 🌦️ Source catalogue / Каталог источников",
        "",
        f"**{len(sources)} источников / sources** · catalogue v{index.get('catalog_version')} · reviewed {index.get('last_reviewed')}",
        "",
        "- 🇷🇺 **[Полный русский каталог](index.ru.md)** — описание каждого источника на русском, доступ, протоколы, форматы и практический приём.",
        "- 🇬🇧 **[Full English catalogue](index.en.md)** — complete English index and the same technical records.",
        "- 🤖 **[`catalog/sources.json`](../../catalog/sources.json)** — complete flattened machine-readable catalogue.",
        "- 🤖 **[`catalog/sources.ndjson`](../../catalog/sources.ndjson)** — one source per line for RAG/streaming ingestion.",
        "- 🧭 **[`catalog/agent-index.json`](../../catalog/agent-index.json)** — compact selection index for agents.",
        "- 🧠 **[`llms.txt`](../../llms.txt)** — repository entry point for LLM/agent tooling.",
        "",
        "## Приоритеты / Tiers",
        "",
        "| Tier | Количество | Назначение |",
        "|---|---:|---|",
        f"| 🟢 primary | {tier_counts.get('primary', 0)} | Основной официальный канал для автоматического/оперативного приёма |",
        f"| 🟡 secondary | {tier_counts.get('secondary', 0)} | Резерв, региональная альтернатива или архив |",
        f"| 🔵 specialized | {tier_counts.get('specialized', 0)} | Специализированные измерения/продукты |",
        f"| ⚪ aggregator | {tier_counts.get('aggregator', 0)} | Удобный агрегатор, но не единственный источник критической системы |",
        "",
        "## Категории / Categories",
        "",
    ]
    for category, count in sorted(categories.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- [{localized_category(category)} / `{category}`](categories/{category}.md) — **{count}**")
    lines += [
        "",
        "## Как читать карточки",
        "",
        "Карточка каждого источника содержит отдельную самостоятельную русскую часть и отдельную английскую часть. "
        "Для реализации приёмника сначала выбирайте `primary` + `operational`, затем проверяйте доступ, протокол, формат, задержку и fallback.",
        "",
    ]
    return "\n".join(lines)


def render_category(category: str, sources: list[dict[str, Any]]) -> str:
    ordered = sorted(sources, key=lambda x: (x["tier"], x["provider"].lower(), x["id"]))
    ru_name = localized_category(category)
    lines = [
        f"# {ru_name} / {category}",
        "",
        f"В этой категории **{len(ordered)}** источников. / **{len(ordered)}** sources in this category.",
        "",
        "## 🇷🇺 Русский",
        "",
    ]
    lines.extend(source_table(ordered, "ru"))
    lines += ["", "## 🇬🇧 English", ""]
    lines.extend(source_table(ordered, "en"))
    lines.append("")
    return "\n".join(lines)


def machine_exports(sources: list[dict[str, Any]], index: dict[str, Any]) -> dict[str, str]:
    public = [public_source(source) for source in sources]
    full = {
        "catalog_version": index.get("catalog_version"),
        "last_reviewed": index.get("last_reviewed"),
        "source_count": len(public),
        "sources": public,
    }
    ndjson = "\n".join(json.dumps(item, ensure_ascii=False, sort_keys=True) for item in public) + "\n"
    compact = []
    for source in public:
        compact.append({
            "id": source["id"],
            "provider": source["provider"],
            "name": source["name"],
            "summary": source["summary"],
            "tier": source["tier"],
            "official": source["official"],
            "operational": source["operational"],
            "categories": source["categories"],
            "coverage": source["coverage"],
            "access_level": source["access"]["level"],
            "protocols": source["protocols"],
            "formats": source["formats"],
            "reliability": source["reliability"],
            "automation": source["automation"],
            "card": f"docs/sources/generated/{source['id']}.md",
        })
    agent_index = {
        "purpose": "Compact source-selection index. Resolve a record by id in catalog/sources.json for full details.",
        "selection_order": [
            "official=true",
            "tier=primary",
            "operational=true for real-time workflows",
            "compatible coverage/access/protocol/format",
            "independent fallback for critical ingestion",
        ],
        "sources": compact,
    }
    return {
        "catalog/sources.json": json.dumps(full, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        "catalog/sources.ndjson": ndjson,
        "catalog/agent-index.json": json.dumps(agent_index, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
    }


def render_llms(sources: list[dict[str, Any]], index: dict[str, Any]) -> str:
    return "\n".join([
        "# Weather Source",
        "",
        "Bilingual operational meteorological data-source knowledge base for humans and AI agents.",
        "Русско-английская база знаний оперативных источников метеоинформации.",
        "",
        "## Canonical machine data",
        "- catalog/sources.yaml — catalogue entry point and source-of-truth file list",
        "- catalog/sources.json — flattened full catalogue",
        "- catalog/sources.ndjson — one source record per line",
        "- catalog/agent-index.json — compact source-selection index",
        "- catalog/schema.json — JSON Schema for source records",
        "",
        "## Human documentation",
        "- docs/sources/index.ru.md — полный русский каталог",
        "- docs/sources/index.en.md — full English catalogue",
        "- docs/sources/generated/<id>.md — bilingual technical card for every source",
        "- docs/sources/wmo-wis2.md — WIS2 transport guide",
        "- docs/sources/aerology.md — upper-air/aerology guide",
        "- docs/agent-guide.md — agent retrieval and decision rules",
        "",
        "## Agent selection policy",
        "1. Prefer official=true and tier=primary.",
        "2. For real-time workflows require operational=true and compatible coverage.",
        "3. Check access.level/auth/terms before choosing an endpoint.",
        "4. Prefer MQTT/WIS2, AMQP, S3/object storage, REST/OGC or direct file trees over scraping HTML viewers.",
        "5. Match native formats to a standards-aware decoder and preserve raw payloads.",
        "6. Use an independent fallback for critical pipelines.",
        "7. Do not confuse observed upper-air profiles with NWP model profiles or satellite retrievals.",
        "",
        f"Catalogue version: {index.get('catalog_version')}; sources: {len(sources)}; reviewed: {index.get('last_reviewed')}",
        "",
    ])


def build_artifacts(catalog_path: Path) -> tuple[dict[str, str], int]:
    index, sources, _ = load_catalog(catalog_path)
    artifacts: dict[str, str] = {}
    for source in sources:
        artifacts[f"docs/sources/generated/{source['id']}.md"] = render_source(source)

    artifacts["docs/sources/index.md"] = render_landing(sources, index)
    artifacts["docs/sources/index.ru.md"] = render_index(sources, index, "ru")
    artifacts["docs/sources/index.en.md"] = render_index(sources, index, "en")

    by_category: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for source in sources:
        for category in source["categories"]:
            by_category[category].append(source)
    for category, items in by_category.items():
        artifacts[f"docs/sources/categories/{category}.md"] = render_category(category, items)

    artifacts.update(machine_exports(sources, index))
    artifacts["llms.txt"] = render_llms(sources, index)
    return artifacts, len(sources)


def write_artifacts(artifacts: dict[str, str], root: Path = REPO_ROOT) -> None:
    managed_dirs = [root / "docs" / "sources" / "generated", root / "docs" / "sources" / "categories"]
    for directory in managed_dirs:
        directory.mkdir(parents=True, exist_ok=True)
        for stale in directory.glob("*.md"):
            stale.unlink()
    for relative, content in artifacts.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def verify_artifacts(artifacts: dict[str, str], root: Path = REPO_ROOT) -> list[str]:
    problems: list[str] = []
    expected_paths = {Path(relative) for relative in artifacts}
    for relative, expected in artifacts.items():
        path = root / relative
        if not path.is_file():
            problems.append(f"missing generated artifact: {relative}")
            continue
        actual = path.read_text(encoding="utf-8")
        if actual != expected:
            problems.append(f"outdated generated artifact: {relative}")
    for managed in (root / "docs" / "sources" / "generated", root / "docs" / "sources" / "categories"):
        if managed.exists():
            for path in managed.glob("*.md"):
                rel = path.relative_to(root)
                if rel not in expected_paths:
                    problems.append(f"stale generated artifact: {rel}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="write all generated documentation and machine indexes")
    mode.add_argument("--check", action="store_true", help="render in a temporary directory and check generator completeness")
    mode.add_argument("--verify", action="store_true", help="verify committed generated artifacts exactly match the YAML catalogue")
    args = parser.parse_args()

    artifacts, count = build_artifacts(args.catalog)

    if args.write:
        write_artifacts(artifacts)
        print(f"Generated {len(artifacts)} artifacts for {count} sources")
        return 0

    if args.verify:
        problems = verify_artifacts(artifacts)
        if problems:
            for problem in problems:
                print(f"ERROR: {problem}")
            print("Run: python scripts/generate_docs.py --write")
            return 1
        print(f"OK: {len(artifacts)} committed artifacts match {count} catalogue sources")
        return 0

    with tempfile.TemporaryDirectory(prefix="weather-source-docs-") as temp_dir:
        root = Path(temp_dir)
        write_artifacts(artifacts, root)
        generated = list((root / "docs" / "sources" / "generated").glob("*.md"))
        if len(generated) != count:
            raise RuntimeError(f"expected {count} source cards, generated {len(generated)}")
        for required in (
            "docs/sources/index.md",
            "docs/sources/index.ru.md",
            "docs/sources/index.en.md",
            "catalog/sources.json",
            "catalog/sources.ndjson",
            "catalog/agent-index.json",
            "llms.txt",
        ):
            if not (root / required).is_file():
                raise RuntimeError(f"missing generated artifact: {required}")
        shutil.rmtree(root / "docs" / "sources" / "generated")
    print(f"OK: generator rendered {len(artifacts)} artifacts for {count} sources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
