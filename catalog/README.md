# Каталог / Catalogue

`catalog/` — авторитетный машиночитаемый слой проекта Weather Source.

## Точка входа

`catalog/sources.yaml` содержит версию каталога, дату ревизии, число источников и список доменных YAML-файлов. Полные записи находятся в `catalog/sources/*.yaml`.

## Генерируемые представления

После каждого изменения YAML workflow `Sync generated catalogue` обновляет и коммитит:

- `catalog/sources.json` — полный плоский JSON со всеми источниками;
- `catalog/sources.ndjson` — одна запись на строку, удобно для RAG/ETL/streaming;
- `catalog/agent-index.json` — компактный индекс для быстрого выбора источника агентом;
- `docs/sources/index*.md` — человекочитаемые каталоги;
- `docs/sources/generated/*.md` — подробные карточки;
- `docs/sources/categories/*.md` — тематические выборки;
- `llms.txt` — краткая точка входа для LLM.

Эти файлы **не редактируются вручную**. Редактировать нужно соответствующую запись YAML, затем выполнить:

```bash
python scripts/validate_catalog.py
python scripts/catalog_docs.py --write
python scripts/catalog_docs.py --verify
```

`catalog_docs.py` — стабильный фронтенд генерации: он использует общий движок `generate_docs.py`, но одновременно нормализует ссылки для прямого просмотра в GitHub и для строгой сборки MkDocs.

## Поля записи

Схема находится в `catalog/schema.json`. Основные поля:

- `id` — стабильный идентификатор;
- `provider` — владелец/центр;
- `name.en`, `name.ru` — двуязычное имя;
- `summary.en`, `summary.ru` — краткое описание;
- `official` — официальный ли это первичный источник;
- `tier` — primary / secondary / specialized / aggregator;
- `categories` — типы данных;
- `coverage` — географическое покрытие;
- `operational` — пригодность для текущего оперативного потока;
- `update_cadence`, `typical_latency`, `archive` — временные характеристики;
- `access` — уровень доступа, авторизация и условия;
- `protocols` — машинные протоколы;
- `formats` — нативные форматы;
- `endpoints` — реальные точки доступа/документации;
- `software` — клиенты, библиотеки, декодеры;
- `documentation` — официальные руководства;
- `reliability`, `automation` — инженерная оценка;
- `last_verified` — дата последней проверки;
- `notes.en`, `notes.ru` — эксплуатационные замечания.

## Правило для ИИ-агента

Для выбора источника сначала использовать `catalog/agent-index.json`, затем раскрывать выбранный `id` в `catalog/sources.json`. Markdown нужен для объяснения человеку, но YAML остаётся источником истины.

## English

The YAML records under `catalog/sources/` are authoritative. JSON/NDJSON, source cards, category pages and `llms.txt` are deterministic generated views and must never be hand-edited independently from the YAML catalogue. Use `scripts/catalog_docs.py` as the public generation/verification interface.
