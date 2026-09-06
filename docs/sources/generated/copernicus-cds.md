# Copernicus Climate Data Store / Copernicus Climate Data Store

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`copernicus-cds` · 🟢 **основной / primary** · неоперативный / non-operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Климатические данные и реанализы включая ERA5 ERA5-Land сезонные продукты и множество производных наборов.

**Поставщик:** Copernicus Climate Change Service / ECMWF  
**Статус:** официальный источник; приоритет — **основной**.  
**Категории:** archive, Реанализ, Климат и архивы.  

### Что можно получить и когда использовать

Отличный архив и сервис реанализа; ERA5 нельзя использовать как замену оперативным наблюдениям или прогнозам.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global and regional depending on dataset |
| Периодичность/режим обновления | dataset dependent; some products are updated routinely |
| Типичная задержка | not intended as a primary real-time feed |
| Архив | extensive multi-decadal climate archive |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https`, `api` |
| Форматы | `NetCDF`, `GRIB`, `ZIP`, `provider-dependent` |

### Доступ и ограничения

- **Уровень доступа:** бесплатный после регистрации (`registration`).
- **Авторизация:** free account and API token for programmatic access.
- **Лицензия/условия:** Copernicus licences and dataset-specific terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| Climate Data Store | `https` | catalog and API | да | [открыть / open](https://cds.climate.copernicus.eu/) |

### ПО, библиотеки и декодеры

- [cdsapi](https://github.com/ecmwf/cdsapi) — official API client.
- [xarray](https://github.com/pydata/xarray) — NetCDF processing.
- [ecCodes](https://github.com/ecmwf/eccodes) — GRIB processing.
- **Быстрый выбор декодера по формату:** xarray / netCDF4, ecCodes / wgrib2 / cfgrib.

### Рекомендуемый алгоритм автоматического приёма

1. Работать через официальный API с явными параметрами времени, области и продукта; соблюдать квоты и rate limit.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: xarray / netCDF4, ecCodes / wgrib2 / cfgrib.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://cds.climate.copernicus.eu/how-to-api](https://cds.climate.copernicus.eu/how-to-api)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/archives.yaml` → `id: copernicus-cds`.
- Для оперативного контура учитывать: `tier=primary`, `operational=false`, `access.level=registration`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.


### 🧪 Проверенный пример получения данных

**Аудит:** 🛠 исправлено/уточнено · **проверено:** `2026-09-06`  
**Реальный режим доступа:** нужны бесплатные/договорные учётные данные (`credentials`)  
**Runtime-адаптер:** `external`  
**Recipe:** `catalog/recipes/archives.json`

Официальным CDS API скачать минимальный ERA5 pressure-level GRIB: geopotential, 1000 hPa, 2024-03-01 13:00 UTC.

```bash
python -m weather_source describe copernicus-cds
python -m weather_source probe copernicus-cds
python -m weather_source fetch copernicus-cds --allow-external
```

**Требуемые переменные окружения:** `CDSAPI_KEY`.

**Что исправлено или обнаружено аудитом:**

- CDS требует бесплатный аккаунт/personal access token и предварительное принятие Terms конкретного dataset.
- Landing page не является проверкой API retrieval; нужен реальный `cdsapi.Client().retrieve`.

**Резервный источник:** `noaa-ncei-igra`.

<details><summary>Команда официального/специализированного клиента</summary>

```bash
python -c "import os,cdsapi; c=cdsapi.Client(url='https://cds.climate.copernicus.eu/api',key=os.environ['CDSAPI_KEY']); c.retrieve('reanalysis-era5-pressure-levels',{'product_type':['reanalysis'],'variable':['geopotential'],'year':['2024'],'month':['03'],'day':['01'],'time':['13:00'],'pressure_level':['1000'],'data_format':'grib'},'era5-1000hpa-z-2024030113.grib')"
```

</details>

> Клиент сохраняет исходные данные; крупные GRIB/NetCDF/радарные объекты по умолчанию блокируются безопасным лимитом. Для осознанной полной загрузки используйте `--full`, когда это применимо.

---

## 🇬🇧 English

### What it is

Climate datasets and reanalyses including ERA5, ERA5-Land, seasonal products and many derived climate datasets.

**Provider:** Copernicus Climate Change Service / ECMWF  
**Status:** official; tier **primary**.  
**Categories:** archive, reanalysis, climate.  

### What it provides and when to use it

Excellent archive and reanalysis service; do not use ERA5 as a substitute for operational observations or forecasts.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global and regional depending on dataset |
| Update cadence | dataset dependent; some products are updated routinely |
| Typical latency | not intended as a primary real-time feed |
| Archive | extensive multi-decadal climate archive |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https`, `api` |
| Formats | `NetCDF`, `GRIB`, `ZIP`, `provider-dependent` |

### Access and restrictions

- **Access level:** `registration`.
- **Authentication:** free account and API token for programmatic access.
- **Terms/licensing:** Copernicus licences and dataset-specific terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| Climate Data Store | `https` | catalog and API | yes | [открыть / open](https://cds.climate.copernicus.eu/) |

### Software and decoders

- [cdsapi](https://github.com/ecmwf/cdsapi) — official API client.
- [xarray](https://github.com/pydata/xarray) — NetCDF processing.
- [ecCodes](https://github.com/ecmwf/eccodes) — GRIB processing.

### Recommended ingestion flow

1. Use the official API with explicit product/time/area parameters and respect quotas and rate limits.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as xarray / netCDF4, ecCodes / wgrib2 / cfgrib.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://cds.climate.copernicus.eu/how-to-api](https://cds.climate.copernicus.eu/how-to-api)

### 🧪 Executable retrieval recipe

**Audit verdict:** `corrected` · **verified:** `2026-09-06`  
**Runtime access:** `credentials` · **adapter:** `external`  
**Recipe:** `catalog/recipes/archives.json`

```bash
python -m weather_source probe copernicus-cds
python -m weather_source fetch copernicus-cds --allow-external
```

Required environment: `CDSAPI_KEY`.

Fallback: `noaa-ncei-igra`.

### Agent note

Authoritative record: `catalog/sources/archives.yaml` → `id: copernicus-cds`. Treat this Markdown as a generated view; never override the YAML record from prose.
