# NOAA NEXRAD Level II и Level III / NEXRAD Level II and Level III

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`noaa-nexrad` · 🟢 **основной / primary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Радиолокационные объёмы и производные продукты американской сети NEXRAD.

**Поставщик:** NOAA/NCEI/NWS  
**Статус:** официальный источник; приоритет — **основной**.  
**Категории:** Метеорологические радары, Осадки, severe-weather.  

### Что можно получить и когда использовать

Для массового оперативного приёма использовать object storage а NCEI — для архива.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | United States and territories |
| Периодичность/режим обновления | volume-scan cadence, typically several minutes |
| Типичная задержка | minutes |
| Архив | long-term NCEI archive; operational cloud/object feeds available |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `s3`, `https` |
| Форматы | `NEXRAD Level II`, `NEXRAD Level III` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** none for public object storage and NCEI access.
- **Лицензия/условия:** NOAA public data terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| NOAA NEXRAD information | `https` | documentation and archive entry | да | [открыть / open](https://www.ncei.noaa.gov/products/radar/next-generation-weather-radar) |
| NOAA Open Data Dissemination | `https` | operational cloud access documentation | да | [открыть / open](https://www.noaa.gov/information-technology/open-data-dissemination) |

### ПО, библиотеки и декодеры

- [Py-ART](https://github.com/ARM-DOE/pyart) — radar reading processing and visualization.
- [MetPy](https://github.com/Unidata/MetPy) — meteorological radar utilities.
- [nexradaws](https://github.com/aarande/nexradaws) — Python access to public NEXRAD object storage.

### Рекомендуемый алгоритм автоматического приёма

1. Использовать S3/object-storage API: листинг по префиксу продукта и времени, затем скачивание только новых объектов.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат специализированным клиентом из раздела ПО; нормализацию выполнять поверх raw-данных.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://www.ncei.noaa.gov/products/radar/next-generation-weather-radar](https://www.ncei.noaa.gov/products/radar/next-generation-weather-radar)
- [https://www.noaa.gov/information-technology/open-data-dissemination](https://www.noaa.gov/information-technology/open-data-dissemination)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/radar.yaml` → `id: noaa-nexrad`.
- Для оперативного контура учитывать: `tier=primary`, `operational=true`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.


### 🧪 Проверенный пример получения данных

**Аудит:** 🛠 исправлено/уточнено · **проверено:** `2026-09-06`  
**Реальный режим доступа:** публичный машинный доступ (`public`)  
**Runtime-адаптер:** `s3_latest`  
**Recipe:** `catalog/recipes/radar.json`

Найти последний Level II volume станции KTLX за текущую UTC-дату в актуальном публичном S3 bucket. Полный volume обычно требует --full.

```bash
python -m weather_source describe noaa-nexrad
python -m weather_source probe noaa-nexrad
python -m weather_source fetch noaa-nexrad
```

**Что исправлено или обнаружено аудитом:**

- В каталоге не указан рабочий S3 bucket.
- Старый bucket noaa-nexrad-level2 прекращён 2025-09-01; актуальный Level II bucket — unidata-nexrad-level2.

**Резервный источник:** `iowa-mesonet`.

> Клиент сохраняет исходные данные; крупные GRIB/NetCDF/радарные объекты по умолчанию блокируются безопасным лимитом. Для осознанной полной загрузки используйте `--full`, когда это применимо.

---

## 🇬🇧 English

### What it is

United States weather-radar volumes and derived products from the NEXRAD network.

**Provider:** NOAA/NCEI/NWS  
**Status:** official; tier **primary**.  
**Categories:** radar, precipitation, severe-weather.  

### What it provides and when to use it

Use object storage for bulk operational reception and NCEI for archive retrieval.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | United States and territories |
| Update cadence | volume-scan cadence, typically several minutes |
| Typical latency | minutes |
| Archive | long-term NCEI archive; operational cloud/object feeds available |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `s3`, `https` |
| Formats | `NEXRAD Level II`, `NEXRAD Level III` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** none for public object storage and NCEI access.
- **Terms/licensing:** NOAA public data terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| NOAA NEXRAD information | `https` | documentation and archive entry | yes | [открыть / open](https://www.ncei.noaa.gov/products/radar/next-generation-weather-radar) |
| NOAA Open Data Dissemination | `https` | operational cloud access documentation | yes | [открыть / open](https://www.noaa.gov/information-technology/open-data-dissemination) |

### Software and decoders

- [Py-ART](https://github.com/ARM-DOE/pyart) — radar reading processing and visualization.
- [MetPy](https://github.com/Unidata/MetPy) — meteorological radar utilities.
- [nexradaws](https://github.com/aarande/nexradaws) — Python access to public NEXRAD object storage.

### Recommended ingestion flow

1. Use the S3/object-storage API, list objects by product/time prefix and download only unseen objects.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Use a provider-specific client from the software section and keep normalization additive to the raw archive.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://www.ncei.noaa.gov/products/radar/next-generation-weather-radar](https://www.ncei.noaa.gov/products/radar/next-generation-weather-radar)
- [https://www.noaa.gov/information-technology/open-data-dissemination](https://www.noaa.gov/information-technology/open-data-dissemination)

### 🧪 Executable retrieval recipe

**Audit verdict:** `corrected` · **verified:** `2026-09-06`  
**Runtime access:** `public` · **adapter:** `s3_latest`  
**Recipe:** `catalog/recipes/radar.json`

```bash
python -m weather_source probe noaa-nexrad
python -m weather_source fetch noaa-nexrad
```

Fallback: `iowa-mesonet`.

### Agent note

Authoritative record: `catalog/sources/radar.yaml` → `id: noaa-nexrad`. Treat this Markdown as a generated view; never override the YAML record from prose.
