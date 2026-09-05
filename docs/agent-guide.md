# 🤖 Руководство для ИИ-агентов / AI agent guide

Этот репозиторий рассчитан не только на человека, но и на автоматический выбор источников программными и ИИ-агентами.

## Что считать источником истины

1. `catalog/sources.yaml` — точка входа и перечень файлов каталога.
2. `catalog/sources/*.yaml` — авторитетные записи источников.
3. `catalog/schema.json` — контракт записи.
4. `catalog/sources.json` — автоматически генерируемое плоское представление полного каталога.
5. `catalog/sources.ndjson` — по одной записи на строку для RAG, потоковой обработки и индексирования.
6. `catalog/agent-index.json` — компактный индекс для первичного выбора.

Markdown-карточки в `docs/sources/generated/` являются детерминированным представлением YAML и удобны для объяснения решения человеку, но не должны переопределять YAML.

## Алгоритм выбора источника

Для оперативного контура агент должен последовательно фильтровать:

1. `official == true`;
2. `tier == primary`;
3. `operational == true`, если нужны текущие данные;
4. подходящее `coverage`;
5. допустимый `access.level` и реальная схема `access.auth`;
6. подходящий машинный `protocols`;
7. нативный `formats`, для которого доступен декодер;
8. `typical_latency`, `update_cadence`, `archive`;
9. `reliability` и `automation`;
10. независимый fallback из другого центра или транспорта.

Нельзя выбирать источник только по известности бренда или удобству веб-страницы.

## Приоритет транспорта

Для автоматизации предпочтителен следующий порядок:

- WIS2/MQTT + HTTPS payload;
- AMQP push;
- S3/object storage;
- REST/OGC API;
- прямое HTTPS/FTP-файловое дерево;
- агрегатор;
- HTML scraping — только как крайний вариант и обычно не должен попадать в production.

## Как работать с форматами

- `BUFR` → ecCodes, pybufrkit;
- `GRIB/GRIB2` → ecCodes, wgrib2, cfgrib/xarray;
- `NetCDF` → xarray, netCDF4;
- `HDF5` → h5py/xarray;
- `ODIM HDF5` → wradlib/h5py;
- `GeoTIFF` → GDAL/rasterio;
- `JSON/GeoJSON` → requests + json/geopandas;
- `WFS/WCS/WMS/OGC API` → OWSLib, GDAL и прямые HTTP-запросы.

Raw payload желательно сохранять до нормализации. Нормализованные таблицы/массивы не должны быть единственной копией исходных метеоданных.

## Аэрология

Нужно различать четыре класса вертикальных профилей:

1. реальные радиозонды/TEMP;
2. авиационные AMDAR/ACARS-профили;
3. профайлеры и lidar/radar wind profiles;
4. спутниковые/GNSS-RO retrievals.

Модельный профиль NWP не является радиозондом и не должен так называться.

Для глобального оперативного TEMP сначала проверять WIS2. IGRA/Wyoming полезны как независимый fallback/архив, но не должны автоматически подменять основной WIS2-поток.

## Пример запроса агента: «нужна аэрология России»

1. Найти записи с `upper-air`.
2. Оставить `operational=true`.
3. Предпочесть `wmo-wis2` и `ru-aviamettelecom-wis2-temp`.
4. Проверить текущую тему WIS2 и publisher metadata.
5. Использовать ecCodes для BUFR.
6. Для контроля полноты подключить IGRA/Wyoming как независимый канал.

## Пример: «нужен радар для nowcasting»

Не достаточно категории `radar`. Агент обязан определить, что именно даёт endpoint:

- raw volume;
- Level II/III;
- ODIM HDF5;
- национальный composite;
- GRIB2 mosaic;
- WMS/PNG visualization.

Для численного nowcasting raw/composite data предпочтительнее картинок.

## Ответ человеку

При рекомендации источника агент должен кратко назвать:

- источник и владельца;
- почему он выбран;
- что именно доступно;
- задержку и периодичность;
- протокол и формат;
- нужна ли регистрация;
- библиотеку/декодер;
- основной endpoint;
- fallback;
- дату `last_verified`.

## English summary

Use `catalog/agent-index.json` for fast ranking and resolve the selected `id` in `catalog/sources.json` for complete details. Prefer official primary operational machine feeds, validate access/coverage/latency/format, preserve raw payloads and keep an independent fallback for critical pipelines.
