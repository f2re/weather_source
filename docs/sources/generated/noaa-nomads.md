# NOAA/NCEP NOMADS / NOMADS

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`noaa-nomads` · 🟢 **основной / primary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Оперативный и архивный доступ к продуктам численного прогноза NOAA/NCEP.

**Поставщик:** NOAA/NCEP  
**Статус:** официальный источник; приоритет — **основной**.  
**Категории:** Численные модели прогноза, Ансамблевые прогнозы, analysis.  

### Что можно получить и когда использовать

NOMADS удобен для выборочных запросов; для массового зеркалирования предпочтительнее NODD object storage.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global |
| Периодичность/режим обновления | model dependent; GFS commonly four cycles per day |
| Типичная задержка | tens of minutes to hours |
| Архив | rolling operational archive; long-term archives through NCEI |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https`, `opendap` |
| Форматы | `GRIB2`, `NetCDF` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** none for standard public endpoints.
- **Лицензия/условия:** NOAA public data terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| NOMADS | `https` | catalog/download | да | [открыть / open](https://nomads.ncep.noaa.gov/) |

### ПО, библиотеки и декодеры

- [wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/) — GRIB2 inspection and extraction.
- [ecCodes](https://github.com/ecmwf/eccodes) — GRIB decoder.
- [cfgrib](https://github.com/ecmwf/cfgrib) — xarray GRIB backend.
- **Быстрый выбор декодера по формату:** ecCodes / wgrib2 / cfgrib, xarray / netCDF4.

### Рекомендуемый алгоритм автоматического приёма

1. Забирать данные напрямую с официального HTTPS/FTP-файлового дерева, не парся HTML-визуализатор.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: ecCodes / wgrib2 / cfgrib, xarray / netCDF4.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://nomads.ncep.noaa.gov/](https://nomads.ncep.noaa.gov/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/nwp.yaml` → `id: noaa-nomads`.
- Для оперативного контура учитывать: `tier=primary`, `operational=true`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

Operational and archive access to NOAA/NCEP numerical weather prediction products.

**Provider:** NOAA/NCEP  
**Status:** official; tier **primary**.  
**Categories:** nwp, ensemble, analysis.  

### What it provides and when to use it

Use NOMADS for selective HTTP/OPeNDAP retrieval and NODD object storage for large-scale mirroring.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global |
| Update cadence | model dependent; GFS commonly four cycles per day |
| Typical latency | tens of minutes to hours |
| Archive | rolling operational archive; long-term archives through NCEI |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https`, `opendap` |
| Formats | `GRIB2`, `NetCDF` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** none for standard public endpoints.
- **Terms/licensing:** NOAA public data terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| NOMADS | `https` | catalog/download | yes | [открыть / open](https://nomads.ncep.noaa.gov/) |

### Software and decoders

- [wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/) — GRIB2 inspection and extraction.
- [ecCodes](https://github.com/ecmwf/eccodes) — GRIB decoder.
- [cfgrib](https://github.com/ecmwf/cfgrib) — xarray GRIB backend.

### Recommended ingestion flow

1. Fetch the official HTTPS/FTP file tree directly; do not scrape rendered product viewers.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as ecCodes / wgrib2 / cfgrib, xarray / netCDF4.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://nomads.ncep.noaa.gov/](https://nomads.ncep.noaa.gov/)

### Agent note

Authoritative record: `catalog/sources/nwp.yaml` → `id: noaa-nomads`. Treat this Markdown as a generated view; never override the YAML record from prose.
