from __future__ import annotations

import re
from typing import Literal

import pandas as pd


PatternLabel = Literal[
    "mm",
    "inch",
    "fraction",
    "range",
    "numeric_only",
    "other",
]


def classify_unit_pattern(value: str) -> PatternLabel:
    """
    Classify a raw dimensional string into a simple pattern label.

    Examples:
      "8.000 in."       -> "inch"
      "75 mm"           -> "mm"
      "3/16 in"         -> "fraction"
      "4 to 6 in"       -> "range"
      "12"              -> "numeric_only"
      "approx. 10 long" -> "other"
    """
    if value is None:
        return "other"

    s = str(value).strip()

    # mm
    if re.search(r"\bmm\b", s, flags=re.IGNORECASE):
        return "mm"

    # inches
    if re.search(r"\b(in\.?|inch(?:es)?)\b", s, flags=re.IGNORECASE):
        return "inch"

    # simple fraction, e.g. "3/16"
    if re.match(r"^\s*\d+\s*/\s*\d+\s*$", s):
        return "fraction"

    # ranges
    if re.search(r"\bto\b|\-", s):
        return "range"

    # numeric only (integer or float)
    if re.match(r"^\s*[\d\.\s/]+\s*$", s):
        return "numeric_only"

    return "other"


def classify_series_patterns(series: pd.Series) -> pd.DataFrame:
    """
    Given a Series of raw dimensional values, return a small
    DataFrame showing counts per pattern label.
    """
    labels = series.dropna().astype(str).map(classify_unit_pattern)
    counts = labels.value_counts().reset_index()
    counts.columns = ["Pattern", "Count"]
    return counts