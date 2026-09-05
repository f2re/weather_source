#!/usr/bin/env python3
"""Download a meteorological object over HTTPS without loading it into RAM."""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

import requests

USER_AGENT = "weather-source-example/1.0 (+https://github.com/f2re/weather_source)"


def download(url: str, output: Path, timeout: float = 30.0) -> tuple[int, str]:
    output.parent.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256()
    size = 0
    with requests.get(url, stream=True, timeout=timeout, headers={"User-Agent": USER_AGENT}) as response:
        response.raise_for_status()
        with output.open("wb") as handle:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if not chunk:
                    continue
                handle.write(chunk)
                digest.update(chunk)
                size += len(chunk)
    return size, digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("output", type=Path)
    parser.add_argument("--timeout", type=float, default=30.0)
    args = parser.parse_args()
    size, sha256 = download(args.url, args.output, args.timeout)
    print(f"saved={args.output} bytes={size} sha256={sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
