# AviationWeather.gov Data API / AviationWeather.gov Data API

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`noaa-aviationweather` · 🟢 **основной / primary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Машинный доступ к METAR TAF и связанным авиационным метеопродуктам.

**Поставщик:** NOAA/NWS Aviation Weather Center  
**Статус:** официальный источник; приоритет — **основной**.  
**Категории:** Наземные наблюдения, aviation.  

### Что можно получить и когда использовать

Для автоматизации использовать документированный API а не парсинг страниц с декодированными METAR.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global aviation network |
| Периодичность/режим обновления | minutes |
| Типичная задержка | minutes |
| Архив | limited operational API history |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https`, `rest` |
| Форматы | `JSON`, `XML`, `CSV`, `text` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** none for normal public use; respect rate limits.
- **Лицензия/условия:** NOAA/NWS terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| Data API | `https` | API documentation | да | [открыть / open](https://aviationweather.gov/data/api/) |

### ПО, библиотеки и декодеры

- [requests](https://requests.readthedocs.io/) — REST client.
- **Быстрый выбор декодера по формату:** requests + stdlib json, lxml / ElementTree, pandas / csv.

### Рекомендуемый алгоритм автоматического приёма

1. Работать через официальный API с явными параметрами времени, области и продукта; соблюдать квоты и rate limit.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: requests + stdlib json, lxml / ElementTree, pandas / csv.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://aviationweather.gov/data/api/](https://aviationweather.gov/data/api/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/surface.yaml` → `id: noaa-aviationweather`.
- Для оперативного контура учитывать: `tier=primary`, `operational=true`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.


### 🧪 Проверенный пример получения данных

**Аудит:** 🛠 исправлено/уточнено · **проверено:** `2026-09-06`  
**Реальный режим доступа:** публичный машинный доступ (`public`)  
**Runtime-адаптер:** `http`  
**Recipe:** `catalog/recipes/surface.json`

Получить последние METAR для KJFK непосредственно из официального AviationWeather Data API в JSON.

```bash
python -m weather_source describe noaa-aviationweather
python -m weather_source probe noaa-aviationweather
python -m weather_source fetch noaa-aviationweather
```

**Что исправлено или обнаружено аудитом:**

- В основном каталоге указан только URL документации, хотя существует прямой Data API.
- Health-check landing page не доказывал получение METAR.

**Резервный источник:** `wmo-wis2`.

> Клиент сохраняет исходные данные; крупные GRIB/NetCDF/радарные объекты по умолчанию блокируются безопасным лимитом. Для осознанной полной загрузки используйте `--full`, когда это применимо.

---

## 🇬🇧 English

### What it is

Machine access to METAR TAF and related aviation weather products.

**Provider:** NOAA/NWS Aviation Weather Center  
**Status:** official; tier **primary**.  
**Categories:** surface, aviation.  

### What it provides and when to use it

Prefer the documented API over scraping decoded METAR pages.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global aviation network |
| Update cadence | minutes |
| Typical latency | minutes |
| Archive | limited operational API history |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https`, `rest` |
| Formats | `JSON`, `XML`, `CSV`, `text` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** none for normal public use; respect rate limits.
- **Terms/licensing:** NOAA/NWS terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| Data API | `https` | API documentation | yes | [открыть / open](https://aviationweather.gov/data/api/) |

### Software and decoders

- [requests](https://requests.readthedocs.io/) — REST client.

### Recommended ingestion flow

1. Use the official API with explicit product/time/area parameters and respect quotas and rate limits.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as requests + stdlib json, lxml / ElementTree, pandas / csv.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://aviationweather.gov/data/api/](https://aviationweather.gov/data/api/)

### 🧪 Executable retrieval recipe

**Audit verdict:** `corrected` · **verified:** `2026-09-06`  
**Runtime access:** `public` · **adapter:** `http`  
**Recipe:** `catalog/recipes/surface.json`

```bash
python -m weather_source probe noaa-aviationweather
python -m weather_source fetch noaa-aviationweather
```

Fallback: `wmo-wis2`.

### Agent note

Authoritative record: `catalog/sources/surface.yaml` → `id: noaa-aviationweather`. Treat this Markdown as a generated view; never override the YAML record from prose.
