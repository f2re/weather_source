# Открытые данные JMA / JMA public meteorological data

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`jma-data` · 🟡 **резервный/региональный / secondary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Публичные наблюдения предупреждения радиолокационные спутниковые и модельные продукты JMA.

**Поставщик:** Japan Meteorological Agency  
**Статус:** официальный источник; приоритет — **резервный/региональный**.  
**Категории:** Наземные наблюдения, Аэрология и верхняя атмосфера, Метеорологические радары, Спутниковые данные, Численные модели прогноза.  

### Что можно получить и когда использовать

Машинный доступ зависит от продукта; перед внедрением проверять конкретный поток.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | Japan / western Pacific / global depending on product |
| Периодичность/режим обновления | minutes to model cycles |
| Типичная задержка | low to hours |
| Архив | dataset dependent |
| Надёжность | `high` |
| Удобство автоматизации | `medium` |
| Протоколы | `https` |
| Форматы | `BUFR`, `GRIB2`, `NetCDF`, `image`, `XML`, `provider-dependent` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** generally anonymous public access; bulk services may differ.
- **Лицензия/условия:** JMA terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| JMA data portal | `https` | portal | да | [открыть / open](https://www.data.jma.go.jp/) |

### ПО, библиотеки и декодеры

- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR/GRIB decoding.
- **Быстрый выбор декодера по формату:** ecCodes / pybufrkit, ecCodes / wgrib2 / cfgrib, xarray / netCDF4, lxml / ElementTree.

### Рекомендуемый алгоритм автоматического приёма

1. Забирать данные напрямую с официального HTTPS/FTP-файлового дерева, не парся HTML-визуализатор.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: ecCodes / pybufrkit, ecCodes / wgrib2 / cfgrib, xarray / netCDF4, lxml / ElementTree.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://www.jma.go.jp/jma/indexe.html](https://www.jma.go.jp/jma/indexe.html)
- [https://www.data.jma.go.jp/](https://www.data.jma.go.jp/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/core.yaml` → `id: jma-data`.
- Для оперативного контура учитывать: `tier=secondary`, `operational=true`, `access.level=open`, `automation=medium`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.


### 🧪 Проверенный пример получения данных

**Аудит:** 🛠 исправлено/уточнено · **проверено:** `2026-09-06`  
**Реальный режим доступа:** публичный машинный доступ (`public`)  
**Runtime-адаптер:** `http`  
**Recipe:** `catalog/recipes/core.json`

Получить официальный регулярный XML feed JMA как проверяемый публичный machine endpoint. Для бинарных продуктов использовать отдельные продуктовые каналы/WIS2.

```bash
python -m weather_source describe jma-data
python -m weather_source probe jma-data
python -m weather_source fetch jma-data
```

**Что исправлено или обнаружено аудитом:**

- `www.data.jma.go.jp` — широкий портал; machine access зависит от продукта. Нельзя обещать единый JMA API для BUFR/GRIB/radar/satellite.

**Резервный источник:** `wmo-wis2`.

> Клиент сохраняет исходные данные; крупные GRIB/NetCDF/радарные объекты по умолчанию блокируются безопасным лимитом. Для осознанной полной загрузки используйте `--full`, когда это применимо.

---

## 🇬🇧 English

### What it is

Public observations warnings radar satellite and NWP products through several JMA services.

**Provider:** Japan Meteorological Agency  
**Status:** official; tier **secondary**.  
**Categories:** surface, upper-air, radar, satellite, nwp.  

### What it provides and when to use it

Machine access is product-specific; validate the exact feed before deployment.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | Japan / western Pacific / global depending on product |
| Update cadence | minutes to model cycles |
| Typical latency | low to hours |
| Archive | dataset dependent |
| Reliability | `high` |
| Automation | `medium` |
| Protocols | `https` |
| Formats | `BUFR`, `GRIB2`, `NetCDF`, `image`, `XML`, `provider-dependent` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** generally anonymous public access; bulk services may differ.
- **Terms/licensing:** JMA terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| JMA data portal | `https` | portal | yes | [открыть / open](https://www.data.jma.go.jp/) |

### Software and decoders

- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR/GRIB decoding.

### Recommended ingestion flow

1. Fetch the official HTTPS/FTP file tree directly; do not scrape rendered product viewers.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as ecCodes / pybufrkit, ecCodes / wgrib2 / cfgrib, xarray / netCDF4, lxml / ElementTree.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://www.jma.go.jp/jma/indexe.html](https://www.jma.go.jp/jma/indexe.html)
- [https://www.data.jma.go.jp/](https://www.data.jma.go.jp/)

### 🧪 Executable retrieval recipe

**Audit verdict:** `corrected` · **verified:** `2026-09-06`  
**Runtime access:** `public` · **adapter:** `http`  
**Recipe:** `catalog/recipes/core.json`

```bash
python -m weather_source probe jma-data
python -m weather_source fetch jma-data
```

Fallback: `wmo-wis2`.

### Agent note

Authoritative record: `catalog/sources/core.yaml` → `id: jma-data`. Treat this Markdown as a generated view; never override the YAML record from prose.
