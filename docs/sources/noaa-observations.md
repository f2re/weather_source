# NOAA observations: operational ingest, archives and assimilation-space

This guide explains how the NOAA/NCEP/NCEI observation sources in the catalogue fit together. The same provider family exposes several fundamentally different data products; they should not be treated as interchangeable.

## Русский

### Какой источник выбирать

| Задача | Рекомендуемый источник | Почему |
|---|---|---|
| Оперативные точечные наблюдения в США | `noaa-nws-observations-api` | простой официальный REST/JSON-LD API, низкий порог интеграции |
| Оперативный многосетевой ingest | `noaa-ncep-madis` | METAR, mesonet, maritime, RAOB, aircraft, profiler и другие сети + QC |
| Глобальные часовые/синоптические станции для архива, ML и верификации | `noaa-ncei-ghcnh` | новый основной NCEI-контур; заменяет legacy ISD/Global Hourly |
| Суточные климатические ряды | `noaa-ncei-ghcnd` | глобальный QC-архив суточных T/осадков/снега и др. |
| Эталонная проверка в США | `noaa-uscrn` | reference-quality сеть с 5-минутными, часовыми и суточными продуктами |
| Исследования observation-space и ассимиляции NCEP | `noaa-ncep-prepbufr` | BUFR dumps и QC PREPBUFR, близкие к реальному входу GDAS/GFS |

### GHCNh и старый ISD

Для новых конвейеров часовых наблюдений следует выбирать **GHCNh**. NCEI позиционирует GHCNh как следующее поколение глобального часового/синоптического набора, заменяющего Integrated Surface Dataset (ISD / Global Hourly). Legacy ISD имеет смысл сохранять только для совместимости со старыми пайплайнами и уже собранными архивами.

Практический паттерн:

```text
GHCNh raw PSV/Parquet
        ↓
сохранение исходного файла + checksum + URL + receive_time
        ↓
парсинг без удаления provider/QC атрибутов
        ↓
нормализованная station/time таблица
        ↓
ML features / model-vs-observation / climate diagnostics
```

Не следует на этапе ingest автоматически усреднять повторные сообщения, выбрасывать QC-поля или молча менять единицы измерения. Сначала сохраняется raw-представление, затем строится нормализованный слой.

### MADIS

MADIS — не просто ещё один METAR endpoint. Это интеграционный контур для большого числа сетей наблюдений. Он особенно полезен, когда требуется единый многосетевой оперативный поток и provider/QC metadata. При этом режимы доступа различаются: публичные sample/current файлы доступны отдельно, а устойчивый real-time/archive доступ через FTP, OPeNDAP, viewer или LDM может требовать регистрации/заявки.

Для production-ingest рекомендуется хранить минимум:

- исходный netCDF/текстовый payload;
- dataset/network name;
- observation time и receive time;
- station/platform identifier;
- provider/source identifier;
- QC flags и rejection/acceptance metadata;
- checksum и исходный URL/path.

### NWS API

`api.weather.gov` удобен как лёгкий оперативный адаптер для станций NWS. Он хорошо подходит для point queries, мониторинга и fallback-логики. Его не следует использовать как замену глобальному bulk archive: для истории лучше GHCNh/GHCNd, для более широкого оперативного ingest — WIS2 или MADIS.

### PREPBUFR и raw NCEP dumps

PREPBUFR — специализированный источник. Он полезен для:

- исследований data assimilation;
- анализа observation-space;
- оценки влияния наблюдений;
- воспроизведения части NCEP ingest/QC;
- подготовки ML-моделей, которые должны работать в пространстве наблюдений, близком к GDAS/GFS.

Но PREPBUFR нельзя трактовать как обычный открытый станционный архив. Отдельные constituent observations могут иметь ограничения на распространение или коммерческое использование. Перед автоматической загрузкой и особенно перераспространением необходимо проверить NCEP Restricted Data guidance. Пример адаптера в репозитории поэтому требует явного `--acknowledge-restrictions` для скачивания PREPBUFR/raw dump файлов.

### USCRN

USCRN полезен не максимальной плотностью сети, а качеством наблюдений и наличием QC. Для проверки постпроцессинга, bias correction, sensor/QC experiments и эталонной оценки моделей на территории США это один из наиболее ценных наборов.

### Рекомендуемая архитектура

```text
                          OPERATIONAL

WIS2 ───────────────┐
MADIS ──────────────┼──→ raw observation store ─→ normalization/QC layer
NWS API ────────────┘                                  │
                                                       ├──→ nowcasting
                                                       ├──→ postprocessing
                                                       └──→ verification

                            ARCHIVE

GHCNh ──────────────┐
GHCNd ──────────────┼──→ station/time warehouse ──────→ ML training / validation
USCRN ──────────────┘

                      ASSIMILATION-SPACE

NCEP BUFR dumps ─→ PREPBUFR ─→ dedicated restricted-data-aware store
                              └→ DA / observation-impact research
```

Главный принцип: **не смешивать raw observations, QC-integrated observations, climate archives и assimilation-space в один тип источника**. У них разные задержки, права доступа, семантика QC и назначение.

## English

Use the NOAA sources according to their role rather than provider name alone:

- **NWS observations API** for low-friction operational station queries in the NWS domain.
- **MADIS** for multi-network operational ingest and QC-aware integration.
- **GHCNh** for new global hourly/synoptic archival station pipelines; treat ISD/Global Hourly as legacy compatibility.
- **GHCNd** for quality-controlled daily climate/station records.
- **USCRN** for reference-quality U.S. validation and sensor/QC work.
- **NCEP PREPBUFR/raw dumps** for data-assimilation and observation-space research, with explicit restricted-data handling.

Preserve raw payloads, source identifiers, timestamps, checksums and QC fields before normalization. Do not collapse archival station data and assimilation-space products into one generic observation layer.

## Example adapters

```bash
# GHCNh station/year URL
python examples/python/noaa_station_observations.py ghcnh-url USW00023183 --year 2026

# Read a few GHCNh PSV records without dropping raw QC/source columns
python examples/python/noaa_station_observations.py ghcnh-head USW00023183 --year 2026 --limit 3

# Latest NWS observation
python examples/python/noaa_station_observations.py nws-latest KJFK

# MADIS public sample/current URL
python examples/python/noaa_assimilation_observations.py madis-url metar 2026-10-19T12:00Z

# PREPBUFR URL only
python examples/python/noaa_assimilation_observations.py prepbufr-url 20261019 12 --model gdas

# Download PREPBUFR only after reviewing NCEP restricted-data conditions
python examples/python/noaa_assimilation_observations.py prepbufr-download 20261019 12 gdas.prepbufr \
  --acknowledge-restrictions
```

## Official references

- GHCNh: <https://www.ncei.noaa.gov/products/global-historical-climatology-network-hourly>
- GHCNd: <https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily>
- MADIS: <https://madis.ncep.noaa.gov/>
- NWS API: <https://www.weather.gov/documentation/services-web-api>
- USCRN: <https://www.ncei.noaa.gov/access/crn/products.html>
- NCEP GFS/GDAS observation products: <https://www.nco.ncep.noaa.gov/pmb/products/gfs/>
- NCEP restricted-data guidance: <https://www.nco.ncep.noaa.gov/pmb/docs/restricted_data/>
