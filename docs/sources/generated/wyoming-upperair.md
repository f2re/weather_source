# University of Wyoming — аэрологические зондирования / Upper Air Soundings

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`wyoming-upperair` · ⚪ **агрегатор / aggregator** · оперативный / operational · проверено / verified **2026-09-06**

---

## 🇷🇺 Русский

### Что это

Удобный глобальный сервис радиозондовых профилей для просмотра и программного резервного получения.

**Поставщик:** University of Wyoming  
**Статус:** неофициальный/агрегированный источник; приоритет — **агрегатор**.  
**Категории:** Аэрология и верхняя атмосфера.  

### Что можно получить и когда использовать

Полезный резерв и удобный интерфейс; не использовать как единственный критический канал приёма.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global |
| Периодичность/режим обновления | standard sounding times; station dependent |
| Типичная задержка | near-real-time, provider dependent |
| Архив | large historical archive |
| Надёжность | `medium` |
| Удобство автоматизации | `medium` |
| Протоколы | `https` |
| Форматы | `text`, `HTML-derived tabular` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** none; avoid abusive scraping.
- **Лицензия/условия:** University service terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| Upper Air | `https` | query and view | да | [открыть / open](https://weather.uwyo.edu/upperair/sounding.html) |

### ПО, библиотеки и декодеры

- [Siphon WyomingUpperAir](https://unidata.github.io/siphon/latest/api/simplewebservice.html) — Python client.

### Рекомендуемый алгоритм автоматического приёма

1. Забирать данные напрямую с официального HTTPS/FTP-файлового дерева, не парся HTML-визуализатор.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат специализированным клиентом из раздела ПО; нормализацию выполнять поверх raw-данных.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://weather.uwyo.edu/upperair/sounding.html](https://weather.uwyo.edu/upperair/sounding.html)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/upper-air.yaml` → `id: wyoming-upperair`.
- Для оперативного контура учитывать: `tier=aggregator`, `operational=true`, `access.level=open`, `automation=medium`, `reliability=medium`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.


### 🧪 Проверенный пример получения данных

**Аудит:** 🛠 исправлено/уточнено · **проверено:** `2026-09-06`  
**Реальный режим доступа:** публичный машинный доступ (`public`)  
**Runtime-адаптер:** `external`  
**Recipe:** `catalog/recipes/upper-air.json`

Воспроизвести документированный Siphon example: GSO, 2024-09-27 00 UTC, сохранить радиозондовый профиль CSV.

```bash
python -m weather_source describe wyoming-upperair
python -m weather_source probe wyoming-upperair
python -m weather_source fetch wyoming-upperair --allow-external
```

**Что исправлено или обнаружено аудитом:**

- В каталоге указана веб-страница; Siphon использует отдельный CGI endpoint и является более устойчивым клиентским слоем.

**Резервный источник:** `noaa-ncei-igra`.

<details><summary>Команда официального/специализированного клиента</summary>

```bash
python -c "from datetime import datetime; from siphon.simplewebservice.wyoming import WyomingUpperAir; df=WyomingUpperAir.request_data(datetime(2024,9,27,0),'GSO'); df.to_csv('wyoming-GSO-2024092700.csv',index=False); print(df[['pressure','height','temperature','dewpoint']].head())"
```

</details>

> Клиент сохраняет исходные данные; крупные GRIB/NetCDF/радарные объекты по умолчанию блокируются безопасным лимитом. Для осознанной полной загрузки используйте `--full`, когда это применимо.

---

## 🇬🇧 English

### What it is

Convenient global radiosonde sounding service widely used for viewing and programmatic fallback.

**Provider:** University of Wyoming  
**Status:** non-official/aggregated; tier **aggregator**.  
**Categories:** upper-air.  

### What it provides and when to use it

Useful fallback and convenience service; do not make it the sole critical ingest path.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global |
| Update cadence | standard sounding times; station dependent |
| Typical latency | near-real-time, provider dependent |
| Archive | large historical archive |
| Reliability | `medium` |
| Automation | `medium` |
| Protocols | `https` |
| Formats | `text`, `HTML-derived tabular` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** none; avoid abusive scraping.
- **Terms/licensing:** University service terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| Upper Air | `https` | query and view | yes | [открыть / open](https://weather.uwyo.edu/upperair/sounding.html) |

### Software and decoders

- [Siphon WyomingUpperAir](https://unidata.github.io/siphon/latest/api/simplewebservice.html) — Python client.

### Recommended ingestion flow

1. Fetch the official HTTPS/FTP file tree directly; do not scrape rendered product viewers.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Use a provider-specific client from the software section and keep normalization additive to the raw archive.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://weather.uwyo.edu/upperair/sounding.html](https://weather.uwyo.edu/upperair/sounding.html)

### 🧪 Executable retrieval recipe

**Audit verdict:** `corrected` · **verified:** `2026-09-06`  
**Runtime access:** `public` · **adapter:** `external`  
**Recipe:** `catalog/recipes/upper-air.json`

```bash
python -m weather_source probe wyoming-upperair
python -m weather_source fetch wyoming-upperair --allow-external
```

Fallback: `noaa-ncei-igra`.

### Agent note

Authoritative record: `catalog/sources/upper-air.yaml` → `id: wyoming-upperair`. Treat this Markdown as a generated view; never override the YAML record from prose.
