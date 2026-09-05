#!/usr/bin/env python3
"""Shared catalogue loading helpers."""
from __future__ import annotations

from pathlib import Path
from typing import Any, Iterable

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CATALOG = REPO_ROOT / "catalog" / "sources.yaml"


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected a YAML mapping at the document root")
    return data


def repository_root_for(index_path: Path) -> Path:
    index_path = index_path.resolve()
    if index_path.parent.name == "catalog":
        return index_path.parent.parent
    return REPO_ROOT


def load_catalog(index_path: Path | str = DEFAULT_CATALOG) -> tuple[dict[str, Any], list[dict[str, Any]], list[Path]]:
    index_path = Path(index_path).resolve()
    index = load_yaml(index_path)
    repo_root = repository_root_for(index_path)
    source_files: list[Path] = []
    sources: list[dict[str, Any]] = []

    files = index.get("files")
    if not isinstance(files, list) or not files:
        raise ValueError(f"{index_path}: 'files' must be a non-empty list")

    for raw_path in files:
        if not isinstance(raw_path, str) or not raw_path.strip():
            raise ValueError(f"{index_path}: invalid source file entry {raw_path!r}")
        path = (repo_root / raw_path).resolve()
        try:
            path.relative_to(repo_root.resolve())
        except ValueError as exc:
            raise ValueError(f"{index_path}: source path escapes repository: {raw_path}") from exc
        if not path.is_file():
            raise FileNotFoundError(f"catalog source file not found: {path}")
        document = load_yaml(path)
        file_sources = document.get("sources")
        if not isinstance(file_sources, list):
            raise ValueError(f"{path}: 'sources' must be a list")
        for source in file_sources:
            if not isinstance(source, dict):
                raise ValueError(f"{path}: every source must be a mapping")
            item = dict(source)
            item["_catalog_file"] = str(path.relative_to(repo_root))
            sources.append(item)
        source_files.append(path)

    return index, sources, source_files


def public_source(source: dict[str, Any]) -> dict[str, Any]:
    """Remove loader-only keys before JSON-Schema validation or export."""
    return {key: value for key, value in source.items() if not key.startswith("_")}


def filter_sources(
    sources: Iterable[dict[str, Any]],
    *,
    tier: str | None = None,
    category: str | None = None,
    operational: bool | None = None,
) -> list[dict[str, Any]]:
    result = []
    for source in sources:
        if tier and source.get("tier") != tier:
            continue
        if category and category not in source.get("categories", []):
            continue
        if operational is not None and source.get("operational") is not operational:
            continue
        result.append(source)
    return result
