# NOAA NUCAPS / HEAP — спутниковые профили атмосферы / NUCAPS / HEAP atmospheric sounding products

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`noaa-nucaps` · 🔵 **специализированный / specialized** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Оперативные спутниковые retrieval-продукты CrIS и ATMS с вертикальными профилями температуры и влажности, облачными параметрами и малыми газовыми составляющими.

**Поставщик:** NOAA/NESDIS/STAR and OSPO  
**Статус:** официальный источник; приоритет — **специализированный**.  
**Категории:** Спутниковые данные, Аэрология и верхняя атмосфера.  

### Что можно получить и когда использовать

Стандартные NetCDF-продукты NUCAPS содержат retrieval-профили на 100 вертикальных точках примерно от 1100 до 0.016 гПа. Это спутниковые retrieval-профили, а не радиозонды.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global polar-orbiting coverage |
| Периодичность/режим обновления | orbital overpasses; production cadence follows JPSS observations and processing |
| Типичная задержка | operational product stream; public archive latency and access path depend on OSPO/NDE/CLASS distribution |
| Архив | long-term Environmental Data Record archive through NOAA CLASS |
| Надёжность | `high` |
| Удобство автоматизации | `medium` |
| Протоколы | `https` |
| Форматы | `NetCDF`, `BUFR` |

### Доступ и ограничения

- **Уровень доступа:** бесплатный после регистрации (`registration`).
- **Авторизация:** archived and operational distribution paths differ; NOAA CLASS/NDE access requirements apply.
- **Лицензия/условия:** NOAA/NESDIS product and CLASS terms.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| NUCAPS product page | `https` | product description and data-access links | да | [открыть / open](https://www.star.nesdis.noaa.gov/jpss/soundings.php) |
| OSPO HEAP NUCAPS | `https` | operational product documentation | да | [открыть / open](https://www.ospo.noaa.gov/products/atmosphere/soundings/heap/nucaps/index.html) |

### ПО, библиотеки и декодеры

- [xarray](https://github.com/pydata/xarray) — NetCDF profile processing.
- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR radiance/profile decoding where applicable.
- **Быстрый выбор декодера по формату:** xarray / netCDF4, ecCodes / pybufrkit.

### Рекомендуемый алгоритм автоматического приёма

1. Забирать данные напрямую с официального HTTPS/FTP-файлового дерева, не парся HTML-визуализатор.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: xarray / netCDF4, ecCodes / pybufrkit.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://www.star.nesdis.noaa.gov/jpss/soundings.php](https://www.star.nesdis.noaa.gov/jpss/soundings.php)
- [https://www.ospo.noaa.gov/products/atmosphere/soundings/heap/nucaps/index.html](https://www.ospo.noaa.gov/products/atmosphere/soundings/heap/nucaps/index.html)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/specialized.yaml` → `id: noaa-nucaps`.
- Для оперативного контура учитывать: `tier=specialized`, `operational=true`, `access.level=registration`, `automation=medium`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.

---

## 🇬🇧 English

### What it is

Operational satellite retrievals from CrIS and ATMS providing vertical temperature and moisture profiles, cloud properties and trace-gas products.

**Provider:** NOAA/NESDIS/STAR and OSPO  
**Status:** official; tier **specialized**.  
**Categories:** satellite, upper-air.  

### What it provides and when to use it

NUCAPS standard NetCDF products contain retrieved profiles on 100 vertical points from roughly 1100 hPa to 0.016 hPa. Treat them as satellite retrievals, not radiosonde observations.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global polar-orbiting coverage |
| Update cadence | orbital overpasses; production cadence follows JPSS observations and processing |
| Typical latency | operational product stream; public archive latency and access path depend on OSPO/NDE/CLASS distribution |
| Archive | long-term Environmental Data Record archive through NOAA CLASS |
| Reliability | `high` |
| Automation | `medium` |
| Protocols | `https` |
| Formats | `NetCDF`, `BUFR` |

### Access and restrictions

- **Access level:** `registration`.
- **Authentication:** archived and operational distribution paths differ; NOAA CLASS/NDE access requirements apply.
- **Terms/licensing:** NOAA/NESDIS product and CLASS terms.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| NUCAPS product page | `https` | product description and data-access links | yes | [открыть / open](https://www.star.nesdis.noaa.gov/jpss/soundings.php) |
| OSPO HEAP NUCAPS | `https` | operational product documentation | yes | [открыть / open](https://www.ospo.noaa.gov/products/atmosphere/soundings/heap/nucaps/index.html) |

### Software and decoders

- [xarray](https://github.com/pydata/xarray) — NetCDF profile processing.
- [ecCodes](https://github.com/ecmwf/eccodes) — BUFR radiance/profile decoding where applicable.

### Recommended ingestion flow

1. Fetch the official HTTPS/FTP file tree directly; do not scrape rendered product viewers.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as xarray / netCDF4, ecCodes / pybufrkit.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://www.star.nesdis.noaa.gov/jpss/soundings.php](https://www.star.nesdis.noaa.gov/jpss/soundings.php)
- [https://www.ospo.noaa.gov/products/atmosphere/soundings/heap/nucaps/index.html](https://www.ospo.noaa.gov/products/atmosphere/soundings/heap/nucaps/index.html)

### Agent note

Authoritative record: `catalog/sources/specialized.yaml` → `id: noaa-nucaps`. Treat this Markdown as a generated view; never override the YAML record from prose.
