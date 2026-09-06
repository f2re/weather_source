# OGIMET — метеорологическая информация / OGIMET professional meteorological information

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`ogimet` · ⚪ **агрегатор / aggregator** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Давно работающий удобный сервис SYNOP METAR и других наблюдений получаемых из международного обмена.

**Поставщик:** OGIMET  
**Статус:** неофициальный/агрегированный источник; приоритет — **агрегатор**.  
**Категории:** Наземные наблюдения, aviation, archive.  

### Что можно получить и когда использовать

Оставлять как резерв для человека; не строить критический приём на HTML-парсинге если доступны WIS2 или официальные API.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global |
| Периодичность/режим обновления | observation dependent |
| Типичная задержка | generally near-real-time but without an official operational SLA |
| Архив | historical query capability |
| Надёжность | `medium` |
| Удобство автоматизации | `low` |
| Протоколы | `https` |
| Форматы | `HTML`, `text` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** generally no account for interactive queries; automated usage must respect service limits.
- **Лицензия/условия:** OGIMET usage policy and upstream data rights.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| OGIMET | `https` | portal and query service | да | [открыть / open](https://www.ogimet.com/) |

### ПО, библиотеки и декодеры

- Специализированный клиент в каталоге пока не зафиксирован; использовать стандартный клиент протокола и декодер формата.

### Рекомендуемый алгоритм автоматического приёма

1. Забирать данные напрямую с официального HTTPS/FTP-файлового дерева, не парся HTML-визуализатор.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат специализированным клиентом из раздела ПО; нормализацию выполнять поверх raw-данных.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://www.ogimet.com/](https://www.ogimet.com/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/aggregators.yaml` → `id: ogimet`.
- Для оперативного контура учитывать: `tier=aggregator`, `operational=true`, `access.level=open`, `automation=low`, `reliability=medium`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.


### 🧪 Проверенный пример получения данных

**Аудит:** 🛠 исправлено/уточнено · **проверено:** `2026-09-06`  
**Реальный режим доступа:** публичный машинный доступ (`public`)  
**Runtime-адаптер:** `http`  
**Recipe:** `catalog/recipes/aggregators.json`

Через документированный `getsynop` CGI получить CSV SYNOP из WMO block 26 за фиксированный 6-часовой интервал 2026-08-24.

```bash
python -m weather_source describe ogimet
python -m weather_source probe ogimet
python -m weather_source fetch ogimet
```

**Что исправлено или обнаружено аудитом:**

- Карточка недооценивала автоматизацию: OGIMET документирует `getsynop` CGI, возвращающий CSV без HTML.
- Сам OGIMET прямо пишет, что его данные не должны использоваться в critical mission; источник остаётся только fallback/диагностикой.

**Резервный источник:** `wmo-wis2`.

> Клиент сохраняет исходные данные; крупные GRIB/NetCDF/радарные объекты по умолчанию блокируются безопасным лимитом. Для осознанной полной загрузки используйте `--full`, когда это применимо.

---

## 🇬🇧 English

### What it is

Long-running convenience service exposing SYNOP METAR and other observation products derived from international exchange.

**Provider:** OGIMET  
**Status:** non-official/aggregated; tier **aggregator**.  
**Categories:** surface, aviation, archive.  

### What it provides and when to use it

Keep as human-facing fallback; do not build a critical ingest pipeline on HTML scraping when WIS2 or official APIs exist.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global |
| Update cadence | observation dependent |
| Typical latency | generally near-real-time but without an official operational SLA |
| Archive | historical query capability |
| Reliability | `medium` |
| Automation | `low` |
| Protocols | `https` |
| Formats | `HTML`, `text` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** generally no account for interactive queries; automated usage must respect service limits.
- **Terms/licensing:** OGIMET usage policy and upstream data rights.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| OGIMET | `https` | portal and query service | yes | [открыть / open](https://www.ogimet.com/) |

### Software and decoders

- No dedicated client is recorded; use a standard protocol client plus a native-format decoder.

### Recommended ingestion flow

1. Fetch the official HTTPS/FTP file tree directly; do not scrape rendered product viewers.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Use a provider-specific client from the software section and keep normalization additive to the raw archive.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://www.ogimet.com/](https://www.ogimet.com/)

### 🧪 Executable retrieval recipe

**Audit verdict:** `corrected` · **verified:** `2026-09-06`  
**Runtime access:** `public` · **adapter:** `http`  
**Recipe:** `catalog/recipes/aggregators.json`

```bash
python -m weather_source probe ogimet
python -m weather_source fetch ogimet
```

Fallback: `wmo-wis2`.

### Agent note

Authoritative record: `catalog/sources/aggregators.yaml` → `id: ogimet`. Treat this Markdown as a generated view; never override the YAML record from prose.
