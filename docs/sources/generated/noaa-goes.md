# Оперативные данные спутников GOES-R / GOES-R Series operational satellite data

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`noaa-goes` · 🟢 **основной / primary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Геостационарные снимки ABI и производные продукты а также данные молниевого картирования GLM со спутников GOES-East и GOES-West.

**Поставщик:** NOAA/NESDIS  
**Статус:** официальный источник; приоритет — **основной**.  
**Категории:** Спутниковые данные, Грозопеленгация и молнии, clouds, radiation.  

### Что можно получить и когда использовать

Для непрерывного приёма использовать публичное object storage; GLM — один из наиболее сильных бесплатных оперативных источников молний.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | Americas Atlantic and eastern Pacific sectors |
| Периодичность/режим обновления | seconds to minutes depending on product and scan mode |
| Типичная задержка | minutes |
| Архив | long-term NOAA archives; operational cloud object storage available |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `s3`, `https` |
| Форматы | `NetCDF`, `HDF5`, `provider-dependent` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** none for many public cloud datasets.
- **Лицензия/условия:** NOAA public data terms and cloud dataset terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| GOES-R program data products | `https` | product documentation | да | [открыть / open](https://www.goes-r.gov/products/overview.html) |
| NOAA Open Data Dissemination | `https` | cloud access documentation | да | [открыть / open](https://www.noaa.gov/information-technology/open-data-dissemination) |

### ПО, библиотеки и декодеры

- [Satpy](https://github.com/pytroll/satpy) — satellite reading resampling and composites.
- [xarray](https://github.com/pydata/xarray) — NetCDF processing.
- **Быстрый выбор декодера по формату:** xarray / netCDF4, h5py / xarray.

### Рекомендуемый алгоритм автоматического приёма

1. Использовать S3/object-storage API: листинг по префиксу продукта и времени, затем скачивание только новых объектов.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: xarray / netCDF4, h5py / xarray.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://www.goes-r.gov/products/overview.html](https://www.goes-r.gov/products/overview.html)
- [https://www.noaa.gov/information-technology/open-data-dissemination](https://www.noaa.gov/information-technology/open-data-dissemination)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/satellite.yaml` → `id: noaa-goes`.
- Для оперативного контура учитывать: `tier=primary`, `operational=true`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.


### 🧪 Проверенный пример получения данных

**Аудит:** 🛠 исправлено/уточнено · **проверено:** `2026-09-06`  
**Реальный режим доступа:** публичный машинный доступ (`public`)  
**Runtime-адаптер:** `s3_latest`  
**Recipe:** `catalog/recipes/satellite.json`

Из публичного GOES-19 S3 bucket получить самый свежий GLM Level-2 Lightning Cluster/Flash/Group product текущего UTC-часа.

```bash
python -m weather_source describe noaa-goes
python -m weather_source probe noaa-goes
python -m weather_source fetch noaa-goes
```

**Что исправлено или обнаружено аудитом:**

- Карточка не называла актуальные публичные buckets.
- В 2026 году GOES-East — GOES-19 (`noaa-goes19`), GOES-West — GOES-18 (`noaa-goes18`).

**Резервный источник:** `eumetsat-data-store`.

> Клиент сохраняет исходные данные; крупные GRIB/NetCDF/радарные объекты по умолчанию блокируются безопасным лимитом. Для осознанной полной загрузки используйте `--full`, когда это применимо.

---

## 🇬🇧 English

### What it is

Geostationary ABI imagery and derived products plus GLM lightning observations from GOES-East and GOES-West.

**Provider:** NOAA/NESDIS  
**Status:** official; tier **primary**.  
**Categories:** satellite, lightning, clouds, radiation.  

### What it provides and when to use it

Use public object storage for continuous reception; GLM is one of the strongest freely accessible operational lightning sources.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | Americas Atlantic and eastern Pacific sectors |
| Update cadence | seconds to minutes depending on product and scan mode |
| Typical latency | minutes |
| Archive | long-term NOAA archives; operational cloud object storage available |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `s3`, `https` |
| Formats | `NetCDF`, `HDF5`, `provider-dependent` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** none for many public cloud datasets.
- **Terms/licensing:** NOAA public data terms and cloud dataset terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| GOES-R program data products | `https` | product documentation | yes | [открыть / open](https://www.goes-r.gov/products/overview.html) |
| NOAA Open Data Dissemination | `https` | cloud access documentation | yes | [открыть / open](https://www.noaa.gov/information-technology/open-data-dissemination) |

### Software and decoders

- [Satpy](https://github.com/pytroll/satpy) — satellite reading resampling and composites.
- [xarray](https://github.com/pydata/xarray) — NetCDF processing.

### Recommended ingestion flow

1. Use the S3/object-storage API, list objects by product/time prefix and download only unseen objects.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as xarray / netCDF4, h5py / xarray.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://www.goes-r.gov/products/overview.html](https://www.goes-r.gov/products/overview.html)
- [https://www.noaa.gov/information-technology/open-data-dissemination](https://www.noaa.gov/information-technology/open-data-dissemination)

### 🧪 Executable retrieval recipe

**Audit verdict:** `corrected` · **verified:** `2026-09-06`  
**Runtime access:** `public` · **adapter:** `s3_latest`  
**Recipe:** `catalog/recipes/satellite.json`

```bash
python -m weather_source probe noaa-goes
python -m weather_source fetch noaa-goes
```

Fallback: `eumetsat-data-store`.

### Agent note

Authoritative record: `catalog/sources/satellite.yaml` → `id: noaa-goes`. Treat this Markdown as a generated view; never override the YAML record from prose.
