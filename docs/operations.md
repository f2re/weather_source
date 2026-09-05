# Operational ingestion architecture / Операционная архитектура приёма

A robust meteorological receiver should treat external providers as independent, failure-prone systems and normalize them behind a stable internal contract.

```text
provider notification / poll
          │
          ▼
 transport adapter ───► source metadata + audit log
          │
          ▼
 immutable raw store (BUFR/GRIB/NetCDF/HDF/...)
          │
          ▼
 format decoder
          │
          ▼
 normalization + units + identifiers
          │
          ▼
 QC / freshness / duplicate detection
          │
          ├──► normalized database / object index
          └──► API, visualisation, alerts, models
```

## 1. Transport adapters

Keep transport-specific code small. A WIS2 adapter understands MQTT notifications and HTTPS payload retrieval; an ECCC adapter may consume AMQP; an object-storage adapter lists/pulls keys; an OGC adapter issues bounded WFS/WCS queries. The decoder must not depend on how bytes arrived.

## 2. Raw store

Store the original payload whenever practical. Recommended metadata:

- `source_id` from this catalogue;
- provider message/object ID;
- canonical URL/topic/object key;
- observation/model cycle time when known;
- receive timestamp;
- SHA-256 or other content hash;
- content type and original file name;
- decoder/version used later.

## 3. Normalize after decoding

Normalize units and identifiers only after the standards-aware decoder has read the native message. For station data keep WIGOS/WMO/ICAO identifiers separately rather than replacing one with another. For model fields keep centre/model/run/step/level/member/parameter metadata.

## 4. Freshness is not connectivity

A provider can return HTTP 200 while serving stale data. Monitor at least three different states:

1. **endpoint health** — can the service be reached;
2. **publication freshness** — did a new expected object/message arrive;
3. **content validity** — can it be decoded and does the timestamp/coverage make sense.

The repository's scheduled health workflow checks the first layer. Production users should add product-specific freshness checks.

## 5. Failover

Suggested source roles:

- **primary** — direct official operational feed;
- **secondary** — independent official fallback or archive path;
- **specialized** — additional sensing technology/product family;
- **aggregator** — convenience/fallback only.

Do not silently merge conflicting observations. Preserve provenance and expose which source supplied a value.

## 6. Aerology pattern

For operational upper air:

```text
WIS2 TEMP/BUFR (primary)
     ├── Russian/other national WIS2 publishers
     └── global WIS2 topics
             │
             ▼
          ecCodes
             │
             ▼
 normalized sounding profile

fallback/archive: NOAA IGRA → Wyoming/Siphon
additional vertical data: E-PROFILE / AMDAR / GNSS-RO
reference QC: GRUAN
```

A model vertical profile is not a radiosonde. Satellite retrievals and aircraft profiles should also keep distinct `observation_type`/provenance.

## 7. Deployment model

For a small Linux server, a simple pattern is sufficient: systemd services/timers, filesystem or object raw store, SQLite/PostgreSQL metadata, Python/C++ decoders, retry queue and structured logs. Kubernetes or a message broker is not mandatory unless scale requires it.

For high-volume satellite/radar/NWP archives, separate raw object storage from the normalized database and avoid inserting entire binary payloads into relational tables.
