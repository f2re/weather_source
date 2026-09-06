# WMO WIS 2.0 — глобальные сервисы / WMO WIS 2.0 Global Services

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`wmo-wis2` · 🟢 **основной / primary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Глобальный событийный обмен основными и рекомендуемыми данными WMO; MQTT-уведомления указывают на HTTPS-файлы.

**Поставщик:** WMO  
**Статус:** официальный источник; приоритет — **основной**.  
**Категории:** Наземные наблюдения, Аэрология и верхняя атмосфера, Авиационные наблюдения, Спутниковые данные, Метеорологические радары, Численные модели прогноза, Метаданные.  

### Что можно получить и когда использовать

Предпочтительный глобальный транспорт оперативных наблюдений WMO при публикации как core data.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global |
| Периодичность/режим обновления | continuous / event driven |
| Типичная задержка | seconds to minutes depending on publisher |
| Архив | provider dependent; Global Cache is not a long-term archive |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `mqtt`, `https` |
| Форматы | `BUFR`, `GRIB2`, `NetCDF`, `JSON`, `XML`, `provider-dependent` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** anonymous for core data; some datasets may require rights.
- **Лицензия/условия:** WMO Unified Data Policy and publisher terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| WIS2 guide | `https` | documentation | да | [открыть / open](https://wmo-im.github.io/wis2-guide/) |
| wis2box documentation | `https` | reference implementation | да | [открыть / open](https://docs.wis2box.wis.wmo.int/) |

### ПО, библиотеки и декодеры

- [wis2downloader](https://github.com/World-Meteorological-Organization/wis2downloader) — WIS2 MQTT consumer/downloader.
- [pywis-pubsub](https://github.com/World-Meteorological-Organization/pywis-pubsub) — WIS2 pub/sub utilities.
- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR/GRIB decoding.
- **Быстрый выбор декодера по формату:** ecCodes / pybufrkit, ecCodes / wgrib2 / cfgrib, xarray / netCDF4, requests + stdlib json, lxml / ElementTree.

### Рекомендуемый алгоритм автоматического приёма

1. Подписаться на нужную WIS2/MQTT-тему, принимать уведомления и скачивать payload по canonical/cache HTTPS-ссылке.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: ecCodes / pybufrkit, ecCodes / wgrib2 / cfgrib, xarray / netCDF4, requests + stdlib json, lxml / ElementTree.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://wmo-im.github.io/wis2-guide/](https://wmo-im.github.io/wis2-guide/)
- [https://docs.wis2box.wis.wmo.int/](https://docs.wis2box.wis.wmo.int/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/core.yaml` → `id: wmo-wis2`.
- Для оперативного контура учитывать: `tier=primary`, `operational=true`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.


### 🧪 Проверенный пример получения данных

**Аудит:** 🛠 исправлено/уточнено · **проверено:** `2026-09-06`  
**Реальный режим доступа:** публичный машинный доступ (`public`)  
**Runtime-адаптер:** `wis2`  
**Recipe:** `catalog/recipes/core.json`

Подписаться на французский WIS2 Global Broker и получить первое core-data уведомление с последующим скачиванием payload.

```bash
python -m weather_source describe wmo-wis2
python -m weather_source probe wmo-wis2
python -m weather_source fetch wmo-wis2
```

**Что исправлено или обнаружено аудитом:**

- Каталог заявлял MQTT, но содержал только документацию и не содержал рабочего Global Broker.
- Для core data используются публичные Global Brokers с everyone/everyone; уведомление содержит ссылку на payload.

**Резервный источник:** `eccc-datamart`.

> Клиент сохраняет исходные данные; крупные GRIB/NetCDF/радарные объекты по умолчанию блокируются безопасным лимитом. Для осознанной полной загрузки используйте `--full`, когда это применимо.

---

## 🇬🇧 English

### What it is

Global event-driven exchange for WMO core and recommended meteorological data; MQTT notifications point to HTTPS payloads.

**Provider:** WMO  
**Status:** official; tier **primary**.  
**Categories:** surface, upper-air, aircraft, satellite, radar, nwp, metadata.  

### What it provides and when to use it

Preferred global transport for operational WMO observations when published as core data.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global |
| Update cadence | continuous / event driven |
| Typical latency | seconds to minutes depending on publisher |
| Archive | provider dependent; Global Cache is not a long-term archive |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `mqtt`, `https` |
| Formats | `BUFR`, `GRIB2`, `NetCDF`, `JSON`, `XML`, `provider-dependent` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** anonymous for core data; some datasets may require rights.
- **Terms/licensing:** WMO Unified Data Policy and publisher terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| WIS2 guide | `https` | documentation | yes | [открыть / open](https://wmo-im.github.io/wis2-guide/) |
| wis2box documentation | `https` | reference implementation | yes | [открыть / open](https://docs.wis2box.wis.wmo.int/) |

### Software and decoders

- [wis2downloader](https://github.com/World-Meteorological-Organization/wis2downloader) — WIS2 MQTT consumer/downloader.
- [pywis-pubsub](https://github.com/World-Meteorological-Organization/pywis-pubsub) — WIS2 pub/sub utilities.
- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR/GRIB decoding.

### Recommended ingestion flow

1. Subscribe to the required WIS2/MQTT topic, consume notifications, then download payloads from canonical/cache HTTPS links.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as ecCodes / pybufrkit, ecCodes / wgrib2 / cfgrib, xarray / netCDF4, requests + stdlib json, lxml / ElementTree.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://wmo-im.github.io/wis2-guide/](https://wmo-im.github.io/wis2-guide/)
- [https://docs.wis2box.wis.wmo.int/](https://docs.wis2box.wis.wmo.int/)

### 🧪 Executable retrieval recipe

**Audit verdict:** `corrected` · **verified:** `2026-09-06`  
**Runtime access:** `public` · **adapter:** `wis2`  
**Recipe:** `catalog/recipes/core.json`

```bash
python -m weather_source probe wmo-wis2
python -m weather_source fetch wmo-wis2
```

Fallback: `eccc-datamart`.

### Agent note

Authoritative record: `catalog/sources/core.yaml` → `id: wmo-wis2`. Treat this Markdown as a generated view; never override the YAML record from prose.
