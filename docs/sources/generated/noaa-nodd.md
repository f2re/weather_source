# NOAA Open Data Dissemination (NODD) / NOAA Open Data Dissemination (NODD)

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`noaa-nodd` · 🟢 **основной / primary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Облачная объектная раздача крупных оперативных наборов NOAA — модели радары спутники и наблюдения.

**Поставщик:** NOAA  
**Статус:** официальный источник; приоритет — **основной**.  
**Категории:** Численные модели прогноза, Метеорологические радары, Спутниковые данные, Наземные наблюдения.  

### Что можно получить и когда использовать

Для автоматизации предпочитать object storage а не парсинг веб-визуализаций NOAA.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global / USA depending on dataset |
| Периодичность/режим обновления | continuous / product dependent |
| Типичная задержка | close to operational publication |
| Архив | dataset dependent |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `s3`, `https` |
| Форматы | `GRIB2`, `NetCDF`, `HDF5`, `Level-II`, `Level-III`, `provider-dependent` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** no cloud account required for many public buckets.
- **Лицензия/условия:** NOAA and cloud-provider dataset terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| NODD program | `https` | documentation | да | [открыть / open](https://www.noaa.gov/information-technology/open-data-dissemination) |

### ПО, библиотеки и декодеры

- [AWS CLI](https://aws.amazon.com/cli/) — S3-compatible listing and download.
- [boto3](https://github.com/boto/boto3) — Python S3 client.
- **Быстрый выбор декодера по формату:** ecCodes / wgrib2 / cfgrib, xarray / netCDF4, h5py / xarray.

### Рекомендуемый алгоритм автоматического приёма

1. Использовать S3/object-storage API: листинг по префиксу продукта и времени, затем скачивание только новых объектов.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: ecCodes / wgrib2 / cfgrib, xarray / netCDF4, h5py / xarray.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://www.noaa.gov/information-technology/open-data-dissemination](https://www.noaa.gov/information-technology/open-data-dissemination)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/core.yaml` → `id: noaa-nodd`.
- Для оперативного контура учитывать: `tier=primary`, `operational=true`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.


### 🧪 Проверенный пример получения данных

**Аудит:** 🛠 исправлено/уточнено · **проверено:** `2026-09-06`  
**Реальный режим доступа:** публичный машинный доступ (`public`)  
**Runtime-адаптер:** `s3_latest`  
**Recipe:** `catalog/recipes/core.json`

Проверить реальный публичный NODD bucket GFS и скачать небольшой последний index-файл из текущего 00 UTC цикла.

```bash
python -m weather_source describe noaa-nodd
python -m weather_source probe noaa-nodd
python -m weather_source fetch noaa-nodd
```

**Что исправлено или обнаружено аудитом:**

- NODD — программа распространения, а не один dataset; каталог не содержал ни одного реального bucket.

**Резервный источник:** `noaa-nomads`.

> Клиент сохраняет исходные данные; крупные GRIB/NetCDF/радарные объекты по умолчанию блокируются безопасным лимитом. Для осознанной полной загрузки используйте `--full`, когда это применимо.

---

## 🇬🇧 English

### What it is

Cloud object-storage dissemination for large operational NOAA model radar satellite and observation datasets.

**Provider:** NOAA  
**Status:** official; tier **primary**.  
**Categories:** nwp, radar, satellite, surface.  

### What it provides and when to use it

Prefer object storage over scraping NOAA web viewers.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global / USA depending on dataset |
| Update cadence | continuous / product dependent |
| Typical latency | close to operational publication |
| Archive | dataset dependent |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `s3`, `https` |
| Formats | `GRIB2`, `NetCDF`, `HDF5`, `Level-II`, `Level-III`, `provider-dependent` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** no cloud account required for many public buckets.
- **Terms/licensing:** NOAA and cloud-provider dataset terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| NODD program | `https` | documentation | yes | [открыть / open](https://www.noaa.gov/information-technology/open-data-dissemination) |

### Software and decoders

- [AWS CLI](https://aws.amazon.com/cli/) — S3-compatible listing and download.
- [boto3](https://github.com/boto/boto3) — Python S3 client.

### Recommended ingestion flow

1. Use the S3/object-storage API, list objects by product/time prefix and download only unseen objects.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as ecCodes / wgrib2 / cfgrib, xarray / netCDF4, h5py / xarray.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://www.noaa.gov/information-technology/open-data-dissemination](https://www.noaa.gov/information-technology/open-data-dissemination)

### 🧪 Executable retrieval recipe

**Audit verdict:** `corrected` · **verified:** `2026-09-06`  
**Runtime access:** `public` · **adapter:** `s3_latest`  
**Recipe:** `catalog/recipes/core.json`

```bash
python -m weather_source probe noaa-nodd
python -m weather_source fetch noaa-nodd
```

Fallback: `noaa-nomads`.

### Agent note

Authoritative record: `catalog/sources/core.yaml` → `id: noaa-nodd`. Treat this Markdown as a generated view; never override the YAML record from prose.
