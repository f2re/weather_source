# EUMETNET E-PROFILE / E-PROFILE

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`eumetnet-eprofile` · 🔵 **специализированный / specialized** · оперативный / operational · проверено / verified **2026-09-06**

---

## 🇷🇺 Русский

### Что это

Европейская сеть профайлеров ветра, VWP по метеорадарам, доплеровских лидаров и ceilometer-продуктов.

**Поставщик:** EUMETNET  
**Статус:** официальный источник; приоритет — **специализированный**.  
**Категории:** Аэрология и верхняя атмосфера, profiler, Метеорологические радары.  

### Что можно получить и когда использовать

Полезен для заполнения промежутков между радиозондами, но единого неограниченного публичного machine endpoint для всех продуктов E-PROFILE нет. Перед оперативным приёмом нужно определить конкретный продукт, поставщика и права.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | Europe |
| Периодичность/режим обновления | minutes to hourly depending on instrument |
| Типичная задержка | near-real-time |
| Архив | archives through partner services |
| Надёжность | `high` |
| Удобство автоматизации | `medium` |
| Протоколы | `https`, `ftp` |
| Форматы | `BUFR`, `NetCDF`, `provider-dependent` |

### Доступ и ограничения

- **Уровень доступа:** ограниченный доступ (`restricted`).
- **Авторизация:** public visualization exists; third-party data use depends on EUMETNET/member licensing and product-specific rights.
- **Лицензия/условия:** EUMETNET/member data policy; no assumption of unrestricted commercial reuse.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| E-PROFILE | `https` | programme information and visualization entry point | да | [открыть / open](https://e-profile.eu/) |

### ПО, библиотеки и декодеры

- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR decoding where BUFR is supplied.
- **Быстрый выбор декодера по формату:** ecCodes / pybufrkit, xarray / netCDF4.

### Рекомендуемый алгоритм автоматического приёма

1. Забирать данные напрямую с официального HTTPS/FTP-файлового дерева, не парся HTML-визуализатор.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: ecCodes / pybufrkit, xarray / netCDF4.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://e-profile.eu/](https://e-profile.eu/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/upper-air.yaml` → `id: eumetnet-eprofile`.
- Для оперативного контура учитывать: `tier=specialized`, `operational=true`, `access.level=restricted`, `automation=medium`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.


### 🧪 Проверенный пример получения данных

**Аудит:** 🛠 исправлено/уточнено · **проверено:** `2026-09-06`  
**Реальный режим доступа:** доступ ограничен правами участника/лицензией (`restricted`)  
**Runtime-адаптер:** `unavailable`  
**Recipe:** `catalog/recipes/upper-air.json`

Использовать E-PROFILE как сеть/каталог и получать конкретный профиль через национального поставщика, WIS2 или лицензированный EUMETNET-канал после проверки прав конкретного продукта.

```bash
python -m weather_source describe eumetnet-eprofile
python -m weather_source probe eumetnet-eprofile
python -m weather_source example eumetnet-eprofile
```

**Что исправлено или обнаружено аудитом:**

- Сеть и продукты E-PROFILE существуют, но текущая карточка ошибочно превращала это в гарантированный anonymous WIS2 feed. Политика EUMETNET ограничивает часть третьестороннего использования и не подтверждает единый unrestricted bulk/API endpoint.

**Почему нет автоматического public fetch:** Нет одного гарантированного unrestricted machine endpoint для всей E-PROFILE сети; доступ зависит от конкретного продукта, поставщика и лицензии.

**Резервный источник:** `fmi-open-data`.

> Клиент сохраняет исходные данные; крупные GRIB/NetCDF/радарные объекты по умолчанию блокируются безопасным лимитом. Для осознанной полной загрузки используйте `--full`, когда это применимо.

---

## 🇬🇧 English

### What it is

European network of radar wind profilers, weather-radar vertical wind profiles, Doppler lidars and ceilometer profiling products.

**Provider:** EUMETNET  
**Status:** official; tier **specialized**.  
**Categories:** upper-air, profiler, radar.  

### What it provides and when to use it

Valuable for filling temporal gaps between radiosonde launches, but there is no single unrestricted public machine endpoint covering every E-PROFILE product. Resolve product rights and provider before operational ingest.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | Europe |
| Update cadence | minutes to hourly depending on instrument |
| Typical latency | near-real-time |
| Archive | archives through partner services |
| Reliability | `high` |
| Automation | `medium` |
| Protocols | `https`, `ftp` |
| Formats | `BUFR`, `NetCDF`, `provider-dependent` |

### Access and restrictions

- **Access level:** `restricted`.
- **Authentication:** public visualization exists; third-party data use depends on EUMETNET/member licensing and product-specific rights.
- **Terms/licensing:** EUMETNET/member data policy; no assumption of unrestricted commercial reuse.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| E-PROFILE | `https` | programme information and visualization entry point | yes | [открыть / open](https://e-profile.eu/) |

### Software and decoders

- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR decoding where BUFR is supplied.

### Recommended ingestion flow

1. Fetch the official HTTPS/FTP file tree directly; do not scrape rendered product viewers.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as ecCodes / pybufrkit, xarray / netCDF4.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://e-profile.eu/](https://e-profile.eu/)

### 🧪 Executable retrieval recipe

**Audit verdict:** `corrected` · **verified:** `2026-09-06`  
**Runtime access:** `restricted` · **adapter:** `unavailable`  
**Recipe:** `catalog/recipes/upper-air.json`

```bash
python -m weather_source probe eumetnet-eprofile
python -m weather_source example eumetnet-eprofile
```

Fallback: `fmi-open-data`.

### Agent note

Authoritative record: `catalog/sources/upper-air.yaml` → `id: eumetnet-eprofile`. Treat this Markdown as a generated view; never override the YAML record from prose.
