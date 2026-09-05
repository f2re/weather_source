#!/usr/bin/env python3
"""Check lightweight HTTP(S) catalogue endpoints and write a JSON report."""
from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

from catalog_lib import DEFAULT_CATALOG, filter_sources, load_catalog

USER_AGENT = "weather-source-health/1.0 (+https://github.com/f2re/weather_source)"


def probe(url: str, timeout: float) -> tuple[bool, int | None, float, str | None]:
    started = time.monotonic()
    try:
        response = requests.get(
            url,
            timeout=timeout,
            allow_redirects=True,
            stream=True,
            headers={"User-Agent": USER_AGENT, "Range": "bytes=0-1023"},
        )
        status = response.status_code
        response.close()
        elapsed = time.monotonic() - started
        ok = 200 <= status < 400 or status == 416
        return ok, status, elapsed, None if ok else f"HTTP {status}"
    except requests.RequestException as exc:
        return False, None, time.monotonic() - started, f"{type(exc).__name__}: {exc}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--tier", choices=["primary", "secondary", "specialized", "aggregator"])
    parser.add_argument("--category")
    parser.add_argument("--retries", type=int, default=2)
    parser.add_argument("--timeout", type=float, default=12.0)
    parser.add_argument("--report", type=Path, default=Path("source-health.json"))
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    if args.retries < 1 or args.timeout <= 0:
        parser.error("retries must be >= 1 and timeout must be > 0")

    _, sources, _ = load_catalog(args.catalog)
    sources = filter_sources(sources, tier=args.tier, category=args.category)
    results = []

    for source in sources:
        for endpoint in source.get("endpoints", []):
            url = str(endpoint.get("url", ""))
            if not endpoint.get("healthcheck") or not url.startswith(("http://", "https://")):
                continue
            attempts = []
            for attempt in range(1, args.retries + 1):
                ok, status, elapsed, error = probe(url, args.timeout)
                attempts.append({
                    "attempt": attempt,
                    "ok": ok,
                    "status": status,
                    "latency_ms": round(elapsed * 1000, 1),
                    "error": error,
                })
                if ok:
                    break
                if attempt < args.retries:
                    time.sleep(min(2 ** (attempt - 1), 4))
            final = attempts[-1]
            item = {
                "source_id": source["id"],
                "tier": source["tier"],
                "endpoint": endpoint["name"],
                "url": url,
                "ok": final["ok"],
                "status": final["status"],
                "latency_ms": final["latency_ms"],
                "error": final["error"],
                "attempts": attempts,
            }
            results.append(item)
            marker = "OK" if item["ok"] else "FAIL"
            print(f"[{marker}] {item['source_id']} :: {item['endpoint']} :: {item['status']}")

    failures = [item for item in results if not item["ok"]]
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "checked": len(results),
        "healthy": len(results) - len(failures),
        "failed": len(failures),
        "results": results,
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Report: {args.report} ({report['healthy']}/{report['checked']} healthy)")
    return 1 if args.strict and failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
