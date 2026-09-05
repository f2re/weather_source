from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from catalog_lib import DEFAULT_CATALOG, load_catalog


def source_ids() -> set[str]:
    _, sources, _ = load_catalog(DEFAULT_CATALOG)
    return {source["id"] for source in sources}


def test_every_catalogue_source_has_one_committed_bilingual_card() -> None:
    _, sources, _ = load_catalog(DEFAULT_CATALOG)
    cards_dir = ROOT / "docs" / "sources" / "generated"
    committed_ids = {path.stem for path in cards_dir.glob("*.md")}
    expected_ids = {source["id"] for source in sources}
    assert committed_ids == expected_ids

    for source in sources:
        text = (cards_dir / f"{source['id']}.md").read_text(encoding="utf-8")
        assert "## 🇷🇺 Русский" in text
        assert "## 🇬🇧 English" in text
        assert source["summary"]["ru"] in text
        assert source["summary"]["en"] in text
        assert "### Рекомендуемый алгоритм автоматического приёма" in text
        assert "### Для ИИ-агента" in text


def test_ru_and_en_indexes_cover_all_sources() -> None:
    _, sources, _ = load_catalog(DEFAULT_CATALOG)
    ru_index = (ROOT / "docs" / "sources" / "index.ru.md").read_text(encoding="utf-8")
    en_index = (ROOT / "docs" / "sources" / "index.en.md").read_text(encoding="utf-8")

    for source in sources:
        assert source["name"]["ru"] in ru_index
        assert source["name"]["en"] in en_index
        link = f"generated/{source['id']}.md"
        assert link in ru_index
        assert link in en_index


def test_machine_views_cover_exactly_the_yaml_catalogue() -> None:
    expected = source_ids()

    full = json.loads((ROOT / "catalog" / "sources.json").read_text(encoding="utf-8"))
    full_ids = {source["id"] for source in full["sources"]}
    assert full["source_count"] == len(expected)
    assert full_ids == expected

    ndjson_ids = {
        json.loads(line)["id"]
        for line in (ROOT / "catalog" / "sources.ndjson").read_text(encoding="utf-8").splitlines()
        if line.strip()
    }
    assert ndjson_ids == expected

    agent = json.loads((ROOT / "catalog" / "agent-index.json").read_text(encoding="utf-8"))
    agent_ids = {source["id"] for source in agent["sources"]}
    assert agent_ids == expected


def test_llms_entrypoint_points_to_human_and_machine_catalogues() -> None:
    text = (ROOT / "llms.txt").read_text(encoding="utf-8")
    required = {
        "catalog/sources.json",
        "catalog/sources.ndjson",
        "catalog/agent-index.json",
        "docs/sources/index.ru.md",
        "docs/sources/index.en.md",
        "docs/agent-guide.md",
    }
    for path in required:
        assert path in text


def test_wis2_and_russian_temp_have_russian_technical_documentation() -> None:
    guide = (ROOT / "docs" / "sources" / "wmo-wis2.md").read_text(encoding="utf-8")
    assert "## 🇷🇺 Русский" in guide
    assert "Российская аэрология" in guide
    assert "cache/a/wis2/ru-aviamettelecom/data/core/weather/surface-based-observations/temp" in guide

    wis2 = (ROOT / "docs" / "sources" / "generated" / "wmo-wis2.md").read_text(encoding="utf-8")
    russian_temp = (
        ROOT / "docs" / "sources" / "generated" / "ru-aviamettelecom-wis2-temp.md"
    ).read_text(encoding="utf-8")
    for text in (wis2, russian_temp):
        assert "## 🇷🇺 Русский" in text
        assert "### ПО, библиотеки и декодеры" in text
        assert "### Рекомендуемый алгоритм автоматического приёма" in text
