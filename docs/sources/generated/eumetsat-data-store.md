# EUMETSAT Data Store и Data Tailor / EUMETSAT Data Store and Data Tailor

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`eumetsat-data-store` · 🟢 **основной / primary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Оперативные и архивные продукты Meteosat Metop MTG и других метеорологических спутников EUMETSAT.

**Поставщик:** EUMETSAT  
**Статус:** официальный источник; приоритет — **основной**.  
**Категории:** Спутниковые данные, Грозопеленгация и молнии, Аэрология и верхняя атмосфера, clouds, Океанографические данные.  

### Что можно получить и когда использовать

Основной европейский спутниковый источник. Для оперативной метеорологии особенно важны MTG Lightning Imager а также IASI/GRAS.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | Europe Africa Atlantic Indian Ocean and global polar products |
| Периодичность/режим обновления | minutes to orbital cadence depending on mission/product |
| Типичная задержка | minutes to hours |
| Архив | extensive mission archives |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https`, `api` |
| Форматы | `NetCDF`, `HDF5`, `BUFR`, `HRIT`, `native`, `GeoTIFF` |

### Доступ и ограничения

- **Уровень доступа:** бесплатный после регистрации (`registration`).
- **Авторизация:** free EUMETSAT account and OAuth credentials for API use.
- **Лицензия/условия:** EUMETSAT data policy and product-specific terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| EUMETSAT Data Store | `https` | catalog/API | да | [открыть / open](https://data.eumetsat.int/) |

### ПО, библиотеки и декодеры

- [EUMDAC](https://gitlab.eumetsat.int/eumetlab/data-services/eumdac) — official Python and CLI client.
- [Satpy](https://github.com/pytroll/satpy) — satellite decoding and composites.
- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR decoding.
- **Быстрый выбор декодера по формату:** xarray / netCDF4, h5py / xarray, ecCodes / pybufrkit, GDAL / rasterio.

### Рекомендуемый алгоритм автоматического приёма

1. Работать через официальный API с явными параметрами времени, области и продукта; соблюдать квоты и rate limit.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: xarray / netCDF4, h5py / xarray, ecCodes / pybufrkit, GDAL / rasterio.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://user.eumetsat.int/resources/user-guides/eumetsat-data-access-client-eumdac-guide](https://user.eumetsat.int/resources/user-guides/eumetsat-data-access-client-eumdac-guide)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/satellite.yaml` → `id: eumetsat-data-store`.
- Для оперативного контура учитывать: `tier=primary`, `operational=true`, `access.level=registration`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.


### 🧪 Проверенный пример получения данных

**Аудит:** 🛠 исправлено/уточнено · **проверено:** `2026-09-06`  
**Реальный режим доступа:** нужны бесплатные/договорные учётные данные (`credentials`)  
**Runtime-адаптер:** `external`  
**Recipe:** `catalog/recipes/satellite.json`

Официальным EUMDAC авторизоваться, выбрать MTG FCI Level 1c collection `EO:EUM:DAT:0665`, найти продукт в небольшом историческом интервале и скачать первый продукт.

```bash
python -m weather_source describe eumetsat-data-store
python -m weather_source probe eumetsat-data-store
python -m weather_source fetch eumetsat-data-store --allow-external
```

**Требуемые переменные окружения:** `EUMETSAT_CONSUMER_KEY`, `EUMETSAT_CONSUMER_SECRET`.

**Что исправлено или обнаружено аудитом:**

- Просмотр коллекций доступен без регистрации, но программная загрузка через EUMDAC использует consumer key/secret. В карточке это нужно отделять от простого browsing.

**Резервный источник:** `noaa-goes`.

<details><summary>Команда официального/специализированного клиента</summary>

```bash
python -c "import os,datetime,shutil,eumdac; t=eumdac.AccessToken((os.environ['EUMETSAT_CONSUMER_KEY'],os.environ['EUMETSAT_CONSUMER_SECRET'])); ds=eumdac.DataStore(t); c=ds.get_collection('EO:EUM:DAT:0665'); p=next(iter(c.search(dtstart=datetime.datetime(2024,7,24,19,30),dtend=datetime.datetime(2024,7,24,19,40)))); f=p.open(); out=open(f.name,'wb'); shutil.copyfileobj(f,out); out.close(); f.close(); print(p)"
```

</details>

> Клиент сохраняет исходные данные; крупные GRIB/NetCDF/радарные объекты по умолчанию блокируются безопасным лимитом. Для осознанной полной загрузки используйте `--full`, когда это применимо.

---

## 🇬🇧 English

### What it is

Operational and archived Meteosat Metop MTG and related meteorological satellite products.

**Provider:** EUMETSAT  
**Status:** official; tier **primary**.  
**Categories:** satellite, lightning, upper-air, clouds, ocean.  

### What it provides and when to use it

Primary European satellite source. MTG Lightning Imager and IASI/GRAS products are especially important for operational meteorology.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | Europe Africa Atlantic Indian Ocean and global polar products |
| Update cadence | minutes to orbital cadence depending on mission/product |
| Typical latency | minutes to hours |
| Archive | extensive mission archives |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https`, `api` |
| Formats | `NetCDF`, `HDF5`, `BUFR`, `HRIT`, `native`, `GeoTIFF` |

### Access and restrictions

- **Access level:** `registration`.
- **Authentication:** free EUMETSAT account and OAuth credentials for API use.
- **Terms/licensing:** EUMETSAT data policy and product-specific terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| EUMETSAT Data Store | `https` | catalog/API | yes | [открыть / open](https://data.eumetsat.int/) |

### Software and decoders

- [EUMDAC](https://gitlab.eumetsat.int/eumetlab/data-services/eumdac) — official Python and CLI client.
- [Satpy](https://github.com/pytroll/satpy) — satellite decoding and composites.
- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR decoding.

### Recommended ingestion flow

1. Use the official API with explicit product/time/area parameters and respect quotas and rate limits.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as xarray / netCDF4, h5py / xarray, ecCodes / pybufrkit, GDAL / rasterio.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://user.eumetsat.int/resources/user-guides/eumetsat-data-access-client-eumdac-guide](https://user.eumetsat.int/resources/user-guides/eumetsat-data-access-client-eumdac-guide)

### 🧪 Executable retrieval recipe

**Audit verdict:** `corrected` · **verified:** `2026-09-06`  
**Runtime access:** `credentials` · **adapter:** `external`  
**Recipe:** `catalog/recipes/satellite.json`

```bash
python -m weather_source probe eumetsat-data-store
python -m weather_source fetch eumetsat-data-store --allow-external
```

Required environment: `EUMETSAT_CONSUMER_KEY`, `EUMETSAT_CONSUMER_SECRET`.

Fallback: `noaa-goes`.

### Agent note

Authoritative record: `catalog/sources/satellite.yaml` → `id: eumetsat-data-store`. Treat this Markdown as a generated view; never override the YAML record from prose.
