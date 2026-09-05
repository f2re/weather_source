#!/usr/bin/env python3
"""Inspect a NetCDF meteorological dataset with xarray without eagerly loading it."""
from __future__ import annotations

import argparse
from pathlib import Path

import xarray as xr


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--group", help="optional NetCDF/HDF group")
    args = parser.parse_args()

    kwargs = {"decode_cf": True}
    if args.group:
        kwargs["group"] = args.group
    dataset = xr.open_dataset(args.file, **kwargs)
    try:
        print(dataset)
        print("dimensions:", dict(dataset.sizes))
        print("variables:", ", ".join(dataset.data_vars))
        print("coordinates:", ", ".join(dataset.coords))
    finally:
        dataset.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
