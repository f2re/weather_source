# WMO WIS2 / WMO WIS2

WIS 2.0 is the preferred global event-driven exchange layer for many WMO operational datasets. The important engineering model is:

```text
MQTT notification
      │
      ▼
WIS2 Notification Message (metadata + links)
      │
      ▼
canonical/cache HTTPS payload
      │
      ▼
BUFR / GRIB2 / NetCDF / other decoder
```

## Why it matters / Почему это важно

Instead of building one bespoke polling script per national service, a receiver can subscribe to one or more WIS2 Global Brokers, filter topics/metadata, and download the referenced payload. This is particularly valuable for global surface and upper-air observations.

Вместо десятков отдельных загрузчиков можно подписаться на WIS2 Global Broker, отфильтровать темы и получать канонические файлы. Для оперативных SYNOP/TEMP это должен быть один из первых вариантов приёма.

## TEMP / upper-air

Conceptual broad subscription:

```text
cache/a/wis2/+/data/core/weather/surface-based-observations/temp
```

Russian publisher path recorded in this repository:

```text
cache/a/wis2/ru-aviamettelecom/data/core/weather/surface-based-observations/temp
```

The exact topic tree and publisher metadata may evolve; always validate against current WIS2 discovery/metadata before hard-coding production rules.

## Recommended tools

- `wis2downloader` — ready receiver/downloader.
- `pywis-pubsub` — Python pub/sub building blocks.
- `ecCodes` — BUFR and GRIB decoding.
- `wis2box` — reference implementation/tooling for publishers and WIS2 workflows.

## Production checklist

1. Configure at least one Global Broker and, for critical operation, a fallback broker/cache.
2. Persist message ID/topic/publisher/canonical link and receive time.
3. Deduplicate notifications before downloading.
4. Validate content type/size and hash the payload.
5. Decode native meteorological data with a standards-aware decoder.
6. Monitor **freshness**, not only broker connectivity.
7. Do not assume all WIS2 data are anonymous: `core` is the preferred open operational class, while other data can have access policies.

## References

- WIS2 Guide: <https://wmo-im.github.io/wis2-guide/>
- wis2box documentation: <https://docs.wis2box.wis.wmo.int/>
- wis2downloader: <https://github.com/World-Meteorological-Organization/wis2downloader>
