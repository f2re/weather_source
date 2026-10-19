# NOAA/NCEP MADIS — оперативные наблюдения / NOAA/NCEP MADIS observations

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`noaa-ncep-madis` · 🟢 **основной / primary** · оперативный / operational · проверено / verified **2026-10-19**

---

## 🇷🇺 Русский

### Что это

Система интеграции и контроля качества наблюдений из множества сетей: METAR, mesonet, maritime, радиозонды, профайлеры, самолётные и другие данные, преимущественно в netCDF.

**Поставщик:** NOAA/NWS/NCEP Meteorological Assimilation Data Ingest System (MADIS)  
**Статус:** официальный источник; приоритет — **основной**.  
**Категории:** Наземные наблюдения, Аэрология и верхняя атмосфера, Авиационные наблюдения, Морские наблюдения, Профайлеры.  

### Что можно получить и когда использовать

MADIS особенно полезен как нормализованный многосетевой источник с флагами поставщика и QC. Нельзя считать все наборы MADIS автоматически неограниченными — права на конкретный dataset необходимо проверять до перераспространения.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global database with highest density over North America |
| Периодичность/режим обновления | continuous / dataset dependent |
| Типичная задержка | near-real-time for supported operational feeds |
| Архив | saved real-time archive available by dataset and date; access conditions vary |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https`, `ftp`, `opendap`, `ldm` |
| Форматы | `NetCDF`, `CSV`, `XML`, `text` |

### Доступ и ограничения

- **Уровень доступа:** бесплатный после регистрации (`registration`).
- **Авторизация:** public sample/current files exist, while sustained real-time, archive, FTP, OPeNDAP or viewer access may require a MADIS account/request.
- **Лицензия/условия:** NOAA/NCEP MADIS terms and per-dataset restrictions.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| MADIS overview | `https` | service documentation | да | [открыть / open](https://madis.ncep.noaa.gov/) |
| MADIS public sample/current data | `https` | public sample and current dataset tree | да | [открыть / open](https://madis-data.ncep.noaa.gov/madisPublic1/data/) |
| MADIS data application | `https` | access request for sustained real-time or archive services | да | [открыть / open](https://madis.ncep.noaa.gov/data_application.shtml) |

### ПО, библиотеки и декодеры

- [xarray](https://github.com/pydata/xarray) — netCDF inspection and normalization.
- [netCDF4-python](https://github.com/Unidata/netcdf4-python) — netCDF reader.
- **Быстрый выбор декодера по формату:** xarray / netCDF4, pandas / csv, lxml / ElementTree.

### Рекомендуемый алгоритм автоматического приёма

1. Забирать данные напрямую с официального HTTPS/FTP-файлового дерева, не парся HTML-визуализатор.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: xarray / netCDF4, pandas / csv, lxml / ElementTree.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://madis.ncep.noaa.gov/madis_ui.shtml](https://madis.ncep.noaa.gov/madis_ui.shtml)
- [https://madis.ncep.noaa.gov/madis_datasets.shtml](https://madis.ncep.noaa.gov/madis_datasets.shtml)
- [https://madis.ncep.noaa.gov/madis_sample_data.shtml](https://madis.ncep.noaa.gov/madis_sample_data.shtml)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/noaa-observations.yaml` → `id: noaa-ncep-madis`.
- Для оперативного контура учитывать: `tier=primary`, `operational=true`, `access.level=registration`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

Multi-network observation ingest, integration and quality-control system covering surface, mesonet, maritime, radiosonde, profiler, aircraft and other datasets, primarily in netCDF.

**Provider:** NOAA/NWS/NCEP Meteorological Assimilation Data Ingest System (MADIS)  
**Status:** official; tier **primary**.  
**Categories:** surface, upper-air, aircraft, marine, profilers.  

### What it provides and when to use it

MADIS is especially valuable when a normalized multi-network feed with provider and QC flags is needed. Do not assume every MADIS dataset is unrestricted; check dataset-specific rights before redistribution.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global database with highest density over North America |
| Update cadence | continuous / dataset dependent |
| Typical latency | near-real-time for supported operational feeds |
| Archive | saved real-time archive available by dataset and date; access conditions vary |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https`, `ftp`, `opendap`, `ldm` |
| Formats | `NetCDF`, `CSV`, `XML`, `text` |

### Access and restrictions

- **Access level:** `registration`.
- **Authentication:** public sample/current files exist, while sustained real-time, archive, FTP, OPeNDAP or viewer access may require a MADIS account/request.
- **Terms/licensing:** NOAA/NCEP MADIS terms and per-dataset restrictions.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| MADIS overview | `https` | service documentation | yes | [открыть / open](https://madis.ncep.noaa.gov/) |
| MADIS public sample/current data | `https` | public sample and current dataset tree | yes | [открыть / open](https://madis-data.ncep.noaa.gov/madisPublic1/data/) |
| MADIS data application | `https` | access request for sustained real-time or archive services | yes | [открыть / open](https://madis.ncep.noaa.gov/data_application.shtml) |

### Software and decoders

- [xarray](https://github.com/pydata/xarray) — netCDF inspection and normalization.
- [netCDF4-python](https://github.com/Unidata/netcdf4-python) — netCDF reader.

### Recommended ingestion flow

1. Fetch the official HTTPS/FTP file tree directly; do not scrape rendered product viewers.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as xarray / netCDF4, pandas / csv, lxml / ElementTree.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://madis.ncep.noaa.gov/madis_ui.shtml](https://madis.ncep.noaa.gov/madis_ui.shtml)
- [https://madis.ncep.noaa.gov/madis_datasets.shtml](https://madis.ncep.noaa.gov/madis_datasets.shtml)
- [https://madis.ncep.noaa.gov/madis_sample_data.shtml](https://madis.ncep.noaa.gov/madis_sample_data.shtml)

### Agent note

Authoritative record: `catalog/sources/noaa-observations.yaml` → `id: noaa-ncep-madis`. Treat this Markdown as a generated view; never override the YAML record from prose.
