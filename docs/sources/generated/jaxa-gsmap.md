# JAXA GSMaP — глобальные осадки / GSMaP global precipitation

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`jaxa-gsmap` · 🔵 **специализированный / specialized** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Оперативные и архивные глобальные спутниковые поля осадков JAXA.

**Поставщик:** JAXA  
**Статус:** официальный источник; приоритет — **специализированный**.  
**Категории:** Спутниковые данные, Осадки.  

### Что можно получить и когда использовать

Независимая глобальная оценка осадков полезная как второй спутниковый источник рядом с IMERG.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global |
| Периодичность/режим обновления | hourly products available for major operational streams |
| Типичная задержка | product dependent; near-real-time variants available |
| Архив | historical archive available |
| Надёжность | `high` |
| Удобство автоматизации | `medium` |
| Протоколы | `https`, `ftp` |
| Форматы | `binary grid`, `NetCDF`, `text`, `GeoTIFF`, `provider-dependent` |

### Доступ и ограничения

- **Уровень доступа:** бесплатный после регистрации (`registration`).
- **Авторизация:** some services require JAXA/EORC registration or credentials.
- **Лицензия/условия:** JAXA GSMaP terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| GSMaP | `https` | portal and documentation | да | [открыть / open](https://sharaku.eorc.jaxa.jp/GSMaP/) |

### ПО, библиотеки и декодеры

- [xarray](https://github.com/pydata/xarray) — NetCDF processing.
- [GDAL](https://gdal.org/) — raster conversion and geospatial processing.
- **Быстрый выбор декодера по формату:** xarray / netCDF4, GDAL / rasterio.

### Рекомендуемый алгоритм автоматического приёма

1. Забирать данные напрямую с официального HTTPS/FTP-файлового дерева, не парся HTML-визуализатор.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: xarray / netCDF4, GDAL / rasterio.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://sharaku.eorc.jaxa.jp/GSMaP/](https://sharaku.eorc.jaxa.jp/GSMaP/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/satellite.yaml` → `id: jaxa-gsmap`.
- Для оперативного контура учитывать: `tier=specialized`, `operational=true`, `access.level=registration`, `automation=medium`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

Near-real-time and historical global satellite precipitation maps from JAXA.

**Provider:** JAXA  
**Status:** official; tier **specialized**.  
**Categories:** satellite, precipitation.  

### What it provides and when to use it

Independent global precipitation estimate useful as a second satellite source alongside IMERG.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global |
| Update cadence | hourly products available for major operational streams |
| Typical latency | product dependent; near-real-time variants available |
| Archive | historical archive available |
| Reliability | `high` |
| Automation | `medium` |
| Protocols | `https`, `ftp` |
| Formats | `binary grid`, `NetCDF`, `text`, `GeoTIFF`, `provider-dependent` |

### Access and restrictions

- **Access level:** `registration`.
- **Authentication:** some services require JAXA/EORC registration or credentials.
- **Terms/licensing:** JAXA GSMaP terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| GSMaP | `https` | portal and documentation | yes | [открыть / open](https://sharaku.eorc.jaxa.jp/GSMaP/) |

### Software and decoders

- [xarray](https://github.com/pydata/xarray) — NetCDF processing.
- [GDAL](https://gdal.org/) — raster conversion and geospatial processing.

### Recommended ingestion flow

1. Fetch the official HTTPS/FTP file tree directly; do not scrape rendered product viewers.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as xarray / netCDF4, GDAL / rasterio.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://sharaku.eorc.jaxa.jp/GSMaP/](https://sharaku.eorc.jaxa.jp/GSMaP/)

### Agent note

Authoritative record: `catalog/sources/satellite.yaml` → `id: jaxa-gsmap`. Treat this Markdown as a generated view; never override the YAML record from prose.
