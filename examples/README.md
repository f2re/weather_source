# Examples / Примеры

These examples are intentionally small building blocks. They demonstrate transport and decoding patterns without hiding provider semantics behind a large framework.

- `python/http_download.py` — bounded streaming HTTPS download with a stable User-Agent.
- `python/wis2_subscribe.py` — MQTT/WIS2 notification subscription skeleton; downloads are deliberately left to a separate HTTP step.
- `python/bufr_decode.py` — inspect BUFR keys using ecCodes Python bindings.
- `python/grib_open.py` — open GRIB2 with cfgrib/xarray.
- `python/netcdf_open.py` — inspect NetCDF with xarray without loading the whole dataset into memory.

CI compiles all examples and unit-tests the repository's catalogue helpers. Examples that require provider credentials or large native libraries are not executed against external services on every pull request. Scheduled `source-health.yml` performs lightweight network checks separately.

## Typical environment

```bash
python -m venv .venv
. .venv/bin/activate
pip install requests paho-mqtt xarray cfgrib eccodes
```

System packages may be required for native ecCodes/netCDF/HDF support depending on your platform.

Перед переносом примера в production добавьте structured logging, retries/backoff, raw-file persistence, checksum, freshness monitoring and provider-specific rate-limit handling.
