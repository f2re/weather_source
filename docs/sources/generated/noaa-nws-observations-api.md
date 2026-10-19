# NWS API — станционные наблюдения / NWS API station observations

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`noaa-nws-observations-api` · 🟢 **основной / primary** · оперативный / operational · проверено / verified **2026-10-19**

---

## 🇷🇺 Русский

### Что это

Официальный JSON-LD API для текущих и недавних станционных наблюдений, метаданных станций и поиска станций по территории США и зависимым территориям.

**Поставщик:** NOAA/National Weather Service  
**Статус:** официальный источник; приоритет — **основной**.  
**Категории:** Наземные наблюдения, aviation, API и агрегаторы.  

### Что можно получить и когда использовать

Удобный оперативный fallback для точечных/станционных наблюдений в зоне NWS. Это не глобальный bulk-архив: для истории использовать GHCNh/GHCNd, а для более широкого оперативного ingest — WIS2/MADIS.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | United States and territories; station availability follows NWS/MADIS ingest |
| Периодичность/режим обновления | minutes / station dependent |
| Типичная задержка | minutes |
| Архив | recent operational API history; not a long-term climate archive |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https`, `rest` |
| Форматы | `JSON`, `JSON-LD`, `GeoJSON` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** no API key; descriptive User-Agent requested and reasonable rate limits apply.
- **Лицензия/условия:** NOAA/NWS open-data terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| NWS API | `rest` | observations, stations, forecasts and metadata API | да | [открыть / open](https://api.weather.gov/) |
| NWS API documentation | `https` | API contract and usage guidance | да | [открыть / open](https://www.weather.gov/documentation/services-web-api) |

### ПО, библиотеки и декодеры

- [requests](https://requests.readthedocs.io/) — REST client.
- **Быстрый выбор декодера по формату:** requests + stdlib json, requests / geopandas.

### Рекомендуемый алгоритм автоматического приёма

1. Работать через официальный API с явными параметрами времени, области и продукта; соблюдать квоты и rate limit.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: requests + stdlib json, requests / geopandas.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://www.weather.gov/documentation/services-web-api](https://www.weather.gov/documentation/services-web-api)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/noaa-observations.yaml` → `id: noaa-nws-observations-api`.
- Для оперативного контура учитывать: `tier=primary`, `operational=true`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

Official JSON-LD API for current and recent station observations, station metadata and station discovery across the United States and territories.

**Provider:** NOAA/National Weather Service  
**Status:** official; tier **primary**.  
**Categories:** surface, aviation, api.  

### What it provides and when to use it

Excellent low-friction operational fallback for point/station observations in the NWS domain. It is not designed as a global bulk station archive; use GHCNh/GHCNd for historical bulk workflows and WIS2/MADIS for broader operational ingest.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | United States and territories; station availability follows NWS/MADIS ingest |
| Update cadence | minutes / station dependent |
| Typical latency | minutes |
| Archive | recent operational API history; not a long-term climate archive |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https`, `rest` |
| Formats | `JSON`, `JSON-LD`, `GeoJSON` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** no API key; descriptive User-Agent requested and reasonable rate limits apply.
- **Terms/licensing:** NOAA/NWS open-data terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| NWS API | `rest` | observations, stations, forecasts and metadata API | yes | [открыть / open](https://api.weather.gov/) |
| NWS API documentation | `https` | API contract and usage guidance | yes | [открыть / open](https://www.weather.gov/documentation/services-web-api) |

### Software and decoders

- [requests](https://requests.readthedocs.io/) — REST client.

### Recommended ingestion flow

1. Use the official API with explicit product/time/area parameters and respect quotas and rate limits.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as requests + stdlib json, requests / geopandas.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://www.weather.gov/documentation/services-web-api](https://www.weather.gov/documentation/services-web-api)

### Agent note

Authoritative record: `catalog/sources/noaa-observations.yaml` → `id: noaa-nws-observations-api`. Treat this Markdown as a generated view; never override the YAML record from prose.
