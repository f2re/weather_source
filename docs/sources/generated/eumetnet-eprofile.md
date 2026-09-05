# EUMETNET E-PROFILE / E-PROFILE

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`eumetnet-eprofile` · 🔵 **специализированный / specialized** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Европейская сеть профайлеров ветра, VWP по метеорадарам, доплеровских лидаров и ceilometer-продуктов.

**Поставщик:** EUMETNET  
**Статус:** официальный источник; приоритет — **специализированный**.  
**Категории:** Аэрология и верхняя атмосфера, profiler, Метеорологические радары.  

### Что можно получить и когда использовать

Полезен для заполнения временных промежутков между радиозондами частыми профилями ветра и другими вертикальными наблюдениями.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | Europe |
| Периодичность/режим обновления | minutes to hourly depending on instrument |
| Типичная задержка | near-real-time |
| Архив | archives through partner services |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `mqtt`, `https`, `wis2` |
| Форматы | `BUFR`, `NetCDF`, `provider-dependent` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** WIS2 core/open subsets where published; some products may have separate rules.
- **Лицензия/условия:** EUMETNET and WMO terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| E-PROFILE | `https` | documentation | да | [открыть / open](https://e-profile.eu/) |

### ПО, библиотеки и декодеры

- [wis2downloader](https://github.com/World-Meteorological-Organization/wis2downloader) — WIS2 receiving where available.
- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR decoding.
- **Быстрый выбор декодера по формату:** ecCodes / pybufrkit, xarray / netCDF4.

### Рекомендуемый алгоритм автоматического приёма

1. Подписаться на нужную WIS2/MQTT-тему, принимать уведомления и скачивать payload по canonical/cache HTTPS-ссылке.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: ecCodes / pybufrkit, xarray / netCDF4.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://e-profile.eu/](https://e-profile.eu/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/upper-air.yaml` → `id: eumetnet-eprofile`.
- Для оперативного контура учитывать: `tier=specialized`, `operational=true`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

European network of radar wind profilers, weather-radar vertical wind profiles, Doppler lidars and ceilometer profiling products.

**Provider:** EUMETNET  
**Status:** official; tier **specialized**.  
**Categories:** upper-air, profiler, radar.  

### What it provides and when to use it

Valuable for filling temporal gaps between radiosonde launches with frequent wind/profile observations.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | Europe |
| Update cadence | minutes to hourly depending on instrument |
| Typical latency | near-real-time |
| Archive | archives through partner services |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `mqtt`, `https`, `wis2` |
| Formats | `BUFR`, `NetCDF`, `provider-dependent` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** WIS2 core/open subsets where published; some products may have separate rules.
- **Terms/licensing:** EUMETNET and WMO terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| E-PROFILE | `https` | documentation | yes | [открыть / open](https://e-profile.eu/) |

### Software and decoders

- [wis2downloader](https://github.com/World-Meteorological-Organization/wis2downloader) — WIS2 receiving where available.
- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR decoding.

### Recommended ingestion flow

1. Subscribe to the required WIS2/MQTT topic, consume notifications, then download payloads from canonical/cache HTTPS links.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as ecCodes / pybufrkit, xarray / netCDF4.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://e-profile.eu/](https://e-profile.eu/)

### Agent note

Authoritative record: `catalog/sources/upper-air.yaml` → `id: eumetnet-eprofile`. Treat this Markdown as a generated view; never override the YAML record from prose.
