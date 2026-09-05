from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from catalog_lib import DEFAULT_CATALOG, filter_sources, load_catalog


def test_declared_source_count_matches_loaded_catalog() -> None:
    index, sources, files = load_catalog(DEFAULT_CATALOG)
    assert files
    assert index["source_count"] == len(sources)
    assert len(sources) >= 40


def test_source_ids_are_unique() -> None:
    _, sources, _ = load_catalog(DEFAULT_CATALOG)
    ids = [source["id"] for source in sources]
    assert len(ids) == len(set(ids))


def test_bilingual_metadata_is_present() -> None:
    _, sources, _ = load_catalog(DEFAULT_CATALOG)
    for source in sources:
        assert source["name"]["en"].strip()
        assert source["name"]["ru"].strip()
        assert source["summary"]["en"].strip()
        assert source["summary"]["ru"].strip()
        assert source["notes"]["en"].strip()
        assert source["notes"]["ru"].strip()


def test_primary_sources_are_official_and_automatable() -> None:
    _, sources, _ = load_catalog(DEFAULT_CATALOG)
    for source in filter_sources(sources, tier="primary"):
        assert source["official"] is True
        if source["operational"]:
            assert source["automation"] in {"high", "medium"}


def test_critical_operational_sources_exist() -> None:
    _, sources, _ = load_catalog(DEFAULT_CATALOG)
    ids = {source["id"] for source in sources}
    expected = {
        "wmo-wis2",
        "ru-aviamettelecom-wis2-temp",
        "noaa-ncei-igra",
        "ecmwf-open-data",
        "noaa-nomads",
        "dwd-open-data",
        "eumetsat-data-store",
        "eccc-datamart",
        "copernicus-marine",
    }
    assert expected <= ids


def test_healthchecks_do_not_point_to_non_http_protocols() -> None:
    _, sources, _ = load_catalog(DEFAULT_CATALOG)
    for source in sources:
        for endpoint in source["endpoints"]:
            if endpoint["healthcheck"]:
                assert endpoint["url"].startswith(("http://", "https://"))
