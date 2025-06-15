"""Simulated DB writer for test environments."""

import logging
from typing import Any

logger = logging.getLogger(__name__)


def write_to_postgres(data: dict[str, Any]) -> None:
    """Simulate writing data to Postgres (no-op for test)."""
    logger.info("📦 [TEST] Would write to Postgres: %s", data)


def write_to_influx(data: dict[str, Any]) -> None:
    """Simulate writing data to InfluxDB (no-op for test)."""
    logger.info("📦 [TEST] Would write to InfluxDB: %s", data)
