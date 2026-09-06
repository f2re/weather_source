from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any


class CatalogueError(RuntimeError):
    """Raised when catalogue and runtime recipes are inconsistent."""


def repo_root() -> Path:
    override = os.environ.get("WEATHER_SOURCE_ROOT")
    if override:
        return Path(override).expanduser().resolve()
    return Path(__file__).resolve().parents[1]


def load_sources(root: Path | None = None) -> dict[str, dict[str, Any]]:
    root = root or repo_root()
    payload = json.loads((root / "catalog" / "sources.json").read_text(encoding="utf-8"))
    records = payload["sources"] if isinstance(payload, dict) else payload
    return {item["id"]: item for item in records}


def load_recipes(root: Path | None = None) -> dict[str, dict[str, Any]]:
    root = root or repo_root()
    recipe_dir = root / "catalog" / "recipes"
    recipes: dict[str, dict[str, Any]] = {}
    for path in sorted(recipe_dir.glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        for source_id, recipe in payload.get("sources", {}).items():
            if source_id in recipes:
                raise CatalogueError(f"Дублирующий runtime-рецепт {source_id}: {path}")
            recipe = dict(recipe)
            recipe["_recipe_file"] = str(path.relative_to(root))
            recipes[source_id] = recipe
    if not recipes:
        raise CatalogueError(f"Runtime-рецепты не найдены в {recipe_dir}")
    return recipes


def get_source(source_id: str, root: Path | None = None) -> tuple[dict[str, Any], dict[str, Any]]:
    sources = load_sources(root)
    recipes = load_recipes(root)
    if source_id not in sources:
        raise CatalogueError(f"Неизвестный source id: {source_id}")
    if source_id not in recipes:
        raise CatalogueError(f"Для {source_id} отсутствует runtime-рецепт")
    return sources[source_id], recipes[source_id]


def validate_runtime_contract(root: Path | None = None) -> list[str]:
    sources = load_sources(root)
    recipes = load_recipes(root)
    errors: list[str] = []

    missing = sorted(set(sources) - set(recipes))
    extra = sorted(set(recipes) - set(sources))
    if missing:
        errors.append("Нет рецептов: " + ", ".join(missing))
    if extra:
        errors.append("Рецепты без источников: " + ", ".join(extra))

    valid_statuses = {"public", "credentials", "restricted", "manual"}
    valid_adapters = {
        "http",
        "html_latest",
        "ftp",
        "s3_latest",
        "wis2",
        "amqp",
        "external",
        "unavailable",
    }
    for source_id, recipe in sorted(recipes.items()):
        status = recipe.get("status")
        adapter = recipe.get("adapter")
        if status not in valid_statuses:
            errors.append(f"{source_id}: неизвестный status={status!r}")
        if adapter not in valid_adapters:
            errors.append(f"{source_id}: неизвестный adapter={adapter!r}")
        if not recipe.get("verified"):
            errors.append(f"{source_id}: нет verified")
        if not recipe.get("example_ru"):
            errors.append(f"{source_id}: нет example_ru")
        if status == "public" and adapter == "unavailable":
            errors.append(f"{source_id}: public не может иметь unavailable adapter")
        if status == "restricted" and adapter not in {"unavailable", "external", "wis2"}:
            errors.append(f"{source_id}: restricted требует явного ограниченного адаптера")
        if adapter != "unavailable" and not recipe.get("request"):
            errors.append(f"{source_id}: для adapter={adapter} отсутствует request")

    return errors
