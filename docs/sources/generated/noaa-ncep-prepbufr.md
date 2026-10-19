# NCEP GDAS/GFS — observation dumps и PREPBUFR / NCEP GDAS/GFS observation dumps and PREPBUFR

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`noaa-ncep-prepbufr` · 🔵 **специализированный / specialized** · оперативный / operational · проверено / verified **2026-10-19**

---

## 🇷🇺 Русский

### Что это

Файлы пространства наблюдений NCEP, используемые в контуре ассимиляции GDAS/GFS: исходные BUFR dumps и подготовленные quality-controlled PREPBUFR.

**Поставщик:** NOAA/NWS/NCEP  
**Статус:** официальный источник; приоритет — **специализированный**.  
**Категории:** Наземные наблюдения, Аэрология и верхняя атмосфера, Авиационные наблюдения, Морские наблюдения, GNSS radio occultation, assimilation.  

### Что можно получить и когда использовать

Использовать этот источник для исследований observation-space, влияния наблюдений и воспроизведения ingest/QC NCEP, а не как обычную замену открытым станционным архивам. PREPBUFR может содержать ограниченные исходные наблюдения; автоматический downloader должен требовать явного подтверждения условий доступа.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global observation streams ingested by NCEP |
| Периодичность/режим обновления | GDAS/GFS cycle cadence |
| Типичная задержка | operational-cycle dependent |
| Архив | rolling NOMADS/NCEP operational product tree; longer retention varies by product |
| Надёжность | `high` |
| Удобство автоматизации | `medium` |
| Протоколы | `https`, `ftp` |
| Форматы | `BUFR`, `PREPBUFR` |

### Доступ и ограничения

- **Уровень доступа:** ограниченный доступ (`restricted`).
- **Авторизация:** public server paths exist for many files, but some constituent observations in dumps/PREPBUFR have redistribution restrictions.
- **Лицензия/условия:** NCEP product terms plus restricted-data rules for constituent observations; inspect restrictions before use or redistribution.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| NCEP GFS/GDAS product inventory | `https` | authoritative filenames and product inventory | да | [открыть / open](https://www.nco.ncep.noaa.gov/pmb/products/gfs/) |
| NCEP observation processing products | `https` | operational GDAS/GFS observation dump and PREPBUFR tree | да | [открыть / open](https://nomads.ncep.noaa.gov/pub/data/nccf/com/obsproc/prod/) |
| NCEP restricted data guidance | `https` | redistribution and use restrictions | да | [открыть / open](https://www.nco.ncep.noaa.gov/pmb/docs/restricted_data/) |

### ПО, библиотеки и декодеры

- [NCEPLIBS-bufr](https://github.com/NOAA-EMC/NCEPLIBS-bufr) — NCEP BUFR/PREPBUFR decoding library.
- **Быстрый выбор декодера по формату:** ecCodes / pybufrkit.

### Рекомендуемый алгоритм автоматического приёма

1. Забирать данные напрямую с официального HTTPS/FTP-файлового дерева, не парся HTML-визуализатор.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: ecCodes / pybufrkit.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://www.nco.ncep.noaa.gov/pmb/products/gfs/](https://www.nco.ncep.noaa.gov/pmb/products/gfs/)
- [https://www.nco.ncep.noaa.gov/pmb/docs/restricted_data/](https://www.nco.ncep.noaa.gov/pmb/docs/restricted_data/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/noaa-observations.yaml` → `id: noaa-ncep-prepbufr`.
- Для оперативного контура учитывать: `tier=specialized`, `operational=true`, `access.level=restricted`, `automation=medium`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

NCEP observation-space files used around GDAS/GFS data assimilation, including raw BUFR dumps and quality-controlled PREPBUFR products.

**Provider:** NOAA/NWS/NCEP  
**Status:** official; tier **specialized**.  
**Categories:** surface, upper-air, aircraft, marine, gnss-ro, assimilation.  

### What it provides and when to use it

Use this source for assimilation-space research, observation-impact studies and reproducing NCEP ingest/QC logic, not as a casual substitute for unrestricted station archives. PREPBUFR can contain restricted constituent observations; automated downloaders should require an explicit acknowledgement of those conditions.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global observation streams ingested by NCEP |
| Update cadence | GDAS/GFS cycle cadence |
| Typical latency | operational-cycle dependent |
| Archive | rolling NOMADS/NCEP operational product tree; longer retention varies by product |
| Reliability | `high` |
| Automation | `medium` |
| Protocols | `https`, `ftp` |
| Formats | `BUFR`, `PREPBUFR` |

### Access and restrictions

- **Access level:** `restricted`.
- **Authentication:** public server paths exist for many files, but some constituent observations in dumps/PREPBUFR have redistribution restrictions.
- **Terms/licensing:** NCEP product terms plus restricted-data rules for constituent observations; inspect restrictions before use or redistribution.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| NCEP GFS/GDAS product inventory | `https` | authoritative filenames and product inventory | yes | [открыть / open](https://www.nco.ncep.noaa.gov/pmb/products/gfs/) |
| NCEP observation processing products | `https` | operational GDAS/GFS observation dump and PREPBUFR tree | yes | [открыть / open](https://nomads.ncep.noaa.gov/pub/data/nccf/com/obsproc/prod/) |
| NCEP restricted data guidance | `https` | redistribution and use restrictions | yes | [открыть / open](https://www.nco.ncep.noaa.gov/pmb/docs/restricted_data/) |

### Software and decoders

- [NCEPLIBS-bufr](https://github.com/NOAA-EMC/NCEPLIBS-bufr) — NCEP BUFR/PREPBUFR decoding library.

### Recommended ingestion flow

1. Fetch the official HTTPS/FTP file tree directly; do not scrape rendered product viewers.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as ecCodes / pybufrkit.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://www.nco.ncep.noaa.gov/pmb/products/gfs/](https://www.nco.ncep.noaa.gov/pmb/products/gfs/)
- [https://www.nco.ncep.noaa.gov/pmb/docs/restricted_data/](https://www.nco.ncep.noaa.gov/pmb/docs/restricted_data/)

### Agent note

Authoritative record: `catalog/sources/noaa-observations.yaml` → `id: noaa-ncep-prepbufr`. Treat this Markdown as a generated view; never override the YAML record from prose.
