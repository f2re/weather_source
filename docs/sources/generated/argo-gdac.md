# Argo GDAC — профили океана / Argo Global Data Assembly Centres

> **Русская версия ниже является самостоятельной технической карточкой.** English reference follows after it.

`argo-gdac` · 🟢 **основной / primary** · оперативный / operational · проверено / verified **2026-09-05**

---

## 🇷🇺 Русский

### Что это

Оперативные и delayed-mode профили автономных буёв Argo: температура солёность давление и биогеохимические параметры.

**Поставщик:** Argo Program / Coriolis / USGODAE  
**Статус:** официальный источник; приоритет — **основной**.  
**Категории:** Океанографические данные, upper-ocean, profiling.  

### Что можно получить и когда использовать

Сильный бесплатный источник in-situ профилей океана; обязательно учитывать QC-флаги и различать real-time и delayed-mode данные.

Эта карточка подходит для выбора источника по покрытию, оперативности, способу автоматизации и нативным форматам. Для критического приёма предпочтительны официальные машинные endpoints и сохранение исходного сообщения/файла.

### Операционные характеристики

| Параметр | Значение |
|---|---|
| Географическое покрытие | global ocean |
| Периодичность/режим обновления | continuously as floats report; individual floats typically cycle over days |
| Типичная задержка | near-real-time products typically within hours to about a day after transmission |
| Архив | complete mission archive through GDACs |
| Надёжность | `high` |
| Удобство автоматизации | `high` |
| Протоколы | `https`, `ftp` |
| Форматы | `NetCDF` |

### Доступ и ограничения

- **Уровень доступа:** открытый без регистрации (`open`).
- **Авторизация:** none for GDAC public files.
- **Лицензия/условия:** Argo data policy and citation requirements.

### Точки доступа

| Endpoint | Протокол | Назначение | Health-check | URL |
|---|---|---|---:|---|
| Argo data access | `https` | access documentation | да | [открыть / open](https://argo.ucsd.edu/data/data-from-gdacs/) |
| Coriolis GDAC | `https` | file tree | да | [открыть / open](https://data-argo.ifremer.fr/) |

### ПО, библиотеки и декодеры

- [argopy](https://github.com/euroargodev/argopy) — Python Argo data client.
- [xarray](https://github.com/pydata/xarray) — NetCDF processing.
- **Быстрый выбор декодера по формату:** xarray / netCDF4.

### Рекомендуемый алгоритм автоматического приёма

1. Забирать данные напрямую с официального HTTPS/FTP-файлового дерева, не парся HTML-визуализатор.
2. Сохранять исходный файл вместе с временем получения, URL/идентификатором продукта и контрольной суммой.
3. Декодировать нативный формат стандартными средствами: xarray / netCDF4.
4. Контролировать не только доступность endpoint, но и свежесть данных; для критического контура держать независимый fallback.

### Официальная документация

- [https://argo.ucsd.edu/data/data-from-gdacs/](https://argo.ucsd.edu/data/data-from-gdacs/)
- [https://argo.ucsd.edu/data/argo-data-user-manual/](https://argo.ucsd.edu/data/argo-data-user-manual/)

### Для ИИ-агента

- Источник истины для этой карточки: `catalog/sources/ocean.yaml` → `id: argo-gdac`.
- Для оперативного контура учитывать: `tier=primary`, `operational=true`, `access.level=open`, `automation=high`, `reliability=high`.
- Не выводить доступность только из названия поставщика: проверять endpoint, права, формат, задержку и свежесть.


### 🧪 Проверенный пример получения данных

**Аудит:** 🛠 исправлено/уточнено · **проверено:** `2026-09-06`  
**Реальный режим доступа:** публичный машинный доступ (`public`)  
**Runtime-адаптер:** `external`  
**Recipe:** `catalog/recipes/ocean.json`

Получить реальные Argo-профили небольшого района через argopy и сохранить NetCDF; QC-флаги остаются в наборе.

```bash
python -m weather_source describe argo-gdac
python -m weather_source probe argo-gdac
python -m weather_source fetch argo-gdac --allow-external
```

**Что исправлено или обнаружено аудитом:**

- В каталоге был только корень GDAC; не было воспроизводимого запроса реальных профилей и проверки QC.

**Резервный источник:** `copernicus-marine`.

<details><summary>Команда официального/специализированного клиента</summary>

```bash
python -c "from argopy import DataFetcher; ds=DataFetcher(src='erddap').region([-75,-65,20,30,0,1000,'2025-01-01','2025-02-01']).to_xarray(); ds.to_netcdf('argo-sample.nc'); print(ds)"
```

</details>

> Клиент сохраняет исходные данные; крупные GRIB/NetCDF/радарные объекты по умолчанию блокируются безопасным лимитом. Для осознанной полной загрузки используйте `--full`, когда это применимо.

---

## 🇬🇧 English

### What it is

Near-real-time and delayed-mode profiling-float observations of temperature salinity pressure and biogeochemical variables.

**Provider:** Argo Program / Coriolis / USGODAE  
**Status:** official; tier **primary**.  
**Categories:** ocean, upper-ocean, profiling.  

### What it provides and when to use it

Strong free source of in-situ subsurface ocean profiles; use quality flags and distinguish real-time from delayed-mode QC.

Use this record to select the feed by geographic coverage, latency, machine access, native formats and operational suitability.

### Operational characteristics

| Field | Value |
|---|---|
| Coverage | global ocean |
| Update cadence | continuously as floats report; individual floats typically cycle over days |
| Typical latency | near-real-time products typically within hours to about a day after transmission |
| Archive | complete mission archive through GDACs |
| Reliability | `high` |
| Automation | `high` |
| Protocols | `https`, `ftp` |
| Formats | `NetCDF` |

### Access and restrictions

- **Access level:** `open`.
- **Authentication:** none for GDAC public files.
- **Terms/licensing:** Argo data policy and citation requirements.

### Endpoints

| Endpoint | Protocol | Role | Health check | URL |
|---|---|---|---:|---|
| Argo data access | `https` | access documentation | yes | [открыть / open](https://argo.ucsd.edu/data/data-from-gdacs/) |
| Coriolis GDAC | `https` | file tree | yes | [открыть / open](https://data-argo.ifremer.fr/) |

### Software and decoders

- [argopy](https://github.com/euroargodev/argopy) — Python Argo data client.
- [xarray](https://github.com/pydata/xarray) — NetCDF processing.

### Recommended ingestion flow

1. Fetch the official HTTPS/FTP file tree directly; do not scrape rendered product viewers.
2. Preserve the raw payload together with receive time, source URL/product identifier and checksum.
3. Decode native payloads with standards-aware tools such as xarray / netCDF4.
4. Monitor data freshness, not just endpoint reachability, and configure an independent fallback for critical ingestion.

### Official/reference documentation

- [https://argo.ucsd.edu/data/data-from-gdacs/](https://argo.ucsd.edu/data/data-from-gdacs/)
- [https://argo.ucsd.edu/data/argo-data-user-manual/](https://argo.ucsd.edu/data/argo-data-user-manual/)

### 🧪 Executable retrieval recipe

**Audit verdict:** `corrected` · **verified:** `2026-09-06`  
**Runtime access:** `public` · **adapter:** `external`  
**Recipe:** `catalog/recipes/ocean.json`

```bash
python -m weather_source probe argo-gdac
python -m weather_source fetch argo-gdac --allow-external
```

Fallback: `copernicus-marine`.

### Agent note

Authoritative record: `catalog/sources/ocean.yaml` → `id: argo-gdac`. Treat this Markdown as a generated view; never override the YAML record from prose.
