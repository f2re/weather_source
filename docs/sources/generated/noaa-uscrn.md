# NOAA U.S. Climate Reference Network (USCRN) / NOAA U.S. Climate Reference Network (USCRN)

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`noaa-uscrn` · 🔵 **специализированный / specialized** · оперативный / operational · проверено / verified **2026-10-19**

---

## 🇷🇺 Русский

### Что это

Эталонная климатическая сеть США с 5-минутными, часовыми и суточными продуктами, QC-флагами и параметрами температуры, осадков, радиации, влажности и состояния почвы.

**Поставщик:** NOAA/NCEI U.S. Climate Reference Network  
**Статус:** официальный источник; приоритет — **специализированный**.  
**Категории:** Наземные наблюдения, Климат и архивы, reference.  

### Что можно получить и когда использовать

USCRN особенно полезен как reference-quality факт для валидации в США, диагностики смещений и экспериментов с QC/датчиками; сеть не предназначена для максимальной пространственной плотности.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | United States reference-station network |
| Периодичность/режим обновления | 5-minute, hourly, daily and monthly products |
| Типичная задержка | near-real-time to routine product update depending on product |
| Архив | full station archive by product/year plus snapshot/update trees |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https`, `ftp` |
| Форматы | `text` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** none.
- **Лицензия/условия:** NOAA/NCEI public-data terms; cite dataset documentation where requested.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| USCRN products | `https` | product documentation and access directory | да | [открыть / open](https://www.ncei.noaa.gov/access/crn/products.html) |
| USCRN hourly files | `https` | hourly station/year text files | да | [открыть / open](https://www.ncei.noaa.gov/pub/data/uscrn/products/hourly02/) |

### ПО, библиотеки и декодеры

- [Python csv](https://docs.python.org/3/library/csv.html) — whitespace/tabular parser after applying documented headers.

### Рекомендуемый алгоритм автоматического приёма

1. Забирать данные напрямую с официального HTTPS/FTP-файлового дерева, не парся HTML-визуализатор.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат специализированным клиентом из раздела ПО; нормализацию выполнять поверх raw-данных.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://www.ncei.noaa.gov/access/crn/products.html](https://www.ncei.noaa.gov/access/crn/products.html)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/noaa-observations.yaml` → `id: noaa-uscrn`.
- Для оперативного контура учитывать: `tier=specialized`, `operational=true`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

Reference-quality U.S. climate observing network with 5-minute, hourly and daily products, quality flags and variables including temperature, precipitation, radiation, humidity and soil measurements.

**Provider:** NOAA/NCEI U.S. Climate Reference Network  
**Status:** official; tier **specialized**.  
**Categories:** surface, climate, reference.  

### What it provides and when to use it

Prefer USCRN as a reference-quality truth set for U.S. validation, bias diagnostics and sensor/QC experiments rather than for dense spatial coverage.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | United States reference-station network |
| Update cadence | 5-minute, hourly, daily and monthly products |
| Typical latency | near-real-time to routine product update depending on product |
| Archive | full station archive by product/year plus snapshot/update trees |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https`, `ftp` |
| Formats | `text` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** none.
- **Terms/licensing:** NOAA/NCEI public-data terms; cite dataset documentation where requested.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| USCRN products | `https` | product documentation and access directory | yes | [открыть / open](https://www.ncei.noaa.gov/access/crn/products.html) |
| USCRN hourly files | `https` | hourly station/year text files | yes | [открыть / open](https://www.ncei.noaa.gov/pub/data/uscrn/products/hourly02/) |

### Software and decoders

- [Python csv](https://docs.python.org/3/library/csv.html) — whitespace/tabular parser after applying documented headers.

### Recommended ingestion flow

1. Fetch the official HTTPS/FTP file tree directly; do not scrape rendered product viewers.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Use a provider-specific client from the software section and keep normalization additive to the raw archive.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://www.ncei.noaa.gov/access/crn/products.html](https://www.ncei.noaa.gov/access/crn/products.html)

### Agent note

Authoritative record: `catalog/sources/noaa-observations.yaml` → `id: noaa-uscrn`. Treat this Markdown as a generated view; never override the YAML record from prose.
