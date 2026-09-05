# 🌦️ Weather Source

[![CI](https://github.com/f2re/weather_source/actions/workflows/ci.yml/badge.svg)](https://github.com/f2re/weather_source/actions/workflows/ci.yml)
[![Проверка источников](https://github.com/f2re/weather_source/actions/workflows/source-health.yml/badge.svg)](https://github.com/f2re/weather_source/actions/workflows/source-health.yml)
[![Документация](https://github.com/f2re/weather_source/actions/workflows/docs.yml/badge.svg)](https://github.com/f2re/weather_source/actions/workflows/docs.yml)
[![Лицензия: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![EN](https://img.shields.io/badge/lang-English-blue)](README.md)

> Русско-английская база знаний **оперативных источников метеорологической информации** для метеоролога, разработчика и ИИ-агента.

Цель — отвечать не только на вопрос «где взять данные», но и на инженерные вопросы: **как подписаться, скачать, декодировать, проверить свежесть, сохранить raw-поток и организовать резервирование**.

## Куда идти сначала

Для человека:

- 🇷🇺 [`docs/sources/index.ru.md`](docs/sources/index.ru.md) — полный русский каталог всех источников.
- 🇬🇧 [`docs/sources/index.en.md`](docs/sources/index.en.md) — полный английский каталог.
- 🌍 [`docs/sources/index.md`](docs/sources/index.md) — двуязычный обзор, уровни приоритета и категории.
- 📄 `docs/sources/generated/<id>.md` — подробная карточка каждого источника: русский раздел первый и самодостаточный, английский — второй.
- 🛰️ [`docs/sources/wmo-wis2.md`](docs/sources/wmo-wis2.md) — практическое руководство по WIS2.
- 🎈 [`docs/sources/aerology.md`](docs/sources/aerology.md) — аэрология и вертикальные профили.
- 🤖 [`docs/agent-guide.md`](docs/agent-guide.md) — правила поиска и выбора для ИИ-агентов.

Для программы или ИИ-агента:

- `llms.txt` — короткая карта репозитория;
- `catalog/agent-index.json` — компактный индекс для быстрого выбора;
- `catalog/sources.json` — полный плоский каталог;
- `catalog/sources.ndjson` — одна полная запись на строку для RAG/ETL;
- `catalog/sources.yaml` + `catalog/sources/*.yaml` — авторитетный источник истины;
- `catalog/schema.json` — контракт записи.

## Что записано для каждого источника

Поставщик, официальность, приоритет, семейства данных, покрытие, оперативность, периодичность, типичная задержка, глубина архива, доступ/регистрация/ключи/условия, машинные протоколы, реальные endpoints, нативные форматы, библиотеки и декодеры, официальная документация, надёжность, пригодность к автоматизации и `last_verified`.

Сгенерированная карточка дополнительно содержит отдельное русское описание, отдельное английское описание, рекомендуемый алгоритм автоматического приёма, подсказки по декодированию и правила выбора для агента.

## Быстрый каталог

| Вид данных | Основные источники | Форматы | Предпочтительный способ |
|---|---|---|---|
| 🌡️ Наземные наблюдения | WIS2, NOAA/NWS, ECCC, DWD, FMI, MeteoSwiss, JMA, BOM | BUFR, SYNOP/METAR, JSON, CSV | WIS2 MQTT+HTTPS, REST/HTTPS |
| 🎈 Аэрология | WIS2 TEMP, Росгидромет/Авиаметтелеком, IGRA, DWD, FMI, Météo-France, MeteoSwiss, ECCC | BUFR, CSV, text, NetCDF | WIS2, HTTPS, WFS |
| 📡 Радиолокация | NEXRAD/MRMS, DWD, ECCC, европейские и национальные сервисы | Level II/III, GRIB2, ODIM HDF5, GeoTIFF | S3/HTTPS, WCS/OGC |
| 🛰️ Спутники | EUMETSAT, NOAA/NODD, NASA Earthdata/LANCE, JAXA | NetCDF, HDF5, BUFR, GeoTIFF | Data Store/API, S3, HTTPS |
| ⚡ Молнии | GOES GLM, MTG LI и отдельно помеченные ограниченные/общественные сети | NetCDF/HDF5/BUFR | object storage / Data Store |
| 🌊 Океан/буи | Copernicus Marine, NDBC, Argo | NetCDF, CSV, JSON | HTTPS/API/object storage |
| 🧠 Модели/ансамбли | ECMWF Open Data, NOMADS/NODD, DWD, Météo-France, ECCC, JMA | GRIB2, NetCDF | HTTPS/S3/API |
| 🗃️ Архивы/климат | NCEI, CDS/ERA5, IGRA, национальные архивы | NetCDF, GRIB, CSV, BUFR | API/HTTPS |

## Правила выбора для оперативной системы

1. Сначала `official: true`.
2. Затем `tier: primary`.
3. Для текущих данных — `operational: true`.
4. Проверить территорию покрытия и реальные права доступа.
5. Предпочитать WIS2/MQTT, AMQP, S3/object storage, REST/OGC и прямые файловые сервисы вместо HTML-scraping.
6. Сопоставить нативный формат с нормальным декодером.
7. Сохранять raw payload до нормализации.
8. Для критического контура держать независимый fallback.

Для WMO-наблюдений сначала проверять **WIS2 core**. Для аэрологии нельзя смешивать реальные TEMP/радиозонды, AMDAR, профайлеры, спутниковые/GNSS-RO retrievals и модельные NWP-профили.

## Каталог теперь должен находиться в `main`

YAML остаётся источником истины, но человекочитаемые и агентные представления не должны существовать только во временной CI-сборке. Workflow `Sync generated catalogue` после изменения авторитетных YAML автоматически обновляет и коммитит:

- `docs/sources/index.md`;
- `docs/sources/index.ru.md`;
- `docs/sources/index.en.md`;
- `docs/sources/generated/*.md`;
- `docs/sources/categories/*.md`;
- `catalog/sources.json`;
- `catalog/sources.ndjson`;
- `catalog/agent-index.json`;
- `llms.txt`.

`python scripts/catalog_docs.py --verify` падает, если любой из этих файлов отсутствует, устарел или остался лишним после удаления источника.

## Локальная проверка

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_catalog.py
python scripts/catalog_docs.py --write
python scripts/catalog_docs.py --verify
python -m compileall -q examples scripts tests
pytest -q
mkdocs build --strict
```

Сетевой health-check вынесен отдельно:

```bash
python scripts/check_endpoints.py --catalog catalog/sources.yaml --tier primary --report source-health.json
```

## Структура

```text
catalog/                     YAML-источник истины + JSON/NDJSON для агентов
docs/sources/index*.md       полный коммитируемый каталог
docs/sources/generated/      одна подробная двуязычная карточка на источник
docs/sources/categories/     тематические каталоги
docs/agent-guide.md          правила работы ИИ-агента
examples/python/             примеры приёма и декодирования
scripts/                     валидация, генерация и health-check
tests/                       тесты каталога и примеров
.github/workflows/           CI, sync, health и публикация документации
```

## Участие и безопасность

Правила — [`CONTRIBUTING.md`](CONTRIBUTING.md), безопасность — [`SECURITY.md`](SECURITY.md). Изменять нужно авторитетную YAML-запись; generated Markdown/JSON вручную отдельно от неё не редактируются.

## Лицензия

Код и оригинальная документация — [MIT](LICENSE). Получаемые метеоданные остаются под лицензиями, условиями и требованиями атрибуции соответствующих поставщиков.
