# Авиационные наблюдения / aircraft

В этой категории **5** источников. / **5** sources in this category.

## 🇷🇺 Русский

| Источник | Описание | Категории | Доступ | Протоколы | Форматы | Оперативный |
|---|---|---|---|---|---|---:|
| 🟢 [NOAA/NCEP MADIS — оперативные наблюдения](../generated/noaa-ncep-madis.md) | Система интеграции и контроля качества наблюдений из множества сетей: METAR, mesonet, maritime, радиозонды, профайлеры, самолётные и другие данные, преимущественно в netCDF. | Наземные наблюдения, Аэрология и верхняя атмосфера, Авиационные наблюдения, Морские наблюдения, Профайлеры | бесплатный после регистрации | https, ftp, opendap, ldm | NetCDF, CSV, XML, text | да |
| 🟢 [WMO WIS 2.0 — глобальные сервисы](../generated/wmo-wis2.md) | Глобальный событийный обмен основными и рекомендуемыми данными WMO; MQTT-уведомления указывают на HTTPS-файлы. | Наземные наблюдения, Аэрология и верхняя атмосфера, Авиационные наблюдения, Спутниковые данные, Метеорологические радары, Численные модели прогноза, Метаданные | открытый без регистрации | mqtt, https | BUFR, GRIB2, NetCDF, JSON, XML, provider-dependent | да |
| 🔵 [AMDAR — самолётные наблюдения](../generated/eumetnet-amdar.md) | Самолётные наблюдения температуры, ветра и части влажностных параметров, включая профили набора и снижения около аэропортов. | Авиационные наблюдения, Аэрология и верхняя атмосфера | ограниченный доступ | mqtt, https, wis2 | BUFR | да |
| 🔵 [NOAA MADIS — система приёма метеорологических наблюдений](../generated/noaa-madis.md) | База и система доставки наблюдений NOAA, включающая радиозонды, профайлеры, самолётные наблюдения, спутниковые зондирования и другие in-situ наборы. | Аэрология и верхняя атмосфера, profiler, Авиационные наблюдения, Наземные наблюдения | бесплатный после регистрации | https, ftp, opendap, ldm | NetCDF, XML, text | да |
| 🔵 [NCEP GDAS/GFS — observation dumps и PREPBUFR](../generated/noaa-ncep-prepbufr.md) | Файлы пространства наблюдений NCEP, используемые в контуре ассимиляции GDAS/GFS: исходные BUFR dumps и подготовленные quality-controlled PREPBUFR. | Наземные наблюдения, Аэрология и верхняя атмосфера, Авиационные наблюдения, Морские наблюдения, GNSS radio occultation, assimilation | ограниченный доступ | https, ftp | BUFR, PREPBUFR | да |

## 🇬🇧 English

| Source | Description | Categories | Access | Protocols | Formats | Operational |
|---|---|---|---|---|---|---:|
| 🟢 [NOAA/NCEP MADIS observations](../generated/noaa-ncep-madis.md) | Multi-network observation ingest, integration and quality-control system covering surface, mesonet, maritime, radiosonde, profiler, aircraft and other datasets, primarily in netCDF. | surface, upper-air, aircraft, marine, profilers | `registration` | https, ftp, opendap, ldm | NetCDF, CSV, XML, text | yes |
| 🟢 [WMO WIS 2.0 Global Services](../generated/wmo-wis2.md) | Global event-driven exchange for WMO core and recommended meteorological data; MQTT notifications point to HTTPS payloads. | surface, upper-air, aircraft, satellite, radar, nwp, metadata | `open` | mqtt, https | BUFR, GRIB2, NetCDF, JSON, XML, provider-dependent | yes |
| 🔵 [AMDAR aircraft observations](../generated/eumetnet-amdar.md) | Aircraft-based temperature, wind and selected humidity observations, including ascent/descent profiles near airports. | aircraft, upper-air | `restricted` | mqtt, https, wis2 | BUFR | yes |
| 🔵 [Meteorological Assimilation Data Ingest System (MADIS)](../generated/noaa-madis.md) | NOAA observational database and delivery system with radiosondes, profiler networks, aircraft observations, satellite soundings and other in-situ datasets. | upper-air, profiler, aircraft, surface | `registration` | https, ftp, opendap, ldm | NetCDF, XML, text | yes |
| 🔵 [NCEP GDAS/GFS observation dumps and PREPBUFR](../generated/noaa-ncep-prepbufr.md) | NCEP observation-space files used around GDAS/GFS data assimilation, including raw BUFR dumps and quality-controlled PREPBUFR products. | surface, upper-air, aircraft, marine, gnss-ro, assimilation | `restricted` | https, ftp | BUFR, PREPBUFR | yes |
