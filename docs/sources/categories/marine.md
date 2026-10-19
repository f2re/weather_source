# Морские наблюдения / marine

В этой категории **6** источников. / **6** sources in this category.

## 🇷🇺 Русский

| Источник | Описание | Категории | Доступ | Протоколы | Форматы | Оперативный |
|---|---|---|---|---|---|---:|
| 🟢 [Copernicus Marine Data Store](../generated/copernicus-marine.md) | Глобальные и региональные океанические анализы прогнозы наблюдения реобработанные продукты и поля волн. | Океанографические данные, Морские наблюдения, waves, analysis, Численные модели прогноза | бесплатный после регистрации | https, api | NetCDF, Zarr, provider-dependent | да |
| 🟢 [ECCC MSC Datamart](../generated/eccc-datamart.md) | Оперативные канадские и международные файлы наблюдений моделей и BUFR-бюллетеней с уведомлениями AMQP. | Наземные наблюдения, Аэрология и верхняя атмосфера, Метеорологические радары, Численные модели прогноза, Морские наблюдения | открытый без регистрации | https, amqp | BUFR, GRIB2, XML, CSV, GeoTIFF, provider-dependent | да |
| 🟢 [NOAA NDBC — буи и морские наблюдения](../generated/noaa-ndbc.md) | Оперативные наблюдения буёв и прибрежных станций включая ветер давление волны температуру воды и другие морские параметры. | Морские наблюдения, Океанографические данные, Наземные наблюдения, waves | открытый без регистрации | https | text, XML, NetCDF, provider-dependent | да |
| 🟢 [NOAA/NCEP MADIS — оперативные наблюдения](../generated/noaa-ncep-madis.md) | Система интеграции и контроля качества наблюдений из множества сетей: METAR, mesonet, maritime, радиозонды, профайлеры, самолётные и другие данные, преимущественно в netCDF. | Наземные наблюдения, Аэрология и верхняя атмосфера, Авиационные наблюдения, Морские наблюдения, Профайлеры | бесплатный после регистрации | https, ftp, opendap, ldm | NetCDF, CSV, XML, text | да |
| 🟡 [BOM — открытые потоки данных](../generated/bom-open-data.md) | Австралийские публичные потоки наблюдений предупреждений моделей и радиолокационных данных. | Наземные наблюдения, Метеорологические радары, Численные модели прогноза, Морские наблюдения | открытый без регистрации | https, ftp | XML, JSON, text, GRIB2, image, provider-dependent | да |
| 🔵 [NCEP GDAS/GFS — observation dumps и PREPBUFR](../generated/noaa-ncep-prepbufr.md) | Файлы пространства наблюдений NCEP, используемые в контуре ассимиляции GDAS/GFS: исходные BUFR dumps и подготовленные quality-controlled PREPBUFR. | Наземные наблюдения, Аэрология и верхняя атмосфера, Авиационные наблюдения, Морские наблюдения, GNSS radio occultation, assimilation | ограниченный доступ | https, ftp | BUFR, PREPBUFR | да |

## 🇬🇧 English

| Source | Description | Categories | Access | Protocols | Formats | Operational |
|---|---|---|---|---|---|---:|
| 🟢 [Copernicus Marine Data Store](../generated/copernicus-marine.md) | Global and regional ocean analyses forecasts observations reprocessed products and wave datasets. | ocean, marine, waves, analysis, nwp | `registration` | https, api | NetCDF, Zarr, provider-dependent | yes |
| 🟢 [MSC Datamart](../generated/eccc-datamart.md) | Operational Canadian and international files including observations model output and BUFR bulletins with AMQP notifications. | surface, upper-air, radar, nwp, marine | `open` | https, amqp | BUFR, GRIB2, XML, CSV, GeoTIFF, provider-dependent | yes |
| 🟢 [NOAA NDBC](../generated/noaa-ndbc.md) | Operational buoy and coastal station observations including wind pressure waves water temperature and selected ocean variables. | marine, ocean, surface, waves | `open` | https | text, XML, NetCDF, provider-dependent | yes |
| 🟢 [NOAA/NCEP MADIS observations](../generated/noaa-ncep-madis.md) | Multi-network observation ingest, integration and quality-control system covering surface, mesonet, maritime, radiosonde, profiler, aircraft and other datasets, primarily in netCDF. | surface, upper-air, aircraft, marine, profilers | `registration` | https, ftp, opendap, ldm | NetCDF, CSV, XML, text | yes |
| 🟡 [BOM data feeds](../generated/bom-open-data.md) | Australian public observations warnings model and radar-related data feeds. | surface, radar, nwp, marine | `open` | https, ftp | XML, JSON, text, GRIB2, image, provider-dependent | yes |
| 🔵 [NCEP GDAS/GFS observation dumps and PREPBUFR](../generated/noaa-ncep-prepbufr.md) | NCEP observation-space files used around GDAS/GFS data assimilation, including raw BUFR dumps and quality-controlled PREPBUFR products. | surface, upper-air, aircraft, marine, gnss-ro, assimilation | `restricted` | https, ftp | BUFR, PREPBUFR | yes |
