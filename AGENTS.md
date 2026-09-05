# AGENTS.md

Weather Source is a knowledge base for humans and software/AI agents. The authoritative machine-readable source is `catalog/sources.yaml`; prose documentation explains it but must not override it.

## Source selection rules

1. Prefer `official: true` and `tier: primary` entries.
2. For operational systems prefer `operational: true`, machine-accessible protocols and stable provider endpoints.
3. Prefer event-driven or object/file APIs (WIS2 MQTT+HTTPS, AMQP, HTTPS, S3/object storage, REST, WFS/WCS) over scraping rendered maps or HTML pages.
4. Do not infer availability from a provider name. Read `access.level`, `access.auth`, `endpoints`, `formats`, `coverage`, `latency`, `update_cadence`, `archive`, `terms` and `status`.
5. Treat `registration` and `free-tier` as free but not anonymous. Treat `restricted` as unusable for unattended public deployment unless credentials/rights are explicitly available.
6. When two equivalent official feeds exist, prefer the one with a protocol designed for automation and keep the second as fallback.
7. For BUFR/GRIB/NetCDF/HDF payloads, preserve raw source files when practical. Normalization should be additive, not destructive.
8. For WMO data, prefer WIS2 core data when available. Subscribe to notifications and download the canonical payload instead of repeatedly polling web pages.
9. For upper-air observations, distinguish real radiosonde/TEMP observations from model profiles, satellite retrievals and aircraft-derived profiles.
10. Never describe a forecast-model profile as a radiosonde observation.

## Reliability policy

- `tier: primary` — recommended direct operational source.
- `tier: secondary` — independent fallback, archive or regional alternative.
- `tier: specialized` — useful for a narrower observation type or workflow.
- `tier: aggregator` — convenient non-primary service; never the sole source in a critical pipeline.

`status` reflects the repository's last review, not a guarantee of permanent availability. Before deployment, run `scripts/check_endpoints.py` for the selected sources.

## Adding or changing a source

A source change should include:

- unique stable `id`;
- provider and bilingual name/summary;
- categories and geographic coverage;
- operational flag, update cadence and typical latency;
- access level, authentication and licence/terms notes;
- at least one official documentation URL;
- machine endpoint(s), with health-check metadata where safe;
- formats and decoders/software;
- source card link;
- `last_verified` date.

Run:

```bash
python scripts/validate_catalog.py
python scripts/generate_docs.py --check
pytest -q
```

## Retrieval examples

### Need global upper-air observations

Filter for `categories` containing `upper-air`, `operational: true`, then prefer WIS2/TEMP entries. Use IGRA/Wyoming as independent fallback/archive paths, not as the primary global real-time transport when WIS2 is available.

### Need global NWP

Filter `categories` for `nwp` or `ensemble`, then compare coverage, latency, update cycle, forecast horizon, grid, formats and access protocol. Prefer direct official object/HTTP/API feeds.

### Need radar

Filter `radar`, then inspect whether the endpoint is raw volume, national composite, image-only, WMS/WCS or object storage. Do not treat a rendered PNG viewer as equivalent to raw radar data.

## Documentation language

Catalogue text should carry both `en` and `ru`. Source cards may be bilingual in one file. Technical identifiers, WMO codes, protocol names and official product names should not be translated when translation would create ambiguity.

## Safety and load

Health checks must be lightweight. Do not download large model/satellite/radar files merely to test availability. Use a catalogue or metadata endpoint, HEAD/range request, small index object or provider status endpoint where possible. Respect documented rate limits.
