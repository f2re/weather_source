# KNMI Data Platform / KNMI Data Platform

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`knmi-open-data` · 🟡 **резервный/региональный / secondary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Открытая платформа KNMI с радарами наблюдениями спутниковыми и модельными данными.

**Поставщик:** KNMI  
**Статус:** официальный источник; приоритет — **резервный/региональный**.  
**Категории:** Наземные наблюдения, Метеорологические радары, Спутниковые данные, Численные модели прогноза.  

### Что можно получить и когда использовать

API-ключ бесплатный но его необходимо получить до запуска автоматического приёма.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | Netherlands / Europe / product dependent |
| Периодичность/режим обновления | minutes to hours |
| Типичная задержка | low |
| Архив | dataset dependent |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https`, `rest` |
| Форматы | `NetCDF`, `HDF5`, `GeoTIFF`, `GRIB2`, `provider-dependent` |

### Доступ и ограничения

- **Уровень доступа:** бесплатный после регистрации (`registration`).
- **Авторизация:** API key required for Open Data API.
- **Лицензия/условия:** KNMI Data Platform terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| KNMI Data Platform | `https` | API documentation | да | [открыть / open](https://developer.dataplatform.knmi.nl/) |

### ПО, библиотеки и декодеры

- [requests](https://requests.readthedocs.io/) — REST client.
- **Быстрый выбор декодера по формату:** xarray / netCDF4, h5py / xarray, GDAL / rasterio, ecCodes / wgrib2 / cfgrib.

### Рекомендуемый алгоритм автоматического приёма

1. Работать через официальный API с явными параметрами времени, области и продукта; соблюдать квоты и rate limit.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: xarray / netCDF4, h5py / xarray, GDAL / rasterio, ecCodes / wgrib2 / cfgrib.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://developer.dataplatform.knmi.nl/](https://developer.dataplatform.knmi.nl/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/core.yaml` → `id: knmi-open-data`.
- Для оперативного контура учитывать: `tier=secondary`, `operational=true`, `access.level=registration`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.


### 🧪 Проверенный пример получения данных

**Аудит:** 🛠 исправлено/уточнено · **проверено:** `2026-09-06`  
**Реальный режим доступа:** нужны бесплатные/договорные учётные данные (`credentials`)  
**Runtime-адаптер:** `external`  
**Recipe:** `catalog/recipes/core.json`

Через KNMI Open Data API получить список последних файлов актуального 10-minute dataset, запросить temporaryDownloadUrl и скачать NetCDF.

```bash
python -m weather_source describe knmi-open-data
python -m weather_source probe knmi-open-data
python -m weather_source fetch knmi-open-data --allow-external
```

**Требуемые переменные окружения:** `KNMI_API_KEY`.

**Что исправлено или обнаружено аудитом:**

- Старые KNMI dataset IDs были выведены из эксплуатации; актуальный dataset — `10-minute-in-situ-meteorological-observations` v1.0. Open Data API требует Authorization key.

**Резервный источник:** `fmi-open-data`.

<details><summary>Команда официального/специализированного клиента</summary>

```bash
python -m weather_source.providers knmi
```

</details>

> Клиент сохраняет исходные данные; крупные GRIB/NetCDF/радарные объекты по умолчанию блокируются безопасным лимитом. Для осознанной полной загрузки используйте `--full`, когда это применимо.

---

## 🇬🇧 English

### What it is

Dutch open radar observations satellite-derived and model datasets.

**Provider:** KNMI  
**Status:** official; tier **secondary**.  
**Categories:** surface, radar, satellite, nwp.  

### What it provides and when to use it

API key is free but must be provisioned before unattended access.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | Netherlands / Europe / product dependent |
| Update cadence | minutes to hours |
| Typical latency | low |
| Archive | dataset dependent |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https`, `rest` |
| Formats | `NetCDF`, `HDF5`, `GeoTIFF`, `GRIB2`, `provider-dependent` |

### Access and restrictions

- **Access level:** `registration`.
- **Authentication:** API key required for Open Data API.
- **Terms/licensing:** KNMI Data Platform terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| KNMI Data Platform | `https` | API documentation | yes | [открыть / open](https://developer.dataplatform.knmi.nl/) |

### Software and decoders

- [requests](https://requests.readthedocs.io/) — REST client.

### Recommended ingestion flow

1. Use the official API with explicit product/time/area parameters and respect quotas and rate limits.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as xarray / netCDF4, h5py / xarray, GDAL / rasterio, ecCodes / wgrib2 / cfgrib.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://developer.dataplatform.knmi.nl/](https://developer.dataplatform.knmi.nl/)

### 🧪 Executable retrieval recipe

**Audit verdict:** `corrected` · **verified:** `2026-09-06`  
**Runtime access:** `credentials` · **adapter:** `external`  
**Recipe:** `catalog/recipes/core.json`

```bash
python -m weather_source probe knmi-open-data
python -m weather_source fetch knmi-open-data --allow-external
```

Required environment: `KNMI_API_KEY`.

Fallback: `fmi-open-data`.

### Agent note

Authoritative record: `catalog/sources/core.yaml` → `id: knmi-open-data`. Treat this Markdown as a generated view; never override the YAML record from prose.
