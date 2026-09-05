# WOUDC — озонозондовые профили и API / WOUDC Ozonesonde archive and API

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`woudc-ozonesonde` · 🔵 **специализированный / specialized** · неоперативный / non-operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Глобальная коллекция World Ozone and Ultraviolet Radiation Data Centre с озонозондовыми профилями и связанными наблюдениями озона и УФ-излучения.

**Поставщик:** WMO Global Atmosphere Watch / WOUDC / Environment and Climate Change Canada  
**Статус:** официальный источник; приоритет — **специализированный**.  
**Категории:** Аэрология и верхняя атмосфера, ozone, archive.  

### Что можно получить и когда использовать

Полные snapshots озонозондового набора распространяются как сжатые CSV-архивы и обновляются еженедельно; в архиве доступны и отдельные станционные файлы.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global specialized station network |
| Периодичность/режим обновления | station submissions are asynchronous; full dataset archive snapshots are updated weekly |
| Типичная задержка | archive/submission oriented rather than synoptic real-time |
| Архив | long-term global ozone and UV archive |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https`, `api` |
| Форматы | `CSV`, `ZIP`, `JSON`, `provider-dependent` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** anonymous public API and web-accessible archive for published data.
- **Лицензия/условия:** WOUDC Data Policy and attribution/citation requirements.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| WOUDC API | `api` | API and OpenAPI documentation | да | [открыть / open](https://api.woudc.org/?f=html) |
| Dataset snapshots | `https` | weekly full-dataset archives | да | [открыть / open](https://woudc.org/archive/Summaries/dataset-snapshots/) |

### ПО, библиотеки и декодеры

- [requests](https://requests.readthedocs.io/) — API and file retrieval.
- [pandas](https://pandas.pydata.org/) — extCSV and tabular processing.
- **Быстрый выбор декодера по формату:** pandas / csv, requests + stdlib json.

### Рекомендуемый алгоритм автоматического приёма

1. Работать через официальный API с явными параметрами времени, области и продукта; соблюдать квоты и rate limit.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: pandas / csv, requests + stdlib json.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://api.woudc.org/?f=html](https://api.woudc.org/?f=html)
- [https://woudc.org/en/data/data-use-policy](https://woudc.org/en/data/data-use-policy)
- [https://woudc.org/archive/Documentation/PDF_files/WOUDC_Guidebooks/o3_guidev2.pdf](https://woudc.org/archive/Documentation/PDF_files/WOUDC_Guidebooks/o3_guidev2.pdf)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/specialized.yaml` → `id: woudc-ozonesonde`.
- Для оперативного контура учитывать: `tier=specialized`, `operational=false`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

Global World Ozone and Ultraviolet Radiation Data Centre collection of ozonesonde profiles and related ozone/UV observations.

**Provider:** WMO Global Atmosphere Watch / WOUDC / Environment and Climate Change Canada  
**Status:** official; tier **specialized**.  
**Categories:** upper-air, ozone, archive.  

### What it provides and when to use it

Whole-dataset ozonesonde snapshots are distributed as compressed CSV archives and are updated weekly; station-level files are also available in the archive.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global specialized station network |
| Update cadence | station submissions are asynchronous; full dataset archive snapshots are updated weekly |
| Typical latency | archive/submission oriented rather than synoptic real-time |
| Archive | long-term global ozone and UV archive |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https`, `api` |
| Formats | `CSV`, `ZIP`, `JSON`, `provider-dependent` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** anonymous public API and web-accessible archive for published data.
- **Terms/licensing:** WOUDC Data Policy and attribution/citation requirements.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| WOUDC API | `api` | API and OpenAPI documentation | yes | [открыть / open](https://api.woudc.org/?f=html) |
| Dataset snapshots | `https` | weekly full-dataset archives | yes | [открыть / open](https://woudc.org/archive/Summaries/dataset-snapshots/) |

### Software and decoders

- [requests](https://requests.readthedocs.io/) — API and file retrieval.
- [pandas](https://pandas.pydata.org/) — extCSV and tabular processing.

### Recommended ingestion flow

1. Use the official API with explicit product/time/area parameters and respect quotas and rate limits.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as pandas / csv, requests + stdlib json.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://api.woudc.org/?f=html](https://api.woudc.org/?f=html)
- [https://woudc.org/en/data/data-use-policy](https://woudc.org/en/data/data-use-policy)
- [https://woudc.org/archive/Documentation/PDF_files/WOUDC_Guidebooks/o3_guidev2.pdf](https://woudc.org/archive/Documentation/PDF_files/WOUDC_Guidebooks/o3_guidev2.pdf)

### Agent note

Authoritative record: `catalog/sources/specialized.yaml` → `id: woudc-ozonesonde`. Treat this Markdown as a generated view; never override the YAML record from prose.
