# Авиационные наблюдения / aircraft

В этой категории **3** источников. / **3** sources in this category.

## 🇷🇺 Русский

| Источник | Описание | Категории | Доступ | Протоколы | Форматы | Оперативный |
|---|---|---|---|---|---|---:|
| 🟢 [WMO WIS 2.0 — глобальные сервисы](../generated/wmo-wis2.md) | Глобальный событийный обмен основными и рекомендуемыми данными WMO; MQTT-уведомления указывают на HTTPS-файлы. | Наземные наблюдения, Аэрология и верхняя атмосфера, Авиационные наблюдения, Спутниковые данные, Метеорологические радары, Численные модели прогноза, Метаданные | открытый без регистрации | mqtt, https | BUFR, GRIB2, NetCDF, JSON, XML, provider-dependent | да |
| 🔵 [AMDAR — самолётные наблюдения](../generated/eumetnet-amdar.md) | Самолётные наблюдения температуры, ветра и части влажностных параметров, включая профили набора и снижения около аэропортов. | Авиационные наблюдения, Аэрология и верхняя атмосфера | ограниченный доступ | mqtt, https, wis2 | BUFR | да |
| 🔵 [NOAA MADIS — система приёма метеорологических наблюдений](../generated/noaa-madis.md) | База и система доставки наблюдений NOAA, включающая радиозонды, профайлеры, самолётные наблюдения, спутниковые зондирования и другие in-situ наборы. | Аэрология и верхняя атмосфера, profiler, Авиационные наблюдения, Наземные наблюдения | бесплатный после регистрации | https, ftp, opendap, ldm | NetCDF, XML, text | да |

## 🇬🇧 English

| Source | Description | Categories | Access | Protocols | Formats | Operational |
|---|---|---|---|---|---|---:|
| 🟢 [WMO WIS 2.0 Global Services](../generated/wmo-wis2.md) | Global event-driven exchange for WMO core and recommended meteorological data; MQTT notifications point to HTTPS payloads. | surface, upper-air, aircraft, satellite, radar, nwp, metadata | `open` | mqtt, https | BUFR, GRIB2, NetCDF, JSON, XML, provider-dependent | yes |
| 🔵 [AMDAR aircraft observations](../generated/eumetnet-amdar.md) | Aircraft-based temperature, wind and selected humidity observations, including ascent/descent profiles near airports. | aircraft, upper-air | `restricted` | mqtt, https, wis2 | BUFR | yes |
| 🔵 [Meteorological Assimilation Data Ingest System (MADIS)](../generated/noaa-madis.md) | NOAA observational database and delivery system with radiosondes, profiler networks, aircraft observations, satellite soundings and other in-situ datasets. | upper-air, profiler, aircraft, surface | `registration` | https, ftp, opendap, ldm | NetCDF, XML, text | yes |
