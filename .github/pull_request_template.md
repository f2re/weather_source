## What changed / Что изменено

<!-- Describe the source, code or documentation change. -->

## Verification / Проверка

- [ ] `python scripts/validate_catalog.py`
- [ ] `python scripts/generate_docs.py --check`
- [ ] `python -m compileall examples scripts tests`
- [ ] `pytest -q`
- [ ] If relevant, the official endpoint/documentation was checked manually.

## Source changes / Изменения источников

If this PR adds or changes a meteorological source:

- **Provider / Поставщик:**
- **Official documentation / Документация:**
- **Protocol(s):**
- **Format(s):**
- **Authentication / Авторизация:**
- **Typical update/latency / Периодичность и задержка:**
- **Licence/terms / Лицензия и условия:**
- **Fallback impact / Влияние на резервирование:**

## Checklist

- [ ] The source ID is stable and unique.
- [ ] English and Russian catalogue text is present.
- [ ] Primary sources are official; aggregators are clearly marked.
- [ ] No credentials, cookies, signed URLs or private data are committed.
- [ ] Health checks are lightweight and do not download large payloads.
- [ ] Raw/model/satellite/radiosonde product classes are described without conflation.
