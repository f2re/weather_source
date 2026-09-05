# Copernicus Marine Data Store / Copernicus Marine Data Store

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`copernicus-marine` · 🟢 **основной / primary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Глобальные и региональные океанические анализы прогнозы наблюдения реобработанные продукты и поля волн.

**Поставщик:** Copernicus Marine Service  
**Статус:** официальный источник; приоритет — **основной**.  
**Категории:** Океанографические данные, Морские наблюдения, waves, analysis, Численные модели прогноза.  

### Что можно получить и когда использовать

Для небольших районов использовать subset/get через официальный toolbox а не скачивать целые глобальные файлы.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global and regional seas |
| Периодичность/режим обновления | product dependent; daily and sub-daily operational products available |
| Типичная задержка | hours to days depending on product |
| Архив | multi-year archives and reprocessed products |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https`, `api` |
| Форматы | `NetCDF`, `Zarr`, `provider-dependent` |

### Доступ и ограничения

- **Уровень доступа:** бесплатный после регистрации (`registration`).
- **Авторизация:** free Copernicus Marine account or supported token/client flow.
- **Лицензия/условия:** Copernicus Marine licence and product terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| Copernicus Marine | `https` | service portal | да | [открыть / open](https://marine.copernicus.eu/) |
| Data Store | `https` | catalog and subset service | да | [открыть / open](https://data.marine.copernicus.eu/) |

### ПО, библиотеки и декодеры

- [copernicusmarine](https://github.com/mercator-ocean/copernicus-marine-toolbox) — official Python and CLI toolbox.
- [xarray](https://github.com/pydata/xarray) — NetCDF and Zarr processing.
- **Быстрый выбор декодера по формату:** xarray / netCDF4.

### Рекомендуемый алгоритм автоматического приёма

1. Работать через официальный API с явными параметрами времени, области и продукта; соблюдать квоты и rate limit.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: xarray / netCDF4.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://help.marine.copernicus.eu/](https://help.marine.copernicus.eu/)
- [https://data.marine.copernicus.eu/](https://data.marine.copernicus.eu/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/ocean.yaml` → `id: copernicus-marine`.
- Для оперативного контура учитывать: `tier=primary`, `operational=true`, `access.level=registration`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

Global and regional ocean analyses forecasts observations reprocessed products and wave datasets.

**Provider:** Copernicus Marine Service  
**Status:** official; tier **primary**.  
**Categories:** ocean, marine, waves, analysis, nwp.  

### What it provides and when to use it

Prefer the toolbox subset/get commands to downloading complete global files when only a small area is required.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global and regional seas |
| Update cadence | product dependent; daily and sub-daily operational products available |
| Typical latency | hours to days depending on product |
| Archive | multi-year archives and reprocessed products |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https`, `api` |
| Formats | `NetCDF`, `Zarr`, `provider-dependent` |

### Access and restrictions

- **Access level:** `registration`.
- **Authentication:** free Copernicus Marine account or supported token/client flow.
- **Terms/licensing:** Copernicus Marine licence and product terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| Copernicus Marine | `https` | service portal | yes | [открыть / open](https://marine.copernicus.eu/) |
| Data Store | `https` | catalog and subset service | yes | [открыть / open](https://data.marine.copernicus.eu/) |

### Software and decoders

- [copernicusmarine](https://github.com/mercator-ocean/copernicus-marine-toolbox) — official Python and CLI toolbox.
- [xarray](https://github.com/pydata/xarray) — NetCDF and Zarr processing.

### Recommended ingestion flow

1. Use the official API with explicit product/time/area parameters and respect quotas and rate limits.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as xarray / netCDF4.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://help.marine.copernicus.eu/](https://help.marine.copernicus.eu/)
- [https://data.marine.copernicus.eu/](https://data.marine.copernicus.eu/)

### Agent note

Authoritative record: `catalog/sources/ocean.yaml` → `id: copernicus-marine`. Treat this Markdown as a generated view; never override the YAML record from prose.
