#!/usr/bin/env python3
"""Subscribe to a WIS2-compatible MQTT broker and print notification messages.

The broker hostname, credentials and topic are intentionally supplied at runtime because
WIS2 Global Broker endpoints and access details must be taken from current WMO metadata.
This example consumes notifications only; download referenced payloads in a separate,
auditable HTTPS step.
"""
from __future__ import annotations

import argparse
import json
import ssl

import paho.mqtt.client as mqtt


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", required=True, help="MQTT broker hostname")
    parser.add_argument("--port", type=int, default=8883)
    parser.add_argument("--topic", required=True, help="WIS2 topic filter, e.g. cache/a/wis2/+/data/core/#")
    parser.add_argument("--username")
    parser.add_argument("--password")
    parser.add_argument("--client-id", default="weather-source-example")
    parser.add_argument("--no-tls", action="store_true", help="disable TLS only for a trusted test broker")
    args = parser.parse_args()

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=args.client_id)
    if args.username:
        client.username_pw_set(args.username, args.password)
    if not args.no_tls:
        client.tls_set(cert_reqs=ssl.CERT_REQUIRED)

    def on_connect(client: mqtt.Client, userdata, flags, reason_code, properties) -> None:
        if reason_code != 0:
            raise RuntimeError(f"MQTT connection failed: {reason_code}")
        print(f"connected; subscribing to {args.topic}")
        client.subscribe(args.topic, qos=1)

    def on_message(client: mqtt.Client, userdata, message: mqtt.MQTTMessage) -> None:
        text = message.payload.decode("utf-8", errors="replace")
        try:
            payload = json.loads(text)
        except json.JSONDecodeError:
            payload = text
        print(json.dumps({"topic": message.topic, "payload": payload}, ensure_ascii=False, indent=2))

    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(args.host, args.port, keepalive=60)
    client.loop_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
