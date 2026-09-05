# Open-Meteo API / Open-Meteo APIs

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`open-meteo` · ⚪ **агрегатор / aggregator** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Удобные API объединяющие модели погоды наблюдения и климатические продукты через единый интерфейс.

**Поставщик:** Open-Meteo  
**Статус:** неофициальный/агрегированный источник; приоритет — **агрегатор**.  
**Категории:** Численные модели прогноза, Наземные наблюдения, archive.  

### Что можно получить и когда использовать

Полезный унифицированный слой для прототипов; перед научным или оперативным использованием проверять исходную модель и её лицензию.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global |
| Периодичность/режим обновления | upstream-model dependent |
| Типичная задержка | upstream dependent |
| Архив | historical and archive APIs available for selected datasets |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https`, `rest` |
| Форматы | `JSON`, `CSV` |

### Доступ и ограничения

- **Уровень доступа:** бесплатный тариф с квотами (`free-tier`).
- **Авторизация:** free non-commercial/open access patterns plus paid/commercial plans; check current limits.
- **Лицензия/условия:** Open-Meteo licence and API terms plus upstream licences.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| Open-Meteo documentation | `https` | API documentation | да | [открыть / open](https://open-meteo.com/en/docs) |

### ПО, библиотеки и декодеры

- [requests](https://requests.readthedocs.io/) — REST client.
- **Быстрый выбор декодера по формату:** requests + stdlib json, pandas / csv.

### Рекомендуемый алгоритм автоматического приёма

1. Работать через официальный API с явными параметрами времени, области и продукта; соблюдать квоты и rate limit.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: requests + stdlib json, pandas / csv.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://open-meteo.com/en/docs](https://open-meteo.com/en/docs)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/aggregators.yaml` → `id: open-meteo`.
- Для оперативного контура учитывать: `tier=aggregator`, `operational=true`, `access.level=free-tier`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

Convenient APIs that aggregate weather models observations and climate-oriented products behind a unified interface.

**Provider:** Open-Meteo  
**Status:** non-official/aggregated; tier **aggregator**.  
**Categories:** nwp, surface, archive.  

### What it provides and when to use it

Useful normalization layer and prototype source; verify upstream model identity and licensing before scientific or operational use.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global |
| Update cadence | upstream-model dependent |
| Typical latency | upstream dependent |
| Archive | historical and archive APIs available for selected datasets |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https`, `rest` |
| Formats | `JSON`, `CSV` |

### Access and restrictions

- **Access level:** `free-tier`.
- **Authentication:** free non-commercial/open access patterns plus paid/commercial plans; check current limits.
- **Terms/licensing:** Open-Meteo licence and API terms plus upstream licences.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| Open-Meteo documentation | `https` | API documentation | yes | [открыть / open](https://open-meteo.com/en/docs) |

### Software and decoders

- [requests](https://requests.readthedocs.io/) — REST client.

### Recommended ingestion flow

1. Use the official API with explicit product/time/area parameters and respect quotas and rate limits.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as requests + stdlib json, pandas / csv.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://open-meteo.com/en/docs](https://open-meteo.com/en/docs)

### Agent note

Authoritative record: `catalog/sources/aggregators.yaml` → `id: open-meteo`. Treat this Markdown as a generated view; never override the YAML record from prose.
