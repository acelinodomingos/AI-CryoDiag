"""Publica telemetria no broker MQTT quando habilitado."""
from __future__ import annotations

import json
import os
from dataclasses import asdict

import paho.mqtt.client as mqtt

from src.telemetry_simulator import generate_reading


def publish_reading(host: str, port: int = 1883, topic: str = "ai-cryodiag/telemetry", tank_id: str = "TANK-001") -> None:
    """Publica uma leitura sintética; credenciais devem vir de variáveis de ambiente."""
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    username = os.getenv("MQTT_USERNAME")
    password = os.getenv("MQTT_PASSWORD")
    if username:
        client.username_pw_set(username, password)
    client.connect(host, port, keepalive=60)
    client.publish(topic, json.dumps(asdict(generate_reading(tank_id))), qos=1)
    client.disconnect()


if __name__ == "__main__":
    publish_reading(os.getenv("MQTT_HOST", "localhost"))

