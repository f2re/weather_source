#!/usr/bin/env python3
"""Generate bilingual Markdown source cards from the machine-readable catalogue."""
from __future__ import annotations

import argparse
import shutil
import tempfile
from collections import defaultdict
from pathlib import Path

from catalog_lib import DEFAULT_CATALOG, REPO_ROOT, load_catalog

DEFAULT_OUTPUT = REPO_ROOT / "docs" / "sources" / "generated"


def md_link(label: str, url: str) -> str:
    return f"[{label}]({url})"


def render_source(source: dict) -> str:
    name = source["name"]
    summary = source["summary"]
    notes = source["notes"]
    lines = [
        f"# {name['en']} / {name['ru']}",
        "",
        f"**ID:** `{source['id']}`  ",
        f"**Provider / Поставщик:** {source['provider']}  ",
        f"**Tier / Приоритет:** `{source['tier']}`  ",
        f"**Official / Официальный:** {'yes' if source['official'] else 'no'}  ",
        f"**Operational / Оперативный:** {'yes' if source['operational'] else 'no'}  ",
        f"**Last verified / Проверено:** {source['last_verified']}",
        "",
        "## Summary / Описание",
        "",
        summary["en"],
        "",
        summary["ru"],
        "",
        "## Data characteristics / Характеристики данных",
        "",
        f"- **Categories / Категории:** {', '.join(f'`{x}`' for x in source['categories'])}",
        f"- **Coverage / Покрытие:** {source['coverage']}",
        f"- **Update cadence / Периодичность:** {source['update_cadence']}",
        f"- **Typical latency / Типичная задержка:** {source['typical_latency']}",
        f"- **Archive / Архив:** {source['archive']}",
        f"- **Formats / Форматы:** {', '.join(f'`{x}`' for x in source['formats'])}",
        f"- **Protocols / Протоколы:** {', '.join(f'`{x}`' for x in source['protocols'])}",
        "",
        "## Access / Доступ",
        "",
        f"- **Level / Уровень:** `{source['access']['level']}`",
        f"- **Authentication / Авторизация:** {source['access']['auth']}",
        f"- **Terms / Условия:** {source['access']['terms']}",
        f"- **Reliability / Надёжность:** `{source['reliability']}`",
        f"- **Automation / Автоматизация:** `{source['automation']}`",
        "",
        "## Endpoints / Точки доступа",
        "",
        "| Name | Protocol | Role | Health check | URL |",
        "|---|---|---|---:|---|",
    ]
    for endpoint in source["endpoints"]:
        lines.append(
            f"| {endpoint['name']} | `{endpoint['protocol']}` | {endpoint['role']} | "
            f"{'yes' if endpoint['healthcheck'] else 'no'} | {md_link('open', endpoint['url']) if endpoint['url'].startswith(('http://', 'https://')) else f'`{endpoint[\"url\"]}`'} |"
        )

    lines += ["", "## Software and decoders / ПО и декодеры", ""]
    if source["software"]:
        for item in source["software"]:
            lines.append(f"- {md_link(item['name'], item['url'])} — {item['role']}")
    else:
        lines.append("- No dedicated client recorded / Специализированный клиент пока не указан.")

    lines += ["", "## Official/reference documentation / Документация", ""]
    for url in source["documentation"]:
        lines.append(f"- {md_link(url, url)}")

    lines += ["", "## Operational notes / Операционные заметки", "", notes["en"], "", notes["ru"], ""]
    return "\n".join(lines)


def render_index(sources: list[dict]) -> str:
    groups: dict[str, list[dict]] = defaultdict(list)
    for source in sources:
        primary_category = source["categories"][0]
        groups[primary_category].append(source)

    lines = [
        "# Source catalogue / Каталог источников",
        "",
        "This index is generated from `catalog/sources.yaml` and its domain files. / Этот индекс генерируется из машиночитаемого каталога.",
        "",
        f"**Sources / Источников:** {len(sources)}",
        "",
    ]
    for category in sorted(groups):
        lines += [f"## {category}", "", "| Source | Tier | Access | Operational | Coverage |", "|---|---|---|---:|---|"]
        for source in sorted(groups[category], key=lambda item: item["id"]):
            link = f"generated/{source['id']}.md"
            title = f"{source['name']['en']} / {source['name']['ru']}"
            lines.append(
                f"| [{title}]({link}) | `{source['tier']}` | `{source['access']['level']}` | "
                f"{'yes' if source['operational'] else 'no'} | {source['coverage']} |"
            )
        lines.append("")
    return "\n".join(lines)


def generate(output: Path, index_output: Path, catalog_path: Path) -> int:
    _, sources, _ = load_catalog(catalog_path)
    output.mkdir(parents=True, exist_ok=True)
    for stale in output.glob("*.md"):
        stale.unlink()
    for source in sources:
        (output / f"{source['id']}.md").write_text(render_source(source), encoding="utf-8")
    index_output.parent.mkdir(parents=True, exist_ok=True)
    index_output.write_text(render_index(sources), encoding="utf-8")
    return len(sources)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--output", type=Path)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="write generated pages under docs/sources")
    mode.add_argument("--check", action="store_true", help="render to a temporary directory and verify generation")
    args = parser.parse_args()

    if args.write:
        output = args.output or DEFAULT_OUTPUT
        index_output = output.parent / "index.md"
        count = generate(output, index_output, args.catalog)
        print(f"Generated {count} source cards in {output}")
        return 0

    if args.output:
        output = args.output
        index_output = output.parent / "index.md"
        count = generate(output, index_output, args.catalog)
        print(f"Generated {count} source cards in {output}")
        return 0

    with tempfile.TemporaryDirectory(prefix="weather-source-docs-") as temp_dir:
        root = Path(temp_dir)
        count = generate(root / "generated", root / "index.md", args.catalog)
        generated = list((root / "generated").glob("*.md"))
        if len(generated) != count or not (root / "index.md").is_file():
            raise RuntimeError("documentation generation produced an incomplete output set")
        shutil.rmtree(root / "generated")
    print(f"OK: generated {count} source cards in check mode")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
