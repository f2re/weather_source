# Iowa Environmental Mesonet / Iowa Environmental Mesonet

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`iowa-mesonet` · ⚪ **агрегатор / aggregator** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Академический агрегатор и API для METAR радаров предупреждений аэрологии и других метеоданных.

**Поставщик:** Iowa Environmental Mesonet / Iowa State University  
**Статус:** неофициальный/агрегированный источник; приоритет — **агрегатор**.  
**Категории:** Наземные наблюдения, Метеорологические радары, Аэрология и верхняя атмосфера, archive.  

### Что можно получить и когда использовать

Очень удобный резервный источник но в критических системах первичными должны оставаться официальные каналы.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | primarily United States; selected global aviation and upper-air data |
| Периодичность/режим обновления | minutes to hours depending on dataset |
| Типичная задержка | near-real-time for many feeds |
| Архив | extensive archives for many US datasets |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https`, `rest` |
| Форматы | `JSON`, `CSV`, `text`, `GeoJSON`, `provider-dependent` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** generally none; respect service policies and request limits.
- **Лицензия/условия:** Iowa State/IEM usage policy and upstream provider terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| IEM | `https` | portal and API documentation | да | [открыть / open](https://mesonet.agron.iastate.edu/) |

### ПО, библиотеки и декодеры

- [Siphon IAStateUpperAir](https://unidata.github.io/siphon/latest/api/simplewebservice.html) — Python upper-air client.
- [requests](https://requests.readthedocs.io/) — REST and file client.
- **Быстрый выбор декодера по формату:** requests + stdlib json, pandas / csv, requests / geopandas.

### Рекомендуемый алгоритм автоматического приёма

1. Работать через официальный API с явными параметрами времени, области и продукта; соблюдать квоты и rate limit.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: requests + stdlib json, pandas / csv, requests / geopandas.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://mesonet.agron.iastate.edu/info/api.phtml](https://mesonet.agron.iastate.edu/info/api.phtml)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/aggregators.yaml` → `id: iowa-mesonet`.
- Для оперативного контура учитывать: `tier=aggregator`, `operational=true`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.


### 🧪 Проверенный пример получения данных

**Аудит:** 🛠 исправлено/уточнено · **проверено:** `2026-09-06`  
**Реальный режим доступа:** публичный машинный доступ (`public`)  
**Runtime-адаптер:** `http`  
**Recipe:** `catalog/recipes/aggregators.json`

Скачать воспроизводимый суточный CSV ASOS станции DSM за 2026-09-05 через официальный IEM CGI backend.

```bash
python -m weather_source describe iowa-mesonet
python -m weather_source probe iowa-mesonet
python -m weather_source fetch iowa-mesonet
```

**Что исправлено или обнаружено аудитом:**

- Карточка указывала только портал IEM; официальный API-документ прямо перечисляет scriptable CGI services, включая ASOS/METAR.

**Резервный источник:** `noaa-aviationweather`.

> Клиент сохраняет исходные данные; крупные GRIB/NetCDF/радарные объекты по умолчанию блокируются безопасным лимитом. Для осознанной полной загрузки используйте `--full`, когда это применимо.

---

## 🇬🇧 English

### What it is

High-value academic aggregation and APIs for METAR radar warnings radiosondes and other weather datasets.

**Provider:** Iowa Environmental Mesonet / Iowa State University  
**Status:** non-official/aggregated; tier **aggregator**.  
**Categories:** surface, radar, upper-air, archive.  

### What it provides and when to use it

Excellent convenience and fallback source but upstream official feeds should remain primary in critical systems.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | primarily United States; selected global aviation and upper-air data |
| Update cadence | minutes to hours depending on dataset |
| Typical latency | near-real-time for many feeds |
| Archive | extensive archives for many US datasets |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https`, `rest` |
| Formats | `JSON`, `CSV`, `text`, `GeoJSON`, `provider-dependent` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** generally none; respect service policies and request limits.
- **Terms/licensing:** Iowa State/IEM usage policy and upstream provider terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| IEM | `https` | portal and API documentation | yes | [открыть / open](https://mesonet.agron.iastate.edu/) |

### Software and decoders

- [Siphon IAStateUpperAir](https://unidata.github.io/siphon/latest/api/simplewebservice.html) — Python upper-air client.
- [requests](https://requests.readthedocs.io/) — REST and file client.

### Recommended ingestion flow

1. Use the official API with explicit product/time/area parameters and respect quotas and rate limits.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as requests + stdlib json, pandas / csv, requests / geopandas.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://mesonet.agron.iastate.edu/info/api.phtml](https://mesonet.agron.iastate.edu/info/api.phtml)

### 🧪 Executable retrieval recipe

**Audit verdict:** `corrected` · **verified:** `2026-09-06`  
**Runtime access:** `public` · **adapter:** `http`  
**Recipe:** `catalog/recipes/aggregators.json`

```bash
python -m weather_source probe iowa-mesonet
python -m weather_source fetch iowa-mesonet
```

Fallback: `noaa-aviationweather`.

### Agent note

Authoritative record: `catalog/sources/aggregators.yaml` → `id: iowa-mesonet`. Treat this Markdown as a generated view; never override the YAML record from prose.
