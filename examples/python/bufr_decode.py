#!/usr/bin/env python3
"""Inspect selected keys from each BUFR message using ecCodes Python bindings."""
from __future__ import annotations

import argparse
from pathlib import Path

from eccodes import codes_bufr_new_from_file, codes_get, codes_release, codes_set

DEFAULT_KEYS = [
    "edition",
    "masterTablesVersionNumber",
    "dataCategory",
    "dataSubCategory",
    "typicalYear",
    "typicalMonth",
    "typicalDay",
    "typicalHour",
]


def decode(path: Path, keys: list[str]) -> None:
    with path.open("rb") as handle:
        number = 0
        while True:
            message = codes_bufr_new_from_file(handle)
            if message is None:
                break
            number += 1
            try:
                codes_set(message, "unpack", 1)
                values = {}
                for key in keys:
                    try:
                        values[key] = codes_get(message, key)
                    except Exception as exc:
                        values[key] = f"<unavailable: {type(exc).__name__}>"
                print(f"message={number} {values}")
            finally:
                codes_release(message)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--key", action="append", dest="keys")
    args = parser.parse_args()
    decode(args.file, args.keys or DEFAULT_KEYS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
