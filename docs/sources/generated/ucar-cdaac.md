# UCAR CDAAC — GNSS radio occultation / CDAAC GNSS Radio Occultation

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`ucar-cdaac` · 🔵 **специализированный / specialized** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Профили GNSS radio occultation с COSMIC и других миссий: рефрактивность и производные профили атмосферы.

**Поставщик:** UCAR/COSMIC  
**Статус:** официальный источник; приоритет — **специализированный**.  
**Категории:** Аэрология и верхняя атмосфера, Спутниковые данные.  

### Что можно получить и когда использовать

Дополняет радиозонды глобальной спутниковой вертикальной информацией; не смешивать retrieval-профили с прямыми in-situ зондированиями.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global |
| Периодичность/режим обновления | mission dependent |
| Типичная задержка | near-real-time for operational streams; public latency varies |
| Архив | large multi-mission archive |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https` |
| Форматы | `NetCDF`, `BUFR`, `native` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** many products are anonymous; service requirements may vary.
- **Лицензия/условия:** UCAR/COSMIC data terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| CDAAC | `https` | catalog and download | да | [открыть / open](https://cdaac-www.cosmic.ucar.edu/cdaac/) |

### ПО, библиотеки и декодеры

- [xarray](https://github.com/pydata/xarray) — NetCDF processing.
- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR decoding.
- **Быстрый выбор декодера по формату:** xarray / netCDF4, ecCodes / pybufrkit.

### Рекомендуемый алгоритм автоматического приёма

1. Забирать данные напрямую с официального HTTPS/FTP-файлового дерева, не парся HTML-визуализатор.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: xarray / netCDF4, ecCodes / pybufrkit.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://cdaac-www.cosmic.ucar.edu/cdaac/](https://cdaac-www.cosmic.ucar.edu/cdaac/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/upper-air.yaml` → `id: ucar-cdaac`.
- Для оперативного контура учитывать: `tier=specialized`, `operational=true`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

GNSS radio-occultation profiles from COSMIC and other missions with refractivity and derived atmospheric profiles.

**Provider:** UCAR/COSMIC  
**Status:** official; tier **specialized**.  
**Categories:** upper-air, satellite.  

### What it provides and when to use it

Complements radiosondes with global satellite-derived vertical information; do not mix retrievals with direct in-situ soundings.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global |
| Update cadence | mission dependent |
| Typical latency | near-real-time for operational streams; public latency varies |
| Archive | large multi-mission archive |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https` |
| Formats | `NetCDF`, `BUFR`, `native` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** many products are anonymous; service requirements may vary.
- **Terms/licensing:** UCAR/COSMIC data terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| CDAAC | `https` | catalog and download | yes | [открыть / open](https://cdaac-www.cosmic.ucar.edu/cdaac/) |

### Software and decoders

- [xarray](https://github.com/pydata/xarray) — NetCDF processing.
- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR decoding.

### Recommended ingestion flow

1. Fetch the official HTTPS/FTP file tree directly; do not scrape rendered product viewers.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as xarray / netCDF4, ecCodes / pybufrkit.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://cdaac-www.cosmic.ucar.edu/cdaac/](https://cdaac-www.cosmic.ucar.edu/cdaac/)

### Agent note

Authoritative record: `catalog/sources/upper-air.yaml` → `id: ucar-cdaac`. Treat this Markdown as a generated view; never override the YAML record from prose.
