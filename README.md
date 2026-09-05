# 🌦️ Weather Source

[![CI](https://github.com/f2re/weather_source/actions/workflows/ci.yml/badge.svg)](https://github.com/f2re/weather_source/actions/workflows/ci.yml)
[![Source health](https://github.com/f2re/weather_source/actions/workflows/source-health.yml/badge.svg)](https://github.com/f2re/weather_source/actions/workflows/source-health.yml)
[![Docs](https://github.com/f2re/weather_source/actions/workflows/docs.yml/badge.svg)](https://github.com/f2re/weather_source/actions/workflows/docs.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![RU](https://img.shields.io/badge/lang-Русский-blue)](README.ru.md)

> A machine-readable, bilingual knowledge base of **operational meteorological data sources**: observations, radiosondes, radar, satellites, lightning, ocean data, NWP/ensembles, analyses and archives.

Weather Source is intended for meteorologists, developers and AI agents that need to answer not only **“where are the data?”**, but also **“how do I receive, decode, validate and operate this feed?”**.

## What is inside

- 🗂️ **Machine-readable catalogue** — [`catalog/sources.yaml`](catalog/sources.yaml) is the source of truth.
- 📚 **Source cards** — one documentation page per provider/source family in [`docs/sources/`](docs/sources/).
- 🌍 **Russian + English descriptions** in the catalogue and documentation.
- 🔌 **Access details** — HTTPS, REST, WFS/WMS, THREDDS/OPeNDAP, S3/object storage, MQTT/WIS2, AMQP, FTP and other transports.
- 📦 **Formats** — BUFR, GRIB/GRIB2, NetCDF, HDF5, GeoTIFF, ODIM HDF5, JSON, XML/GML, CSV and text bulletins.
- 🛠️ **Software and decoders** — ecCodes, wgrib2, cfgrib/xarray, netCDF4, h5py, GDAL, pybufrkit, Siphon, EUMDAC, cdsapi, earthaccess and provider-specific clients.
- 🧪 **Executable examples** in [`examples/`](examples/).
- ✅ **CI validation** — schema, catalogue invariants, documentation generation and Python examples are checked on every PR.
- ❤️ **Scheduled source health checks** — selected official endpoints are probed with retries and a machine-readable report is uploaded as an artifact.

## Catalogue at a glance

| Data family | Primary free/open sources | Typical formats | Recommended access |
|---|---|---|---|
| 🌡️ Surface observations | WIS2, NOAA/NWS, ECCC, DWD, FMI, MeteoSwiss, JMA, BOM | BUFR, METAR/SYNOP text, JSON, CSV | WIS2 MQTT+HTTPS, REST/HTTPS |
| 🎈 Upper air / aerology | WIS2 TEMP, Roshydromet/Aviamettelecom, IGRA, DWD, FMI, Météo-France, MeteoSwiss, ECCC, Wyoming | BUFR, CSV, text, NetCDF | WIS2, HTTPS, WFS |
| 📡 Weather radar | NOAA NEXRAD/MRMS, DWD, ECCC, OPERA/E-PROFILE metadata, national services | Level II/III, GRIB2, ODIM HDF5, GeoTIFF | S3/HTTPS, WMS/WCS |
| 🛰️ Satellites | EUMETSAT, NOAA/NESDIS/NODD, NASA Earthdata/LANCE, JAXA | NetCDF, HDF5, HRIT/LRIT, BUFR, GeoTIFF | Data Store/API, S3, HTTPS |
| ⚡ Lightning | NOAA GOES GLM, EUMETSAT MTG Lightning Imager, community/restricted networks documented separately | NetCDF/HDF5/BUFR | S3/Data Store |
| 🌊 Ocean / marine | Copernicus Marine, NOAA NDBC, Argo GDAC, ERDDAP services | NetCDF, CSV, JSON | HTTPS, ERDDAP, object storage |
| 🧠 NWP / ensembles | ECMWF Open Data, NOAA NOMADS/NODD, DWD Open Data, Météo-France, ECCC, JMA, Copernicus | GRIB2, NetCDF | HTTPS/S3/API |
| 🗃️ Climate / archives | NCEI, Copernicus CDS, ERA5, IGRA, ISD, national climate archives | NetCDF, GRIB, CSV, BUFR | API/HTTPS |

The catalogue contains availability, latency/update cadence, spatial coverage, archive depth, authentication, licences/terms, protocols, endpoints, formats, software, decoders, reliability and automation notes for each entry.

## Fast paths

### I need global operational observations

Start with **WMO WIS2**. Subscribe to WIS2 notifications over MQTT, then download canonical payloads via HTTPS. Keep national HTTPS/API feeds as independent fallbacks.

### I need radiosondes / TEMP for Russia and the world

Use **WIS2 TEMP** as the primary operational transport. Russian upper-air observations are published through the WIS2 ecosystem; use **NOAA IGRA** and **University of Wyoming/Siphon** as independent fallback/archive paths. See [`docs/sources/wmo-wis2.md`](docs/sources/wmo-wis2.md) and [`docs/sources/aerology.md`](docs/sources/aerology.md).

### I need global forecast models

Use **ECMWF Open Data**, **NOAA NOMADS/NODD**, **DWD Open Data**, **ECCC Datamart/GeoMet** and other national open feeds. Keep at least two providers for operational resilience.

## Repository layout

```text
catalog/
  sources.yaml          # authoritative data catalogue
  schema.json           # JSON Schema for catalogue entries
docs/
  index.md              # documentation landing page
  formats.md            # meteorological formats
  protocols.md          # transport/access protocols
  software.md           # receiving/decoding software
  operations.md         # recommended ingestion architecture
  sources/              # one source/provider card per file
examples/
  python/               # small reusable ingestion/decoding examples
scripts/
  validate_catalog.py   # structural and semantic validation
  check_endpoints.py    # live endpoint health checker
  generate_docs.py      # verifies/updates generated source index
.github/workflows/
  ci.yml                # deterministic PR checks
  source-health.yml     # scheduled live checks
  docs.yml              # MkDocs build
```

## Use from an AI agent

Read [`AGENTS.md`](AGENTS.md) first. For source selection, prefer `catalog/sources.yaml` over prose. An agent should:

1. filter by `categories`, `coverage`, `operational`, `access.level` and `formats`;
2. prefer official `tier: primary` sources;
3. use `endpoints[].url` and the documented protocol rather than scraping web visualisations;
4. preserve raw meteorological payloads when practical;
5. verify licence/terms and authentication before deployment;
6. implement fallback sources for operational systems.

## Local validation

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_catalog.py
python scripts/generate_docs.py --check
python -m compileall examples scripts tests
pytest -q
```

Optional live check:

```bash
python scripts/check_endpoints.py --catalog catalog/sources.yaml --tier primary --report source-health.json
```

Live network checks are intentionally separated from deterministic PR validation because external meteorological services can have maintenance windows and transient outages.

## Contributing

New sources and corrections are welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md), the source request template and [`SECURITY.md`](SECURITY.md). A catalogue change should include official documentation, access/format details and a health-checkable endpoint where possible.

## Scope and status

This is a **living operational reference**, not a claim that every meteorological dataset on Earth is already indexed. The priority is primary, official, free/open or practically accessible feeds that can be automated. Aggregators and restricted/community networks are listed separately and clearly labelled.

Last major catalogue review: **2026-09-05**.

## License

Repository code and original documentation are licensed under the [MIT License](LICENSE). Data obtained from external providers remain subject to each provider's own licence, terms of use and attribution requirements.