# NASA GPM IMERG — спутниковые осадки / GPM IMERG precipitation

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`nasa-gpm-imerg` · 🔵 **специализированный / specialized** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Глобальные мультиспутниковые оценки осадков с оперативными Early/Late и окончательными Final продуктами.

**Поставщик:** NASA GPM  
**Статус:** официальный источник; приоритет — **специализированный**.  
**Категории:** Спутниковые данные, Осадки.  

### Что можно получить и когда использовать

Полезен там где нет наземных радаров; спутниковые оценки осадков необходимо отличать от радиолокационных и станционных наблюдений.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | near-global |
| Периодичность/режим обновления | half-hourly product grid; run availability differs |
| Типичная задержка | Early and Late runs are near-real-time with product-specific latency; Final is delayed research quality |
| Архив | multi-year archive through NASA GES DISC |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https`, `opendap`, `api` |
| Форматы | `HDF5`, `NetCDF`, `GeoTIFF` |

### Доступ и ограничения

- **Уровень доступа:** бесплатный после регистрации (`registration`).
- **Авторизация:** Earthdata Login for standard authenticated downloads.
- **Лицензия/условия:** NASA/GPM data terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| GPM IMERG | `https` | product documentation | да | [открыть / open](https://gpm.nasa.gov/data/imerg) |
| GES DISC | `https` | search and download | да | [открыть / open](https://disc.gsfc.nasa.gov/) |

### ПО, библиотеки и декодеры

- [earthaccess](https://github.com/nsidc/earthaccess) — search and download.
- [xarray](https://github.com/pydata/xarray) — NetCDF processing.
- **Быстрый выбор декодера по формату:** h5py / xarray, xarray / netCDF4, GDAL / rasterio.

### Рекомендуемый алгоритм автоматического приёма

1. Работать через официальный API с явными параметрами времени, области и продукта; соблюдать квоты и rate limit.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: h5py / xarray, xarray / netCDF4, GDAL / rasterio.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://gpm.nasa.gov/data/imerg](https://gpm.nasa.gov/data/imerg)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/satellite.yaml` → `id: nasa-gpm-imerg`.
- Для оперативного контура учитывать: `tier=specialized`, `operational=true`, `access.level=registration`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.


### 🧪 Проверенный пример получения данных

**Аудит:** 🛠 исправлено/уточнено · **проверено:** `2026-09-06`  
**Реальный режим доступа:** нужны бесплатные/договорные учётные данные (`credentials`)  
**Runtime-адаптер:** `external`  
**Recipe:** `catalog/recipes/satellite.json`

Через earthaccess найти один IMERG Early half-hour granule (`GPM_3IMERGHHE`) за фиксированную дату и скачать HDF5.

```bash
python -m weather_source describe nasa-gpm-imerg
python -m weather_source probe nasa-gpm-imerg
python -m weather_source fetch nasa-gpm-imerg --allow-external
```

**Требуемые переменные окружения:** `EARTHDATA_USERNAME`, `EARTHDATA_PASSWORD`.

**Что исправлено или обнаружено аудитом:**

- Карточка перечисляла портал GES DISC, но не давала воспроизводимого granule search/download. Стандартные GES DISC downloads используют Earthdata Login.

**Резервный источник:** `jaxa-gsmap`.

<details><summary>Команда официального/специализированного клиента</summary>

```bash
python -c "import earthaccess; earthaccess.login(strategy='environment'); r=earthaccess.search_data(short_name='GPM_3IMERGHHE',temporal=('2026-08-01T00:00:00Z','2026-08-01T00:30:00Z'),count=1); print(r); earthaccess.download(r,'nasa-imerg')"
```

</details>

> Клиент сохраняет исходные данные; крупные GRIB/NetCDF/радарные объекты по умолчанию блокируются безопасным лимитом. Для осознанной полной загрузки используйте `--full`, когда это применимо.

---

## 🇬🇧 English

### What it is

Multi-satellite global precipitation estimates with Early Late and Final runs.

**Provider:** NASA GPM  
**Status:** official; tier **specialized**.  
**Categories:** satellite, precipitation.  

### What it provides and when to use it

Useful where ground radar coverage is absent; distinguish satellite precipitation estimates from radar or gauge observations.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | near-global |
| Update cadence | half-hourly product grid; run availability differs |
| Typical latency | Early and Late runs are near-real-time with product-specific latency; Final is delayed research quality |
| Archive | multi-year archive through NASA GES DISC |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https`, `opendap`, `api` |
| Formats | `HDF5`, `NetCDF`, `GeoTIFF` |

### Access and restrictions

- **Access level:** `registration`.
- **Authentication:** Earthdata Login for standard authenticated downloads.
- **Terms/licensing:** NASA/GPM data terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| GPM IMERG | `https` | product documentation | yes | [открыть / open](https://gpm.nasa.gov/data/imerg) |
| GES DISC | `https` | search and download | yes | [открыть / open](https://disc.gsfc.nasa.gov/) |

### Software and decoders

- [earthaccess](https://github.com/nsidc/earthaccess) — search and download.
- [xarray](https://github.com/pydata/xarray) — NetCDF processing.

### Recommended ingestion flow

1. Use the official API with explicit product/time/area parameters and respect quotas and rate limits.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as h5py / xarray, xarray / netCDF4, GDAL / rasterio.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://gpm.nasa.gov/data/imerg](https://gpm.nasa.gov/data/imerg)

### 🧪 Executable retrieval recipe

**Audit verdict:** `corrected` · **verified:** `2026-09-06`  
**Runtime access:** `credentials` · **adapter:** `external`  
**Recipe:** `catalog/recipes/satellite.json`

```bash
python -m weather_source probe nasa-gpm-imerg
python -m weather_source fetch nasa-gpm-imerg --allow-external
```

Required environment: `EARTHDATA_USERNAME`, `EARTHDATA_PASSWORD`.

Fallback: `jaxa-gsmap`.

### Agent note

Authoritative record: `catalog/sources/satellite.yaml` → `id: nasa-gpm-imerg`. Treat this Markdown as a generated view; never override the YAML record from prose.
