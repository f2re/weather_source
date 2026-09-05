# Meteorological data formats / Форматы метеоданных

| Format | Typical use | Recommended tooling | Notes |
|---|---|---|---|
| **BUFR (WMO FM 94)** | SYNOP, TEMP, aircraft, profilers, satellite products, international exchange | **ecCodes**, pybufrkit | Table-driven binary format. Keep the original message and use current WMO tables. |
| **GRIB / GRIB2** | NWP, analyses, ensembles, gridded radar/multisensor products | **ecCodes**, wgrib2, cfgrib+xarray | Efficient field-oriented meteorological grid format. Select messages before loading large global files. |
| **NetCDF** | Satellite, ocean, climate, scientific gridded/profile products | **xarray**, netCDF4 | Inspect CF conventions, coordinates, packing and missing-value metadata. |
| **HDF5** | Satellite and remote-sensing products | **h5py**, xarray where supported | HDF5 is a container; product semantics remain provider-specific. |
| **ODIM HDF5** | European weather radar volumes/products | **wradlib**, BALTRAD tools | Standardized radar conventions on top of HDF5. |
| **NEXRAD Level II/III** | US weather radar | **Py-ART**, MetPy, nexradaws | Level II is close to radar volume data; Level III contains derived products. |
| **GeoTIFF** | Raster products, derived grids, GIS distribution | **GDAL/rasterio** | Good for geospatial interoperability; often a derived rather than native meteorological format. |
| **HRIT/LRIT/native satellite formats** | Geostationary satellite dissemination | **Satpy/PyTroll**, vendor tools | Usually mission/product-specific wrappers and segmentation rules. |
| **JSON / GeoJSON** | APIs, metadata, decoded observations | requests/httpx, pandas, GeoPandas | Convenient but normally less compact than native binary meteorological formats. |
| **XML / GML** | OGC/WFS and aviation/weather exchange products | OWSLib, lxml | Often verbose; preserve identifiers and units from the source schema. |
| **CSV / text** | Stations, simple profiles, archives | pandas, csv | Easy to inspect but frequently loses rich metadata unless provider documentation is followed. |

## Decoder policy / Политика декодирования

For WMO BUFR and GRIB, **ECMWF ecCodes is the default recommendation** because it tracks WMO tables and supports C, Fortran, command-line utilities and Python bindings. `bufr_dump`, `grib_ls`, `grib_get`, `grib_filter` and Python bindings are useful for diagnostics and production pipelines.

Для BUFR и GRIB по умолчанию рекомендуется **ecCodes**. Не следует писать собственный бинарный декодер, если задача решается актуальными таблицами WMO и ecCodes.

## Preserve raw data / Сохраняйте исходные данные

A normalized database is not a substitute for the original payload. Whenever storage allows, keep the raw object together with at least:

- provider/source ID;
- canonical source URL or WIS2 message identifier;
- retrieval timestamp;
- content hash;
- original filename/content type;
- decoder/version used for normalization.

Это позволяет повторно декодировать BUFR/GRIB после обновления таблиц, исправления библиотеки или изменения бизнес-логики без повторного запроса к внешнему источнику.
