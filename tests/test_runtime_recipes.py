from __future__ import annotations

from weather_source.catalog import load_recipes, load_sources, validate_runtime_contract


def test_every_source_has_exactly_one_runtime_recipe() -> None:
    sources = load_sources()
    recipes = load_recipes()
    assert len(sources) == 47
    assert set(recipes) == set(sources)
    assert validate_runtime_contract() == []


def test_every_fallback_points_to_a_real_source() -> None:
    sources = load_sources()
    for source_id, recipe in load_recipes().items():
        fallback = recipe.get("fallback")
        if fallback:
            assert fallback in sources, f"{source_id}: unknown fallback {fallback}"
            assert fallback != source_id


def test_public_recipes_are_actually_executable() -> None:
    for source_id, recipe in load_recipes().items():
        if recipe["status"] != "public":
            continue
        assert recipe["adapter"] != "unavailable", source_id
        assert recipe.get("request"), source_id
        assert recipe.get("example_ru"), source_id


def test_known_2026_migrations_and_access_corrections_are_locked() -> None:
    recipes = load_recipes()

    russian_temp = recipes["ru-aviamettelecom-wis2-temp"]
    assert russian_temp["request"]["broker"] == "gb.wis.cma.cn"
    assert russian_temp["request"]["topic"].startswith(
        "cache/a/wis2/ru-aviamettelecom/data/core/weather/surface-based-observations/temp"
    )
    assert "wis2://" not in str(russian_temp)

    madis = recipes["noaa-madis"]
    assert madis["request"]["url"].startswith("https://madis-data.ncep.noaa.gov/")
    assert "ftp://" not in str(madis).lower()

    smhi = recipes["smhi-open-data"]
    assert "snow1g/version/1" in smhi["request"]["url"]
    assert "pmp3g/version/2" not in smhi["request"]["url"]

    nexrad = recipes["noaa-nexrad"]
    assert nexrad["request"]["bucket"] == "unidata-nexrad-level2"

    goes = recipes["noaa-goes"]
    assert goes["request"]["bucket"] == "noaa-goes19"

    nucaps = recipes["noaa-nucaps"]
    assert nucaps["status"] == "public"
    assert nucaps["request"]["bucket"] == "noaa-nesdis-n20-pds"

    eprofile = recipes["eumetnet-eprofile"]
    assert eprofile["status"] == "restricted"
    assert eprofile["adapter"] == "unavailable"

    arm = recipes["doe-arm-sonde"]
    assert arm["status"] == "credentials"
    assert arm["adapter"] == "unavailable"

    blitz = recipes["blitzortung"]
    assert blitz["status"] == "restricted"
    assert blitz["adapter"] == "unavailable"

    met_no = recipes["met-norway-api"]
    assert met_no["status"] == "public"
    assert "locationforecast/2.0" in met_no["request"]["url"]


def test_unique_provider_flows_perform_real_retrievals() -> None:
    recipes = load_recipes()

    ads_command = recipes["copernicus-ads"]["request"]["command"]
    assert ".retrieve(" in ads_command
    assert "cams-global-atmospheric-composition-forecasts" in ads_command

    marine_command = recipes["copernicus-marine"]["request"]["command"]
    assert "copernicusmarine.subset" in marine_command
    assert "start_datetime" in marine_command
    assert "end_datetime" in marine_command

    knmi_command = recipes["knmi-open-data"]["request"]["command"]
    assert "weather_source.providers knmi" in knmi_command

    nomads_command = recipes["noaa-nomads"]["request"]["command"]
    assert "weather_source.providers nomads-gfs" in nomads_command


def test_credentials_recipes_declare_required_environment() -> None:
    for source_id, recipe in load_recipes().items():
        if recipe["status"] == "credentials":
            assert recipe.get("env"), f"{source_id} requires credentials but declares no env variables"
