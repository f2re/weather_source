# Aerology / Аэрология

Aerology in this repository is deliberately split into different observing technologies. A radiosonde, an aircraft profile, a radar wind profiler and a satellite retrieval are not interchangeable even when all produce a vertical profile.

## Recommended operational stack / Рекомендуемый оперативный стек

| Priority | Source family | Role |
|---|---|---|
| 1 | **WIS2 TEMP/BUFR** | Primary global operational radiosonde transport. |
| 1 | **Russian WIS2 TEMP publisher** | Primary path for Russian upper-air observations where published. |
| 2 | **NOAA IGRA 2** | Independent near-real-time/historical fallback and archive. |
| 2 | **DWD/FMI/Météo-France/MeteoSwiss/ECCC** | National independent feeds and regional detail. |
| 3 | **EUMETNET E-PROFILE** | Frequent wind-profiler/radar VWP/lidar profiles between radiosonde launches. |
| 3 | **AMDAR/aircraft** | High-frequency ascent/descent and en-route temperature/wind observations; access rights vary. |
| 4 | **GNSS-RO / UCAR CDAAC, GRAS** | Global satellite-derived refractivity/temperature/moisture profile information. |
| 4 | **IASI/NUCAPS-type retrievals** | Satellite thermodynamic retrievals; useful coverage but not in-situ soundings. |
| 5 | **GRUAN** | Reference-quality validation, corrections and uncertainty work. |

## Radiosonde/TEMP data model

A normalized profile should retain at least:

```text
source_id
wigos_id / station_id
launch_time
observation_time
received_time
level_index
pressure_hpa
geopotential_height_m
geometric_height_m
temperature_c
dewpoint_c
relative_humidity_pct
wind_direction_deg
wind_speed_ms
u_ms / v_ms
latitude / longitude
sonde_type
qc_flags
raw_message_id / raw_object
```

Do not discard the native pressure/significant-level structure merely to force every sounding onto fixed model levels.

## Russia / Россия

The catalogue records the WIS2 topic path used for Russian TEMP publication in the WIS2 ecosystem:

```text
cache/a/wis2/ru-aviamettelecom/data/core/weather/surface-based-observations/temp
```

Production code should discover/verify active publisher metadata and should not rely on University of Wyoming as the sole real-time source. IGRA and Wyoming are valuable as independent fallback/archive paths.

## Decoding

For BUFR, use **ecCodes** with current WMO tables. Keep the original BUFR object so it can be re-decoded after table/library updates. For simple provider CSV (for example some national sounding products), retain the original provider columns and units in metadata even after normalization.

## Quality control

Basic automated checks should include:

- monotonic/physically plausible pressure progression with explicit handling of missing levels;
- unit and range checks for T/RH/wind/geopotential;
- duplicate launch/message detection;
- launch time vs receive time and source freshness;
- station identifier/location consistency;
- provider QC flags without silently overwriting them;
- explicit provenance when merging supplements such as AMDAR or profiler data.

Satellite retrievals and model profiles must carry a distinct `observation_type` so downstream software cannot accidentally label them as radiosondes.
