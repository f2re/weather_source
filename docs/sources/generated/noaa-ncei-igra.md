# NOAA IGRA 2 — глобальная аэрология / Integrated Global Radiosonde Archive (IGRA) 2

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`noaa-ncei-igra` · 🟡 **резервный/региональный / secondary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Глобальный архив радиозондов и шар-пилотов с близким к оперативному обновлением для многих действующих станций.

**Поставщик:** NOAA/NCEI  
**Статус:** официальный источник; приоритет — **резервный/региональный**.  
**Категории:** Аэрология и верхняя атмосфера, archive, Климат и архивы.  

### Что можно получить и когда использовать

Сильный независимый резерв и архив аэрологии; не заменяет событийный оперативный приём через WIS2.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global |
| Периодичность/режим обновления | daily ingest; sounding schedules are station dependent |
| Типичная задержка | near-real-time to daily |
| Архив | 1905-present across the network; station dependent |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https` |
| Форматы | `fixed-width text`, `CSV-derived`, `BUFR-source` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** none.
- **Лицензия/условия:** NOAA/NCEI terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| IGRA product page | `https` | documentation and download | да | [открыть / open](https://www.ncei.noaa.gov/products/weather-balloon/integrated-global-radiosonde-archive) |

### ПО, библиотеки и декодеры

- [Siphon IGRAUpperAir](https://unidata.github.io/siphon/latest/api/simplewebservice.html) — Python retrieval client.
- **Быстрый выбор декодера по формату:** pandas / csv, ecCodes / pybufrkit.

### Рекомендуемый алгоритм автоматического приёма

1. Забирать данные напрямую с официального HTTPS/FTP-файлового дерева, не парся HTML-визуализатор.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: pandas / csv, ecCodes / pybufrkit.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://www.ncei.noaa.gov/products/weather-balloon/integrated-global-radiosonde-archive](https://www.ncei.noaa.gov/products/weather-balloon/integrated-global-radiosonde-archive)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/upper-air.yaml` → `id: noaa-ncei-igra`.
- Для оперативного контура учитывать: `tier=secondary`, `operational=true`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

Global radiosonde and pilot-balloon archive with near-real-time updates for many active stations.

**Provider:** NOAA/NCEI  
**Status:** official; tier **secondary**.  
**Categories:** upper-air, archive, climate.  

### What it provides and when to use it

Strong independent fallback and archive for radiosondes; not a substitute for event-driven WIS2 reception.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global |
| Update cadence | daily ingest; sounding schedules are station dependent |
| Typical latency | near-real-time to daily |
| Archive | 1905-present across the network; station dependent |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https` |
| Formats | `fixed-width text`, `CSV-derived`, `BUFR-source` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** none.
- **Terms/licensing:** NOAA/NCEI terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| IGRA product page | `https` | documentation and download | yes | [открыть / open](https://www.ncei.noaa.gov/products/weather-balloon/integrated-global-radiosonde-archive) |

### Software and decoders

- [Siphon IGRAUpperAir](https://unidata.github.io/siphon/latest/api/simplewebservice.html) — Python retrieval client.

### Recommended ingestion flow

1. Fetch the official HTTPS/FTP file tree directly; do not scrape rendered product viewers.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as pandas / csv, ecCodes / pybufrkit.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://www.ncei.noaa.gov/products/weather-balloon/integrated-global-radiosonde-archive](https://www.ncei.noaa.gov/products/weather-balloon/integrated-global-radiosonde-archive)

### Agent note

Authoritative record: `catalog/sources/upper-air.yaml` → `id: noaa-ncei-igra`. Treat this Markdown as a generated view; never override the YAML record from prose.
