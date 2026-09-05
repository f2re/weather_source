# Meteostat — погода и климат / Meteostat weather and climate data

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`meteostat` · ⚪ **агрегатор / aggregator** · неоперативный / non-operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Open-source интерфейс к историческим и недавним станционным данным собранным из нескольких источников.

**Поставщик:** Meteostat  
**Статус:** неофициальный/агрегированный источник; приоритет — **агрегатор**.  
**Категории:** Наземные наблюдения, Климат и архивы, archive.  

### Что можно получить и когда использовать

Удобен для истории; когда важны происхождение и оперативная задержка использовать национальные или WMO-источники.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global station network |
| Периодичность/режим обновления | periodic; not intended as a primary real-time feed |
| Типичная задержка | provider dependent and unsuitable for strict real-time SLAs |
| Архив | extensive historical station archive |
| Надёжность | `medium` |
| Удобство автоматизации | `high` |
| Протоколы | `https`, `api` |
| Форматы | `CSV`, `JSON`, `tabular` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** library and bulk access patterns vary.
- **Лицензия/условия:** Meteostat licence and upstream data terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| Meteostat developers | `https` | documentation | да | [открыть / open](https://dev.meteostat.net/) |

### ПО, библиотеки и декодеры

- [meteostat-python](https://github.com/meteostat/meteostat-python) — Python data client.
- [pandas](https://pandas.pydata.org/) — tabular processing.
- **Быстрый выбор декодера по формату:** pandas / csv, requests + stdlib json.

### Рекомендуемый алгоритм автоматического приёма

1. Работать через официальный API с явными параметрами времени, области и продукта; соблюдать квоты и rate limit.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: pandas / csv, requests + stdlib json.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://dev.meteostat.net/](https://dev.meteostat.net/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/aggregators.yaml` → `id: meteostat`.
- Для оперативного контура учитывать: `tier=aggregator`, `operational=false`, `access.level=open`, `automation=high`, `reliability=medium`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

Community/open-source interface to historical and recent station-based weather data assembled from multiple providers.

**Provider:** Meteostat  
**Status:** non-official/aggregated; tier **aggregator**.  
**Categories:** surface, climate, archive.  

### What it provides and when to use it

Good historical convenience layer; use national or WMO sources when provenance and operational latency matter.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global station network |
| Update cadence | periodic; not intended as a primary real-time feed |
| Typical latency | provider dependent and unsuitable for strict real-time SLAs |
| Archive | extensive historical station archive |
| Reliability | `medium` |
| Automation | `high` |
| Protocols | `https`, `api` |
| Formats | `CSV`, `JSON`, `tabular` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** library and bulk access patterns vary.
- **Terms/licensing:** Meteostat licence and upstream data terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| Meteostat developers | `https` | documentation | yes | [открыть / open](https://dev.meteostat.net/) |

### Software and decoders

- [meteostat-python](https://github.com/meteostat/meteostat-python) — Python data client.
- [pandas](https://pandas.pydata.org/) — tabular processing.

### Recommended ingestion flow

1. Use the official API with explicit product/time/area parameters and respect quotas and rate limits.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as pandas / csv, requests + stdlib json.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://dev.meteostat.net/](https://dev.meteostat.net/)

### Agent note

Authoritative record: `catalog/sources/aggregators.yaml` → `id: meteostat`. Treat this Markdown as a generated view; never override the YAML record from prose.
