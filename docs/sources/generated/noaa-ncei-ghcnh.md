# NOAA/NCEI Global Historical Climatology Network hourly (GHCNh) / NOAA/NCEI Global Historical Climatology Network hourly (GHCNh)

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`noaa-ncei-ghcnh` · 🟢 **основной / primary** · неоперативный / non-operational · проверено / verified **2026-10-19**

---

## 🇷🇺 Русский

### Что это

Глобальный архив часовых и синоптических наземных наблюдений нового поколения, заменяющий legacy Integrated Surface Dataset (ISD); данные доступны по станциям и годам в PSV и Parquet.

**Поставщик:** NOAA National Centers for Environmental Information (NCEI)  
**Статус:** официальный источник; приоритет — **основной**.  
**Категории:** Наземные наблюдения, Климат и архивы, archive.  

### Что можно получить и когда использовать

Для новых конвейеров часовых станционных данных NOAA/NCEI использовать GHCNh. ISD/Global Hourly следует считать legacy-источником совместимости, а не основным новым контуром. При подготовке выборок для ML и верификации сохранять QC- и source-атрибуты поставщика.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global fixed land stations |
| Периодичность/режим обновления | daily dataset updates; station/year and period-of-record files |
| Типичная задержка | archival / near-current daily updates rather than a real-time feed |
| Архив | multi-decadal to century-scale station records depending on station |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https` |
| Форматы | `PSV`, `Parquet` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** none for bulk HTTPS access.
- **Лицензия/условия:** NOAA/NCEI public-data terms and dataset documentation.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| GHCNh product page | `https` | product documentation and access entry point | да | [открыть / open](https://www.ncei.noaa.gov/products/global-historical-climatology-network-hourly) |
| GHCNh station/year access | `https` | station/year PSV and Parquet bulk files | да | [открыть / open](https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/access/by-year/) |

### ПО, библиотеки и декодеры

- [Python csv](https://docs.python.org/3/library/csv.html) — PSV streaming parser.
- [Apache Arrow / PyArrow](https://arrow.apache.org/docs/python/) — Parquet reader for large-volume workflows.

### Рекомендуемый алгоритм автоматического приёма

1. Забирать данные напрямую с официального HTTPS/FTP-файлового дерева, не парся HTML-визуализатор.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат специализированным клиентом из раздела ПО; нормализацию выполнять поверх raw-данных.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://www.ncei.noaa.gov/products/global-historical-climatology-network-hourly](https://www.ncei.noaa.gov/products/global-historical-climatology-network-hourly)
- [https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/doc/ghcnh_DOCUMENTATION.pdf](https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/doc/ghcnh_DOCUMENTATION.pdf)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/noaa-observations.yaml` → `id: noaa-ncei-ghcnh`.
- Для оперативного контура учитывать: `tier=primary`, `operational=false`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

Next-generation global hourly and synoptic land-station archive replacing the legacy Integrated Surface Dataset (ISD), distributed in station/year PSV and Parquet files.

**Provider:** NOAA National Centers for Environmental Information (NCEI)  
**Status:** official; tier **primary**.  
**Categories:** surface, climate, archive.  

### What it provides and when to use it

Use GHCNh for new NOAA/NCEI hourly station pipelines. Treat ISD/Global Hourly as a legacy compatibility source rather than the preferred target for new ingestion. Preserve provider QC/source attributes when building training or verification datasets.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global fixed land stations |
| Update cadence | daily dataset updates; station/year and period-of-record files |
| Typical latency | archival / near-current daily updates rather than a real-time feed |
| Archive | multi-decadal to century-scale station records depending on station |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https` |
| Formats | `PSV`, `Parquet` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** none for bulk HTTPS access.
- **Terms/licensing:** NOAA/NCEI public-data terms and dataset documentation.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| GHCNh product page | `https` | product documentation and access entry point | yes | [открыть / open](https://www.ncei.noaa.gov/products/global-historical-climatology-network-hourly) |
| GHCNh station/year access | `https` | station/year PSV and Parquet bulk files | yes | [открыть / open](https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/access/by-year/) |

### Software and decoders

- [Python csv](https://docs.python.org/3/library/csv.html) — PSV streaming parser.
- [Apache Arrow / PyArrow](https://arrow.apache.org/docs/python/) — Parquet reader for large-volume workflows.

### Recommended ingestion flow

1. Fetch the official HTTPS/FTP file tree directly; do not scrape rendered product viewers.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Use a provider-specific client from the software section and keep normalization additive to the raw archive.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://www.ncei.noaa.gov/products/global-historical-climatology-network-hourly](https://www.ncei.noaa.gov/products/global-historical-climatology-network-hourly)
- [https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/doc/ghcnh_DOCUMENTATION.pdf](https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/doc/ghcnh_DOCUMENTATION.pdf)

### Agent note

Authoritative record: `catalog/sources/noaa-observations.yaml` → `id: noaa-ncei-ghcnh`. Treat this Markdown as a generated view; never override the YAML record from prose.
