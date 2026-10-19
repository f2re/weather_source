#!/usr/bin/env python3
"""Access NOAA/NCEI and NWS station-observation sources.

The adapter intentionally separates operational point observations (NWS API)
from bulk climate/station archives (GHCNh, GHCNd, USCRN). It preserves raw
provider fields instead of silently converting units or discarding QC flags.
"""
from __future__ import annotations

import argparse
import csv
import json
from itertools import islice
from typing import Any, Iterable, Iterator

import requests

USER_AGENT = "weather-source-example/1.0 (+https://github.com/f2re/weather_source)"
GHCNH_BASE = "https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/access"
GHCND_BASE = "https://www.ncei.noaa.gov/pub/data/ghcn/daily"
USCRN_BASE = "https://www.ncei.noaa.gov/pub/data/uscrn/products"
NWS_BASE = "https://api.weather.gov"


def ghcnh_url(station: str, year: int | None = None, file_format: str = "psv") -> str:
    """Build an official GHCNh station URL.

    Period-of-record files are PSV. Station/year files are available as PSV and
    Parquet. Station IDs are GHCN identifiers such as USW00023183.
    """
    station = station.strip().upper()
    if not station or any(ch not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" for ch in station):
        raise ValueError("station must be an alphanumeric GHCN identifier")
    if file_format not in {"psv", "parquet"}:
        raise ValueError("file_format must be 'psv' or 'parquet'")
    if year is None:
        if file_format != "psv":
            raise ValueError("period-of-record GHCNh access is documented as PSV; provide --year for Parquet")
        return f"{GHCNH_BASE}/by-station/GHCNh_{station}_por.psv"
    if year < 1700 or year > 2200:
        raise ValueError("year is outside a plausible range")
    suffix = "psv" if file_format == "psv" else "parquet"
    return f"{GHCNH_BASE}/by-year/{year}/{suffix}/GHCNh_{station}_{year}.{suffix}"


def ghcnd_year_url(year: int) -> str:
    """Build the yearly bulk GHCNd CSV.gz URL."""
    if year < 1700 or year > 2200:
        raise ValueError("year is outside a plausible range")
    return f"{GHCND_BASE}/by_year/{year}.csv.gz"


def uscrn_hourly_directory(year: int) -> str:
    """Return the USCRN hourly02 directory containing station/year text files."""
    if year < 2000 or year > 2200:
        raise ValueError("USCRN year is outside a plausible range")
    return f"{USCRN_BASE}/hourly02/{year}/"


def _get(url: str, *, timeout: float = 30.0, accept: str | None = None) -> requests.Response:
    headers = {"User-Agent": USER_AGENT}
    if accept:
        headers["Accept"] = accept
    response = requests.get(url, timeout=timeout, headers=headers)
    response.raise_for_status()
    return response


def _decoded_lines(response: requests.Response) -> Iterator[str]:
    encoding = response.encoding or "utf-8"
    for line in response.iter_lines():
        if line:
            yield line.decode(encoding, errors="replace")


def read_ghcnh_psv(url: str, *, limit: int = 5, timeout: float = 30.0) -> list[dict[str, str]]:
    """Stream the first GHCNh PSV records without altering QC/source columns."""
    headers = {"User-Agent": USER_AGENT}
    with requests.get(url, stream=True, timeout=timeout, headers=headers) as response:
        response.raise_for_status()
        reader = csv.DictReader(_decoded_lines(response), delimiter="|")
        return list(islice(reader, max(0, limit)))


def nws_latest_observation(station: str, *, timeout: float = 30.0) -> dict[str, Any]:
    """Fetch and lightly normalize the latest NWS station observation.

    QuantitativeValue objects are retained so the provider's unit codes remain
    explicit. The full raw properties mapping is also returned.
    """
    station = station.strip().upper()
    url = f"{NWS_BASE}/stations/{station}/observations/latest"
    payload = _get(url, timeout=timeout, accept="application/geo+json").json()
    properties = payload.get("properties", {})
    return {
        "station": station,
        "timestamp": properties.get("timestamp"),
        "textDescription": properties.get("textDescription"),
        "temperature": properties.get("temperature"),
        "dewpoint": properties.get("dewpoint"),
        "relativeHumidity": properties.get("relativeHumidity"),
        "windDirection": properties.get("windDirection"),
        "windSpeed": properties.get("windSpeed"),
        "barometricPressure": properties.get("barometricPressure"),
        "seaLevelPressure": properties.get("seaLevelPressure"),
        "visibility": properties.get("visibility"),
        "rawMessage": properties.get("rawMessage"),
        "raw_properties": properties,
    }


def _print_json(rows: Iterable[dict[str, Any]] | dict[str, Any]) -> None:
    print(json.dumps(rows, ensure_ascii=False, indent=2, default=str))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p_ghcnh_url = sub.add_parser("ghcnh-url", help="print a GHCNh station download URL")
    p_ghcnh_url.add_argument("station")
    p_ghcnh_url.add_argument("--year", type=int)
    p_ghcnh_url.add_argument("--format", choices=["psv", "parquet"], default="psv")

    p_ghcnh_head = sub.add_parser("ghcnh-head", help="stream the first PSV records from GHCNh")
    p_ghcnh_head.add_argument("station")
    p_ghcnh_head.add_argument("--year", type=int)
    p_ghcnh_head.add_argument("--limit", type=int, default=5)
    p_ghcnh_head.add_argument("--timeout", type=float, default=30.0)

    p_nws = sub.add_parser("nws-latest", help="fetch the latest NWS observation for a station")
    p_nws.add_argument("station", help="NWS station identifier, e.g. KJFK")
    p_nws.add_argument("--timeout", type=float, default=30.0)

    p_ghcnd = sub.add_parser("ghcnd-year-url", help="print the yearly GHCNd CSV.gz URL")
    p_ghcnd.add_argument("year", type=int)

    p_uscrn = sub.add_parser("uscrn-hourly-dir", help="print the USCRN hourly02 year directory")
    p_uscrn.add_argument("year", type=int)

    args = parser.parse_args()
    if args.command == "ghcnh-url":
        print(ghcnh_url(args.station, args.year, args.format))
    elif args.command == "ghcnh-head":
        url = ghcnh_url(args.station, args.year, "psv")
        _print_json(read_ghcnh_psv(url, limit=args.limit, timeout=args.timeout))
    elif args.command == "nws-latest":
        _print_json(nws_latest_observation(args.station, timeout=args.timeout))
    elif args.command == "ghcnd-year-url":
        print(ghcnd_year_url(args.year))
    elif args.command == "uscrn-hourly-dir":
        print(uscrn_hourly_directory(args.year))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
