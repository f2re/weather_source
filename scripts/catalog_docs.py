#!/usr/bin/env python3
"""Stable front-end for generated catalogue artifacts.

The YAML catalogue remains authoritative for meteorological metadata. Runtime
recipes under ``catalog/recipes/*.json`` are the authoritative executable layer:
every source id must have exactly one audited recipe describing how data can
actually be retrieved (or why a public machine feed cannot honestly be offered).

This front-end augments the base generator with runtime examples, audit results
and agent-readable recipe exports while preserving deterministic --write and
--verify behaviour.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any

import generate_docs as engine

GITHUB_BLOB = "https://github.com/f2re/weather_source/blob/main"
AUDIT_DATE = "2026-09-06"
RECIPES_DIR = engine.REPO_ROOT / "catalog" / "recipes"

_original_render_category = engine.render_category
_original_render_landing = engine.render_landing
_original_render_source = engine.render_source
_original_build_artifacts = engine.build_artifacts


STATUS_RU = {
    "public": "публичный машинный доступ",
    "credentials": "нужны бесплатные/договорные учётные данные",
    "restricted": "доступ ограничен правами участника/лицензией",
    "manual": "публичный стабильный machine endpoint не подтверждён",
}

VERDICT_RU = {
    "ok": "✅ подтверждено",
    "corrected": "🛠 исправлено/уточнено",
    "restricted": "🔐 ограничения уточнены",
    "manual": "⚠️ автоматический доступ не подтверждён",
}


def load_runtime_recipes() -> dict[str, dict[str, Any]]:
    recipes: dict[str, dict[str, Any]] = {}
    for path in sorted(RECIPES_DIR.glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        for source_id, item in payload.get("sources", {}).items():
            if source_id in recipes:
                raise RuntimeError(f"duplicate runtime recipe for {source_id}")
            recipe = dict(item)
            recipe["_recipe_file"] = str(path.relative_to(engine.REPO_ROOT))
            recipes[source_id] = recipe
    return recipes


def cli_fetch_command(source_id: str, recipe: dict[str, Any]) -> str:
    adapter = recipe.get("adapter")
    if adapter == "unavailable":
        return f"python -m weather_source example {source_id}"
    suffix = " --allow-external" if adapter == "external" else ""
    return f"python -m weather_source fetch {source_id}{suffix}"


def render_runtime_ru(source_id: str, recipe: dict[str, Any]) -> str:
    verdict = VERDICT_RU.get(recipe.get("verdict"), recipe.get("verdict", "—"))
    status = STATUS_RU.get(recipe.get("status"), recipe.get("status", "—"))
    lines = [
        "### 🧪 Проверенный пример получения данных",
        "",
        f"**Аудит:** {verdict} · **проверено:** `{recipe.get('verified', '—')}`  ",
        f"**Реальный режим доступа:** {status} (`{recipe.get('status', '—')}`)  ",
        f"**Runtime-адаптер:** `{recipe.get('adapter', '—')}`  ",
        f"**Recipe:** `{recipe.get('_recipe_file', '')}`",
        "",
        recipe.get("example_ru", ""),
        "",
        "```bash",
        f"python -m weather_source describe {source_id}",
        f"python -m weather_source probe {source_id}",
        cli_fetch_command(source_id, recipe),
        "```",
    ]
    if recipe.get("env"):
        lines += ["", "**Требуемые переменные окружения:** " + ", ".join(f"`{x}`" for x in recipe["env"]) + "."]
    if recipe.get("issues_ru"):
        lines += ["", "**Что исправлено или обнаружено аудитом:**", ""]
        for issue in recipe["issues_ru"]:
            lines.append(f"- {issue}")
    if recipe.get("reason_ru"):
        lines += ["", f"**Почему нет автоматического public fetch:** {recipe['reason_ru']}"]
    if recipe.get("fallback"):
        lines += ["", f"**Резервный источник:** `{recipe['fallback']}`."]
    request = recipe.get("request", {})
    if request.get("command"):
        lines += [
            "",
            "<details><summary>Команда официального/специализированного клиента</summary>",
            "",
            "```bash",
            request["command"],
            "```",
            "",
            "</details>",
        ]
    lines += [
        "",
        "> Клиент сохраняет исходные данные; крупные GRIB/NetCDF/радарные объекты по умолчанию блокируются безопасным лимитом. "
        "Для осознанной полной загрузки используйте `--full`, когда это применимо.",
    ]
    return "\n".join(lines)


def render_runtime_en(source_id: str, recipe: dict[str, Any]) -> str:
    lines = [
        "### 🧪 Executable retrieval recipe",
        "",
        f"**Audit verdict:** `{recipe.get('verdict', 'unknown')}` · **verified:** `{recipe.get('verified', '—')}`  ",
        f"**Runtime access:** `{recipe.get('status', '—')}` · **adapter:** `{recipe.get('adapter', '—')}`  ",
        f"**Recipe:** `{recipe.get('_recipe_file', '')}`",
        "",
        "```bash",
        f"python -m weather_source probe {source_id}",
        cli_fetch_command(source_id, recipe),
        "```",
    ]
    if recipe.get("env"):
        lines += ["", "Required environment: " + ", ".join(f"`{x}`" for x in recipe["env"]) + "."]
    if recipe.get("fallback"):
        lines += ["", f"Fallback: `{recipe['fallback']}`."]
    return "\n".join(lines)


def render_source(source: dict[str, Any]) -> str:
    recipes = load_runtime_recipes()
    source_id = source["id"]
    if source_id not in recipes:
        raise RuntimeError(f"source {source_id} has no runtime recipe")
    text = _original_render_source(source)
    ru_section = render_runtime_ru(source_id, recipes[source_id])
    en_section = render_runtime_en(source_id, recipes[source_id])
    marker_en = "\n---\n\n## 🇬🇧 English"
    if marker_en not in text:
        raise RuntimeError(f"cannot place Russian runtime section for {source_id}")
    text = text.replace(marker_en, f"\n\n{ru_section}\n\n---\n\n## 🇬🇧 English", 1)
    marker_agent = "\n### Agent note\n"
    if marker_agent not in text:
        raise RuntimeError(f"cannot place English runtime section for {source_id}")
    text = text.replace(marker_agent, f"\n{en_section}\n\n### Agent note\n", 1)
    return text


def render_category(category, sources):
    """Category files live one directory below source indexes."""
    text = _original_render_category(category, sources)
    return text.replace("](generated/", "](../generated/")


def render_landing(sources, index):
    """Links outside docs/ must be absolute for both GitHub and MkDocs."""
    text = _original_render_landing(sources, index)
    replacements = {
        "(../../catalog/sources.json)": f"({GITHUB_BLOB}/catalog/sources.json)",
        "(../../catalog/sources.ndjson)": f"({GITHUB_BLOB}/catalog/sources.ndjson)",
        "(../../catalog/agent-index.json)": f"({GITHUB_BLOB}/catalog/agent-index.json)",
        "(../../llms.txt)": f"({GITHUB_BLOB}/llms.txt)",
    }
    for before, after in replacements.items():
        text = text.replace(before, after)
    text += "\n## Аудит и рабочий код / Audit and executable clients\n\n"
    text += f"- [Аудит всех источников]({GITHUB_BLOB}/docs/audit/source-audit-{AUDIT_DATE}.md)\n"
    text += f"- [Runtime recipes]({GITHUB_BLOB}/catalog/recipes.json)\n"
    text += f"- [Python client package]({GITHUB_BLOB}/weather_source/)\n"
    return text


def render_audit(sources: list[dict[str, Any]], recipes: dict[str, dict[str, Any]]) -> str:
    verdicts = Counter(recipe.get("verdict", "unknown") for recipe in recipes.values())
    statuses = Counter(recipe.get("status", "unknown") for recipe in recipes.values())
    lines = [
        f"# Аудит источников — {AUDIT_DATE}",
        "",
        "Проверка отвечает на два разных вопроса: корректна ли запись каталога и можно ли реально получить данные машинным способом. "
        "Landing page или HTTP 200 сами по себе больше не считаются доказательством работоспособности источника.",
        "",
        f"**Источников:** {len(sources)} · **recipes:** {len(recipes)} · "
        f"**исправлено/уточнено:** {verdicts.get('corrected', 0)} · **без существенных исправлений:** {verdicts.get('ok', 0)}",
        "",
        "Режимы runtime-доступа: " + ", ".join(f"`{k}`={v}" for k, v in sorted(statuses.items())) + ".",
        "",
        "## Сводная таблица",
        "",
        "| Источник | Вердикт | Runtime | Адаптер | Что найдено | Рабочий запуск |",
        "|---|---|---|---|---|---|",
    ]
    for source in sorted(sources, key=lambda x: x["id"]):
        recipe = recipes[source["id"]]
        issues = "<br>".join(recipe.get("issues_ru") or ["Существенных коллизий в текущей записи не выявлено."])
        command = cli_fetch_command(source["id"], recipe).replace("|", "\\|")
        lines.append(
            f"| [`{source['id']}`](../sources/generated/{source['id']}.md) | `{recipe.get('verdict')}` | "
            f"`{recipe.get('status')}` | `{recipe.get('adapter')}` | {issues.replace('|', '\\|')} | `{command}` |"
        )
    lines += [
        "",
        "## Правила интерпретации",
        "",
        "- `public`: пример можно запускать без секрета; это не означает отсутствие лицензионных ограничений на дальнейшее использование.",
        "- `credentials`: код рабочий, но поставщик требует ключ, токен, бесплатную регистрацию или договорные credentials.",
        "- `restricted`: данные существуют, но права не являются универсально публичными; репозиторий не обходит ограничения.",
        "- `manual`: публичный стабильный machine endpoint не подтверждён. Вместо фиктивного URL указан официальный путь и fallback.",
        "- `probe` проверяет лёгкий machine endpoint; `fetch` получает реальные данные. Для больших объектов полный download требует явного `--full`.",
        "",
        "## Кодовая база",
        "",
        "```bash",
        "python -m weather_source verify-recipes",
        "python -m weather_source list",
        "python -m weather_source describe wmo-wis2",
        "python -m weather_source example noaa-nexrad",
        "python -m weather_source probe fmi-open-data",
        "python -m weather_source fetch noaa-aviationweather",
        "```",
        "",
        "Общие транспорты находятся в `weather_source/adapters.py`, уникальные API-последовательности — в `weather_source/providers.py`, "
        "а параметры каждого конкретного источника — в `catalog/recipes/*.json`.",
        "",
    ]
    return "\n".join(lines)


def flatten_recipes(recipes: dict[str, dict[str, Any]]) -> str:
    public = {}
    for source_id, recipe in sorted(recipes.items()):
        item = {k: v for k, v in recipe.items() if not k.startswith("_")}
        item["recipe_file"] = recipe.get("_recipe_file")
        item["fetch_command"] = cli_fetch_command(source_id, recipe)
        public[source_id] = item
    return json.dumps({"verified": AUDIT_DATE, "source_count": len(public), "sources": public}, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def build_artifacts(catalog_path: Path):
    artifacts, count = _original_build_artifacts(catalog_path)
    index, sources, _ = engine.load_catalog(catalog_path)
    recipes = load_runtime_recipes()
    source_ids = {source["id"] for source in sources}
    recipe_ids = set(recipes)
    if source_ids != recipe_ids:
        missing = sorted(source_ids - recipe_ids)
        extra = sorted(recipe_ids - source_ids)
        raise RuntimeError(f"runtime recipe coverage mismatch: missing={missing}, extra={extra}")
    artifacts[f"docs/audit/source-audit-{AUDIT_DATE}.md"] = render_audit(sources, recipes)
    artifacts["catalog/recipes.json"] = flatten_recipes(recipes)
    artifacts["llms.txt"] += "\n## Executable source access\n- catalog/recipes.json — audited runtime access recipe for every source id\n- weather_source/ — reusable Python transport/adapters\n- docs/audit/source-audit-2026-09-06.md — per-source audit and corrections\n"
    return artifacts, count


engine.render_source = render_source
engine.render_category = render_category
engine.render_landing = render_landing
engine.build_artifacts = build_artifacts

if __name__ == "__main__":
    raise SystemExit(engine.main())
