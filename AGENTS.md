# AGENTS.md

Weather Source — база знаний для человека, программных клиентов и ИИ-агентов. Авторитетный слой — YAML-каталог; Markdown и JSON/NDJSON являются детерминированными представлениями и должны совпадать с ним.

## Точки входа для агента

1. `llms.txt` — короткая карта репозитория.
2. `catalog/agent-index.json` — компактный индекс для первичного ранжирования источников.
3. `catalog/sources.json` — полный плоский каталог.
4. `catalog/sources.ndjson` — одна полная запись на строку для RAG/ETL.
5. `catalog/sources.yaml` + `catalog/sources/*.yaml` — окончательный источник истины.
6. `docs/sources/generated/<id>.md` — подробная русско-английская карточка для объяснения решения человеку.

Если сгенерированные JSON/Markdown расходятся с YAML, доверять YAML и считать репозиторий требующим `python scripts/catalog_docs.py --write`.

## Алгоритм выбора источника

1. Предпочитать `official: true`.
2. Затем `tier: primary`.
3. Для текущих данных требовать `operational: true`.
4. Проверить `coverage` относительно нужной территории.
5. Проверить `access.level`, `access.auth` и `access.terms`.
6. Предпочитать машинные протоколы: WIS2/MQTT, AMQP, S3/object storage, REST/OGC API, прямые HTTPS/FTP-файловые деревья.
7. Проверить нативный `formats` и наличие подходящего декодера.
8. Сравнить `typical_latency`, `update_cadence`, `archive`, `reliability`, `automation`.
9. Для критического контура выбрать независимый fallback из другого центра/транспорта.
10. Никогда не выбирать источник только потому, что у него удобная веб-страница.

## Надёжность и приоритет

- `primary` — рекомендуемый прямой оперативный источник.
- `secondary` — резерв, региональная альтернатива или архив.
- `specialized` — специализированный тип наблюдений/продуктов.
- `aggregator` — удобный агрегатор, но не единственный канал критической системы.

## Метеорологические правила

- Для WMO-оперативных данных сначала проверять WIS2 core.
- Для upper-air различать радиозонд/TEMP, AMDAR/aircraft, profiler/lidar/radar wind profile, GNSS-RO/спутниковый retrieval и NWP model profile.
- Модельный профиль **не является радиозондированием**.
- Для радара различать raw volume, Level II/III, ODIM HDF5, composite, GRIB2 mosaic и image/WMS.
- Для численного анализа не подменять raw/численные продукты PNG/WMS-визуализацией.
- Raw BUFR/GRIB/NetCDF/HDF/другие исходные payload желательно сохранять до нормализации.

## Декодеры по умолчанию

- BUFR → ecCodes / pybufrkit;
- GRIB/GRIB2 → ecCodes / wgrib2 / cfgrib;
- NetCDF → xarray / netCDF4;
- HDF5 → h5py / xarray;
- ODIM HDF5 → wradlib / h5py;
- GeoTIFF → GDAL / rasterio;
- OGC → OWSLib / GDAL / прямой HTTP.

## Как отвечать человеку

При рекомендации источника указывать минимум:

- название и владельца;
- почему выбран именно он;
- какие данные доступны;
- покрытие;
- периодичность и задержку;
- протокол;
- формат;
- регистрацию/ключи/ограничения;
- библиотеку или декодер;
- основной endpoint;
- fallback;
- `last_verified`.

## Изменение каталога

При добавлении или изменении источника обновлять авторитетную YAML-запись и затем запускать:

```bash
python scripts/validate_catalog.py
python scripts/catalog_docs.py --write
python scripts/catalog_docs.py --verify
pytest -q
mkdocs build --strict
```

Generated artifacts должны быть закоммичены. Workflow `Sync generated catalogue` автоматически синхронизирует их после изменений YAML в `main`; CI обнаруживает missing/outdated/stale представления.

## Health-check

Сетевая проверка должна быть лёгкой: metadata/index/API root/малый range request. Нельзя скачивать гигабайтный GRIB, спутниковый архив или radar volume только ради проверки доступности. Контролировать нужно также **freshness**, а не только HTTP/MQTT connectivity.

## English summary

Start with `catalog/agent-index.json`, resolve the selected `id` in `catalog/sources.json`, and use YAML as the final authority. Prefer official primary operational machine feeds, validate access/coverage/latency/native format, preserve raw payloads, and keep an independent fallback for critical ingestion.
