# NASA LANCE / Earthdata Near Real-Time / NASA LANCE / Earthdata Near Real-Time

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`nasa-earthdata-lance` · 🔵 **специализированный / specialized** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Спутниковые продукты близкого к реальному времени для атмосферы суши пожаров аэрозолей осадков и других наблюдений Земли.

**Поставщик:** NASA Earthdata  
**Статус:** официальный источник; приоритет — **специализированный**.  
**Категории:** Спутниковые данные, Осадки, aerosol, fire, clouds.  

### Что можно получить и когда использовать

Очень полезное специализированное NRT-дополнение; перед автономным развёртыванием заранее настроить Earthdata Login.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global |
| Периодичность/режим обновления | orbital/product dependent |
| Типичная задержка | generally near-real-time; product targets range from minutes to a few hours |
| Архив | long-term products through NASA Earthdata/DAACs |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https`, `api` |
| Форматы | `HDF5`, `NetCDF`, `GeoTIFF`, `provider-dependent` |

### Доступ и ограничения

- **Уровень доступа:** бесплатный после регистрации (`registration`).
- **Авторизация:** Earthdata Login for many download APIs.
- **Лицензия/условия:** NASA Earthdata terms and dataset-specific licences.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| LANCE | `https` | near-real-time portal | да | [открыть / open](https://lance.modaps.eosdis.nasa.gov/) |
| Earthdata | `https` | catalog and access documentation | да | [открыть / open](https://www.earthdata.nasa.gov/) |

### ПО, библиотеки и декодеры

- [earthaccess](https://github.com/nsidc/earthaccess) — Python search and download client.
- [xarray](https://github.com/pydata/xarray) — NetCDF processing.
- [h5py](https://github.com/h5py/h5py) — HDF5 processing.
- **Быстрый выбор декодера по формату:** h5py / xarray, xarray / netCDF4, GDAL / rasterio.

### Рекомендуемый алгоритм автоматического приёма

1. Работать через официальный API с явными параметрами времени, области и продукта; соблюдать квоты и rate limit.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: h5py / xarray, xarray / netCDF4, GDAL / rasterio.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://www.earthdata.nasa.gov/data/tools/lance](https://www.earthdata.nasa.gov/data/tools/lance)
- [https://earthaccess.readthedocs.io/](https://earthaccess.readthedocs.io/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/satellite.yaml` → `id: nasa-earthdata-lance`.
- Для оперативного контура учитывать: `tier=specialized`, `operational=true`, `access.level=registration`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.


### 🧪 Проверенный пример получения данных

**Аудит:** 🛠 исправлено/уточнено · **проверено:** `2026-09-06`  
**Реальный режим доступа:** нужны бесплатные/договорные учётные данные (`credentials`)  
**Runtime-адаптер:** `external`  
**Recipe:** `catalog/recipes/satellite.json`

Через earthaccess найти один near-real-time VIIRS 375 m active-fire granule `VNP14IMGTDL_NRT` и скачать его с Earthdata Login.

```bash
python -m weather_source describe nasa-earthdata-lance
python -m weather_source probe nasa-earthdata-lance
python -m weather_source fetch nasa-earthdata-lance --allow-external
```

**Требуемые переменные окружения:** `EARTHDATA_USERNAME`, `EARTHDATA_PASSWORD`.

**Что исправлено или обнаружено аудитом:**

- LANCE/LAADS web pages открыты, но scripted HTTPS downloads требуют Earthdata/LAADS token или Earthdata Login. Нельзя маркировать скачивание как anonymous.

**Резервный источник:** `noaa-goes`.

<details><summary>Команда официального/специализированного клиента</summary>

```bash
python -c "import earthaccess; earthaccess.login(strategy='environment'); r=earthaccess.search_data(short_name='VNP14IMGTDL_NRT',count=1); print(r); earthaccess.download(r,'nasa-lance')"
```

</details>

> Клиент сохраняет исходные данные; крупные GRIB/NetCDF/радарные объекты по умолчанию блокируются безопасным лимитом. Для осознанной полной загрузки используйте `--full`, когда это применимо.

---

## 🇬🇧 English

### What it is

Near-real-time satellite products for atmosphere land fire aerosols precipitation and related Earth observations.

**Provider:** NASA Earthdata  
**Status:** official; tier **specialized**.  
**Categories:** satellite, precipitation, aerosol, fire, clouds.  

### What it provides and when to use it

Very useful specialized NRT supplement; authentication should be provisioned before unattended deployment.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global |
| Update cadence | orbital/product dependent |
| Typical latency | generally near-real-time; product targets range from minutes to a few hours |
| Archive | long-term products through NASA Earthdata/DAACs |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https`, `api` |
| Formats | `HDF5`, `NetCDF`, `GeoTIFF`, `provider-dependent` |

### Access and restrictions

- **Access level:** `registration`.
- **Authentication:** Earthdata Login for many download APIs.
- **Terms/licensing:** NASA Earthdata terms and dataset-specific licences.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| LANCE | `https` | near-real-time portal | yes | [открыть / open](https://lance.modaps.eosdis.nasa.gov/) |
| Earthdata | `https` | catalog and access documentation | yes | [открыть / open](https://www.earthdata.nasa.gov/) |

### Software and decoders

- [earthaccess](https://github.com/nsidc/earthaccess) — Python search and download client.
- [xarray](https://github.com/pydata/xarray) — NetCDF processing.
- [h5py](https://github.com/h5py/h5py) — HDF5 processing.

### Recommended ingestion flow

1. Use the official API with explicit product/time/area parameters and respect quotas and rate limits.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as h5py / xarray, xarray / netCDF4, GDAL / rasterio.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://www.earthdata.nasa.gov/data/tools/lance](https://www.earthdata.nasa.gov/data/tools/lance)
- [https://earthaccess.readthedocs.io/](https://earthaccess.readthedocs.io/)

### 🧪 Executable retrieval recipe

**Audit verdict:** `corrected` · **verified:** `2026-09-06`  
**Runtime access:** `credentials` · **adapter:** `external`  
**Recipe:** `catalog/recipes/satellite.json`

```bash
python -m weather_source probe nasa-earthdata-lance
python -m weather_source fetch nasa-earthdata-lance --allow-external
```

Required environment: `EARTHDATA_USERNAME`, `EARTHDATA_PASSWORD`.

Fallback: `noaa-goes`.

### Agent note

Authoritative record: `catalog/sources/satellite.yaml` → `id: nasa-earthdata-lance`. Treat this Markdown as a generated view; never override the YAML record from prose.
