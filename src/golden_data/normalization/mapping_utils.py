from __future__ import annotations

from typing import Literal

import pandas as pd


def find_unmapped(
    series: pd.Series,
    mapping_df: pd.DataFrame,
    mapping_raw_col: str = "raw_value",
) -> pd.Series:
    """
    Return unique raw values in `series` that do NOT exist in the mapping.

    Parameters
    ----------
    series : pd.Series
        Raw values from the dataset (e.g., Material column).
    mapping_df : pd.DataFrame
        Mapping table with at least a 'raw_value' column.
    mapping_raw_col : str
        Column name in mapping_df that contains raw values.

    Returns
    -------
    pd.Series
        Unique unmapped values.
    """
    mapped_raw = set(mapping_df[mapping_raw_col].astype(str))
    series_str = series.dropna().astype(str)
    unmapped_mask = ~series_str.isin(mapped_raw)
    return series_str[unmapped_mask].drop_duplicates()


def mapping_coverage_report(
    series: pd.Series,
    mapping_df: pd.DataFrame,
    mapping_raw_col: str = "raw_value",
    normalized_col: str = "normalized_value",
) -> pd.DataFrame:
    """
    Compute basic coverage metrics for a mapping against a raw series.

    Returns a one-row DataFrame with:
      - total_values
      - unique_values
      - mapped_unique_values
      - unmapped_unique_values
      - coverage_percent
    """
    series_str = series.dropna().astype(str)
    raw_unique = set(series_str)

    mapped_raw = set(mapping_df[mapping_raw_col].astype(str))
    mapped_unique = raw_unique.intersection(mapped_raw)
    unmapped_unique = raw_unique.difference(mapped_raw)

    total = len(series_str)
    uniq = len(raw_unique)
    mapped_uniq_count = len(mapped_unique)
    unmapped_uniq_count = len(unmapped_unique)
    coverage = (mapped_uniq_count / uniq * 100.0) if uniq else 0.0

    return pd.DataFrame(
        [
            {
                "total_values": total,
                "unique_values": uniq,
                "mapped_unique_values": mapped_uniq_count,
                "unmapped_unique_values": unmapped_uniq_count,
                "coverage_percent": round(coverage, 2),
            }
        ]
    )


def apply_mapping(
    series: pd.Series,
    mapping_df: pd.DataFrame,
    mapping_raw_col: str = "raw_value",
    normalized_col: str = "normalized_value",
    policy: Literal["keep_raw", "set_nan", "flag"] = "keep_raw",
    flag_prefix: str = "UNMAPPED::",
) -> pd.Series:
    """
    Apply a mapping table to normalize a Pandas Series.

    Parameters
    ----------
    series : pd.Series
        Raw values to normalize.
    mapping_df : pd.DataFrame
        Mapping table with raw and normalized columns.
    mapping_raw_col : str
        Column with raw values in the mapping.
    normalized_col : str
        Column with normalized values in the mapping.
    policy : {"keep_raw", "set_nan", "flag"}
        Behavior when a value is not present in the mapping:
          - keep_raw = return original value
          - set_nan = return <NA>
          - flag = return 'UNMAPPED::<raw>'
    flag_prefix : str
        Prefix used when policy == "flag".

    Returns
    -------
    pd.Series
        Series of normalized values.
    """
    mapping = mapping_df.set_index(mapping_raw_col)[normalized_col].astype(str)

    def _normalize(val):
        if pd.isna(val):
            return val
        s = str(val)
        if s in mapping.index:
            return mapping[s]
        if policy == "set_nan":
            return pd.NA
        if policy == "flag":
            return f"{flag_prefix}{s}"
        return s  # keep_raw

    return series.map(_normalize)