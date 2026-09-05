# MET Norway — открытые API / MET Norway open APIs

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`met-norway-api` · 🟡 **резервный/региональный / secondary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Открытые API наблюдений прогнозов и метаданных; Frost предоставляет исторические наблюдения.

**Поставщик:** MET Norway  
**Статус:** официальный источник; приоритет — **резервный/региональный**.  
**Категории:** Наземные наблюдения, Численные модели прогноза, Климат и архивы.  

### Что можно получить и когда использовать

Соблюдать требование идентифицирующего User-Agent и опубликованную политику запросов.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | Norway / Nordic / selected global forecast services |
| Периодичность/режим обновления | minutes to hours |
| Типичная задержка | low |
| Архив | historical observations through Frost |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https`, `rest` |
| Форматы | `JSON`, `GeoJSON`, `NetCDF`, `provider-dependent` |

### Доступ и ограничения

- **Уровень доступа:** бесплатный после регистрации (`registration`).
- **Авторизация:** some APIs anonymous with User-Agent policy; Frost uses client credentials.
- **Лицензия/условия:** MET Norway licence and terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| MET APIs | `https` | API index | да | [открыть / open](https://api.met.no/) |
| Frost API | `https` | observations API | да | [открыть / open](https://frost.met.no/) |

### ПО, библиотеки и декодеры

- [requests](https://requests.readthedocs.io/) — REST client.
- **Быстрый выбор декодера по формату:** requests + stdlib json, requests / geopandas, xarray / netCDF4.

### Рекомендуемый алгоритм автоматического приёма

1. Работать через официальный API с явными параметрами времени, области и продукта; соблюдать квоты и rate limit.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: requests + stdlib json, requests / geopandas, xarray / netCDF4.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://api.met.no/](https://api.met.no/)
- [https://frost.met.no/](https://frost.met.no/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/core.yaml` → `id: met-norway-api`.
- Для оперативного контура учитывать: `tier=secondary`, `operational=true`, `access.level=registration`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

Open APIs for observations forecasts and metadata; Frost provides historical observations.

**Provider:** MET Norway  
**Status:** official; tier **secondary**.  
**Categories:** surface, nwp, climate.  

### What it provides and when to use it

Respect the required identifying User-Agent and documented request policy.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | Norway / Nordic / selected global forecast services |
| Update cadence | minutes to hours |
| Typical latency | low |
| Archive | historical observations through Frost |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https`, `rest` |
| Formats | `JSON`, `GeoJSON`, `NetCDF`, `provider-dependent` |

### Access and restrictions

- **Access level:** `registration`.
- **Authentication:** some APIs anonymous with User-Agent policy; Frost uses client credentials.
- **Terms/licensing:** MET Norway licence and terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| MET APIs | `https` | API index | yes | [открыть / open](https://api.met.no/) |
| Frost API | `https` | observations API | yes | [открыть / open](https://frost.met.no/) |

### Software and decoders

- [requests](https://requests.readthedocs.io/) — REST client.

### Recommended ingestion flow

1. Use the official API with explicit product/time/area parameters and respect quotas and rate limits.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as requests + stdlib json, requests / geopandas, xarray / netCDF4.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://api.met.no/](https://api.met.no/)
- [https://frost.met.no/](https://frost.met.no/)

### Agent note

Authoritative record: `catalog/sources/core.yaml` → `id: met-norway-api`. Treat this Markdown as a generated view; never override the YAML record from prose.
