# Открытые данные Météo-France / Météo-France Open Data

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`meteofrance-open-data` · 🟢 **основной / primary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Открытые наблюдения аэрология радиолокация и модельные продукты через французские сервисы.

**Поставщик:** Météo-France  
**Статус:** официальный источник; приоритет — **основной**.  
**Категории:** Наземные наблюдения, Аэрология и верхняя атмосфера, Метеорологические радары, Численные модели прогноза, Климат и архивы.  

### Что можно получить и когда использовать

Для каждого продукта отдельно проверять авторизацию — портал объединяет несколько схем доступа.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | France and overseas territories; selected global products |
| Периодичность/режим обновления | product dependent |
| Типичная задержка | minutes to hours |
| Архив | dataset dependent |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https`, `api` |
| Форматы | `BUFR`, `GRIB2`, `CSV`, `JSON`, `GeoTIFF`, `provider-dependent` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** some products may require account or token.
- **Лицензия/условия:** Etalab/Open Licence or dataset-specific terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| Météo-France data portal | `https` | catalog | да | [открыть / open](https://meteo.data.gouv.fr/) |

### ПО, библиотеки и декодеры

- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR/GRIB decoding.
- [pandas](https://pandas.pydata.org/) — CSV/tabular processing.
- **Быстрый выбор декодера по формату:** ecCodes / pybufrkit, ecCodes / wgrib2 / cfgrib, pandas / csv, requests + stdlib json, GDAL / rasterio.

### Рекомендуемый алгоритм автоматического приёма

1. Работать через официальный API с явными параметрами времени, области и продукта; соблюдать квоты и rate limit.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: ecCodes / pybufrkit, ecCodes / wgrib2 / cfgrib, pandas / csv, requests + stdlib json, GDAL / rasterio.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://meteo.data.gouv.fr/](https://meteo.data.gouv.fr/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/core.yaml` → `id: meteofrance-open-data`.
- Для оперативного контура учитывать: `tier=primary`, `operational=true`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.


### 🧪 Проверенный пример получения данных

**Аудит:** 🛠 исправлено/уточнено · **проверено:** `2026-09-06`  
**Реальный режим доступа:** публичный машинный доступ (`public`)  
**Runtime-адаптер:** `external`  
**Recipe:** `catalog/recipes/core.json`

Автоматически найти последний доступный 3-часовой SYNOP CSV Météo-France в `donnees_libres/Txt/Synop/`.

```bash
python -m weather_source describe meteofrance-open-data
python -m weather_source probe meteofrance-open-data
python -m weather_source fetch meteofrance-open-data --allow-external
```

**Что исправлено или обнаружено аудитом:**

- `meteo.data.gouv.fr` — каталог; для части данных существуют прямые anonymous files. Из-за разных схем нельзя считать весь портал одинаково open/API.

**Резервный источник:** `wmo-wis2`.

<details><summary>Команда официального/специализированного клиента</summary>

```bash
python -m weather_source.providers meteofrance-synop
```

</details>

> Клиент сохраняет исходные данные; крупные GRIB/NetCDF/радарные объекты по умолчанию блокируются безопасным лимитом. Для осознанной полной загрузки используйте `--full`, когда это применимо.

---

## 🇬🇧 English

### What it is

Open observations radiosondes radar and model products through French open-data services.

**Provider:** Météo-France  
**Status:** official; tier **primary**.  
**Categories:** surface, upper-air, radar, nwp, climate.  

### What it provides and when to use it

Check authentication per product because the portal contains multiple access patterns.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | France and overseas territories; selected global products |
| Update cadence | product dependent |
| Typical latency | minutes to hours |
| Archive | dataset dependent |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https`, `api` |
| Formats | `BUFR`, `GRIB2`, `CSV`, `JSON`, `GeoTIFF`, `provider-dependent` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** some products may require account or token.
- **Terms/licensing:** Etalab/Open Licence or dataset-specific terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| Météo-France data portal | `https` | catalog | yes | [открыть / open](https://meteo.data.gouv.fr/) |

### Software and decoders

- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR/GRIB decoding.
- [pandas](https://pandas.pydata.org/) — CSV/tabular processing.

### Recommended ingestion flow

1. Use the official API with explicit product/time/area parameters and respect quotas and rate limits.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as ecCodes / pybufrkit, ecCodes / wgrib2 / cfgrib, pandas / csv, requests + stdlib json, GDAL / rasterio.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://meteo.data.gouv.fr/](https://meteo.data.gouv.fr/)

### 🧪 Executable retrieval recipe

**Audit verdict:** `corrected` · **verified:** `2026-09-06`  
**Runtime access:** `public` · **adapter:** `external`  
**Recipe:** `catalog/recipes/core.json`

```bash
python -m weather_source probe meteofrance-open-data
python -m weather_source fetch meteofrance-open-data --allow-external
```

Fallback: `wmo-wis2`.

### Agent note

Authoritative record: `catalog/sources/core.yaml` → `id: meteofrance-open-data`. Treat this Markdown as a generated view; never override the YAML record from prose.
