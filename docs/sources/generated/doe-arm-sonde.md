# DOE ARM SONDE — радиозондовые наблюдения / ARM Balloon-Borne Sounding System (SONDE)

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`doe-arm-sonde` · 🔵 **специализированный / specialized** · неоперативный / non-operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Научные радиозондовые наблюдения обсерваторий и полевых кампаний ARM с давлением, температурой, влажностью и горизонтальным ветром.

**Поставщик:** U.S. Department of Energy Atmospheric Radiation Measurement (ARM) User Facility  
**Статус:** официальный источник; приоритет — **специализированный**.  
**Категории:** Аэрология и верхняя атмосфера, reference, research.  

### Что можно получить и когда использовать

Ценный набор для верификации и исследований со стандартизованными NetCDF-зондированиями. Не предназначен для замены синоптического realtime-приёма TEMP через WIS2.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | ARM observatories and field campaigns across multiple continents and oceans |
| Периодичность/режим обновления | launch schedule depends on observatory or campaign; many soundings are separated by 6-12 hours |
| Типичная задержка | ARM datastreams are generally available for download within 48 hours |
| Архив | more than 30 years of ARM atmospheric observations; site and campaign dependent |
| Надёжность | `high` |
| Удобство автоматизации | `medium` |
| Протоколы | `https` |
| Форматы | `NetCDF`, `ASCII`, `MWX` |

### Доступ и ограничения

- **Уровень доступа:** бесплатный после регистрации (`registration`).
- **Авторизация:** free ARM user account required for data download.
- **Лицензия/условия:** ARM data policy and citation requirements.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| ARM SONDE | `https` | instrument/product documentation | да | [открыть / open](https://arm.gov/data/vaps/sonde/) |
| ARM Data Discovery | `https` | search and download | да | [открыть / open](https://adc.arm.gov/discovery/) |

### ПО, библиотеки и декодеры

- [xarray](https://github.com/pydata/xarray) — NetCDF sounding processing.
- [netCDF4](https://github.com/Unidata/netcdf4-python) — NetCDF access.
- **Быстрый выбор декодера по формату:** xarray / netCDF4.

### Рекомендуемый алгоритм автоматического приёма

1. Забирать данные напрямую с официального HTTPS/FTP-файлового дерева, не парся HTML-визуализатор.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: xarray / netCDF4.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://arm.gov/data/vaps/sonde/](https://arm.gov/data/vaps/sonde/)
- [https://www.arm.gov/publications/tech_reports/handbooks/sonde_handbook.pdf](https://www.arm.gov/publications/tech_reports/handbooks/sonde_handbook.pdf)
- [https://armgov.svcs.arm.gov/data/](https://armgov.svcs.arm.gov/data/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/specialized.yaml` → `id: doe-arm-sonde`.
- Для оперативного контура учитывать: `tier=specialized`, `operational=false`, `access.level=registration`, `automation=medium`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

Research-quality radiosonde observations from ARM observatories and field campaigns measuring pressure, temperature, moisture and horizontal wind.

**Provider:** U.S. Department of Energy Atmospheric Radiation Measurement (ARM) User Facility  
**Status:** official; tier **specialized**.  
**Categories:** upper-air, reference, research.  

### What it provides and when to use it

Valuable validation/research dataset with standardized NetCDF sounding files. It is not intended to replace synoptic real-time WIS2 TEMP reception.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | ARM observatories and field campaigns across multiple continents and oceans |
| Update cadence | launch schedule depends on observatory or campaign; many soundings are separated by 6-12 hours |
| Typical latency | ARM datastreams are generally available for download within 48 hours |
| Archive | more than 30 years of ARM atmospheric observations; site and campaign dependent |
| Reliability | `high` |
| Automation | `medium` |
| Protocols | `https` |
| Formats | `NetCDF`, `ASCII`, `MWX` |

### Access and restrictions

- **Access level:** `registration`.
- **Authentication:** free ARM user account required for data download.
- **Terms/licensing:** ARM data policy and citation requirements.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| ARM SONDE | `https` | instrument/product documentation | yes | [открыть / open](https://arm.gov/data/vaps/sonde/) |
| ARM Data Discovery | `https` | search and download | yes | [открыть / open](https://adc.arm.gov/discovery/) |

### Software and decoders

- [xarray](https://github.com/pydata/xarray) — NetCDF sounding processing.
- [netCDF4](https://github.com/Unidata/netcdf4-python) — NetCDF access.

### Recommended ingestion flow

1. Fetch the official HTTPS/FTP file tree directly; do not scrape rendered product viewers.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as xarray / netCDF4.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://arm.gov/data/vaps/sonde/](https://arm.gov/data/vaps/sonde/)
- [https://www.arm.gov/publications/tech_reports/handbooks/sonde_handbook.pdf](https://www.arm.gov/publications/tech_reports/handbooks/sonde_handbook.pdf)
- [https://armgov.svcs.arm.gov/data/](https://armgov.svcs.arm.gov/data/)

### Agent note

Authoritative record: `catalog/sources/specialized.yaml` → `id: doe-arm-sonde`. Treat this Markdown as a generated view; never override the YAML record from prose.
