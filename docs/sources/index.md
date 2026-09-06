# 🌦️ Source catalogue / Каталог источников

**47 источников / sources** · catalogue v1 · reviewed 2026-09-05

- 🇷🇺 **[Полный русский каталог](index.ru.md)** — описание каждого источника на русском, доступ, протоколы, форматы и практический приём.
- 🇬🇧 **[Full English catalogue](index.en.md)** — complete English index and the same technical records.
- 🤖 **[`catalog/sources.json`](https://github.com/f2re/weather_source/blob/main/catalog/sources.json)** — complete flattened machine-readable catalogue.
- 🤖 **[`catalog/sources.ndjson`](https://github.com/f2re/weather_source/blob/main/catalog/sources.ndjson)** — one source per line for RAG/streaming ingestion.
- 🧭 **[`catalog/agent-index.json`](https://github.com/f2re/weather_source/blob/main/catalog/agent-index.json)** — compact selection index for agents.
- 🧠 **[`llms.txt`](https://github.com/f2re/weather_source/blob/main/llms.txt)** — repository entry point for LLM/agent tooling.

## Приоритеты / Tiers

| Tier | Количество | Назначение |
|---|---:|---|
| 🟢 primary | 21 | Основной официальный канал для автоматического/оперативного приёма |
| 🟡 secondary | 9 | Резерв, региональная альтернатива или архив |
| 🔵 specialized | 11 | Специализированные измерения/продукты |
| ⚪ aggregator | 6 | Удобный агрегатор, но не единственный источник критической системы |

## Категории / Categories

- [Наземные наблюдения / `surface`](categories/surface.md) — **22**
- [Аэрология и верхняя атмосфера / `upper-air`](categories/upper-air.md) — **22**
- [Численные модели прогноза / `nwp`](categories/nwp.md) — **19**
- [Метеорологические радары / `radar`](categories/radar.md) — **15**
- [Спутниковые данные / `satellite`](categories/satellite.md) — **11**
- [Климат и архивы / `climate`](categories/climate.md) — **10**
- [archive / `archive`](categories/archive.md) — **8**
- [Осадки / `precipitation`](categories/precipitation.md) — **5**
- [Морские наблюдения / `marine`](categories/marine.md) — **4**
- [Океанографические данные / `ocean`](categories/ocean.md) — **4**
- [Авиационные наблюдения / `aircraft`](categories/aircraft.md) — **3**
- [clouds / `clouds`](categories/clouds.md) — **3**
- [Грозопеленгация и молнии / `lightning`](categories/lightning.md) — **3**
- [analysis / `analysis`](categories/analysis.md) — **2**
- [aviation / `aviation`](categories/aviation.md) — **2**
- [Ансамблевые прогнозы / `ensemble`](categories/ensemble.md) — **2**
- [profiler / `profiler`](categories/profiler.md) — **2**
- [Реанализ / `reanalysis`](categories/reanalysis.md) — **2**
- [reference / `reference`](categories/reference.md) — **2**
- [severe-weather / `severe-weather`](categories/severe-weather.md) — **2**
- [waves / `waves`](categories/waves.md) — **2**
- [aerosol / `aerosol`](categories/aerosol.md) — **1**
- [air-quality / `air-quality`](categories/air-quality.md) — **1**
- [fire / `fire`](categories/fire.md) — **1**
- [hydrology / `hydrology`](categories/hydrology.md) — **1**
- [Метаданные / `metadata`](categories/metadata.md) — **1**
- [ozone / `ozone`](categories/ozone.md) — **1**
- [profiling / `profiling`](categories/profiling.md) — **1**
- [radiation / `radiation`](categories/radiation.md) — **1**
- [research / `research`](categories/research.md) — **1**
- [upper-ocean / `upper-ocean`](categories/upper-ocean.md) — **1**

## Как читать карточки

Карточка каждого источника содержит отдельную самостоятельную русскую часть и отдельную английскую часть. Для реализации приёмника сначала выбирайте `primary` + `operational`, затем проверяйте доступ, протокол, формат, задержку и fallback.

## Аудит и рабочий код / Audit and executable clients

- [Аудит всех источников](https://github.com/f2re/weather_source/blob/main/docs/audit/source-audit-2026-09-06.md)
- [Runtime recipes](https://github.com/f2re/weather_source/blob/main/catalog/recipes.json)
- [Python client package](https://github.com/f2re/weather_source/blob/main/weather_source/)
