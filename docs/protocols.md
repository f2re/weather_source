# Access protocols / Протоколы доступа

Meteorological systems often separate **notification/transport** from **payload format**. A WIS2 MQTT message, for example, usually points to a canonical HTTPS object that may contain BUFR, GRIB2 or another product.

| Protocol / service | Best use | Operational notes |
|---|---|---|
| **WIS2 MQTT + HTTPS** | WMO global operational exchange | Subscribe to topic notifications, verify metadata, download the canonical object over HTTPS. Prefer core data and keep a second Global Broker/Cache for resilience. |
| **AMQP** | Event notification, notably ECCC/MSC Datamart | Avoid high-frequency polling. Consume file notifications, then download the referenced object. |
| **HTTPS file trees** | DWD, ECCC, NDBC and many national services | Simple and robust. Track provider directory conventions and timestamps; use conditional requests/index files when available. |
| **REST/API** | Observation queries, metadata, subset services | Respect quotas, authentication and pagination. Persist the exact request parameters used. |
| **S3/object storage** | NODD, NEXRAD, large model/satellite archives | Ideal for bulk automation. Use anonymous/public access when supported, prefix listing, and partial/selective downloads. |
| **WFS / OGC API Features** | Station observations and metadata | Good for structured geospatial queries. Use server-side spatial/time filtering. |
| **WMS** | Rendered map layers | Primarily visualization. Do not use WMS pixels as the canonical numeric dataset when WCS/API/raw data exist. |
| **WCS / OGC API Coverages** | Gridded numeric subsets | Prefer over WMS for scientific values; request only the needed spatial/temporal subset. |
| **OPeNDAP / THREDDS** | Scientific NetCDF-style remote subsetting | Useful for slices; can be inefficient for many small repeated requests. Cache intentionally. |
| **FTP/FTPS/SFTP** | Legacy or bulk dissemination | Still common in some archives. Prefer HTTPS/object storage when the provider offers an equivalent modern endpoint. |

## WIS2 topic strategy / Стратегия WIS2

For broad operational collection, subscribe at a sufficiently high topic level, then filter by metadata rather than creating hundreds of station-specific connections. For a specific source, pin the publisher/topic as an additional monitoring rule.

Example conceptual TEMP subscription:

```text
cache/a/wis2/+/data/core/weather/surface-based-observations/temp
```

Russian upper-air example recorded in the catalogue:

```text
cache/a/wis2/ru-aviamettelecom/data/core/weather/surface-based-observations/temp
```

Do not assume that MQTT itself carries the final meteorological file. A robust receiver stores the notification metadata, retrieves the canonical payload and then passes that payload to the appropriate decoder.

## Polling policy / Политика опроса

- Prefer push/event mechanisms where officially supported.
- Add jitter/backoff to polling loops.
- Do not repeatedly download full GRIB/satellite/radar files merely to detect an update.
- Use directory listings, object metadata, ETag/Last-Modified, message IDs or provider indexes.
- Distinguish **service health checks** from **data freshness checks**: HTTP 200 does not prove that a product is current.
