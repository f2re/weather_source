# Software and libraries / ПО и библиотеки

## Core meteorological decoders

| Tool | Use | Recommendation |
|---|---|---|
| **ECMWF ecCodes** | BUFR and GRIB/GRIB2 decode/encode, CLI and Python | Default for WMO binary formats. |
| **wgrib2** | GRIB2 inventory, extraction, transformation | Excellent operational CLI companion for NWP. |
| **cfgrib + xarray** | Open GRIB as labelled xarray datasets | Good for Python analytics; understand GRIB message grouping. |
| **netCDF4 / xarray** | NetCDF and CF-style data | Default scientific Python stack for many satellite/ocean/climate products. |
| **h5py** | HDF5 containers | Low-level access when no product-specific reader exists. |
| **GDAL / rasterio** | GeoTIFF and geospatial raster/vector conversion | Use for GIS-oriented derived products. |

## Receiving and provider clients

| Tool | Provider/protocol | Notes |
|---|---|---|
| **wis2downloader** | WMO WIS2 | MQTT notifications + referenced payload download. |
| **pywis-pubsub** | WMO WIS2 | Python pub/sub utilities for WIS2 workflows. |
| **EUMDAC** | EUMETSAT | Official Python/CLI client for Data Store services. |
| **ecmwf-opendata** | ECMWF Open Data | Official convenient retrieval client. |
| **cdsapi** | Copernicus CDS/ADS | API client for climate/atmosphere datasets requiring an account/token. |
| **copernicusmarine** | Copernicus Marine | Official CLI/Python toolbox supporting subset/get workflows. |
| **earthaccess** | NASA Earthdata | Search, authentication and download for many NASA datasets. |
| **Siphon** | Unidata services / upper air | Convenient clients for Wyoming, IGRA and Iowa State upper-air services. |
| **OWSLib** | WFS/WMS/WCS | Generic OGC service client. |
| **boto3 / AWS CLI** | S3/object storage | Useful for NOAA NODD and other public buckets. |
| **pika** | AMQP | Suitable for ECCC/MSC Datamart notification consumers. |

## Radar and satellite libraries

- **Py-ART** — radar volumes, especially NEXRAD and research workflows.
- **wradlib** — weather-radar processing, ODIM HDF5 and georeferencing.
- **Satpy/PyTroll** — multi-mission satellite reading, resampling and compositing.
- **MetPy** — meteorological calculations, units, sounding/radar utilities.

## Ocean/profile libraries

- **argopy** — Argo float discovery and profile access.
- **xarray** — NetCDF/Zarr ocean and atmospheric datasets.
- **pandas** — station tables, CSV and simple profile formats.

## Selection rule / Правило выбора

Prefer a provider-maintained client when it materially handles authentication, pagination, subsetting or product naming. Prefer generic stable decoders for standard formats. Do not make an obscure wrapper library the only dependency in a critical pipeline if the official HTTP/object endpoint is simple enough to consume directly.

Для BUFR/GRIB лучше строить систему вокруг ecCodes, а не вокруг самописного парсера. Для нестандартных сервисов полезно отделять небольшой адаптер получения данных от декодера и внутренней модели данных.
