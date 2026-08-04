"""API HTTP mínima para receber e consultar telemetria do AI-CryoDiag."""
from __future__ import annotations

from collections import deque
from datetime import datetime, timezone
from typing import Deque

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="AI-CryoDiag API", version="0.1.0", description="API de telemetria sintética para desenvolvimento")
readings: Deque[TelemetryIn] = deque(maxlen=1000)


class TelemetryIn(BaseModel):
    tank_id: str = Field(min_length=1, max_length=64)
    pressure_bar: float = Field(ge=0, le=100)
    level_percent: float = Field(ge=0, le=100)
    temperature_c: float = Field(ge=-300, le=100)
    timestamp: datetime | None = None


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "ai-cryodiag-api"}


@app.get("/telemetry")
def list_telemetry(limit: int = 50) -> list[TelemetryIn]:
    limit = max(1, min(limit, 1000))
    return list(readings)[-limit:][::-1]


@app.post("/telemetry", status_code=201)
def ingest_telemetry(reading: TelemetryIn) -> TelemetryIn:
    if reading.timestamp is None:
        reading.timestamp = datetime.now(timezone.utc)
    readings.append(reading)
    return reading

