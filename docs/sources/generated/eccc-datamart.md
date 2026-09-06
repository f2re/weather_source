# ECCC MSC Datamart / MSC Datamart

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`eccc-datamart` · 🟢 **основной / primary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Оперативные канадские и международные файлы наблюдений моделей и BUFR-бюллетеней с уведомлениями AMQP.

**Поставщик:** Environment and Climate Change Canada  
**Статус:** официальный источник; приоритет — **основной**.  
**Категории:** Наземные наблюдения, Аэрология и верхняя атмосфера, Метеорологические радары, Численные модели прогноза, Морские наблюдения.  

### Что можно получить и когда использовать

AMQP делает Datamart особенно удобным для событийного оперативного приёма.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | Canada plus international exchange and global model products |
| Периодичность/режим обновления | minutes to model-cycle cadence |
| Типичная задержка | low |
| Архив | rolling operational archive |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https`, `amqp` |
| Форматы | `BUFR`, `GRIB2`, `XML`, `CSV`, `GeoTIFF`, `provider-dependent` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** none for public Datamart.
- **Лицензия/условия:** Government of Canada open-data terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| MSC Datamart | `https` | file tree | да | [открыть / open](https://dd.weather.gc.ca/) |
| MSC Open Data docs | `https` | documentation | да | [открыть / open](https://eccc-msc.github.io/open-data/msc-data/readme_en/) |

### ПО, библиотеки и декодеры

- [pika](https://pika.readthedocs.io/) — AMQP notification consumer.
- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR/GRIB decoding.
- **Быстрый выбор декодера по формату:** ecCodes / pybufrkit, ecCodes / wgrib2 / cfgrib, lxml / ElementTree, pandas / csv, GDAL / rasterio.

### Рекомендуемый алгоритм автоматического приёма

1. Подключиться к AMQP-уведомлениям и получать новые файлы событийно, без постоянного polling.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: ecCodes / pybufrkit, ecCodes / wgrib2 / cfgrib, lxml / ElementTree, pandas / csv, GDAL / rasterio.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://eccc-msc.github.io/open-data/](https://eccc-msc.github.io/open-data/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/core.yaml` → `id: eccc-datamart`.
- Для оперативного контура учитывать: `tier=primary`, `operational=true`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.


### 🧪 Проверенный пример получения данных

**Аудит:** 🛠 исправлено/уточнено · **проверено:** `2026-09-06`  
**Реальный режим доступа:** публичный машинный доступ (`public`)  
**Runtime-адаптер:** `html_latest`  
**Recipe:** `catalog/recipes/core.json`

Из официального `/today/observations/swob-ml/latest/` выбрать и скачать последний SWOB XML.

```bash
python -m weather_source describe eccc-datamart
python -m weather_source probe eccc-datamart
python -m weather_source fetch eccc-datamart
```

**Что исправлено или обнаружено аудитом:**

- Корень Datamart не доказывал получение данных. Для текущих данных есть `/today/`; ECCC рекомендует AMQP/Sarracenia для событийного приёма.

**Резервный источник:** `eccc-geomet`.

> Клиент сохраняет исходные данные; крупные GRIB/NetCDF/радарные объекты по умолчанию блокируются безопасным лимитом. Для осознанной полной загрузки используйте `--full`, когда это применимо.

---

## 🇬🇧 English

### What it is

Operational Canadian and international files including observations model output and BUFR bulletins with AMQP notifications.

**Provider:** Environment and Climate Change Canada  
**Status:** official; tier **primary**.  
**Categories:** surface, upper-air, radar, nwp, marine.  

### What it provides and when to use it

AMQP makes Datamart particularly suitable for event-driven operational reception.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | Canada plus international exchange and global model products |
| Update cadence | minutes to model-cycle cadence |
| Typical latency | low |
| Archive | rolling operational archive |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https`, `amqp` |
| Formats | `BUFR`, `GRIB2`, `XML`, `CSV`, `GeoTIFF`, `provider-dependent` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** none for public Datamart.
- **Terms/licensing:** Government of Canada open-data terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| MSC Datamart | `https` | file tree | yes | [открыть / open](https://dd.weather.gc.ca/) |
| MSC Open Data docs | `https` | documentation | yes | [открыть / open](https://eccc-msc.github.io/open-data/msc-data/readme_en/) |

### Software and decoders

- [pika](https://pika.readthedocs.io/) — AMQP notification consumer.
- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR/GRIB decoding.

### Recommended ingestion flow

1. Consume AMQP notifications and fetch new products event-by-event instead of continuously polling directories.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as ecCodes / pybufrkit, ecCodes / wgrib2 / cfgrib, lxml / ElementTree, pandas / csv, GDAL / rasterio.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://eccc-msc.github.io/open-data/](https://eccc-msc.github.io/open-data/)

### 🧪 Executable retrieval recipe

**Audit verdict:** `corrected` · **verified:** `2026-09-06`  
**Runtime access:** `public` · **adapter:** `html_latest`  
**Recipe:** `catalog/recipes/core.json`

```bash
python -m weather_source probe eccc-datamart
python -m weather_source fetch eccc-datamart
```

Fallback: `eccc-geomet`.

### Agent note

Authoritative record: `catalog/sources/core.yaml` → `id: eccc-datamart`. Treat this Markdown as a generated view; never override the YAML record from prose.
