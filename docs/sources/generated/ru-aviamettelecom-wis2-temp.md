# Российская аэрология TEMP через WIS2 / Russian upper-air TEMP via WIS2

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`ru-aviamettelecom-wis2-temp` · 🟢 **основной / primary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Российские радиозондовые наблюдения TEMP, публикуемые в экосистеме WIS2.

**Поставщик:** Aviamettelecom of Roshydromet / WMO  
**Статус:** официальный источник; приоритет — **основной**.  
**Категории:** Аэрология и верхняя атмосфера.  

### Что можно получить и когда использовать

Для машинного приёма использовать WIS2 как основной путь; IGRA/Wyoming держать как независимый резерв и архив.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | Russia |
| Периодичность/режим обновления | typically 00/12 UTC; station dependent |
| Типичная задержка | minutes after publication |
| Архив | WIS2 cache retention; long-term archive via other services |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `mqtt`, `https`, `wis2` |
| Форматы | `BUFR` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** anonymous WIS2 core access where published.
- **Лицензия/условия:** WMO Unified Data Policy and publisher terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| WIS2 topic | `wis2` | subscription topic | нет | `wis2://cache/a/wis2/ru-aviamettelecom/data/core/weather/surface-based-observations/temp` |
| WIS2 guide | `https` | documentation | да | [открыть / open](https://wmo-im.github.io/wis2-guide/) |

### ПО, библиотеки и декодеры

- [wis2downloader](https://github.com/World-Meteorological-Organization/wis2downloader) — receive notifications and payloads.
- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR decoding.
- **Быстрый выбор декодера по формату:** ecCodes / pybufrkit.

### Рекомендуемый алгоритм автоматического приёма

1. Подписаться на нужную WIS2/MQTT-тему, принимать уведомления и скачивать payload по canonical/cache HTTPS-ссылке.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: ecCodes / pybufrkit.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://wmo-im.github.io/wis2-guide/](https://wmo-im.github.io/wis2-guide/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/upper-air.yaml` → `id: ru-aviamettelecom-wis2-temp`.
- Для оперативного контура учитывать: `tier=primary`, `operational=true`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

Russian radiosonde/TEMP observations published in the WIS2 ecosystem.

**Provider:** Aviamettelecom of Roshydromet / WMO  
**Status:** official; tier **primary**.  
**Categories:** upper-air.  

### What it provides and when to use it

Use WIS2 as the primary machine path; keep IGRA/Wyoming as independent fallback and archive paths.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | Russia |
| Update cadence | typically 00/12 UTC; station dependent |
| Typical latency | minutes after publication |
| Archive | WIS2 cache retention; long-term archive via other services |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `mqtt`, `https`, `wis2` |
| Formats | `BUFR` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** anonymous WIS2 core access where published.
- **Terms/licensing:** WMO Unified Data Policy and publisher terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| WIS2 topic | `wis2` | subscription topic | no | `wis2://cache/a/wis2/ru-aviamettelecom/data/core/weather/surface-based-observations/temp` |
| WIS2 guide | `https` | documentation | yes | [открыть / open](https://wmo-im.github.io/wis2-guide/) |

### Software and decoders

- [wis2downloader](https://github.com/World-Meteorological-Organization/wis2downloader) — receive notifications and payloads.
- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR decoding.

### Recommended ingestion flow

1. Subscribe to the required WIS2/MQTT topic, consume notifications, then download payloads from canonical/cache HTTPS links.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as ecCodes / pybufrkit.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://wmo-im.github.io/wis2-guide/](https://wmo-im.github.io/wis2-guide/)

### Agent note

Authoritative record: `catalog/sources/upper-air.yaml` → `id: ru-aviamettelecom-wis2-temp`. Treat this Markdown as a generated view; never override the YAML record from prose.
