# BOM — открытые потоки данных / BOM data feeds

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`bom-open-data` · 🟡 **резервный/региональный / secondary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Австралийские публичные потоки наблюдений предупреждений моделей и радиолокационных данных.

**Поставщик:** Australian Bureau of Meteorology  
**Статус:** официальный источник; приоритет — **резервный/региональный**.  
**Категории:** Наземные наблюдения, Метеорологические радары, Численные модели прогноза, Морские наблюдения.  

### Что можно получить и когда использовать

Переезды сервисов и машинный доступ к конкретным продуктам следует периодически перепроверять.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | Australia and surrounding oceans |
| Периодичность/режим обновления | minutes to hours |
| Типичная задержка | low |
| Архив | dataset dependent |
| Надёжность | `high` |
| Удобство автоматизации | `medium` |
| Протоколы | `https`, `ftp` |
| Форматы | `XML`, `JSON`, `text`, `GRIB2`, `image`, `provider-dependent` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** many public feeds anonymous; product rules vary.
- **Лицензия/условия:** Bureau of Meteorology terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| BOM data feeds | `https` | documentation | да | [открыть / open](https://www.bom.gov.au/catalogue/data-feeds.shtml) |

### ПО, библиотеки и декодеры

- [requests](https://requests.readthedocs.io/) — HTTP client.
- [ecCodes](https://github.com/ecmwf/eccodes) — GRIB decoding.
- **Быстрый выбор декодера по формату:** lxml / ElementTree, requests + stdlib json, ecCodes / wgrib2 / cfgrib.

### Рекомендуемый алгоритм автоматического приёма

1. Забирать данные напрямую с официального HTTPS/FTP-файлового дерева, не парся HTML-визуализатор.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: lxml / ElementTree, requests + stdlib json, ecCodes / wgrib2 / cfgrib.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://www.bom.gov.au/catalogue/data-feeds.shtml](https://www.bom.gov.au/catalogue/data-feeds.shtml)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/core.yaml` → `id: bom-open-data`.
- Для оперативного контура учитывать: `tier=secondary`, `operational=true`, `access.level=open`, `automation=medium`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.


### 🧪 Проверенный пример получения данных

**Аудит:** 🛠 исправлено/уточнено · **проверено:** `2026-09-06`  
**Реальный режим доступа:** публичный машинный доступ (`public`)  
**Runtime-адаптер:** `ftp`  
**Recipe:** `catalog/recipes/core.json`

Скачать XML-файл оперативных наблюдений NSW с официального anonymous FTP BOM.

```bash
python -m weather_source describe bom-open-data
python -m weather_source probe bom-open-data
python -m weather_source fetch bom-open-data
```

**Что исправлено или обнаружено аудитом:**

- BOM действительно предоставляет anonymous FTP, но доступ не означает свободную коммерческую лицензию.
- Anonymous products разрешены для личного использования/внутри организации и не должны автоматически маркироваться как unrestricted redistribution.

**Резервный источник:** `wmo-wis2`.

> Клиент сохраняет исходные данные; крупные GRIB/NetCDF/радарные объекты по умолчанию блокируются безопасным лимитом. Для осознанной полной загрузки используйте `--full`, когда это применимо.

---

## 🇬🇧 English

### What it is

Australian public observations warnings model and radar-related data feeds.

**Provider:** Australian Bureau of Meteorology  
**Status:** official; tier **secondary**.  
**Categories:** surface, radar, nwp, marine.  

### What it provides and when to use it

Service migration and product-specific machine access should be rechecked periodically.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | Australia and surrounding oceans |
| Update cadence | minutes to hours |
| Typical latency | low |
| Archive | dataset dependent |
| Reliability | `high` |
| Automation | `medium` |
| Protocols | `https`, `ftp` |
| Formats | `XML`, `JSON`, `text`, `GRIB2`, `image`, `provider-dependent` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** many public feeds anonymous; product rules vary.
- **Terms/licensing:** Bureau of Meteorology terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| BOM data feeds | `https` | documentation | yes | [открыть / open](https://www.bom.gov.au/catalogue/data-feeds.shtml) |

### Software and decoders

- [requests](https://requests.readthedocs.io/) — HTTP client.
- [ecCodes](https://github.com/ecmwf/eccodes) — GRIB decoding.

### Recommended ingestion flow

1. Fetch the official HTTPS/FTP file tree directly; do not scrape rendered product viewers.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as lxml / ElementTree, requests + stdlib json, ecCodes / wgrib2 / cfgrib.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://www.bom.gov.au/catalogue/data-feeds.shtml](https://www.bom.gov.au/catalogue/data-feeds.shtml)

### 🧪 Executable retrieval recipe

**Audit verdict:** `corrected` · **verified:** `2026-09-06`  
**Runtime access:** `public` · **adapter:** `ftp`  
**Recipe:** `catalog/recipes/core.json`

```bash
python -m weather_source probe bom-open-data
python -m weather_source fetch bom-open-data
```

Fallback: `wmo-wis2`.

### Agent note

Authoritative record: `catalog/sources/core.yaml` → `id: bom-open-data`. Treat this Markdown as a generated view; never override the YAML record from prose.
