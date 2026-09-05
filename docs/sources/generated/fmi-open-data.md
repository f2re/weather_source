# Открытые данные FMI / FMI Open Data

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`fmi-open-data` · 🟢 **основной / primary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

WFS/API-доступ к наблюдениям аэрологии радиолокации и моделям Финляндии.

**Поставщик:** Finnish Meteorological Institute  
**Статус:** официальный источник; приоритет — **основной**.  
**Категории:** Наземные наблюдения, Аэрология и верхняя атмосфера, Метеорологические радары, Численные модели прогноза.  

### Что можно получить и когда использовать

Сильный машиночитаемый региональный источник включая stored queries аэрологии.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | Finland and selected surrounding or global products |
| Периодичность/режим обновления | minutes to hours |
| Типичная задержка | low |
| Архив | dataset dependent; long archives for some observations |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `wfs`, `https` |
| Форматы | `GML`, `XML`, `coverage-formats`, `GRIB2`, `provider-dependent` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** no API key for standard open-data service; rate limits apply.
- **Лицензия/условия:** FMI open data licence.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| FMI Open Data | `https` | documentation | да | [открыть / open](https://en.ilmatieteenlaitos.fi/open-data) |
| FMI WFS | `wfs` | API | да | [открыть / open](https://opendata.fmi.fi/wfs) |

### ПО, библиотеки и декодеры

- [OWSLib](https://github.com/geopython/OWSLib) — WFS client.
- [requests](https://requests.readthedocs.io/) — HTTP client.
- **Быстрый выбор декодера по формату:** OWSLib / GDAL, lxml / ElementTree, ecCodes / wgrib2 / cfgrib.

### Рекомендуемый алгоритм автоматического приёма

1. Использовать OGC API/WFS/WCS для численных данных; WMS применять главным образом для визуализации.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: OWSLib / GDAL, lxml / ElementTree, ecCodes / wgrib2 / cfgrib.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://en.ilmatieteenlaitos.fi/open-data](https://en.ilmatieteenlaitos.fi/open-data)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/core.yaml` → `id: fmi-open-data`.
- Для оперативного контура учитывать: `tier=primary`, `operational=true`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

WFS/API access to Finnish observations soundings radar and model datasets.

**Provider:** Finnish Meteorological Institute  
**Status:** official; tier **primary**.  
**Categories:** surface, upper-air, radar, nwp.  

### What it provides and when to use it

Strong machine-readable regional source including upper-air stored queries.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | Finland and selected surrounding or global products |
| Update cadence | minutes to hours |
| Typical latency | low |
| Archive | dataset dependent; long archives for some observations |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `wfs`, `https` |
| Formats | `GML`, `XML`, `coverage-formats`, `GRIB2`, `provider-dependent` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** no API key for standard open-data service; rate limits apply.
- **Terms/licensing:** FMI open data licence.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| FMI Open Data | `https` | documentation | yes | [открыть / open](https://en.ilmatieteenlaitos.fi/open-data) |
| FMI WFS | `wfs` | API | yes | [открыть / open](https://opendata.fmi.fi/wfs) |

### Software and decoders

- [OWSLib](https://github.com/geopython/OWSLib) — WFS client.
- [requests](https://requests.readthedocs.io/) — HTTP client.

### Recommended ingestion flow

1. Use OGC API/WFS/WCS for data values; treat WMS primarily as a presentation service.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as OWSLib / GDAL, lxml / ElementTree, ecCodes / wgrib2 / cfgrib.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://en.ilmatieteenlaitos.fi/open-data](https://en.ilmatieteenlaitos.fi/open-data)

### Agent note

Authoritative record: `catalog/sources/core.yaml` → `id: fmi-open-data`. Treat this Markdown as a generated view; never override the YAML record from prose.
