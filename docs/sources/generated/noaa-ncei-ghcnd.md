# NOAA/NCEI Global Historical Climatology Network daily (GHCNd) / NOAA/NCEI Global Historical Climatology Network daily (GHCNd)

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`noaa-ncei-ghcnd` · 🟢 **основной / primary** · неоперативный / non-operational · проверено / verified **2026-10-19**

---

## 🇷🇺 Русский

### Что это

Глобальный контролируемый архив суточных наземных наблюдений с температурой, осадками, снегом и другими элементами; доступен по станциям и годовыми bulk CSV-архивами.

**Поставщик:** NOAA National Centers for Environmental Information (NCEI)  
**Статус:** официальный источник; приоритет — **основной**.  
**Категории:** Наземные наблюдения, Климат и архивы, archive.  

### Что можно получить и когда использовать

Использовать GHCNd для суточной верификации, климатических базовых рядов и ML-targets, когда нужны суточные экстремумы/осадки. Он не заменяет субсуточные оперативные наблюдения.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global land stations |
| Периодичность/режим обновления | daily updates plus periodic full reconstruction |
| Типичная задержка | typically daily to recent-month coverage depending on contributing network |
| Архив | global long-term daily station archive |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https` |
| Форматы | `CSV`, `gzip`, `fixed-width text` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** none for HTTPS bulk files.
- **Лицензия/условия:** NOAA/NCEI public-data terms and dataset documentation.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| GHCNd product page | `https` | product documentation | да | [открыть / open](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily) |
| GHCNd bulk directory | `https` | station files, metadata and yearly bulk CSV archives | да | [открыть / open](https://www.ncei.noaa.gov/pub/data/ghcn/daily/) |

### ПО, библиотеки и декодеры

- [Python gzip](https://docs.python.org/3/library/gzip.html) — streaming decompression for yearly CSV.gz files.
- [Python csv](https://docs.python.org/3/library/csv.html) — CSV parser.
- **Быстрый выбор декодера по формату:** pandas / csv.

### Рекомендуемый алгоритм автоматического приёма

1. Забирать данные напрямую с официального HTTPS/FTP-файлового дерева, не парся HTML-визуализатор.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: pandas / csv.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily)
- [https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/noaa-observations.yaml` → `id: noaa-ncei-ghcnd`.
- Для оперативного контура учитывать: `tier=primary`, `operational=false`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

Global quality-controlled daily land-station climate archive with temperature, precipitation, snowfall and other daily elements, available as station files and yearly bulk CSV archives.

**Provider:** NOAA National Centers for Environmental Information (NCEI)  
**Status:** official; tier **primary**.  
**Categories:** surface, climate, archive.  

### What it provides and when to use it

Use GHCNd for daily verification, climate baselines and ML targets where daily extrema/precipitation are appropriate. Do not use it as a substitute for sub-daily operational observations.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global land stations |
| Update cadence | daily updates plus periodic full reconstruction |
| Typical latency | typically daily to recent-month coverage depending on contributing network |
| Archive | global long-term daily station archive |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https` |
| Formats | `CSV`, `gzip`, `fixed-width text` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** none for HTTPS bulk files.
- **Terms/licensing:** NOAA/NCEI public-data terms and dataset documentation.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| GHCNd product page | `https` | product documentation | yes | [открыть / open](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily) |
| GHCNd bulk directory | `https` | station files, metadata and yearly bulk CSV archives | yes | [открыть / open](https://www.ncei.noaa.gov/pub/data/ghcn/daily/) |

### Software and decoders

- [Python gzip](https://docs.python.org/3/library/gzip.html) — streaming decompression for yearly CSV.gz files.
- [Python csv](https://docs.python.org/3/library/csv.html) — CSV parser.

### Recommended ingestion flow

1. Fetch the official HTTPS/FTP file tree directly; do not scrape rendered product viewers.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as pandas / csv.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily)
- [https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt)

### Agent note

Authoritative record: `catalog/sources/noaa-observations.yaml` → `id: noaa-ncei-ghcnd`. Treat this Markdown as a generated view; never override the YAML record from prose.
