# Осадки / precipitation

В этой категории **5** источников. / **5** sources in this category.

## 🇷🇺 Русский

| Источник | Описание | Категории | Доступ | Протоколы | Форматы | Оперативный |
|---|---|---|---|---|---|---:|
| 🟢 [NOAA NEXRAD Level II и Level III](../generated/noaa-nexrad.md) | Радиолокационные объёмы и производные продукты американской сети NEXRAD. | Метеорологические радары, Осадки, severe-weather | открытый без регистрации | s3, https | NEXRAD Level II, NEXRAD Level III | да |
| 🟢 [NOAA MRMS — Multi-Radar Multi-Sensor](../generated/noaa-mrms.md) | Быстро обновляемые сеточные радиолокационные и мультисенсорные продукты включая отражаемость осадки и диагностику опасных явлений. | Метеорологические радары, Осадки, severe-weather | открытый без регистрации | https, s3 | GRIB2, NetCDF, GeoTIFF, provider-dependent | да |
| 🔵 [JAXA GSMaP — глобальные осадки](../generated/jaxa-gsmap.md) | Оперативные и архивные глобальные спутниковые поля осадков JAXA. | Спутниковые данные, Осадки | бесплатный после регистрации | https, ftp | binary grid, NetCDF, text, GeoTIFF, provider-dependent | да |
| 🔵 [NASA LANCE / Earthdata Near Real-Time](../generated/nasa-earthdata-lance.md) | Спутниковые продукты близкого к реальному времени для атмосферы суши пожаров аэрозолей осадков и других наблюдений Земли. | Спутниковые данные, Осадки, aerosol, fire, clouds | бесплатный после регистрации | https, api | HDF5, NetCDF, GeoTIFF, provider-dependent | да |
| 🔵 [NASA GPM IMERG — спутниковые осадки](../generated/nasa-gpm-imerg.md) | Глобальные мультиспутниковые оценки осадков с оперативными Early/Late и окончательными Final продуктами. | Спутниковые данные, Осадки | бесплатный после регистрации | https, opendap, api | HDF5, NetCDF, GeoTIFF | да |

## 🇬🇧 English

| Source | Description | Categories | Access | Protocols | Formats | Operational |
|---|---|---|---|---|---|---:|
| 🟢 [NEXRAD Level II and Level III](../generated/noaa-nexrad.md) | United States weather-radar volumes and derived products from the NEXRAD network. | radar, precipitation, severe-weather | `open` | s3, https | NEXRAD Level II, NEXRAD Level III | yes |
| 🟢 [Multi-Radar Multi-Sensor (MRMS)](../generated/noaa-mrms.md) | Rapid-update gridded radar and multisensor products including reflectivity precipitation and severe-weather diagnostics. | radar, precipitation, severe-weather | `open` | https, s3 | GRIB2, NetCDF, GeoTIFF, provider-dependent | yes |
| 🔵 [GSMaP global precipitation](../generated/jaxa-gsmap.md) | Near-real-time and historical global satellite precipitation maps from JAXA. | satellite, precipitation | `registration` | https, ftp | binary grid, NetCDF, text, GeoTIFF, provider-dependent | yes |
| 🔵 [NASA LANCE / Earthdata Near Real-Time](../generated/nasa-earthdata-lance.md) | Near-real-time satellite products for atmosphere land fire aerosols precipitation and related Earth observations. | satellite, precipitation, aerosol, fire, clouds | `registration` | https, api | HDF5, NetCDF, GeoTIFF, provider-dependent | yes |
| 🔵 [GPM IMERG precipitation](../generated/nasa-gpm-imerg.md) | Multi-satellite global precipitation estimates with Early Late and Final runs. | satellite, precipitation | `registration` | https, opendap, api | HDF5, NetCDF, GeoTIFF | yes |
