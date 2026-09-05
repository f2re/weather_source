# Contributing / Участие в проекте

Weather Source is maintained as an operational reference. Accuracy, provenance and reproducibility are more important than the raw number of links.

## What to contribute / Что добавлять

Useful contributions include:

- a new official meteorological source or machine endpoint;
- a changed/retired endpoint, protocol or authentication flow;
- corrected update cadence, latency, archive depth, format or licence information;
- a decoder/client example;
- an independent fallback for an operational data family;
- a reproducible health/freshness check;
- Russian or English documentation improvements.

Полезны новые официальные источники, исправления endpoint'ов и условий доступа, уточнение периодичности/задержки/архива, рабочие декодеры и клиенты, резервные каналы и улучшения русской/английской документации.

## Source record requirements / Требования к записи

Every catalogue source must include:

1. stable `id`;
2. provider and bilingual `name`, `summary`, `notes`;
3. categories and geographic coverage;
4. operational flag, update cadence and typical latency;
5. archive description;
6. access level, authentication and terms/licence notes;
7. protocols and native/served formats;
8. at least one endpoint;
9. official/reference documentation;
10. recommended software/decoder where known;
11. reliability and automation assessment;
12. `last_verified` date.

Prefer official machine endpoints over visual web pages. An aggregator must be marked `tier: aggregator` and `official: false`.

## Health checks / Проверка доступности

Set `healthcheck: true` only for a lightweight HTTP(S) endpoint that can be probed without downloading a large model, radar or satellite payload. A status/catalog/index endpoint is preferable.

Do not confuse:

- endpoint availability;
- product freshness;
- successful meteorological decoding.

The repository's scheduled workflow checks endpoint availability. Product-specific freshness/decoder checks may be added when they remain lightweight and stable.

## Development workflow

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_catalog.py
python scripts/generate_docs.py --check
python -m compileall examples scripts tests
pytest -q
python scripts/generate_docs.py --write
mkdocs build --strict
```

For an optional live check:

```bash
python scripts/check_endpoints.py --tier primary --retries 2 --report source-health.json
```

Do not commit generated `site/`, temporary data files, API keys, cookies or provider credentials.

## Pull requests

Keep changes scoped. Explain:

- what source/product changed;
- why it is useful;
- how access was verified;
- whether authentication or rate limits apply;
- whether the change affects existing source IDs or automation.

A source record should remain readable by both humans and software agents. Avoid marketing descriptions; document the actual engineering interface.

## Language

Technical identifiers, WMO codes, product names, API paths and protocol names should remain exact. Human-readable description should be available in both English and Russian when the catalogue schema requires it.

## Licence

By contributing, you agree that your original code/documentation contributions are provided under the repository's MIT License. External meteorological data remain subject to their providers' own licences and terms.