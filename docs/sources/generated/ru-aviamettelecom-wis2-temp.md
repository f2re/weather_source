# Российская аэрология TEMP через WIS2 / Russian upper-air TEMP via WIS2

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`ru-aviamettelecom-wis2-temp` · 🟢 **основной / primary** · оперативный / operational · проверено / verified **2026-09-06**

---

## 🇷🇺 Русский

### Что это

Российские радиозондовые наблюдения TEMP, публикуемые как основные данные WMO в WIS2.

**Поставщик:** Aviamettelecom of Roshydromet / WMO  
**Статус:** официальный источник; приоритет — **основной**.  
**Категории:** Аэрология и верхняя атмосфера.  

### Что можно получить и когда использовать

Подписываться на точную тему из WIS2 GDC, а полезную нагрузку скачивать по ссылке из уведомления. IGRA/Wyoming держать как независимый резерв и архив.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | Russia |
| Периодичность/режим обновления | typically 00/12 UTC; station dependent |
| Типичная задержка | minutes after publication |
| Архив | WIS2 cache retention; long-term archive via IGRA/NCEI and other services |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `mqtt`, `https`, `wis2` |
| Форматы | `BUFR` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** everyone/everyone on public WIS2 Global Brokers for core-data subscription.
- **Лицензия/условия:** WMO Unified Data Policy and publisher terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| WIS2 Global Broker (CMA) | `mqtt` | subscribe to cache/a/wis2/ru-aviamettelecom/data/core/weather/surface-based-observations/temp | нет | `mqtts://gb.wis.cma.cn:8883` |
| WIS2 Global Discovery Catalogue record | `https` | authoritative discovery metadata and generated subscription examples | да | [открыть / open](https://wis2-gdc.weather.gc.ca/collections/wis2-discovery-metadata/items/urn%3Awmo%3Amd%3Aru-aviamettelecom%3Acore.surface-based-observations.temp?f=html) |
| WIS2 guide | `https` | documentation | да | [открыть / open](https://wmo-im.github.io/wis2-guide/) |

### ПО, библиотеки и декодеры

- [wis2downloader](https://github.com/World-Meteorological-Organization/wis2downloader) — receive notifications and payloads.
- [pywis-pubsub](https://github.com/World-Meteorological-Organization/pywis-pubsub) — WIS2 MQTT subscriber utilities.
- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR decoding.
- **Быстрый выбор декодера по формату:** ecCodes / pybufrkit.

### Рекомендуемый алгоритм автоматического приёма

1. Подписаться на нужную WIS2/MQTT-тему, принимать уведомления и скачивать payload по canonical/cache HTTPS-ссылке.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: ecCodes / pybufrkit.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://wis2-gdc.weather.gc.ca/collections/wis2-discovery-metadata/items/urn%3Awmo%3Amd%3Aru-aviamettelecom%3Acore.surface-based-observations.temp?f=html](https://wis2-gdc.weather.gc.ca/collections/wis2-discovery-metadata/items/urn%3Awmo%3Amd%3Aru-aviamettelecom%3Acore.surface-based-observations.temp?f=html)
- [https://wmo-im.github.io/wis2-guide/](https://wmo-im.github.io/wis2-guide/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/upper-air.yaml` → `id: ru-aviamettelecom-wis2-temp`.
- Для оперативного контура учитывать: `tier=primary`, `operational=true`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.


### 🧪 Проверенный пример получения данных

**Аудит:** 🛠 исправлено/уточнено · **проверено:** `2026-09-06`  
**Реальный режим доступа:** публичный машинный доступ (`public`)  
**Runtime-адаптер:** `wis2`  
**Recipe:** `catalog/recipes/upper-air.json`

Подписаться на точную российскую TEMP-тему из WIS2 GDC через публичный CMA Global Broker и сохранить первый пришедший BUFR payload.

```bash
python -m weather_source describe ru-aviamettelecom-wis2-temp
python -m weather_source probe ru-aviamettelecom-wis2-temp
python -m weather_source fetch ru-aviamettelecom-wis2-temp
```

**Что исправлено или обнаружено аудитом:**

- Старый `wis2://cache/...` был записан как URL, хотя это не рабочий URI загрузки.
- Актуальная WIS2 GDC запись публикует точную MQTT-тему `cache/a/wis2/ru-aviamettelecom/data/core/weather/surface-based-observations/temp` и конфигурацию Global Broker. Payload берётся из WIS2 notification.

**Резервный источник:** `noaa-ncei-igra`.

> Клиент сохраняет исходные данные; крупные GRIB/NetCDF/радарные объекты по умолчанию блокируются безопасным лимитом. Для осознанной полной загрузки используйте `--full`, когда это применимо.

---

## 🇬🇧 English

### What it is

Russian radiosonde/TEMP observations published as WMO core data in WIS2.

**Provider:** Aviamettelecom of Roshydromet / WMO  
**Status:** official; tier **primary**.  
**Categories:** upper-air.  

### What it provides and when to use it

Subscribe to the exact topic published by the WIS2 GDC; download the data payload from links in the notification. Keep IGRA/Wyoming as independent fallback and archive paths.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | Russia |
| Update cadence | typically 00/12 UTC; station dependent |
| Typical latency | minutes after publication |
| Archive | WIS2 cache retention; long-term archive via IGRA/NCEI and other services |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `mqtt`, `https`, `wis2` |
| Formats | `BUFR` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** everyone/everyone on public WIS2 Global Brokers for core-data subscription.
- **Terms/licensing:** WMO Unified Data Policy and publisher terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| WIS2 Global Broker (CMA) | `mqtt` | subscribe to cache/a/wis2/ru-aviamettelecom/data/core/weather/surface-based-observations/temp | no | `mqtts://gb.wis.cma.cn:8883` |
| WIS2 Global Discovery Catalogue record | `https` | authoritative discovery metadata and generated subscription examples | yes | [открыть / open](https://wis2-gdc.weather.gc.ca/collections/wis2-discovery-metadata/items/urn%3Awmo%3Amd%3Aru-aviamettelecom%3Acore.surface-based-observations.temp?f=html) |
| WIS2 guide | `https` | documentation | yes | [открыть / open](https://wmo-im.github.io/wis2-guide/) |

### Software and decoders

- [wis2downloader](https://github.com/World-Meteorological-Organization/wis2downloader) — receive notifications and payloads.
- [pywis-pubsub](https://github.com/World-Meteorological-Organization/pywis-pubsub) — WIS2 MQTT subscriber utilities.
- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR decoding.

### Recommended ingestion flow

1. Subscribe to the required WIS2/MQTT topic, consume notifications, then download payloads from canonical/cache HTTPS links.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as ecCodes / pybufrkit.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://wis2-gdc.weather.gc.ca/collections/wis2-discovery-metadata/items/urn%3Awmo%3Amd%3Aru-aviamettelecom%3Acore.surface-based-observations.temp?f=html](https://wis2-gdc.weather.gc.ca/collections/wis2-discovery-metadata/items/urn%3Awmo%3Amd%3Aru-aviamettelecom%3Acore.surface-based-observations.temp?f=html)
- [https://wmo-im.github.io/wis2-guide/](https://wmo-im.github.io/wis2-guide/)

### 🧪 Executable retrieval recipe

**Audit verdict:** `corrected` · **verified:** `2026-09-06`  
**Runtime access:** `public` · **adapter:** `wis2`  
**Recipe:** `catalog/recipes/upper-air.json`

```bash
python -m weather_source probe ru-aviamettelecom-wis2-temp
python -m weather_source fetch ru-aviamettelecom-wis2-temp
```

Fallback: `noaa-ncei-igra`.

### Agent note

Authoritative record: `catalog/sources/upper-air.yaml` → `id: ru-aviamettelecom-wis2-temp`. Treat this Markdown as a generated view; never override the YAML record from prose.
