from __future__ import annotations

import math
import re
from typing import Optional, Tuple, Literal

import pandas as pd


DimensionUnit = Literal["mm", "inch"]
ParseMode = Literal["single", "range_min", "range_max", "range_avg"]


INCH_TO_MM = 25.4


def _parse_fraction_to_float(s: str) -> Optional[float]:
    """
    Parse strings like '3/16' into a float.
    Returns None if it cannot be parsed.
    """
    s = s.strip()
    if "/" not in s:
        return None
    try:
        num, den = s.split("/", 1)
        return float(num) / float(den)
    except Exception:
        return None


def _extract_numeric_tokens(raw: str) -> list[float]:
    """
    Extract numeric tokens (integers, floats, simple fractions) from a string.
    Returns a list of numeric values.
    """
    s = str(raw)

    # Find fraction tokens first
    fraction_tokens = re.findall(r"\d+\s*/\s*\d+", s)
    numbers: list[float] = []

    for tok in fraction_tokens:
        val = _parse_fraction_to_float(tok)
        if val is not None:
            numbers.append(val)

    # Remove fractions so they don't interfere with float/int search
    s_no_frac = re.sub(r"\d+\s*/\s*\d+", " ", s)

    # Find floats/ints
    for tok in re.findall(r"[-+]?\d*\.?\d+", s_no_frac):
        try:
            numbers.append(float(tok))
        except Exception:
            continue

    return numbers


def _detect_unit(raw: str) -> Optional[DimensionUnit]:
    s = str(raw).lower()
    if "mm" in s:
        return "mm"
    if "in" in s or "inch" in s:
        return "inch"
    return None


def parse_dimension_raw(
    raw: str,
    mode: ParseMode = "single",
    target_unit: DimensionUnit = "mm",
) -> Tuple[Optional[float], Optional[DimensionUnit]]:
    """
    Parse a raw dimensional string into a numeric value and unit.

    Parameters
    ----------
    raw : str
        Raw string, e.g. "8.000 in.", "3/16 in", "75 mm", "4 to 6 in".
    mode : {"single", "range_min", "range_max", "range_avg"}
        How to handle multiple numbers / ranges:
          - single: first number
          - range_min: min of numbers
          - range_max: max of numbers
          - range_avg: average of numbers
    target_unit : {"mm", "inch"}
        Output unit.

    Returns
    -------
    (value, unit)
        value: float in target_unit, or None if parsing failed
        unit: detected original unit ("mm" or "inch") or None
    """
    if raw is None or (isinstance(raw, float) and math.isnan(raw)):
        return None, None

    numbers = _extract_numeric_tokens(str(raw))
    if not numbers:
        return None, None

    unit = _detect_unit(str(raw)) or target_unit

    if mode == "range_min":
        base_val = min(numbers)
    elif mode == "range_max":
        base_val = max(numbers)
    elif mode == "range_avg":
        base_val = sum(numbers) / len(numbers)
    else:
        base_val = numbers[0]

    # Convert to target_unit
    val = base_val
    if unit == "inch" and target_unit == "mm":
        val = base_val * INCH_TO_MM
    elif unit == "mm" and target_unit == "inch":
        val = base_val / INCH_TO_MM

    return val, unit


def parse_dimension_series(
    series: pd.Series,
    mode: ParseMode = "single",
    target_unit: DimensionUnit = "mm",
) -> pd.DataFrame:
    """
    Parse a Series of raw dimension strings into a DataFrame with:
      - raw_value
      - value_<target_unit>
      - original_unit
    """
    records = []
    for raw in series:
        value, orig_unit = parse_dimension_raw(raw, mode=mode, target_unit=target_unit)
        records.append(
            {
                "raw_value": raw,
                f"value_{target_unit}": value,
                "original_unit": orig_unit,
            }
        )
    return pd.DataFrame(records)