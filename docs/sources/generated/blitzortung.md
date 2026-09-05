# Blitzortung — общественная сеть регистрации молний / Blitzortung community lightning network

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`blitzortung` · ⚪ **агрегатор / aggregator** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Общественная сеть регистрации молний с полезной визуализацией и доступом к данным на условиях проекта.

**Поставщик:** Blitzortung.org  
**Статус:** неофициальный/агрегированный источник; приоритет — **агрегатор**.  
**Категории:** Грозопеленгация и молнии.  

### Что можно получить и когда использовать

Включён для полноты; нельзя считать что существует неограниченный публичный API. При подходящем покрытии предпочитать официальные GLM или MTG-LI.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | broad international coverage depending on receiver density |
| Периодичность/режим обновления | seconds to minutes |
| Типичная задержка | near-real-time visualization |
| Архив | access depends on participant/status and service terms |
| Надёжность | `medium` |
| Удобство автоматизации | `low` |
| Протоколы | `https` |
| Форматы | `web visualization`, `provider-dependent` |

### Доступ и ограничения

- **Уровень доступа:** ограниченный доступ (`restricted`).
- **Авторизация:** detailed/raw access and redistribution rights are restricted; participant access differs.
- **Лицензия/условия:** Blitzortung terms prohibit treating the service as unrestricted public commercial data.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| Blitzortung | `https` | project and visualization | да | [открыть / open](https://www.blitzortung.org/) |

### ПО, библиотеки и декодеры

- Специализированный клиент в каталоге пока не зафиксирован; использовать стандартный клиент протокола и декодер формата.

### Рекомендуемый алгоритм автоматического приёма

1. Забирать данные напрямую с официального HTTPS/FTP-файлового дерева, не парся HTML-визуализатор.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат специализированным клиентом из раздела ПО; нормализацию выполнять поверх raw-данных.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://www.blitzortung.org/](https://www.blitzortung.org/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/aggregators.yaml` → `id: blitzortung`.
- Для оперативного контура учитывать: `tier=aggregator`, `operational=true`, `access.level=restricted`, `automation=low`, `reliability=medium`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

Community-operated lightning detection network with useful visualization and community data access under restrictive terms.

**Provider:** Blitzortung.org  
**Status:** non-official/aggregated; tier **aggregator**.  
**Categories:** lightning.  

### What it provides and when to use it

Documented for awareness only; do not assume an unrestricted public API. Prefer official GLM or MTG-LI where their coverage fits.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | broad international coverage depending on receiver density |
| Update cadence | seconds to minutes |
| Typical latency | near-real-time visualization |
| Archive | access depends on participant/status and service terms |
| Reliability | `medium` |
| Automation | `low` |
| Protocols | `https` |
| Formats | `web visualization`, `provider-dependent` |

### Access and restrictions

- **Access level:** `restricted`.
- **Authentication:** detailed/raw access and redistribution rights are restricted; participant access differs.
- **Terms/licensing:** Blitzortung terms prohibit treating the service as unrestricted public commercial data.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| Blitzortung | `https` | project and visualization | yes | [открыть / open](https://www.blitzortung.org/) |

### Software and decoders

- No dedicated client is recorded; use a standard protocol client plus a native-format decoder.

### Recommended ingestion flow

1. Fetch the official HTTPS/FTP file tree directly; do not scrape rendered product viewers.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Use a provider-specific client from the software section and keep normalization additive to the raw archive.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://www.blitzortung.org/](https://www.blitzortung.org/)

### Agent note

Authoritative record: `catalog/sources/aggregators.yaml` → `id: blitzortung`. Treat this Markdown as a generated view; never override the YAML record from prose.
