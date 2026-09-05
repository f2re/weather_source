# 🌦️ Weather Source

[![CI](https://github.com/f2re/weather_source/actions/workflows/ci.yml/badge.svg)](https://github.com/f2re/weather_source/actions/workflows/ci.yml)
[![Проверка источников](https://github.com/f2re/weather_source/actions/workflows/source-health.yml/badge.svg)](https://github.com/f2re/weather_source/actions/workflows/source-health.yml)
[![Документация](https://github.com/f2re/weather_source/actions/workflows/docs.yml/badge.svg)](https://github.com/f2re/weather_source/actions/workflows/docs.yml)
[![Лицензия: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![EN](https://img.shields.io/badge/lang-English-blue)](README.md)

> Машиночитаемая двуязычная база знаний **оперативных источников метеорологической информации**: наземные наблюдения, аэрология, радары, спутники, грозопеленгация, океан, модели/ансамбли, анализы и архивы.

Цель проекта — отвечать не только на вопрос «где взять данные», но и на инженерные вопросы: **как подписаться, скачать, декодировать, проверить, хранить и резервировать поток**.

## Что находится в репозитории

- 🗂️ [`catalog/sources.yaml`](catalog/sources.yaml) — единый машиночитаемый каталог и источник истины.
- 📚 [`docs/sources/`](docs/sources/) — карточки источников/провайдеров с описанием на русском и английском.
- 🔌 Протоколы: HTTPS/REST, WFS/WMS/WCS, THREDDS/OPeNDAP, S3/object storage, MQTT/WIS2, AMQP, FTP и другие.
- 📦 Форматы: BUFR, GRIB/GRIB2, NetCDF, HDF5, GeoTIFF, ODIM HDF5, JSON, XML/GML, CSV и текстовые бюллетени.
- 🛠️ Готовые средства: ecCodes, wgrib2, cfgrib/xarray, netCDF4, h5py, GDAL, pybufrkit, Siphon, EUMDAC, cdsapi, earthaccess и специализированные клиенты центров.
- 🧪 [`examples/`](examples/) — минимальные рабочие примеры приёма и декодирования.
- ✅ CI на каждый PR: схема каталога, семантические проверки, генерация документации, компиляция и тесты примеров.
- ❤️ Плановая проверка доступности выбранных официальных endpoint'ов с повторами и отчётом.

## Быстрый каталог

| Вид данных | Основные бесплатные/открытые источники | Форматы | Предпочтительный способ |
|---|---|---|---|
| 🌡️ Наземные наблюдения | WIS2, NOAA/NWS, ECCC, DWD, FMI, MeteoSwiss, JMA, BOM | BUFR, METAR/SYNOP, JSON, CSV | WIS2 MQTT+HTTPS, REST/HTTPS |
| 🎈 Аэрология | WIS2 TEMP, Росгидромет/Авиаметтелеком, IGRA, DWD, FMI, Météo-France, MeteoSwiss, ECCC, Wyoming | BUFR, CSV, text, NetCDF | WIS2, HTTPS, WFS |
| 📡 Радиолокация | NOAA NEXRAD/MRMS, DWD, ECCC, национальные сервисы | Level II/III, GRIB2, ODIM HDF5, GeoTIFF | S3/HTTPS, WMS/WCS |
| 🛰️ Спутники | EUMETSAT, NOAA/NESDIS/NODD, NASA Earthdata/LANCE, JAXA | NetCDF, HDF5, HRIT/LRIT, BUFR, GeoTIFF | Data Store/API, S3, HTTPS |
| ⚡ Молнии | NOAA GOES GLM, EUMETSAT MTG LI; закрытые/общественные сети вынесены отдельно | NetCDF/HDF5/BUFR | S3/Data Store |
| 🌊 Океан/буи | Copernicus Marine, NOAA NDBC, Argo GDAC, ERDDAP | NetCDF, CSV, JSON | HTTPS, ERDDAP, object storage |
| 🧠 Модели/ансамбли | ECMWF Open Data, NOAA NOMADS/NODD, DWD, Météo-France, ECCC, JMA, Copernicus | GRIB2, NetCDF | HTTPS/S3/API |
| 🗃️ Архивы | NCEI, Copernicus CDS, ERA5, IGRA, ISD, национальные климатические архивы | NetCDF, GRIB, CSV, BUFR | API/HTTPS |

## Что записано для каждого источника

Каталог хранит: владельца/центр, официальность, категории данных, географическое покрытие, оперативность, периодичность, типичную задержку, глубину архива, уровень бесплатности, необходимость регистрации/API key, лицензию и ограничения, протоколы, реальные endpoint'ы, форматы, готовые библиотеки и программы, декодеры, документацию, устойчивость, удобство автоматизации и приоритет использования.

## Для оперативной системы

Рекомендуемая логика — **не привязывать каждый продукт к одному сайту**. Для глобальных наблюдений предпочтителен WIS2, для моделей — несколько независимых центров, для спутников/радаров — официальный объектный или файловый канал. Raw-файлы BUFR/GRIB/NetCDF желательно сохранять рядом с нормализованными данными.

### Аэрология России и мира

Основной транспорт — **WIS2 TEMP/BUFR**. Для России каталог отдельно фиксирует WIS2-потоки Росгидромета/Авиаметтелекома. В качестве независимого резерва/архива используются NOAA IGRA и University of Wyoming/Siphon. Подробности: [`docs/sources/aerology.md`](docs/sources/aerology.md).

## Структура

```text
catalog/                 # машиночитаемый каталог и схема
docs/                    # справочник форматов, протоколов и карточки источников
examples/python/         # небольшие рабочие примеры
scripts/                 # валидация, health-check, генерация документации
tests/                   # тесты каталога и примеров
.github/workflows/       # CI, проверки источников, документация
```

## Использование агентами

Сначала прочитать [`AGENTS.md`](AGENTS.md). Для автоматического выбора источника агент должен фильтровать `catalog/sources.yaml` по `categories`, `coverage`, `operational`, `access.level`, `formats` и `tier`, а не ориентироваться только на текст README.

## Локальная проверка

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_catalog.py
python scripts/generate_docs.py --check
python -m compileall examples scripts tests
pytest -q
```

Проверка реальных сетевых endpoint'ов:

```bash
python scripts/check_endpoints.py --catalog catalog/sources.yaml --tier primary --report source-health.json
```

Она вынесена из детерминированного PR-CI, поскольку внешние метеосервисы имеют регламентные работы и кратковременные сбои.

## Участие в проекте

Правила добавления источников — [`CONTRIBUTING.md`](CONTRIBUTING.md). Исправления endpoint'ов, форматов и условий доступа особенно полезны. В issue templates предусмотрены отдельные сценарии для нового источника и сломанного канала.

## Статус

Это развиваемый оперативный справочник. Приоритет — **первичные официальные, бесплатные/открытые или практически доступные машинные каналы**, которые можно автоматизировать. Агрегаторы и сервисы с ограничениями помечаются явно.

Дата крупной ревизии каталога: **05.09.2026**.

## Лицензия

Код и оригинальная документация репозитория — [MIT](LICENSE). Сами метеоданные остаются под лицензиями и условиями соответствующих поставщиков.