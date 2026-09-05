# Weather Source

Weather Source is a bilingual operational reference for obtaining meteorological data programmatically. The machine-readable catalogue is authoritative; these pages explain how to choose, receive and decode the feeds.

**Русская версия:** [index.ru.md](index.ru.md)

## Start here

- [Source catalogue](sources/index.md) — generated from the catalogue at documentation build time.
- [Protocols](protocols.md) — WIS2/MQTT, AMQP, HTTPS, object storage, OGC services, OPeNDAP and FTP.
- [Formats](formats.md) — BUFR, GRIB2, NetCDF, HDF5, ODIM HDF5, GeoTIFF, JSON/XML/CSV.
- [Software](software.md) — receivers, decoders and analysis libraries.
- [Operational architecture](operations.md) — recommended ingestion, raw storage, decoding, normalization and failover.
- [Aerology](sources/aerology.md) — radiosondes/TEMP, profilers, aircraft observations and satellite profiles.
- [WMO WIS2](sources/wmo-wis2.md) — the preferred global event-driven exchange layer for many WMO observations.

## Principles

1. Prefer official primary feeds over convenient aggregators.
2. Prefer machine protocols over scraping visual web pages.
3. Separate transport from meteorological format: e.g. MQTT may deliver a notification whose canonical HTTPS object is BUFR.
4. Preserve raw BUFR/GRIB/NetCDF/HDF payloads when practical.
5. Keep at least one independent fallback for operational pipelines.
6. Treat model profiles, satellite retrievals and radiosondes as different observation/product classes.
7. Run scheduled health checks, but do not fail every pull request because an external provider has a temporary outage.

The catalogue is reviewed continuously. `last_verified` describes the most recent repository review of an entry, not a permanent availability guarantee.
