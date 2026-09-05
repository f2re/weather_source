# NOAA MRMS — Multi-Radar Multi-Sensor / Multi-Radar Multi-Sensor (MRMS)

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`noaa-mrms` · 🟢 **основной / primary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Быстро обновляемые сеточные радиолокационные и мультисенсорные продукты включая отражаемость осадки и диагностику опасных явлений.

**Поставщик:** NOAA/NSSL/NCEP  
**Статус:** официальный источник; приоритет — **основной**.  
**Категории:** Метеорологические радары, Осадки, severe-weather.  

### Что можно получить и когда использовать

Ценный источник для наукастинга осадков и опасных явлений; для health-check использовать небольшие индексные или метаданные файлы.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | CONUS and selected surrounding regions/products |
| Периодичность/режим обновления | approximately minutes; product dependent |
| Типичная задержка | minutes |
| Архив | operational and research archives vary by product |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https`, `s3` |
| Форматы | `GRIB2`, `NetCDF`, `GeoTIFF`, `provider-dependent` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** none for public NOAA dissemination.
- **Лицензия/условия:** NOAA public data terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| MRMS operational data | `https` | operational file tree | да | [открыть / open](https://mrms.ncep.noaa.gov/data/) |
| MRMS documentation | `https` | product documentation | да | [открыть / open](https://www.nssl.noaa.gov/projects/mrms/) |

### ПО, библиотеки и декодеры

- [wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/) — GRIB2 inspection and extraction.
- [ecCodes](https://github.com/ecmwf/eccodes) — GRIB2 decoding.
- [xarray](https://github.com/pydata/xarray) — gridded data analysis.
- **Быстрый выбор декодера по формату:** ecCodes / wgrib2 / cfgrib, xarray / netCDF4, GDAL / rasterio.

### Рекомендуемый алгоритм автоматического приёма

1. Использовать S3/object-storage API: листинг по префиксу продукта и времени, затем скачивание только новых объектов.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: ecCodes / wgrib2 / cfgrib, xarray / netCDF4, GDAL / rasterio.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://www.nssl.noaa.gov/projects/mrms/](https://www.nssl.noaa.gov/projects/mrms/)
- [https://mrms.ncep.noaa.gov/data/](https://mrms.ncep.noaa.gov/data/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/radar.yaml` → `id: noaa-mrms`.
- Для оперативного контура учитывать: `tier=primary`, `operational=true`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

Rapid-update gridded radar and multisensor products including reflectivity precipitation and severe-weather diagnostics.

**Provider:** NOAA/NSSL/NCEP  
**Status:** official; tier **primary**.  
**Categories:** radar, precipitation, severe-weather.  

### What it provides and when to use it

High-value source for precipitation nowcasting and severe-weather applications; select small metadata or index files for health checks.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | CONUS and selected surrounding regions/products |
| Update cadence | approximately minutes; product dependent |
| Typical latency | minutes |
| Archive | operational and research archives vary by product |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https`, `s3` |
| Formats | `GRIB2`, `NetCDF`, `GeoTIFF`, `provider-dependent` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** none for public NOAA dissemination.
- **Terms/licensing:** NOAA public data terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| MRMS operational data | `https` | operational file tree | yes | [открыть / open](https://mrms.ncep.noaa.gov/data/) |
| MRMS documentation | `https` | product documentation | yes | [открыть / open](https://www.nssl.noaa.gov/projects/mrms/) |

### Software and decoders

- [wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/) — GRIB2 inspection and extraction.
- [ecCodes](https://github.com/ecmwf/eccodes) — GRIB2 decoding.
- [xarray](https://github.com/pydata/xarray) — gridded data analysis.

### Recommended ingestion flow

1. Use the S3/object-storage API, list objects by product/time prefix and download only unseen objects.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as ecCodes / wgrib2 / cfgrib, xarray / netCDF4, GDAL / rasterio.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://www.nssl.noaa.gov/projects/mrms/](https://www.nssl.noaa.gov/projects/mrms/)
- [https://mrms.ncep.noaa.gov/data/](https://mrms.ncep.noaa.gov/data/)

### Agent note

Authoritative record: `catalog/sources/radar.yaml` → `id: noaa-mrms`. Treat this Markdown as a generated view; never override the YAML record from prose.
