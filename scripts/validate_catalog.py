#!/usr/bin/env python3
"""Validate catalogue structure and operational invariants."""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import date
from pathlib import Path

from jsonschema import Draft202012Validator

from catalog_lib import DEFAULT_CATALOG, load_catalog, load_yaml, public_source

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = REPO_ROOT / "catalog" / "schema.json"


def validate_catalog(catalog_path: Path, schema_path: Path) -> list[str]:
    errors: list[str] = []
    index, sources, source_files = load_catalog(catalog_path)
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)

    for source_file in source_files:
        document = load_yaml(source_file)
        for error in sorted(validator.iter_errors(document), key=lambda item: list(item.path)):
            location = ".".join(str(part) for part in error.absolute_path) or "<root>"
            errors.append(f"{source_file}: {location}: {error.message}")

    declared = index.get("source_count")
    if declared != len(sources):
        errors.append(f"catalog source_count={declared!r}, but loaded {len(sources)} sources")

    ids = [source.get("id") for source in sources]
    duplicates = sorted(source_id for source_id, count in Counter(ids).items() if count > 1)
    if duplicates:
        errors.append("duplicate source ids: " + ", ".join(str(item) for item in duplicates))

    today = date.today()
    for source in sources:
        source_id = source.get("id", "<missing-id>")
        if source.get("tier") == "primary" and source.get("official") is not True:
            errors.append(f"{source_id}: primary source must be official")
        if source.get("tier") == "aggregator" and source.get("official") is not False:
            errors.append(f"{source_id}: aggregator must have official: false")
        if source.get("operational") and source.get("automation") == "low" and source.get("tier") == "primary":
            errors.append(f"{source_id}: primary operational source cannot have low automation")

        docs = source.get("documentation", [])
        if not docs:
            errors.append(f"{source_id}: at least one official/reference documentation URL is required")

        for endpoint in source.get("endpoints", []):
            if endpoint.get("healthcheck") and not str(endpoint.get("url", "")).startswith(("http://", "https://")):
                errors.append(f"{source_id}: healthcheck endpoint must be HTTP(S): {endpoint.get('url')}")

        raw_verified = source.get("last_verified")
        try:
            verified = date.fromisoformat(str(raw_verified))
        except ValueError:
            errors.append(f"{source_id}: invalid last_verified date: {raw_verified!r}")
        else:
            if verified > today:
                errors.append(f"{source_id}: last_verified is in the future: {verified.isoformat()}")

        cleaned = public_source(source)
        if any(key.startswith("_") for key in cleaned):
            errors.append(f"{source_id}: internal loader metadata leaked into public record")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    args = parser.parse_args()

    try:
        errors = validate_catalog(args.catalog, args.schema)
    except Exception as exc:  # fail with a compact actionable message in CI
        print(f"catalog validation failed to start: {exc}", file=sys.stderr)
        return 2

    if errors:
        print(f"catalog validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    index, sources, files = load_catalog(args.catalog)
    print(f"OK: {len(sources)} sources in {len(files)} files; catalogue v{index.get('catalog_version')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
