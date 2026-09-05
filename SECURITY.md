# Security Policy / Политика безопасности

Weather Source is primarily a catalogue, documentation set and validation tooling, but security issues can still affect users who automate external downloads.

## Supported versions

Security fixes apply to the current `main` branch. Historical commits are not maintained as separate release lines.

## Reporting a vulnerability

Do **not** publish credentials, private provider tokens, cookies, signed URLs or other secrets in an issue.

If you find a vulnerability in repository code or CI configuration, use GitHub's private vulnerability reporting/security advisory mechanism for this repository when available. If private reporting is unavailable, open a minimal public issue that describes the affected component without publishing exploit details or secrets, so the maintainer can establish a private channel.

Для уязвимостей не публикуйте в issue ключи API, пароли, cookie, OAuth-токены, подписанные URL и иные секреты. По возможности используйте private vulnerability reporting GitHub.

## External provider security

Catalogue entries link to third-party meteorological services. Their security, authentication and availability are controlled by the respective providers. Before production deployment:

- verify the hostname against official provider documentation;
- use TLS verification; do not disable certificate checks in production;
- store API keys/tokens in environment variables or a secret store, never in the catalogue;
- apply provider rate limits and least-privilege credentials;
- validate downloaded content type/size before decoding;
- keep native decoders such as ecCodes, netCDF/HDF libraries and XML parsers updated;
- treat downloaded files and metadata as untrusted input.

## Health-check workflow

The scheduled endpoint checker uses only catalogue endpoints explicitly marked `healthcheck: true`, performs small streaming/range-style requests where possible and stores a JSON report as an Actions artifact. It is not intended to bypass authentication or probe restricted services.

## Scope

Incorrect meteorological values, stale provider data or scientific interpretation errors are normally data-quality issues rather than security vulnerabilities. Please report them using the normal issue templates unless they arise from code execution, credential exposure, injection, unsafe parsing or another security boundary failure.
