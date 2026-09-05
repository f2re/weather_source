from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from check_endpoints import summarize_source_health


def test_source_is_healthy_if_any_endpoint_is_healthy() -> None:
    summary = summarize_source_health(
        [
            {"source_id": "alpha", "endpoint": "primary", "ok": True},
            {"source_id": "alpha", "endpoint": "docs", "ok": False},
        ]
    )

    assert summary == [
        {
            "source_id": "alpha",
            "healthy": True,
            "checked_endpoints": 2,
            "healthy_endpoints": 1,
            "failed_endpoints": ["docs"],
        }
    ]


def test_source_is_unhealthy_only_if_all_endpoints_fail() -> None:
    summary = summarize_source_health(
        [
            {"source_id": "alpha", "endpoint": "one", "ok": False},
            {"source_id": "alpha", "endpoint": "two", "ok": False},
            {"source_id": "beta", "endpoint": "main", "ok": True},
        ]
    )

    by_id = {item["source_id"]: item for item in summary}
    assert by_id["alpha"]["healthy"] is False
    assert by_id["alpha"]["failed_endpoints"] == ["one", "two"]
    assert by_id["beta"]["healthy"] is True
