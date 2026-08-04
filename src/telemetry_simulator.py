"""Simulador de telemetria sintética do AI-CryoDiag."""
from __future__ import annotations

import argparse
import json
import random
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone


@dataclass
class Telemetry:
    tank_id: str
    timestamp: str
    pressure_bar: float
    level_percent: float
    temperature_c: float
    anomaly: bool = False


def generate_reading(tank_id: str = "TANK-001", anomaly_rate: float = 0.05) -> Telemetry:
    """Gera uma leitura sintética sem acessar equipamentos reais."""
    anomaly = random.random() < anomaly_rate
    if anomaly:
        pressure = random.uniform(2.0, 24.5)
        level = random.uniform(5.0, 98.0)
        temperature = random.uniform(-210.0, -130.0)
    else:
        pressure = random.gauss(12.0, 0.8)
        level = min(100.0, max(0.0, random.gauss(68.0, 2.5)))
        temperature = random.gauss(-183.0, 3.0)
    return Telemetry(tank_id, datetime.now(timezone.utc).isoformat(), round(pressure, 3), round(level, 3), round(temperature, 3), anomaly)


def main() -> None:
    parser = argparse.ArgumentParser(description="Gera telemetria sintética")
    parser.add_argument("--tank-id", default="TANK-001")
    parser.add_argument("--count", type=int, default=10)
    parser.add_argument("--interval", type=float, default=0.0)
    parser.add_argument("--anomaly-rate", type=float, default=0.05)
    args = parser.parse_args()
    if args.count < 1 or not 0 <= args.anomaly_rate <= 1:
        parser.error("count deve ser positivo e anomaly-rate deve estar entre 0 e 1")
    for _ in range(args.count):
        print(json.dumps(asdict(generate_reading(args.tank_id, args.anomaly_rate)), ensure_ascii=False))
        if args.interval > 0:
            time.sleep(args.interval)


if __name__ == "__main__":
    main()

