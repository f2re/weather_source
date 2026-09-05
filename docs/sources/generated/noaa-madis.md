# NOAA MADIS — система приёма метеорологических наблюдений / Meteorological Assimilation Data Ingest System (MADIS)

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`noaa-madis` · 🔵 **специализированный / specialized** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

База и система доставки наблюдений NOAA, включающая радиозонды, профайлеры, самолётные наблюдения, спутниковые зондирования и другие in-situ наборы.

**Поставщик:** NOAA/NCEP MADIS  
**Статус:** официальный источник; приоритет — **специализированный**.  
**Категории:** Аэрология и верхняя атмосфера, profiler, Авиационные наблюдения, Наземные наблюдения.  

### Что можно получить и когда использовать

Сильный дополнительный источник аэрологии и профайлеров. Перед распространением данных проверять права конкретного набора, особенно для самолётных наблюдений.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global database with highest density over North America |
| Периодичность/режим обновления | dataset dependent; continuous, minutes or hourly depending on feed |
| Типичная задержка | near-real-time for operational datasets; exact latency is dataset dependent |
| Архив | archives exist for many datasets; start dates vary by dataset |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https`, `ftp`, `opendap`, `ldm` |
| Форматы | `NetCDF`, `XML`, `text` |

### Доступ и ограничения

- **Уровень доступа:** бесплатный после регистрации (`registration`).
- **Авторизация:** free MADIS data application/account for machine access; unrestricted and restricted dataset classes coexist.
- **Лицензия/условия:** NOAA MADIS data policy; radiosonde, Multi-Agency Profiler, satellite sounding and several other datasets are unrestricted, while aircraft and some mesonet data have restrictions.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| MADIS home | `https` | documentation and service entry point | да | [открыть / open](https://madis.ncep.noaa.gov/) |
| MADIS data application | `https` | account and access request | да | [открыть / open](https://madis.ncep.noaa.gov/data_application.shtml) |

### ПО, библиотеки и декодеры

- [xarray](https://github.com/pydata/xarray) — NetCDF processing.
- [netCDF4](https://github.com/Unidata/netcdf4-python) — NetCDF processing.
- **Быстрый выбор декодера по формату:** xarray / netCDF4, lxml / ElementTree.

### Рекомендуемый алгоритм автоматического приёма

1. Забирать данные напрямую с официального HTTPS/FTP-файлового дерева, не парся HTML-визуализатор.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: xarray / netCDF4, lxml / ElementTree.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://madis.ncep.noaa.gov/madis_datasets.shtml](https://madis.ncep.noaa.gov/madis_datasets.shtml)
- [https://madis.ncep.noaa.gov/madis_restrictions.shtml](https://madis.ncep.noaa.gov/madis_restrictions.shtml)
- [https://madis.ncep.noaa.gov/data_application.shtml](https://madis.ncep.noaa.gov/data_application.shtml)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/specialized.yaml` → `id: noaa-madis`.
- Для оперативного контура учитывать: `tier=specialized`, `operational=true`, `access.level=registration`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

NOAA observational database and delivery system with radiosondes, profiler networks, aircraft observations, satellite soundings and other in-situ datasets.

**Provider:** NOAA/NCEP MADIS  
**Status:** official; tier **specialized**.  
**Categories:** upper-air, profiler, aircraft, surface.  

### What it provides and when to use it

Strong supplement for upper-air and profiler data. Check per-dataset rights before redistributing data, especially aircraft observations.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global database with highest density over North America |
| Update cadence | dataset dependent; continuous, minutes or hourly depending on feed |
| Typical latency | near-real-time for operational datasets; exact latency is dataset dependent |
| Archive | archives exist for many datasets; start dates vary by dataset |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https`, `ftp`, `opendap`, `ldm` |
| Formats | `NetCDF`, `XML`, `text` |

### Access and restrictions

- **Access level:** `registration`.
- **Authentication:** free MADIS data application/account for machine access; unrestricted and restricted dataset classes coexist.
- **Terms/licensing:** NOAA MADIS data policy; radiosonde, Multi-Agency Profiler, satellite sounding and several other datasets are unrestricted, while aircraft and some mesonet data have restrictions.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| MADIS home | `https` | documentation and service entry point | yes | [открыть / open](https://madis.ncep.noaa.gov/) |
| MADIS data application | `https` | account and access request | yes | [открыть / open](https://madis.ncep.noaa.gov/data_application.shtml) |

### Software and decoders

- [xarray](https://github.com/pydata/xarray) — NetCDF processing.
- [netCDF4](https://github.com/Unidata/netcdf4-python) — NetCDF processing.

### Recommended ingestion flow

1. Fetch the official HTTPS/FTP file tree directly; do not scrape rendered product viewers.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as xarray / netCDF4, lxml / ElementTree.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://madis.ncep.noaa.gov/madis_datasets.shtml](https://madis.ncep.noaa.gov/madis_datasets.shtml)
- [https://madis.ncep.noaa.gov/madis_restrictions.shtml](https://madis.ncep.noaa.gov/madis_restrictions.shtml)
- [https://madis.ncep.noaa.gov/data_application.shtml](https://madis.ncep.noaa.gov/data_application.shtml)

### Agent note

Authoritative record: `catalog/sources/specialized.yaml` → `id: noaa-madis`. Treat this Markdown as a generated view; never override the YAML record from prose.
