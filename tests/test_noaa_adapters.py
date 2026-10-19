from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_example(name: str):
    path = ROOT / "examples" / "python" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_station_adapter_urls() -> None:
    mod = load_example("noaa_station_observations")
    assert mod.ghcnh_url("USW00023183", 2026) == (
        "https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/access/"
        "by-year/2026/psv/GHCNh_USW00023183_2026.psv"
    )
    assert mod.ghcnh_url("USW00023183") == (
        "https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/access/"
        "by-station/GHCNh_USW00023183_por.psv"
    )
    assert mod.ghcnd_year_url(2026).endswith("/ghcn/daily/by_year/2026.csv.gz")
    assert mod.uscrn_hourly_directory(2026).endswith("/uscrn/products/hourly02/2026/")


def test_assimilation_adapter_urls() -> None:
    mod = load_example("noaa_assimilation_observations")
    ts = mod.parse_timestamp("2026-10-19T12:00Z")
    assert mod.madis_url("metar", ts).endswith("/point/metar/netcdf/20261019_1200.gz")
    assert mod.prepbufr_url("20261019", "12", "gdas") == (
        "https://nomads.ncep.noaa.gov/pub/data/nccf/com/obsproc/prod/"
        "gdas.20261019/gdas.t12z.prepbufr.nr"
    )
    assert mod.ncep_dump_url("20261019", "00", "adpsfc", "gdas").endswith(
        "/gdas.20261019/gdas.t00z.adpsfc.tm00.bufr_d"
    )
