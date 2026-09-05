# SMHI — открытые данные / SMHI Open Data

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`smhi-open-data` · 🟡 **резервный/региональный / secondary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Шведские наблюдения анализы радиолокационные и модельные продукты через API и файлы.

**Поставщик:** SMHI  
**Статус:** официальный источник; приоритет — **резервный/региональный**.  
**Категории:** Наземные наблюдения, Метеорологические радары, Численные модели прогноза, hydrology.  

### Что можно получить и когда использовать

Хороший региональный резерв для Скандинавии вместе с FMI и MET Norway.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | Sweden / Nordic region |
| Периодичность/режим обновления | minutes to hours |
| Типичная задержка | low |
| Архив | dataset dependent |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https`, `rest` |
| Форматы | `JSON`, `CSV`, `GRIB2`, `NetCDF`, `provider-dependent` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** none for standard open-data endpoints.
- **Лицензия/условия:** SMHI open data terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| SMHI Open Data | `https` | portal/API | да | [открыть / open](https://opendata.smhi.se/) |

### ПО, библиотеки и декодеры

- [requests](https://requests.readthedocs.io/) — HTTP/API client.
- [ecCodes](https://github.com/ecmwf/eccodes) — GRIB decoding.
- **Быстрый выбор декодера по формату:** requests + stdlib json, pandas / csv, ecCodes / wgrib2 / cfgrib, xarray / netCDF4.

### Рекомендуемый алгоритм автоматического приёма

1. Работать через официальный API с явными параметрами времени, области и продукта; соблюдать квоты и rate limit.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: requests + stdlib json, pandas / csv, ecCodes / wgrib2 / cfgrib, xarray / netCDF4.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://opendata.smhi.se/](https://opendata.smhi.se/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/core.yaml` → `id: smhi-open-data`.
- Для оперативного контура учитывать: `tier=secondary`, `operational=true`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

Swedish observations analyses radar and model products through APIs and files.

**Provider:** SMHI  
**Status:** official; tier **secondary**.  
**Categories:** surface, radar, nwp, hydrology.  

### What it provides and when to use it

Good Nordic regional fallback alongside FMI and MET Norway.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | Sweden / Nordic region |
| Update cadence | minutes to hours |
| Typical latency | low |
| Archive | dataset dependent |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https`, `rest` |
| Formats | `JSON`, `CSV`, `GRIB2`, `NetCDF`, `provider-dependent` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** none for standard open-data endpoints.
- **Terms/licensing:** SMHI open data terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| SMHI Open Data | `https` | portal/API | yes | [открыть / open](https://opendata.smhi.se/) |

### Software and decoders

- [requests](https://requests.readthedocs.io/) — HTTP/API client.
- [ecCodes](https://github.com/ecmwf/eccodes) — GRIB decoding.

### Recommended ingestion flow

1. Use the official API with explicit product/time/area parameters and respect quotas and rate limits.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as requests + stdlib json, pandas / csv, ecCodes / wgrib2 / cfgrib, xarray / netCDF4.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://opendata.smhi.se/](https://opendata.smhi.se/)

### Agent note

Authoritative record: `catalog/sources/core.yaml` → `id: smhi-open-data`. Treat this Markdown as a generated view; never override the YAML record from prose.
