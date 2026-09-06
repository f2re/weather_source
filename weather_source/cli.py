from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .adapters import FetchError, fetch, probe
from .catalog import CatalogueError, get_source, load_recipes, load_sources, validate_runtime_contract


def _print_source(source: dict, recipe: dict) -> None:
    print(f"{source['id']} — {source['name']['ru']}")
    print(f"Поставщик: {source['provider']}")
    print(f"Статус доступа: {recipe['status']} | adapter: {recipe['adapter']} | verified: {recipe['verified']}")
    print(f"Каталог: tier={source['tier']} operational={source['operational']} access={source['access']['level']}")
    print(f"Описание: {source['summary']['ru']}")
    print(f"Практический пример: {recipe['example_ru']}")
    if recipe.get('env'):
        print("Переменные окружения: " + ", ".join(recipe['env']))
    if recipe.get('reason_ru'):
        print("Ограничение: " + recipe['reason_ru'])
    if recipe.get('fallback'):
        print("Резерв: " + recipe['fallback'])


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m weather_source",
        description="Получение метеоданных из конкретного источника каталога Weather Source.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    list_cmd = sub.add_parser("list", help="показать все source id и runtime-статус")
    list_cmd.add_argument("--status", choices=["public", "credentials", "restricted", "manual"])

    describe = sub.add_parser("describe", help="показать карточку подключения источника")
    describe.add_argument("source_id")

    example = sub.add_parser("example", help="показать конкретный рабочий пример")
    example.add_argument("source_id")

    probe_cmd = sub.add_parser("probe", help="лёгкая проверка machine endpoint")
    probe_cmd.add_argument("source_id")
    probe_cmd.add_argument("--timeout", type=float, default=12.0)

    fetch_cmd = sub.add_parser("fetch", help="получить данные из конкретного источника")
    fetch_cmd.add_argument("source_id")
    fetch_cmd.add_argument("--output", type=Path)
    fetch_cmd.add_argument("--timeout", type=float, default=30.0)
    fetch_cmd.add_argument("--full", action="store_true", help="разрешить полный крупный продукт")
    fetch_cmd.add_argument(
        "--allow-external",
        action="store_true",
        help="разрешить запуск официального внешнего CLI/клиента из рецепта",
    )

    sub.add_parser("verify-recipes", help="проверить покрытие всех источников рецептами")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "list":
            sources = load_sources()
            recipes = load_recipes()
            for source_id in sorted(sources):
                recipe = recipes[source_id]
                if args.status and recipe["status"] != args.status:
                    continue
                print(
                    f"{source_id:32} {recipe['status']:11} {recipe['adapter']:12} "
                    f"{sources[source_id]['name']['ru']}"
                )
            return 0

        if args.command == "verify-recipes":
            errors = validate_runtime_contract()
            if errors:
                for error in errors:
                    print("ERROR:", error, file=sys.stderr)
                return 1
            print(f"OK: {len(load_recipes())} runtime-рецептов совпадают с каталогом")
            return 0

        source, recipe = get_source(args.source_id)
        if args.command == "describe":
            _print_source(source, recipe)
            return 0
        if args.command == "example":
            print(recipe["example_ru"])
            if recipe.get("command"):
                print("\nКоманда/код:\n" + recipe["command"])
            if recipe.get("env"):
                print("\nТребуется: " + ", ".join(recipe["env"]))
            if recipe.get("fallback"):
                print("\nFallback: " + recipe["fallback"])
            return 0
        if args.command == "probe":
            ok, message = probe(recipe, timeout=args.timeout)
            print(("OK: " if ok else "FAIL: ") + message)
            return 0 if ok else 2
        if args.command == "fetch":
            result = fetch(
                args.source_id,
                recipe,
                output=args.output,
                timeout=args.timeout,
                full=args.full,
                allow_external=args.allow_external,
            )
            print(
                json.dumps(
                    {
                        "source_id": result.source_id,
                        "adapter": result.adapter,
                        "url": result.url,
                        "path": str(result.path) if result.path else None,
                        "bytes": result.bytes_written,
                        "metadata": result.metadata,
                    },
                    ensure_ascii=False,
                    indent=2,
                    default=str,
                )
            )
            return 0
    except (CatalogueError, FetchError, KeyError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
