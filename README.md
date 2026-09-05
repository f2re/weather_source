# 🌦️ Weather Source

[![CI](https://github.com/f2re/weather_source/actions/workflows/ci.yml/badge.svg)](https://github.com/f2re/weather_source/actions/workflows/ci.yml)
[![Source health](https://github.com/f2re/weather_source/actions/workflows/source-health.yml/badge.svg)](https://github.com/f2re/weather_source/actions/workflows/source-health.yml)
[![Docs](https://github.com/f2re/weather_source/actions/workflows/docs.yml/badge.svg)](https://github.com/f2re/weather_source/actions/workflows/docs.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![RU](https://img.shields.io/badge/lang-Русский-blue)](README.ru.md)

> Bilingual knowledge base of operational meteorological data sources for meteorologists, developers and AI agents.

Weather Source answers not only **where to get the data**, but also **how to receive, decode, validate, archive and operate the feed**.

## Start here

For a human:

- 🇬🇧 [`docs/sources/index.en.md`](docs/sources/index.en.md) — complete English catalogue.
- 🇷🇺 [`docs/sources/index.ru.md`](docs/sources/index.ru.md) — complete Russian catalogue.
- 🌍 [`docs/sources/index.md`](docs/sources/index.md) — bilingual overview, tiers and categories.
- 📄 `docs/sources/generated/<id>.md` — detailed bilingual technical card for every source, Russian first.
- 🛰️ [`docs/sources/wmo-wis2.md`](docs/sources/wmo-wis2.md) — implementation-oriented WIS2 guide.
- 🤖 [`docs/agent-guide.md`](docs/agent-guide.md) — retrieval and source-selection rules for agents.

For software/AI agents:

- `llms.txt` — compact repository map;
- `catalog/agent-index.json` — compact ranking/index layer;
- `catalog/sources.json` — full flattened catalogue;
- `catalog/sources.ndjson` — one complete source per line;
- `catalog/sources.yaml` + `catalog/sources/*.yaml` — authoritative source of truth;
- `catalog/schema.json` — record contract.

## What every source record contains

Provider, official/primary status, data families, coverage, operational suitability, update cadence, expected latency, archive depth, access/authentication/terms, machine protocols, native formats, real endpoints, libraries/decoders, official documentation, reliability, automation suitability and last verification date.

The generated source card adds a practical Russian and English ingestion flow, decoder hints and agent-selection notes.

## Main data families

| Data family | Representative primary sources | Native formats | Preferred machine access |
|---|---|---|---|
| 🌡️ Surface observations | WIS2, NOAA/NWS, ECCC, DWD, FMI, MeteoSwiss, JMA, BOM | BUFR, text, JSON, CSV | WIS2 MQTT+HTTPS, REST/HTTPS |
| 🎈 Upper air | WIS2 TEMP, Roshydromet/Aviamettelecom, IGRA, DWD, FMI, Météo-France, MeteoSwiss, ECCC | BUFR, CSV, text, NetCDF | WIS2, HTTPS, WFS |
| 📡 Radar | NEXRAD/MRMS, DWD, ECCC, European/national services | Level II/III, GRIB2, ODIM HDF5, GeoTIFF | S3/HTTPS, WCS/OGC |
| 🛰️ Satellite | EUMETSAT, NOAA/NODD, NASA Earthdata/LANCE, JAXA | NetCDF, HDF5, BUFR, GeoTIFF | Data Store/API, S3, HTTPS |
| ⚡ Lightning | GOES GLM, MTG LI and documented restricted/community networks | NetCDF/HDF5/BUFR | object storage / Data Store |
| 🌊 Ocean/marine | Copernicus Marine, NDBC, Argo | NetCDF, CSV, JSON | HTTPS/API/object storage |
| 🧠 NWP/ensembles | ECMWF Open Data, NOMADS/NODD, DWD, Météo-France, ECCC, JMA | GRIB2, NetCDF | HTTPS/S3/API |
| 🗃️ Climate/archives | NCEI, CDS/ERA5, IGRA, national archives | NetCDF, GRIB, CSV, BUFR | API/HTTPS |

## Operational selection rules

1. Prefer `official: true`.
2. Prefer `tier: primary`.
3. Require `operational: true` for real-time workflows.
4. Match geographic coverage and access rights.
5. Prefer event/object/API transports over scraping: WIS2/MQTT, AMQP, S3, REST/OGC, direct file services.
6. Match the native format to a standards-aware decoder.
7. Preserve raw payloads before normalization.
8. Keep an independent fallback for critical ingestion.

For WMO observations, check **WIS2 core data first**. For upper air, never confuse radiosonde/TEMP, AMDAR, profiler, satellite/GNSS-RO retrieval and NWP model profiles.

## Generated catalogue is committed

The YAML catalogue remains authoritative, but human and agent views are committed to `main`, not hidden inside a CI build. `Sync generated catalogue` regenerates and commits the indexes/cards after catalogue changes. `generate_docs.py --verify` detects missing, stale or outdated generated artifacts.

## Local validation

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_catalog.py
python scripts/generate_docs.py --write
python scripts/generate_docs.py --verify
python -m compileall -q examples scripts tests
pytest -q
mkdocs build --strict
```

Live endpoint checks remain separate from deterministic PR validation:

```bash
python scripts/check_endpoints.py --catalog catalog/sources.yaml --tier primary --report source-health.json
```

## Repository structure

```text
catalog/                     authoritative YAML + JSON/NDJSON agent views
docs/sources/index*.md       committed human catalogues
docs/sources/generated/      one detailed bilingual card per source
docs/sources/categories/     category indexes
docs/agent-guide.md           AI-agent retrieval rules
examples/python/             ingestion/decoder examples
scripts/                     validation, generation and health checks
tests/                       catalogue and runtime tests
.github/workflows/           CI, sync, health and documentation workflows
```

## Contributing and security

See [`CONTRIBUTING.md`](CONTRIBUTING.md), [`SECURITY.md`](SECURITY.md) and the issue templates. Update the authoritative YAML record, not generated Markdown/JSON independently.

## License

Repository code and original documentation are licensed under the [MIT License](LICENSE). External meteorological datasets remain subject to their providers' licences, terms and attribution requirements.
