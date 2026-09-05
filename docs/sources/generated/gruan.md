# GRUAN — эталонная аэрология / GCOS Reference Upper-Air Network

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`gruan` · 🔵 **специализированный / specialized** · неоперативный / non-operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Эталонные верхнеаэрологические наблюдения с документированными поправками и неопределённостями.

**Поставщик:** GRUAN / WMO  
**Статус:** официальный источник; приоритет — **специализированный**.  
**Категории:** Аэрология и верхняя атмосфера, Климат и архивы, reference.  

### Что можно получить и когда использовать

Лучше всего подходит для эталонной верификации, гомогенизации и исследований с учётом неопределённостей.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global sparse network |
| Периодичность/режим обновления | site and campaign dependent |
| Типичная задержка | not designed for synoptic real-time use |
| Архив | long-term reference archive |
| Надёжность | `high` |
| Удобство автоматизации | `medium` |
| Протоколы | `https` |
| Форматы | `NetCDF` |

### Доступ и ограничения

- **Уровень доступа:** бесплатный после регистрации (`registration`).
- **Авторизация:** data access may require registration.
- **Лицензия/условия:** GRUAN data policy.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| GRUAN | `https` | documentation and data access | да | [открыть / open](https://www.gruan.org/) |

### ПО, библиотеки и декодеры

- [xarray](https://github.com/pydata/xarray) — NetCDF analysis.
- **Быстрый выбор декодера по формату:** xarray / netCDF4.

### Рекомендуемый алгоритм автоматического приёма

1. Забирать данные напрямую с официального HTTPS/FTP-файлового дерева, не парся HTML-визуализатор.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: xarray / netCDF4.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://www.gruan.org/](https://www.gruan.org/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/upper-air.yaml` → `id: gruan`.
- Для оперативного контура учитывать: `tier=specialized`, `operational=false`, `access.level=registration`, `automation=medium`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

Reference-quality upper-air observations with documented corrections and uncertainties.

**Provider:** GRUAN / WMO  
**Status:** official; tier **specialized**.  
**Categories:** upper-air, climate, reference.  

### What it provides and when to use it

Best suited to reference validation, homogenization and uncertainty-aware research.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global sparse network |
| Update cadence | site and campaign dependent |
| Typical latency | not designed for synoptic real-time use |
| Archive | long-term reference archive |
| Reliability | `high` |
| Automation | `medium` |
| Protocols | `https` |
| Formats | `NetCDF` |

### Access and restrictions

- **Access level:** `registration`.
- **Authentication:** data access may require registration.
- **Terms/licensing:** GRUAN data policy.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| GRUAN | `https` | documentation and data access | yes | [открыть / open](https://www.gruan.org/) |

### Software and decoders

- [xarray](https://github.com/pydata/xarray) — NetCDF analysis.

### Recommended ingestion flow

1. Fetch the official HTTPS/FTP file tree directly; do not scrape rendered product viewers.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as xarray / netCDF4.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://www.gruan.org/](https://www.gruan.org/)

### Agent note

Authoritative record: `catalog/sources/upper-air.yaml` → `id: gruan`. Treat this Markdown as a generated view; never override the YAML record from prose.
