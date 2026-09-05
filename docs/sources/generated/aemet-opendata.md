# AEMET OpenData / AEMET OpenData

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`aemet-opendata` · 🟡 **резервный/региональный / secondary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

API испанской AEMET для наблюдений прогнозов климатологии и выбранных продуктов.

**Поставщик:** AEMET  
**Статус:** официальный источник; приоритет — **резервный/региональный**.  
**Категории:** Наземные наблюдения, Численные модели прогноза, Климат и архивы.  

### Что можно получить и когда использовать

Бесплатный ключ позволяет автоматизацию но учётные данные необходимо хранить безопасно.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | Spain and territories |
| Периодичность/режим обновления | minutes to hours |
| Типичная задержка | low |
| Архив | dataset dependent |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https`, `rest` |
| Форматы | `JSON`, `CSV`, `text`, `provider-dependent` |

### Доступ и ограничения

- **Уровень доступа:** бесплатный после регистрации (`registration`).
- **Авторизация:** free API key required.
- **Лицензия/условия:** AEMET OpenData terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| AEMET OpenData | `https` | portal/API | да | [открыть / open](https://opendata.aemet.es/centrodedescargas/inicio) |

### ПО, библиотеки и декодеры

- [requests](https://requests.readthedocs.io/) — REST client.
- **Быстрый выбор декодера по формату:** requests + stdlib json, pandas / csv.

### Рекомендуемый алгоритм автоматического приёма

1. Работать через официальный API с явными параметрами времени, области и продукта; соблюдать квоты и rate limit.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: requests + stdlib json, pandas / csv.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://opendata.aemet.es/centrodedescargas/inicio](https://opendata.aemet.es/centrodedescargas/inicio)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/core.yaml` → `id: aemet-opendata`.
- Для оперативного контура учитывать: `tier=secondary`, `operational=true`, `access.level=registration`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

Spanish State Meteorological Agency API for observations forecasts climatology and selected products.

**Provider:** AEMET  
**Status:** official; tier **secondary**.  
**Categories:** surface, nwp, climate.  

### What it provides and when to use it

Free key makes the service automatable but credentials must be managed securely.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | Spain and territories |
| Update cadence | minutes to hours |
| Typical latency | low |
| Archive | dataset dependent |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https`, `rest` |
| Formats | `JSON`, `CSV`, `text`, `provider-dependent` |

### Access and restrictions

- **Access level:** `registration`.
- **Authentication:** free API key required.
- **Terms/licensing:** AEMET OpenData terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| AEMET OpenData | `https` | portal/API | yes | [открыть / open](https://opendata.aemet.es/centrodedescargas/inicio) |

### Software and decoders

- [requests](https://requests.readthedocs.io/) — REST client.

### Recommended ingestion flow

1. Use the official API with explicit product/time/area parameters and respect quotas and rate limits.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as requests + stdlib json, pandas / csv.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://opendata.aemet.es/centrodedescargas/inicio](https://opendata.aemet.es/centrodedescargas/inicio)

### Agent note

Authoritative record: `catalog/sources/core.yaml` → `id: aemet-opendata`. Treat this Markdown as a generated view; never override the YAML record from prose.
