# ECMWF Open Data / ECMWF Open Data

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`ecmwf-open-data` · 🟢 **основной / primary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Бесплатный оперативный набор детерминированных и ансамблевых прогнозов ECMWF.

**Поставщик:** ECMWF  
**Статус:** официальный источник; приоритет — **основной**.  
**Категории:** Численные модели прогноза, Ансамблевые прогнозы.  

### Что можно получить и когда использовать

Сильный основной глобальный источник прогнозов; для отказоустойчивости держать NOAA или DWD.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global |
| Периодичность/режим обновления | 00/06/12/18 UTC streams; product dependent |
| Типичная задержка | files appear progressively after analysis time |
| Архив | short rolling operational retention |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https`, `s3` |
| Форматы | `GRIB2` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** none for public open-data endpoints.
- **Лицензия/условия:** ECMWF Open Data licence and terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| ECMWF Open Data | `https` | documentation | да | [открыть / open](https://www.ecmwf.int/en/forecasts/datasets/open-data) |

### ПО, библиотеки и декодеры

- [ecmwf-opendata](https://github.com/ecmwf/ecmwf-opendata) — official Python client.
- [ecCodes](https://github.com/ecmwf/eccodes) — GRIB2 decoder.
- [cfgrib](https://github.com/ecmwf/cfgrib) — xarray GRIB backend.
- **Быстрый выбор декодера по формату:** ecCodes / wgrib2 / cfgrib.

### Рекомендуемый алгоритм автоматического приёма

1. Использовать S3/object-storage API: листинг по префиксу продукта и времени, затем скачивание только новых объектов.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: ecCodes / wgrib2 / cfgrib.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://www.ecmwf.int/en/forecasts/datasets/open-data](https://www.ecmwf.int/en/forecasts/datasets/open-data)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/nwp.yaml` → `id: ecmwf-open-data`.
- Для оперативного контура учитывать: `tier=primary`, `operational=true`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.


### 🧪 Проверенный пример получения данных

**Аудит:** 🛠 исправлено/уточнено · **проверено:** `2026-09-06`  
**Реальный режим доступа:** публичный машинный доступ (`public`)  
**Runtime-адаптер:** `external`  
**Recipe:** `catalog/recipes/nwp.json`

Официальным ecmwf-opendata скачать из последнего доступного IFS-прогноза 2m temperature на шаге 24 в GRIB2.

```bash
python -m weather_source describe ecmwf-open-data
python -m weather_source probe ecmwf-open-data
python -m weather_source fetch ecmwf-open-data --allow-external
```

**Что исправлено или обнаружено аудитом:**

- В каталоге была только страница документации, хотя ECMWF поддерживает официальный ecmwf-opendata клиент.

**Резервный источник:** `noaa-nomads`.

<details><summary>Команда официального/специализированного клиента</summary>

```bash
python -c "from ecmwf.opendata import Client; r=Client(source='ecmwf').retrieve(type='fc', step=24, param='2t', target='ecmwf-2t.grib2'); print(r.datetime)"
```

</details>

> Клиент сохраняет исходные данные; крупные GRIB/NetCDF/радарные объекты по умолчанию блокируются безопасным лимитом. Для осознанной полной загрузки используйте `--full`, когда это применимо.

---

## 🇬🇧 English

### What it is

Free operational subset of ECMWF deterministic and ensemble forecasts.

**Provider:** ECMWF  
**Status:** official; tier **primary**.  
**Categories:** nwp, ensemble.  

### What it provides and when to use it

Strong primary global forecast source; keep NOAA or DWD as independent fallback.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global |
| Update cadence | 00/06/12/18 UTC streams; product dependent |
| Typical latency | files appear progressively after analysis time |
| Archive | short rolling operational retention |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https`, `s3` |
| Formats | `GRIB2` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** none for public open-data endpoints.
- **Terms/licensing:** ECMWF Open Data licence and terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| ECMWF Open Data | `https` | documentation | yes | [открыть / open](https://www.ecmwf.int/en/forecasts/datasets/open-data) |

### Software and decoders

- [ecmwf-opendata](https://github.com/ecmwf/ecmwf-opendata) — official Python client.
- [ecCodes](https://github.com/ecmwf/eccodes) — GRIB2 decoder.
- [cfgrib](https://github.com/ecmwf/cfgrib) — xarray GRIB backend.

### Recommended ingestion flow

1. Use the S3/object-storage API, list objects by product/time prefix and download only unseen objects.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as ecCodes / wgrib2 / cfgrib.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://www.ecmwf.int/en/forecasts/datasets/open-data](https://www.ecmwf.int/en/forecasts/datasets/open-data)

### 🧪 Executable retrieval recipe

**Audit verdict:** `corrected` · **verified:** `2026-09-06`  
**Runtime access:** `public` · **adapter:** `external`  
**Recipe:** `catalog/recipes/nwp.json`

```bash
python -m weather_source probe ecmwf-open-data
python -m weather_source fetch ecmwf-open-data --allow-external
```

Fallback: `noaa-nomads`.

### Agent note

Authoritative record: `catalog/sources/nwp.yaml` → `id: ecmwf-open-data`. Treat this Markdown as a generated view; never override the YAML record from prose.
