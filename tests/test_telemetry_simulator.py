from src.telemetry_simulator import generate_reading


def test_reading_has_expected_fields():
    reading = generate_reading("TEST-001", anomaly_rate=0)
    assert reading.tank_id == "TEST-001"
    assert reading.pressure_bar > 0
    assert 0 <= reading.level_percent <= 100
    assert reading.temperature_c < 0
    assert reading.anomaly is False


def test_anomaly_rate_one_generates_anomaly():
    reading = generate_reading("TEST-002", anomaly_rate=1)
    assert reading.anomaly is True

