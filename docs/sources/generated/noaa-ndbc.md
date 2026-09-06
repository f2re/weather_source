# NOAA NDBC — буи и морские наблюдения / NOAA NDBC

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`noaa-ndbc` · 🟢 **основной / primary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Оперативные наблюдения буёв и прибрежных станций включая ветер давление волны температуру воды и другие морские параметры.

**Поставщик:** NOAA National Data Buoy Center  
**Статус:** официальный источник; приоритет — **основной**.  
**Категории:** Морские наблюдения, Океанографические данные, Наземные наблюдения, waves.  

### Что можно получить и когда использовать

Простой официальный источник морских наблюдений хорошо подходящий для автоматического приёма.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | United States waters plus selected global partner stations |
| Периодичность/режим обновления | typically minutes to hourly depending on platform |
| Типичная задержка | minutes to tens of minutes |
| Архив | historical station files available |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https` |
| Форматы | `text`, `XML`, `NetCDF`, `provider-dependent` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** none.
- **Лицензия/условия:** NOAA public data terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| NDBC | `https` | operational portal and files | да | [открыть / open](https://www.ndbc.noaa.gov/) |
| NDBC data access | `https` | access documentation | да | [открыть / open](https://www.ndbc.noaa.gov/data_access.shtml) |

### ПО, библиотеки и декодеры

- [pandas](https://pandas.pydata.org/) — text and tabular processing.
- [xarray](https://github.com/pydata/xarray) — NetCDF processing.
- **Быстрый выбор декодера по формату:** lxml / ElementTree, xarray / netCDF4.

### Рекомендуемый алгоритм автоматического приёма

1. Забирать данные напрямую с официального HTTPS/FTP-файлового дерева, не парся HTML-визуализатор.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: lxml / ElementTree, xarray / netCDF4.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://www.ndbc.noaa.gov/data_access.shtml](https://www.ndbc.noaa.gov/data_access.shtml)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/ocean.yaml` → `id: noaa-ndbc`.
- Для оперативного контура учитывать: `tier=primary`, `operational=true`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.


### 🧪 Проверенный пример получения данных

**Аудит:** 🛠 исправлено/уточнено · **проверено:** `2026-09-06`  
**Реальный режим доступа:** публичный машинный доступ (`public`)  
**Runtime-адаптер:** `http`  
**Recipe:** `catalog/recipes/ocean.json`

Скачать официальный realtime2 текстовый поток буя 46042 (последние наблюдения).

```bash
python -m weather_source describe noaa-ndbc
python -m weather_source probe noaa-ndbc
python -m weather_source fetch noaa-ndbc
```

**Что исправлено или обнаружено аудитом:**

- Каталог ссылался на портал, но не содержал прямой operational-файл станции.

**Резервный источник:** `eccc-datamart`.

> Клиент сохраняет исходные данные; крупные GRIB/NetCDF/радарные объекты по умолчанию блокируются безопасным лимитом. Для осознанной полной загрузки используйте `--full`, когда это применимо.

---

## 🇬🇧 English

### What it is

Operational buoy and coastal station observations including wind pressure waves water temperature and selected ocean variables.

**Provider:** NOAA National Data Buoy Center  
**Status:** official; tier **primary**.  
**Categories:** marine, ocean, surface, waves.  

### What it provides and when to use it

Straightforward official marine observation source suitable for unattended ingestion.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | United States waters plus selected global partner stations |
| Update cadence | typically minutes to hourly depending on platform |
| Typical latency | minutes to tens of minutes |
| Archive | historical station files available |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https` |
| Formats | `text`, `XML`, `NetCDF`, `provider-dependent` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** none.
- **Terms/licensing:** NOAA public data terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| NDBC | `https` | operational portal and files | yes | [открыть / open](https://www.ndbc.noaa.gov/) |
| NDBC data access | `https` | access documentation | yes | [открыть / open](https://www.ndbc.noaa.gov/data_access.shtml) |

### Software and decoders

- [pandas](https://pandas.pydata.org/) — text and tabular processing.
- [xarray](https://github.com/pydata/xarray) — NetCDF processing.

### Recommended ingestion flow

1. Fetch the official HTTPS/FTP file tree directly; do not scrape rendered product viewers.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as lxml / ElementTree, xarray / netCDF4.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://www.ndbc.noaa.gov/data_access.shtml](https://www.ndbc.noaa.gov/data_access.shtml)

### 🧪 Executable retrieval recipe

**Audit verdict:** `corrected` · **verified:** `2026-09-06`  
**Runtime access:** `public` · **adapter:** `http`  
**Recipe:** `catalog/recipes/ocean.json`

```bash
python -m weather_source probe noaa-ndbc
python -m weather_source fetch noaa-ndbc
```

Fallback: `eccc-datamart`.

### Agent note

Authoritative record: `catalog/sources/ocean.yaml` → `id: noaa-ndbc`. Treat this Markdown as a generated view; never override the YAML record from prose.
