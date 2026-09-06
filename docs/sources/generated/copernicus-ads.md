# Copernicus Atmosphere Data Store (ADS) / Copernicus Atmosphere Data Store

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`copernicus-ads` · 🟢 **основной / primary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Анализы прогнозы и реанализы состава атмосферы CAMS.

**Поставщик:** ECMWF / Copernicus Atmosphere Monitoring Service  
**Статус:** официальный источник; приоритет — **основной**.  
**Категории:** air-quality, Численные модели прогноза, Реанализ.  

### Что можно получить и когда использовать

Специализированный источник состава атмосферы а не замена общему метеорологическому NWP.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global and Europe |
| Периодичность/режим обновления | product dependent |
| Типичная задержка | hours |
| Архив | archive available |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https`, `api` |
| Форматы | `GRIB`, `NetCDF` |

### Доступ и ограничения

- **Уровень доступа:** бесплатный после регистрации (`registration`).
- **Авторизация:** free account and API token.
- **Лицензия/условия:** Copernicus terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| Atmosphere Data Store | `https` | catalog/API | да | [открыть / open](https://ads.atmosphere.copernicus.eu/) |

### ПО, библиотеки и декодеры

- [cdsapi](https://github.com/ecmwf/cdsapi) — API client.
- **Быстрый выбор декодера по формату:** ecCodes / wgrib2 / cfgrib, xarray / netCDF4.

### Рекомендуемый алгоритм автоматического приёма

1. Работать через официальный API с явными параметрами времени, области и продукта; соблюдать квоты и rate limit.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: ecCodes / wgrib2 / cfgrib, xarray / netCDF4.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://ads.atmosphere.copernicus.eu/](https://ads.atmosphere.copernicus.eu/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/nwp.yaml` → `id: copernicus-ads`.
- Для оперативного контура учитывать: `tier=primary`, `operational=true`, `access.level=registration`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.


### 🧪 Проверенный пример получения данных

**Аудит:** 🛠 исправлено/уточнено · **проверено:** `2026-09-06`  
**Реальный режим доступа:** нужны бесплатные/договорные учётные данные (`credentials`)  
**Runtime-адаптер:** `external`  
**Recipe:** `catalog/recipes/nwp.json`

Через CDS API Atmosphere Data Store скачать небольшой CAMS analysis: total aerosol optical depth 670 nm, 2021-03-24 00 UTC, область 69–70N / 17–18W, NetCDF ZIP.

```bash
python -m weather_source describe copernicus-ads
python -m weather_source probe copernicus-ads
python -m weather_source fetch copernicus-ads --allow-external
```

**Требуемые переменные окружения:** `CDSAPI_KEY`.

**Что исправлено или обнаружено аудитом:**

- Программный доступ требует учётную запись/API token и принятие условий ADS.
- Предыдущий recipe только создавал `cdsapi.Client` и не получал данных; теперь он выполняет реальный минимальный CAMS retrieval.

**Резервный источник:** `nasa-earthdata-lance`.

<details><summary>Команда официального/специализированного клиента</summary>

```bash
python -c "import os,cdsapi; c=cdsapi.Client(url='https://ads.atmosphere.copernicus.eu/api',key=os.environ['CDSAPI_KEY']); c.retrieve('cams-global-atmospheric-composition-forecasts',{'date':'2021-03-24','time':['00:00'],'leadtime_hour':'0','area':[70,-18,69,-17],'type':'analysis','variable':'total_aerosol_optical_depth_670nm','format':'netcdf_zip'},'cams-aod670-2021032400.zip')"
```

</details>

> Клиент сохраняет исходные данные; крупные GRIB/NetCDF/радарные объекты по умолчанию блокируются безопасным лимитом. Для осознанной полной загрузки используйте `--full`, когда это применимо.

---

## 🇬🇧 English

### What it is

CAMS atmospheric composition analyses forecasts and reanalyses.

**Provider:** ECMWF / Copernicus Atmosphere Monitoring Service  
**Status:** official; tier **primary**.  
**Categories:** air-quality, nwp, reanalysis.  

### What it provides and when to use it

Specialized source for atmospheric composition rather than a replacement for general-purpose NWP.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global and Europe |
| Update cadence | product dependent |
| Typical latency | hours |
| Archive | archive available |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https`, `api` |
| Formats | `GRIB`, `NetCDF` |

### Access and restrictions

- **Access level:** `registration`.
- **Authentication:** free account and API token.
- **Terms/licensing:** Copernicus terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| Atmosphere Data Store | `https` | catalog/API | yes | [открыть / open](https://ads.atmosphere.copernicus.eu/) |

### Software and decoders

- [cdsapi](https://github.com/ecmwf/cdsapi) — API client.

### Recommended ingestion flow

1. Use the official API with explicit product/time/area parameters and respect quotas and rate limits.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as ecCodes / wgrib2 / cfgrib, xarray / netCDF4.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://ads.atmosphere.copernicus.eu/](https://ads.atmosphere.copernicus.eu/)

### 🧪 Executable retrieval recipe

**Audit verdict:** `corrected` · **verified:** `2026-09-06`  
**Runtime access:** `credentials` · **adapter:** `external`  
**Recipe:** `catalog/recipes/nwp.json`

```bash
python -m weather_source probe copernicus-ads
python -m weather_source fetch copernicus-ads --allow-external
```

Required environment: `CDSAPI_KEY`.

Fallback: `nasa-earthdata-lance`.

### Agent note

Authoritative record: `catalog/sources/nwp.yaml` → `id: copernicus-ads`. Treat this Markdown as a generated view; never override the YAML record from prose.
