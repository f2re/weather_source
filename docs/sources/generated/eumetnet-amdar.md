# AMDAR — самолётные наблюдения / AMDAR aircraft observations

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`eumetnet-amdar` · 🔵 **специализированный / specialized** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Самолётные наблюдения температуры, ветра и части влажностных параметров, включая профили набора и снижения около аэропортов.

**Поставщик:** EUMETNET / WMO  
**Статус:** официальный источник; приоритет — **специализированный**.  
**Категории:** Авиационные наблюдения, Аэрология и верхняя атмосфера.  

### Что можно получить и когда использовать

Очень ценные частые оперативные профили, но перед автоматическим использованием необходимо проверить права доступа.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global routes; strong European coverage through EUMETNET |
| Периодичность/режим обновления | continuous with flights |
| Типичная задержка | minutes to hours |
| Архив | availability and rights vary |
| Надёжность | `high` |
| Удобство автоматизации | `medium` |
| Протоколы | `mqtt`, `https`, `wis2` |
| Форматы | `BUFR` |

### Доступ и ограничения

- **Уровень доступа:** ограниченный доступ (`restricted`).
- **Авторизация:** some WIS2/core subsets may be open; many aircraft feeds have access restrictions.
- **Лицензия/условия:** WMO, EUMETNET and aircraft-operator terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| WMO aircraft-based observations | `https` | documentation | да | [открыть / open](https://community.wmo.int/en/activity-areas/aircraft-based-observations) |

### ПО, библиотеки и декодеры

- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR decoding.
- **Быстрый выбор декодера по формату:** ecCodes / pybufrkit.

### Рекомендуемый алгоритм автоматического приёма

1. Подписаться на нужную WIS2/MQTT-тему, принимать уведомления и скачивать payload по canonical/cache HTTPS-ссылке.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: ecCodes / pybufrkit.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://community.wmo.int/en/activity-areas/aircraft-based-observations](https://community.wmo.int/en/activity-areas/aircraft-based-observations)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/upper-air.yaml` → `id: eumetnet-amdar`.
- Для оперативного контура учитывать: `tier=specialized`, `operational=true`, `access.level=restricted`, `automation=medium`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

Aircraft-based temperature, wind and selected humidity observations, including ascent/descent profiles near airports.

**Provider:** EUMETNET / WMO  
**Status:** official; tier **specialized**.  
**Categories:** aircraft, upper-air.  

### What it provides and when to use it

Operationally valuable high-frequency profiles, but access rights must be checked before automated use.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global routes; strong European coverage through EUMETNET |
| Update cadence | continuous with flights |
| Typical latency | minutes to hours |
| Archive | availability and rights vary |
| Reliability | `high` |
| Automation | `medium` |
| Protocols | `mqtt`, `https`, `wis2` |
| Formats | `BUFR` |

### Access and restrictions

- **Access level:** `restricted`.
- **Authentication:** some WIS2/core subsets may be open; many aircraft feeds have access restrictions.
- **Terms/licensing:** WMO, EUMETNET and aircraft-operator terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| WMO aircraft-based observations | `https` | documentation | yes | [открыть / open](https://community.wmo.int/en/activity-areas/aircraft-based-observations) |

### Software and decoders

- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR decoding.

### Recommended ingestion flow

1. Subscribe to the required WIS2/MQTT topic, consume notifications, then download payloads from canonical/cache HTTPS links.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as ecCodes / pybufrkit.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://community.wmo.int/en/activity-areas/aircraft-based-observations](https://community.wmo.int/en/activity-areas/aircraft-based-observations)

### Agent note

Authoritative record: `catalog/sources/upper-air.yaml` → `id: eumetnet-amdar`. Treat this Markdown as a generated view; never override the YAML record from prose.
