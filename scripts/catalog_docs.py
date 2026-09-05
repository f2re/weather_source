#!/usr/bin/env python3
"""Stable front-end for generated catalogue artifacts.

The main rendering engine lives in generate_docs.py. This module applies the
path rules that differ between GitHub's repository view and MkDocs' docs root,
then delegates all CLI modes (--check/--write/--verify) to the same engine.
"""
from __future__ import annotations

import generate_docs as engine

GITHUB_BLOB = "https://github.com/f2re/weather_source/blob/main"

_original_render_category = engine.render_category
_original_render_landing = engine.render_landing


def render_category(category, sources):
    """Category files live one directory below source indexes."""
    text = _original_render_category(category, sources)
    return text.replace("](generated/", "](../generated/")


def render_landing(sources, index):
    """Links outside docs/ must be absolute for both GitHub and MkDocs."""
    text = _original_render_landing(sources, index)
    replacements = {
        "(../../catalog/sources.json)": f"({GITHUB_BLOB}/catalog/sources.json)",
        "(../../catalog/sources.ndjson)": f"({GITHUB_BLOB}/catalog/sources.ndjson)",
        "(../../catalog/agent-index.json)": f"({GITHUB_BLOB}/catalog/agent-index.json)",
        "(../../llms.txt)": f"({GITHUB_BLOB}/llms.txt)",
    }
    for before, after in replacements.items():
        text = text.replace(before, after)
    return text


engine.render_category = render_category
engine.render_landing = render_landing

if __name__ == "__main__":
    raise SystemExit(engine.main())
