#!/usr/bin/env python3
"""Open a GRIB/GRIB2 file with xarray+cfgrib and print a compact inventory."""
from __future__ import annotations

import argparse
from pathlib import Path

import xarray as xr


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--filter-key", action="append", default=[], help="cfgrib filter key as name=value")
    args = parser.parse_args()

    filter_by_keys = {}
    for raw in args.filter_key:
        key, separator, value = raw.partition("=")
        if not separator:
            parser.error(f"invalid --filter-key {raw!r}; expected name=value")
        filter_by_keys[key] = value

    backend_kwargs = {"indexpath": ""}
    if filter_by_keys:
        backend_kwargs["filter_by_keys"] = filter_by_keys
    dataset = xr.open_dataset(args.file, engine="cfgrib", backend_kwargs=backend_kwargs)
    try:
        print(dataset)
        print("variables:", ", ".join(dataset.data_vars))
    finally:
        dataset.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
