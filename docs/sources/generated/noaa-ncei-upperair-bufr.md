# NOAA/NCEI — глобальный поток аэрологии BUFR / Global Upper-Air BUFR Data Stream

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`noaa-ncei-upperair-bufr` · 🟡 **резервный/региональный / secondary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Сырые радиозондовые и шар-пилотные наблюдения глобального обмена WMO, получаемые через NWS Telecommunications Gateway и архивируемые NCEI.

**Поставщик:** NOAA/NCEI  
**Статус:** официальный источник; приоритет — **резервный/региональный**.  
**Категории:** Аэрология и верхняя атмосфера, archive.  

### Что можно получить и когда использовать

Сохранять исходные BUFR, если важны высокое вертикальное разрешение и оригинальные метаданные. Для реального времени при наличии предпочитать WIS2.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global, approximately 90S to 83N for the NWSTG collection |
| Периодичность/режим обновления | NCEI NWSTG collection updated daily; observations are typically synoptic sounding reports |
| Типичная задержка | archive-oriented daily update rather than event-driven real-time delivery |
| Архив | NWSTG global BUFR from 2017-present; related ECMWF and NWS-managed raw upper-air streams are also archived |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https` |
| Форматы | `BUFR` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** none for standard electronic download.
- **Лицензия/условия:** NOAA/NCEI data terms; dataset citation requested.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| Global BUFR upper-air dataset | `https` | metadata and direct-download entry | да | [открыть / open](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc%3AC01500) |
| IGRA raw BUFR overview | `https` | raw BUFR stream documentation | да | [открыть / open](https://www.ncei.noaa.gov/products/weather-balloon/integrated-global-radiosonde-archive) |

### ПО, библиотеки и декодеры

- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR decoding.
- [pybufrkit](https://github.com/ywangd/pybufrkit) — alternative Python BUFR toolkit.
- **Быстрый выбор декодера по формату:** ecCodes / pybufrkit.

### Рекомендуемый алгоритм автоматического приёма

1. Забирать данные напрямую с официального HTTPS/FTP-файлового дерева, не парся HTML-визуализатор.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: ecCodes / pybufrkit.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc%3AC01500](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc%3AC01500)
- [https://www.ncei.noaa.gov/products/weather-balloon/integrated-global-radiosonde-archive](https://www.ncei.noaa.gov/products/weather-balloon/integrated-global-radiosonde-archive)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/specialized.yaml` → `id: noaa-ncei-upperair-bufr`.
- Для оперативного контура учитывать: `tier=secondary`, `operational=true`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

Raw radiosonde and pilot-balloon observations received through the NWS Telecommunications Gateway from the global WMO exchange and archived by NCEI.

**Provider:** NOAA/NCEI  
**Status:** official; tier **secondary**.  
**Categories:** upper-air, archive.  

### What it provides and when to use it

Preserve these raw BUFR messages when high vertical resolution or original metadata are important. For real-time reception, prefer WIS2 where available.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global, approximately 90S to 83N for the NWSTG collection |
| Update cadence | NCEI NWSTG collection updated daily; observations are typically synoptic sounding reports |
| Typical latency | archive-oriented daily update rather than event-driven real-time delivery |
| Archive | NWSTG global BUFR from 2017-present; related ECMWF and NWS-managed raw upper-air streams are also archived |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https` |
| Formats | `BUFR` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** none for standard electronic download.
- **Terms/licensing:** NOAA/NCEI data terms; dataset citation requested.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| Global BUFR upper-air dataset | `https` | metadata and direct-download entry | yes | [открыть / open](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc%3AC01500) |
| IGRA raw BUFR overview | `https` | raw BUFR stream documentation | yes | [открыть / open](https://www.ncei.noaa.gov/products/weather-balloon/integrated-global-radiosonde-archive) |

### Software and decoders

- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR decoding.
- [pybufrkit](https://github.com/ywangd/pybufrkit) — alternative Python BUFR toolkit.

### Recommended ingestion flow

1. Fetch the official HTTPS/FTP file tree directly; do not scrape rendered product viewers.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as ecCodes / pybufrkit.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc%3AC01500](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc%3AC01500)
- [https://www.ncei.noaa.gov/products/weather-balloon/integrated-global-radiosonde-archive](https://www.ncei.noaa.gov/products/weather-balloon/integrated-global-radiosonde-archive)

### Agent note

Authoritative record: `catalog/sources/specialized.yaml` → `id: noaa-ncei-upperair-bufr`. Treat this Markdown as a generated view; never override the YAML record from prose.
