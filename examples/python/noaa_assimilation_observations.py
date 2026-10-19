#!/usr/bin/env python3
"""Access NOAA/NCEP MADIS and GDAS/GFS observation-space products.

MADIS URLs point to public sample/current files where available. PREPBUFR and
some raw NCEP observation dumps can contain observations with redistribution or
use restrictions, so downloads require an explicit acknowledgement flag.
"""
from __future__ import annotations

import argparse
import hashlib
from datetime import datetime
from pathlib import Path

import requests

USER_AGENT = "weather-source-example/1.0 (+https://github.com/f2re/weather_source)"
MADIS_BASE = "https://madis-data.ncep.noaa.gov/madisPublic1/data"
NCEP_OBSPROC_BASE = "https://nomads.ncep.noaa.gov/pub/data/nccf/com/obsproc/prod"

MADIS_DATASETS = {
    "metar": "point/metar/netcdf",
    "maritime": "point/maritime/netcdf",
    "raob": "point/raob/netcdf",
    "acars": "point/acars/netcdf",
    "acars-profiles": "point/acarsProfiles/netcdf",
    "mesonet": "LDAD/mesonet/netCDF",
    "crn": "LDAD/crn/netCDF",
    "profiler": "LDAD/profiler/netCDF",
    "hydro": "LDAD/hydro/netCDF",
    "snow": "LDAD/snow/netCDF",
}


def parse_timestamp(value: str) -> datetime:
    """Parse UTC timestamps accepted by the URL builders."""
    cleaned = value.strip().replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(cleaned)
    except ValueError as exc:
        raise ValueError("timestamp must be ISO-8601, e.g. 2026-10-19T12:00Z") from exc


def madis_url(dataset: str, timestamp: datetime) -> str:
    """Build a MADIS public current/sample netCDF gzip URL."""
    try:
        path = MADIS_DATASETS[dataset]
    except KeyError as exc:
        raise ValueError(f"unknown MADIS dataset {dataset!r}; choose from {sorted(MADIS_DATASETS)}") from exc
    stamp = timestamp.strftime("%Y%m%d_%H%M")
    return f"{MADIS_BASE}/{path}/{stamp}.gz"


def prepbufr_url(date: str, cycle: str, model: str = "gdas") -> str:
    """Build a NOMADS PREPBUFR URL using NCEP's documented filename pattern."""
    if model not in {"gdas", "gfs"}:
        raise ValueError("model must be 'gdas' or 'gfs'")
    try:
        datetime.strptime(date, "%Y%m%d")
    except ValueError as exc:
        raise ValueError("date must be YYYYMMDD") from exc
    if cycle not in {"00", "06", "12", "18"}:
        raise ValueError("cycle must be one of 00, 06, 12, 18")
    return f"{NCEP_OBSPROC_BASE}/{model}.{date}/{model}.t{cycle}z.prepbufr.nr"


def ncep_dump_url(date: str, cycle: str, dump_name: str, model: str = "gdas") -> str:
    """Build a raw NCEP BUFR dump URL such as adpsfc/adpupa/sfcshp."""
    if model not in {"gdas", "gfs"}:
        raise ValueError("model must be 'gdas' or 'gfs'")
    try:
        datetime.strptime(date, "%Y%m%d")
    except ValueError as exc:
        raise ValueError("date must be YYYYMMDD") from exc
    if cycle not in {"00", "06", "12", "18"}:
        raise ValueError("cycle must be one of 00, 06, 12, 18")
    name = dump_name.strip()
    if not name or any(ch not in "abcdefghijklmnopqrstuvwxyz0123456789_" for ch in name):
        raise ValueError("dump_name must use lowercase letters, digits or underscore")
    return f"{NCEP_OBSPROC_BASE}/{model}.{date}/{model}.t{cycle}z.{name}.tm00.bufr_d"


def download(url: str, output: Path, *, timeout: float = 60.0) -> tuple[int, str]:
    """Stream a raw product to disk and return byte count plus SHA-256."""
    output.parent.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256()
    size = 0
    headers = {"User-Agent": USER_AGENT}
    with requests.get(url, stream=True, timeout=timeout, headers=headers) as response:
        response.raise_for_status()
        with output.open("wb") as handle:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if not chunk:
                    continue
                handle.write(chunk)
                digest.update(chunk)
                size += len(chunk)
    return size, digest.hexdigest()


def _require_restriction_ack(args: argparse.Namespace, parser: argparse.ArgumentParser) -> None:
    if not args.acknowledge_restrictions:
        parser.error(
            "NCEP PREPBUFR/raw dumps can contain restricted constituent observations. "
            "Read https://www.nco.ncep.noaa.gov/pmb/docs/restricted_data/ and rerun "
            "with --acknowledge-restrictions only if your intended use complies."
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p_madis_url = sub.add_parser("madis-url", help="print a MADIS public sample/current data URL")
    p_madis_url.add_argument("dataset", choices=sorted(MADIS_DATASETS))
    p_madis_url.add_argument("timestamp", help="UTC ISO-8601 timestamp, e.g. 2026-10-19T12:00Z")

    p_madis_get = sub.add_parser("madis-download", help="download a MADIS public sample/current netCDF.gz file")
    p_madis_get.add_argument("dataset", choices=sorted(MADIS_DATASETS))
    p_madis_get.add_argument("timestamp")
    p_madis_get.add_argument("output", type=Path)
    p_madis_get.add_argument("--timeout", type=float, default=60.0)

    p_prep_url = sub.add_parser("prepbufr-url", help="print a GDAS/GFS PREPBUFR URL")
    p_prep_url.add_argument("date", help="YYYYMMDD")
    p_prep_url.add_argument("cycle", choices=["00", "06", "12", "18"])
    p_prep_url.add_argument("--model", choices=["gdas", "gfs"], default="gdas")

    p_dump_url = sub.add_parser("dump-url", help="print a raw NCEP observation BUFR dump URL")
    p_dump_url.add_argument("date", help="YYYYMMDD")
    p_dump_url.add_argument("cycle", choices=["00", "06", "12", "18"])
    p_dump_url.add_argument("dump_name", help="e.g. adpsfc, adpupa, sfcshp")
    p_dump_url.add_argument("--model", choices=["gdas", "gfs"], default="gdas")

    for name, help_text in (
        ("prepbufr-download", "download PREPBUFR after acknowledging restrictions"),
        ("dump-download", "download a raw NCEP observation dump after acknowledging restrictions"),
    ):
        p = sub.add_parser(name, help=help_text)
        p.add_argument("date", help="YYYYMMDD")
        p.add_argument("cycle", choices=["00", "06", "12", "18"])
        if name == "dump-download":
            p.add_argument("dump_name")
        p.add_argument("output", type=Path)
        p.add_argument("--model", choices=["gdas", "gfs"], default="gdas")
        p.add_argument("--timeout", type=float, default=60.0)
        p.add_argument("--acknowledge-restrictions", action="store_true")

    args = parser.parse_args()
    if args.command == "madis-url":
        print(madis_url(args.dataset, parse_timestamp(args.timestamp)))
    elif args.command == "madis-download":
        url = madis_url(args.dataset, parse_timestamp(args.timestamp))
        size, sha256 = download(url, args.output, timeout=args.timeout)
        print(f"saved={args.output} bytes={size} sha256={sha256} source={url}")
    elif args.command == "prepbufr-url":
        print(prepbufr_url(args.date, args.cycle, args.model))
    elif args.command == "dump-url":
        print(ncep_dump_url(args.date, args.cycle, args.dump_name, args.model))
    elif args.command == "prepbufr-download":
        _require_restriction_ack(args, parser)
        url = prepbufr_url(args.date, args.cycle, args.model)
        size, sha256 = download(url, args.output, timeout=args.timeout)
        print(f"saved={args.output} bytes={size} sha256={sha256} source={url}")
    elif args.command == "dump-download":
        _require_restriction_ack(args, parser)
        url = ncep_dump_url(args.date, args.cycle, args.dump_name, args.model)
        size, sha256 = download(url, args.output, timeout=args.timeout)
        print(f"saved={args.output} bytes={size} sha256={sha256} source={url}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
