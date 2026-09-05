# UK Met Office Weather DataHub / Met Office Weather DataHub

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`metoffice-datahub` · 🟡 **резервный/региональный / secondary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

API-доступ к выбранным наблюдениям и прогнозным продуктам UK Met Office.

**Поставщик:** UK Met Office  
**Статус:** официальный источник; приоритет — **резервный/региональный**.  
**Категории:** Наземные наблюдения, Численные модели прогноза, Аэрология и верхняя атмосфера.  

### Что можно получить и когда использовать

Бесплатный доступ полезен но необходимо проверять квоты и доступность конкретного продукта.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | UK and selected global products |
| Периодичность/режим обновления | product dependent |
| Типичная задержка | minutes to hours |
| Архив | product dependent |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https`, `rest` |
| Форматы | `JSON`, `GeoJSON`, `GRIB2`, `provider-dependent` |

### Доступ и ограничения

- **Уровень доступа:** бесплатный тариф с квотами (`free-tier`).
- **Авторизация:** account and API key; quotas depend on product or plan.
- **Лицензия/условия:** Met Office DataHub terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| Weather DataHub | `https` | portal/API | да | [открыть / open](https://datahub.metoffice.gov.uk/) |

### ПО, библиотеки и декодеры

- [requests](https://requests.readthedocs.io/) — REST client.
- **Быстрый выбор декодера по формату:** requests + stdlib json, requests / geopandas, ecCodes / wgrib2 / cfgrib.

### Рекомендуемый алгоритм автоматического приёма

1. Работать через официальный API с явными параметрами времени, области и продукта; соблюдать квоты и rate limit.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: requests + stdlib json, requests / geopandas, ecCodes / wgrib2 / cfgrib.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://datahub.metoffice.gov.uk/](https://datahub.metoffice.gov.uk/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/core.yaml` → `id: metoffice-datahub`.
- Для оперативного контура учитывать: `tier=secondary`, `operational=true`, `access.level=free-tier`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

API access to selected Met Office observations and forecast products.

**Provider:** UK Met Office  
**Status:** official; tier **secondary**.  
**Categories:** surface, nwp, upper-air.  

### What it provides and when to use it

Free access is useful but quota and product entitlement must be checked.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | UK and selected global products |
| Update cadence | product dependent |
| Typical latency | minutes to hours |
| Archive | product dependent |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https`, `rest` |
| Formats | `JSON`, `GeoJSON`, `GRIB2`, `provider-dependent` |

### Access and restrictions

- **Access level:** `free-tier`.
- **Authentication:** account and API key; quotas depend on product or plan.
- **Terms/licensing:** Met Office DataHub terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| Weather DataHub | `https` | portal/API | yes | [открыть / open](https://datahub.metoffice.gov.uk/) |

### Software and decoders

- [requests](https://requests.readthedocs.io/) — REST client.

### Recommended ingestion flow

1. Use the official API with explicit product/time/area parameters and respect quotas and rate limits.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as requests + stdlib json, requests / geopandas, ecCodes / wgrib2 / cfgrib.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://datahub.metoffice.gov.uk/](https://datahub.metoffice.gov.uk/)

### Agent note

Authoritative record: `catalog/sources/core.yaml` → `id: metoffice-datahub`. Treat this Markdown as a generated view; never override the YAML record from prose.
