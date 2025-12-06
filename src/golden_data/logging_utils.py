from __future__ import annotations

import logging
from pathlib import Path

from .config import BASE_DIR


def get_normalization_logger(name: str = "golden_data.normalization") -> logging.Logger:
    """
    Return a logger configured for normalization / mapping work.

    Logs go both to console and to a file under BASE_DIR / "logs".
    """
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger  # already configured

    logger.setLevel(logging.INFO)

    log_dir = BASE_DIR / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "normalization.log"

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch_formatter = logging.Formatter("[%(levelname)s] %(message)s")
    ch.setFormatter(ch_formatter)

    # File handler
    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setLevel(logging.INFO)
    fh_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    fh.setFormatter(fh_formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger


def log_normalization_event(
    logger: logging.Logger,
    field_name: str,
    raw_value: str,
    normalized_value: str,
    mapping_source: str,
    status: str = "normalized",
):
    """
    Helper to write a standard normalization log line.

    status: "normalized", "unmapped", "skipped", etc.
    """
    logger.info(
        "field=%s status=%s raw='%s' normalized='%s' mapping='%s'",
        field_name,
        status,
        raw_value,
        normalized_value,
        mapping_source,
    )