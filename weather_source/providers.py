from __future__ import annotations

import argparse
import ftplib
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urljoin

import requests

USER_AGENT = "weather-source/0.1 (+https://github.com/f2re/weather_source)"


def _output(default: str) -> Path:
    path = Path(os.environ.get("WEATHER_SOURCE_OUTPUT", default))
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def _download(url: str, path: Path, *, headers: dict[str, str] | None = None, timeout: float = 30.0) -> Path:
    merged = {"User-Agent": USER_AGENT}
    if headers:
        merged.update(headers)
    with requests.get(url, headers=merged, timeout=timeout, stream=True) as response:
        response.raise_for_status()
        with path.open("wb") as fh:
            for chunk in response.iter_content(1024 * 256):
                if chunk:
                    fh.write(chunk)
    print(path)
    return path


def aemet() -> Path:
    key = os.environ.get("AEMET_API_KEY")
    if not key:
        raise RuntimeError("Задайте AEMET_API_KEY")
    endpoint = "https://opendata.aemet.es/opendata/api/observacion/convencional/todas"
    response = requests.get(endpoint, params={"api_key": key}, headers={"User-Agent": USER_AGENT}, timeout=30)
    response.raise_for_status()
    metadata = response.json()
    data_url = metadata.get("datos")
    if not data_url:
        raise RuntimeError(f"AEMET не вернул поле datos: {metadata}")
    return _download(data_url, _output("aemet-observations.json"))


def knmi() -> Path:
    key = os.environ.get("KNMI_API_KEY")
    if not key:
        raise RuntimeError("Задайте KNMI_API_KEY (registered или актуальный anonymous key)")
    base = "https://api.dataplatform.knmi.nl/open-data/v1"
    dataset = "10-minute-in-situ-meteorological-observations"
    version = "1.0"
    headers = {"Authorization": key, "User-Agent": USER_AGENT}
    listing = requests.get(
        f"{base}/datasets/{dataset}/versions/{version}/files",
        params={"maxKeys": 1, "orderBy": "created", "sorting": "desc"},
        headers=headers,
        timeout=30,
    )
    listing.raise_for_status()
    files = listing.json().get("files", [])
    if not files:
        raise RuntimeError("KNMI API не вернул файлов")
    filename = files[0]["filename"]
    link = requests.get(
        f"{base}/datasets/{dataset}/versions/{version}/files/{filename}/url",
        headers=headers,
        timeout=30,
    )
    link.raise_for_status()
    download_url = link.json()["temporaryDownloadUrl"]
    return _download(download_url, _output(filename))


def meteofrance_synop() -> Path:
    now = datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0)
    hour = (now.hour // 3) * 3
    candidate = now.replace(hour=hour)
    base = "https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/"
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})
    last_error: str | None = None
    for offset in range(0, 8):
        term = candidate - timedelta(hours=3 * offset)
        filename = f"synop.{term:%Y%m%d%H}.csv"
        url = urljoin(base, filename)
        response = session.get(url, timeout=20)
        if response.status_code == 200 and len(response.content) > 100:
            path = _output(filename)
            path.write_bytes(response.content)
            print(path)
            return path
        last_error = f"{response.status_code} {url}"
    raise RuntimeError(f"Не найден ни один из последних SYNOP-сроков Météo-France: {last_error}")


def nomads_gfs() -> Path:
    now = datetime.now(timezone.utc)
    cycles = [18, 12, 6, 0]
    candidates: list[tuple[datetime, int]] = []
    for day_offset in (0, 1):
        date = (now - timedelta(days=day_offset)).date()
        for cycle in cycles:
            dt = datetime(date.year, date.month, date.day, cycle, tzinfo=timezone.utc)
            if dt <= now:
                candidates.append((dt, cycle))
    candidates.sort(reverse=True)
    endpoint = "https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl"
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})
    errors: list[str] = []
    for dt, cycle in candidates[:6]:
        params = {
            "file": f"gfs.t{cycle:02d}z.pgrb2.0p25.f000",
            "lev_2_m_above_ground": "on",
            "var_TMP": "on",
            "subregion": "",
            "leftlon": 29,
            "rightlon": 31,
            "toplat": 61,
            "bottomlat": 59,
            "dir": f"/gfs.{dt:%Y%m%d}/{cycle:02d}/atmos",
        }
        response = session.get(endpoint, params=params, timeout=30)
        ctype = response.headers.get("Content-Type", "")
        if response.status_code == 200 and len(response.content) > 1000 and "text/html" not in ctype:
            filename = f"gfs-{dt:%Y%m%d}-{cycle:02d}-t2m.grib2"
            path = _output(filename)
            path.write_bytes(response.content)
            print(path)
            return path
        errors.append(f"{dt:%Y%m%d%H}: HTTP {response.status_code}, {len(response.content)} bytes")
    raise RuntimeError("NOMADS GFS не отдал ни один из последних циклов: " + "; ".join(errors))


def meteostat_bulk() -> Path:
    year = datetime.now(timezone.utc).year - 1
    url = f"https://data.meteostat.net/hourly/{year}.parquet"
    return _download(url, _output(f"meteostat-hourly-{year}.parquet"), timeout=60)


def meteoswiss_stac() -> Path:
    collection = "ch.meteoschweiz.ogd-smn"
    items_url = f"https://data.geo.admin.ch/api/stac/v1/collections/{collection}/items"
    response = requests.get(items_url, params={"limit": 1}, headers={"User-Agent": USER_AGENT}, timeout=30)
    response.raise_for_status()
    payload = response.json()
    features = payload.get("features", [])
    if not features:
        raise RuntimeError("MeteoSwiss STAC collection не вернула items")
    assets = features[0].get("assets", {})
    href = next((asset.get("href") for asset in assets.values() if asset.get("href")), None)
    if not href:
        raise RuntimeError("MeteoSwiss STAC item не содержит downloadable asset")
    name = Path(href.split("?", 1)[0]).name or "meteoswiss-data.bin"
    return _download(href, _output(name))


def cdaac_avnprf() -> Path:
    base = "https://data.cosmic.ucar.edu/gnss-ro/cosmic2/nrt/level2/"
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})
    now = datetime.now(timezone.utc)
    errors: list[str] = []
    for offset in range(1, 8):
        day = now - timedelta(days=offset)
        day_url = f"{base}{day:%Y}/{day:%j}/"
        response = session.get(day_url, timeout=20)
        if response.status_code != 200:
            errors.append(f"{day:%Y-%j}: HTTP {response.status_code}")
            continue
        match = re.search(r'href=["\'](avnPrf_nrt_[^"\']+\.tar\.gz)["\']', response.text)
        if not match:
            errors.append(f"{day:%Y-%j}: avnPrf отсутствует")
            continue
        filename = match.group(1)
        return _download(urljoin(day_url, filename), _output(filename), timeout=120)
    raise RuntimeError("Не найден свежий COSMIC-2 avnPrf: " + "; ".join(errors))


def jaxa_gsmap() -> Path:
    host = os.environ.get("JAXA_GSMAP_HOST")
    user = os.environ.get("JAXA_GSMAP_USER")
    password = os.environ.get("JAXA_GSMAP_PASSWORD")
    if not all((host, user, password)):
        raise RuntimeError("Задайте JAXA_GSMAP_HOST, JAXA_GSMAP_USER и JAXA_GSMAP_PASSWORD из письма GSMaP registration")
    remote_dir = "/now/latest/"
    with ftplib.FTP(host, timeout=30) as ftp:
        ftp.login(user=user, passwd=password)
        names = ftp.nlst(remote_dir)
        candidates = sorted(name for name in names if name.endswith(".dat.gz"))
        if not candidates:
            raise RuntimeError(f"В {remote_dir} нет GSMaP .dat.gz файлов")
        remote = candidates[-1]
        path = _output(Path(remote).name)
        with path.open("wb") as fh:
            ftp.retrbinary(f"RETR {remote}", fh.write)
    print(path)
    return path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Source-specific retrieval flows used by runtime recipes")
    parser.add_argument(
        "provider",
        choices=[
            "aemet",
            "knmi",
            "meteofrance-synop",
            "nomads-gfs",
            "meteostat-bulk",
            "meteoswiss-stac",
            "cdaac-avnprf",
            "jaxa-gsmap",
        ],
    )
    args = parser.parse_args(argv)
    try:
        {
            "aemet": aemet,
            "knmi": knmi,
            "meteofrance-synop": meteofrance_synop,
            "nomads-gfs": nomads_gfs,
            "meteostat-bulk": meteostat_bulk,
            "meteoswiss-stac": meteoswiss_stac,
            "cdaac-avnprf": cdaac_avnprf,
            "jaxa-gsmap": jaxa_gsmap,
        }[args.provider]()
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
