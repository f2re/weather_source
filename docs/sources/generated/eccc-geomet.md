# ECCC MSC GeoMet / MSC GeoMet

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`eccc-geomet` · 🟢 **основной / primary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

OGC-сервисы канадских метеорологических и экологических слоёв.

**Поставщик:** Environment and Climate Change Canada  
**Статус:** официальный источник; приоритет — **основной**.  
**Категории:** Наземные наблюдения, Метеорологические радары, Численные модели прогноза, Климат и архивы.  

### Что можно получить и когда использовать

Для численных данных использовать WCS или OGC API; WMS прежде всего предназначен для визуализации.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | Canada |
| Периодичность/режим обновления | dataset dependent |
| Типичная задержка | minutes to hours |
| Архив | dataset dependent |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `wms`, `wcs`, `ogc-api`, `https` |
| Форматы | `GeoTIFF`, `PNG`, `JSON`, `GML`, `coverage-formats` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** none.
- **Лицензия/условия:** Government of Canada open-data terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| GeoMet API | `https` | OGC API | да | [открыть / open](https://api.weather.gc.ca/) |

### ПО, библиотеки и декодеры

- [OWSLib](https://github.com/geopython/OWSLib) — OGC client.
- [GDAL](https://gdal.org/) — raster/vector decoding.
- **Быстрый выбор декодера по формату:** GDAL / rasterio, requests + stdlib json, OWSLib / GDAL.

### Рекомендуемый алгоритм автоматического приёма

1. Использовать OGC API/WFS/WCS для численных данных; WMS применять главным образом для визуализации.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: GDAL / rasterio, requests + stdlib json, OWSLib / GDAL.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://eccc-msc.github.io/open-data/msc-geomet/readme_en/](https://eccc-msc.github.io/open-data/msc-geomet/readme_en/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/core.yaml` → `id: eccc-geomet`.
- Для оперативного контура учитывать: `tier=primary`, `operational=true`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.


### 🧪 Проверенный пример получения данных

**Аудит:** 🛠 исправлено/уточнено · **проверено:** `2026-09-06`  
**Реальный режим доступа:** публичный машинный доступ (`public`)  
**Runtime-адаптер:** `http`  
**Recipe:** `catalog/recipes/core.json`

Получить одну актуальную Surface Weather Observation из OGC API collection `swob-realtime` в JSON.

```bash
python -m weather_source describe eccc-geomet
python -m weather_source probe eccc-geomet
python -m weather_source fetch eccc-geomet
```

**Что исправлено или обнаружено аудитом:**

- Каталог указывал только API root; теперь пример подтверждает получение численных/атрибутивных данных, а не WMS-картинки.

**Резервный источник:** `eccc-datamart`.

> Клиент сохраняет исходные данные; крупные GRIB/NetCDF/радарные объекты по умолчанию блокируются безопасным лимитом. Для осознанной полной загрузки используйте `--full`, когда это применимо.

---

## 🇬🇧 English

### What it is

OGC web services for Canadian meteorological and environmental layers.

**Provider:** Environment and Climate Change Canada  
**Status:** official; tier **primary**.  
**Categories:** surface, radar, nwp, climate.  

### What it provides and when to use it

Use WCS or OGC API for data values; WMS is primarily presentation.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | Canada |
| Update cadence | dataset dependent |
| Typical latency | minutes to hours |
| Archive | dataset dependent |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `wms`, `wcs`, `ogc-api`, `https` |
| Formats | `GeoTIFF`, `PNG`, `JSON`, `GML`, `coverage-formats` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** none.
- **Terms/licensing:** Government of Canada open-data terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| GeoMet API | `https` | OGC API | yes | [открыть / open](https://api.weather.gc.ca/) |

### Software and decoders

- [OWSLib](https://github.com/geopython/OWSLib) — OGC client.
- [GDAL](https://gdal.org/) — raster/vector decoding.

### Recommended ingestion flow

1. Use OGC API/WFS/WCS for data values; treat WMS primarily as a presentation service.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as GDAL / rasterio, requests + stdlib json, OWSLib / GDAL.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://eccc-msc.github.io/open-data/msc-geomet/readme_en/](https://eccc-msc.github.io/open-data/msc-geomet/readme_en/)

### 🧪 Executable retrieval recipe

**Audit verdict:** `corrected` · **verified:** `2026-09-06`  
**Runtime access:** `public` · **adapter:** `http`  
**Recipe:** `catalog/recipes/core.json`

```bash
python -m weather_source probe eccc-geomet
python -m weather_source fetch eccc-geomet
```

Fallback: `eccc-datamart`.

### Agent note

Authoritative record: `catalog/sources/core.yaml` → `id: eccc-geomet`. Treat this Markdown as a generated view; never override the YAML record from prose.
