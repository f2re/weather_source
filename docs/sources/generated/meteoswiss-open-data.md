# MeteoSwiss Open Government Data / MeteoSwiss Open Government Data

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`meteoswiss-open-data` · 🟢 **основной / primary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Швейцарские открытые метеорологические и климатические данные включая наблюдения и радиозонды.

**Поставщик:** MeteoSwiss  
**Статус:** официальный источник; приоритет — **основной**.  
**Категории:** Наземные наблюдения, Аэрология и верхняя атмосфера, Климат и архивы.  

### Что можно получить и когда использовать

Особенно удобен для простого файлового приёма радиозондов и станционных данных.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | Switzerland |
| Периодичность/режим обновления | minutes to 12-hourly depending on dataset |
| Типичная задержка | low |
| Архив | dataset dependent |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https` |
| Форматы | `CSV`, `NetCDF`, `provider-dependent` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** none for published OGD files.
- **Лицензия/условия:** Swiss OGD terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| MeteoSwiss Open Data | `https` | documentation | да | [открыть / open](https://www.meteoswiss.admin.ch/services-and-publications/service/open-data.html) |

### ПО, библиотеки и декодеры

- [pandas](https://pandas.pydata.org/) — CSV processing.
- [xarray](https://github.com/pydata/xarray) — NetCDF processing.
- **Быстрый выбор декодера по формату:** pandas / csv, xarray / netCDF4.

### Рекомендуемый алгоритм автоматического приёма

1. Забирать данные напрямую с официального HTTPS/FTP-файлового дерева, не парся HTML-визуализатор.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: pandas / csv, xarray / netCDF4.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://www.meteoswiss.admin.ch/services-and-publications/service/open-data.html](https://www.meteoswiss.admin.ch/services-and-publications/service/open-data.html)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/core.yaml` → `id: meteoswiss-open-data`.
- Для оперативного контура учитывать: `tier=primary`, `operational=true`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.


### 🧪 Проверенный пример получения данных

**Аудит:** 🛠 исправлено/уточнено · **проверено:** `2026-09-06`  
**Реальный режим доступа:** публичный машинный доступ (`public`)  
**Runtime-адаптер:** `external`  
**Recipe:** `catalog/recipes/core.json`

Через официальный STAC collection MeteoSwiss получить один реальный downloadable asset автоматической сети SMN.

```bash
python -m weather_source describe meteoswiss-open-data
python -m weather_source probe meteoswiss-open-data
python -m weather_source fetch meteoswiss-open-data --allow-external
```

**Что исправлено или обнаружено аудитом:**

- Карточка не отражала текущую STAC-раздачу `data.geo.admin.ch`. Портал документации недостаточен для автоматизации.

**Резервный источник:** `fmi-open-data`.

<details><summary>Команда официального/специализированного клиента</summary>

```bash
python -m weather_source.providers meteoswiss-stac
```

</details>

> Клиент сохраняет исходные данные; крупные GRIB/NetCDF/радарные объекты по умолчанию блокируются безопасным лимитом. Для осознанной полной загрузки используйте `--full`, когда это применимо.

---

## 🇬🇧 English

### What it is

Swiss open weather and climate datasets including observations and radiosonde products.

**Provider:** MeteoSwiss  
**Status:** official; tier **primary**.  
**Categories:** surface, upper-air, climate.  

### What it provides and when to use it

Particularly convenient for simple file-based radiosonde and station ingestion.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | Switzerland |
| Update cadence | minutes to 12-hourly depending on dataset |
| Typical latency | low |
| Archive | dataset dependent |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https` |
| Formats | `CSV`, `NetCDF`, `provider-dependent` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** none for published OGD files.
- **Terms/licensing:** Swiss OGD terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| MeteoSwiss Open Data | `https` | documentation | yes | [открыть / open](https://www.meteoswiss.admin.ch/services-and-publications/service/open-data.html) |

### Software and decoders

- [pandas](https://pandas.pydata.org/) — CSV processing.
- [xarray](https://github.com/pydata/xarray) — NetCDF processing.

### Recommended ingestion flow

1. Fetch the official HTTPS/FTP file tree directly; do not scrape rendered product viewers.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as pandas / csv, xarray / netCDF4.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://www.meteoswiss.admin.ch/services-and-publications/service/open-data.html](https://www.meteoswiss.admin.ch/services-and-publications/service/open-data.html)

### 🧪 Executable retrieval recipe

**Audit verdict:** `corrected` · **verified:** `2026-09-06`  
**Runtime access:** `public` · **adapter:** `external`  
**Recipe:** `catalog/recipes/core.json`

```bash
python -m weather_source probe meteoswiss-open-data
python -m weather_source fetch meteoswiss-open-data --allow-external
```

Fallback: `fmi-open-data`.

### Agent note

Authoritative record: `catalog/sources/core.yaml` → `id: meteoswiss-open-data`. Treat this Markdown as a generated view; never override the YAML record from prose.
