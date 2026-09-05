# Открытые данные DWD / DWD Open Data

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`dwd-open-data` · 🟢 **основной / primary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Открытые оперативные наблюдения радиолокация модели и климатические файлы Немецкой метеослужбы.

**Поставщик:** DWD  
**Статус:** официальный источник; приоритет — **основной**.  
**Категории:** Наземные наблюдения, Аэрология и верхняя атмосфера, Метеорологические радары, Численные модели прогноза, Климат и архивы.  

### Что можно получить и когда использовать

Один из самых удобных европейских файловых сервисов для постоянного автоматического приёма.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | Germany / Europe / global depending on product |
| Периодичность/режим обновления | minutes to model-cycle cadence |
| Типичная задержка | low for operational products |
| Архив | recent and historical directory trees |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https` |
| Форматы | `BUFR`, `GRIB2`, `NetCDF`, `ODIM HDF5`, `text`, `CSV` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** none.
- **Лицензия/условия:** DWD Open Data terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| DWD Open Data | `https` | file tree | да | [открыть / open](https://opendata.dwd.de/) |

### ПО, библиотеки и декодеры

- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR/GRIB decoder.
- [wradlib](https://github.com/wradlib/wradlib) — weather-radar processing.
- **Быстрый выбор декодера по формату:** ecCodes / pybufrkit, ecCodes / wgrib2 / cfgrib, xarray / netCDF4, wradlib / h5py, pandas / csv.

### Рекомендуемый алгоритм автоматического приёма

1. Забирать данные напрямую с официального HTTPS/FTP-файлового дерева, не парся HTML-визуализатор.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: ecCodes / pybufrkit, ecCodes / wgrib2 / cfgrib, xarray / netCDF4, wradlib / h5py, pandas / csv.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://opendata.dwd.de/](https://opendata.dwd.de/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/core.yaml` → `id: dwd-open-data`.
- Для оперативного контура учитывать: `tier=primary`, `operational=true`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

German Weather Service open operational observations radar NWP and climate files.

**Provider:** DWD  
**Status:** official; tier **primary**.  
**Categories:** surface, upper-air, radar, nwp, climate.  

### What it provides and when to use it

One of the simplest high-value European file services for unattended ingest.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | Germany / Europe / global depending on product |
| Update cadence | minutes to model-cycle cadence |
| Typical latency | low for operational products |
| Archive | recent and historical directory trees |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https` |
| Formats | `BUFR`, `GRIB2`, `NetCDF`, `ODIM HDF5`, `text`, `CSV` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** none.
- **Terms/licensing:** DWD Open Data terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| DWD Open Data | `https` | file tree | yes | [открыть / open](https://opendata.dwd.de/) |

### Software and decoders

- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR/GRIB decoder.
- [wradlib](https://github.com/wradlib/wradlib) — weather-radar processing.

### Recommended ingestion flow

1. Fetch the official HTTPS/FTP file tree directly; do not scrape rendered product viewers.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as ecCodes / pybufrkit, ecCodes / wgrib2 / cfgrib, xarray / netCDF4, wradlib / h5py, pandas / csv.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://opendata.dwd.de/](https://opendata.dwd.de/)

### Agent note

Authoritative record: `catalog/sources/core.yaml` → `id: dwd-open-data`. Treat this Markdown as a generated view; never override the YAML record from prose.
