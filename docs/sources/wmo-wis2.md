# WMO WIS 2.0 — практическое руководство / Practical guide

WIS 2.0 — основной современный слой распространения многих оперативных данных WMO. Для инженера важно воспринимать его не как «сайт с файлами», а как **событийную транспортную систему**: уведомление приходит через MQTT, а само метеосообщение/файл скачивается по HTTPS-ссылке из WIS2 Notification Message.

---

## 🇷🇺 Русский

### Что такое WIS2

WMO Information System 2.0 (WIS2) заменяет старую логику, где потребитель был вынужден знать десятки национальных FTP/HTTP-каталогов и регулярно их опрашивать. В WIS2 публикация новых данных порождает уведомление. Получатель подписывается на нужные темы, получает метаданные и ссылку на payload, после чего загружает фактические BUFR/GRIB2/NetCDF/другие данные.

```text
WIS2 Global Broker (MQTT)
        │
        ▼
WIS2 Notification Message
metadata + topic + id + links
        │
        ├── canonical HTTPS URL
        └── Global Cache HTTPS URL
                 │
                 ▼
        BUFR / GRIB2 / NetCDF / ...
                 │
                 ▼
        ecCodes / xarray / decoder
```

### Зачем использовать

WIS2 особенно полезен, когда требуется:

- глобальный оперативный приём наблюдений;
- TEMP/радиозонды и другие upper-air сообщения;
- SYNOP и другие наземные наблюдения;
- данные нескольких национальных центров через единый механизм;
- событийный приём без постоянного сканирования каталогов;
- резервирование через несколько Global Broker/Global Cache.

Для новой автоматизированной системы WIS2 следует проверять **до** написания отдельного scraper/downloader под сайт конкретной метеослужбы.

### Классы данных и права

WIS2 транспортирует разные классы данных. Для публичной автоматизации наиболее интересны **core data**, распространяемые в рамках WMO Unified Data Policy. Нельзя предполагать, что абсолютно любой WIS2 topic доступен анонимно: права определяются классом данных и политикой publisher.

### Как подписываться

Широкая концептуальная тема TEMP:

```text
cache/a/wis2/+/data/core/weather/surface-based-observations/temp
```

Зафиксированный в каталоге российский publisher:

```text
cache/a/wis2/ru-aviamettelecom/data/core/weather/surface-based-observations/temp
```

Тема является инженерным ориентиром, а не строкой «навсегда»: перед production-деплоем нужно проверить текущий topic hierarchy, discovery metadata и publisher в WIS2.

### Что приходит в MQTT

MQTT несёт **не обязательно сам бинарный BUFR**, а WIS2 Notification Message. В нём нужно сохранять минимум:

- уникальный идентификатор уведомления/сообщения;
- topic;
- publisher;
- время публикации и время приёма;
- canonical link;
- cache link, если присутствует;
- media/content type;
- checksum/size, если предоставляются.

После дедупликации payload скачивается по HTTPS.

### Рекомендуемый стек

| Задача | Инструмент |
|---|---|
| Готовый WIS2 consumer/downloader | `wis2downloader` |
| Python pub/sub | `pywis-pubsub` |
| MQTT | `paho-mqtt` |
| BUFR и GRIB | ECMWF `ecCodes` |
| GRIB → xarray | `cfgrib` |
| NetCDF | `xarray`, `netCDF4` |
| Publisher/reference stack | `wis2box` |

### Production-пайплайн

1. Выбрать Global Broker и резервный broker/cache.
2. Подписаться только на нужные topic subtree, а не на весь WIS2 без фильтрации.
3. Валидировать WIS2 Notification Message.
4. Дедуплицировать по message/id/topic/payload identity.
5. Скачать canonical/cache payload.
6. Сохранить raw-файл неизменным.
7. Декодировать нативным WMO-aware декодером.
8. Нормализовать данные в собственную схему.
9. Контролировать **freshness**, а не только MQTT connection state.
10. Сигнализировать, если ожидаемый поток перестал обновляться.

### Что мониторить

Проверка «TCP/MQTT соединение живо» недостаточна. Для эксплуатации нужны метрики:

- `last_notification_time`;
- `last_payload_time`;
- `publisher_delay`;
- число сообщений/час;
- процент ошибок скачивания;
- процент ошибок BUFR/GRIB decoding;
- дубликаты;
- пропуски ожидаемых station/product cycles.

### Российская аэрология

Для радиозондов России в этой базе основным глобальным машинным маршрутом считается WIS2 TEMP. Отдельная запись каталога `ru-aviamettelecom-wis2-temp` фиксирует российский publisher. Для независимого контроля полноты следует использовать IGRA/Wyoming/другие архивно-агрегирующие каналы, но не подменять ими WIS2 в новой оперативной архитектуре без причины.

### Минимальная архитектура

```text
MQTT consumer
    │
    ├── notification store
    ├── dedup queue
    │
    ▼
HTTPS downloader
    │
    ├── raw archive
    ▼
decoder workers
    │
    ├── BUFR → normalized observations
    ├── GRIB2 → fields
    └── NetCDF → arrays
    │
    ▼
DB / object store / API
```

### Частые ошибки

- считать MQTT payload самим BUFR без разбора notification schema;
- жёстко прошивать один broker и не иметь fallback;
- скачивать одинаковый payload после повторных уведомлений;
- не сохранять raw данные;
- проверять доступность broker, но не свежесть продукта;
- путать topic discovery с постоянным контрактом;
- считать все WIS2 datasets анонимными/open;
- интерпретировать TEMP как модельный вертикальный профиль — TEMP является наблюдением.

### Официальные ресурсы

- WIS2 Guide: <https://wmo-im.github.io/wis2-guide/>
- wis2box: <https://docs.wis2box.wis.wmo.int/>
- wis2downloader: <https://github.com/World-Meteorological-Organization/wis2downloader>
- pywis-pubsub: <https://github.com/World-Meteorological-Organization/pywis-pubsub>

---

## 🇬🇧 English

### What WIS2 is

WMO Information System 2.0 is an event-driven dissemination layer for operational WMO data. Consumers subscribe to MQTT topics, receive WIS2 Notification Messages and retrieve the actual meteorological payload from canonical/cache HTTPS links.

### Why it matters

It removes the need to build and continuously poll one bespoke downloader per national service. WIS2 is especially valuable for global surface and upper-air observations and for systems that need a uniform event-driven transport with broker/cache redundancy.

### Typical flow

1. Select a Global Broker and a fallback broker/cache.
2. Subscribe to the smallest useful topic subtree.
3. Validate and persist each notification.
4. Deduplicate before downloading.
5. Fetch the canonical/cache payload over HTTPS.
6. Preserve the raw payload.
7. Decode BUFR/GRIB/NetCDF with standards-aware tools.
8. Normalize into an internal schema.
9. Monitor data freshness and expected product/station cycles.

### TEMP example

Conceptual broad TEMP subscription:

```text
cache/a/wis2/+/data/core/weather/surface-based-observations/temp
```

Russian publisher recorded by this repository:

```text
cache/a/wis2/ru-aviamettelecom/data/core/weather/surface-based-observations/temp
```

Always validate current discovery metadata and topic hierarchy before hard-coding production subscriptions.

### Recommended software

- `wis2downloader` — ready consumer/downloader;
- `pywis-pubsub` — WIS2 pub/sub utilities;
- `paho-mqtt` — MQTT client;
- `ecCodes` — BUFR/GRIB decoder;
- `cfgrib`/`xarray` — GRIB array access;
- `wis2box` — reference publisher/tooling stack.

### Agent rule

For operational WMO observations, an agent should check WIS2 core availability before recommending a national HTML/FTP workaround. The authoritative source records are `wmo-wis2` and the relevant publisher-specific entries in `catalog/sources.json`.
