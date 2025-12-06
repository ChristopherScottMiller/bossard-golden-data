from __future__ import annotations

from pathlib import Path
from typing import Literal

import pandas as pd

from .config import BASE_DIR, DATA_INTERIM

# Where mapping tables will live
MAPPINGS_DIR = BASE_DIR / "mappings"
MAPPINGS_DIR.mkdir(parents=True, exist_ok=True)


def get_mapping_path(field_name: str) -> Path:
    """
    Return the path to the mapping CSV for a given field
    (e.g., 'Material' -> mappings/material_mapping.csv).
    """
    safe = field_name.lower().replace(" ", "_")
    return MAPPINGS_DIR / f"{safe}_mapping.csv"


def create_mapping_template_from_top_values(
    top_values_path: Path,
    field_name: str,
    normalized_column: str | None = None,
    overwrite: bool = False,
) -> Path:
    """
    Create a mapping CSV for a field based on a previously saved
    *_top_values.csv file from DATA_INTERIM.

    Example:
        material_top_values.csv -> mappings/material_mapping.csv

    Columns:
        raw_value, normalized_value, notes
    """
    mapping_path = get_mapping_path(field_name)
    if mapping_path.exists() and not overwrite:
        return mapping_path

    if normalized_column is None:
        normalized_column = "normalized_value"

    df_top = pd.read_csv(top_values_path)
    raw_col = [c for c in df_top.columns if c.endswith("_Value")]
    if not raw_col:
        raise ValueError(f"Could not find a *_Value column in {top_values_path}")
    raw_col = raw_col[0]

    template = pd.DataFrame(
        {
            "raw_value": df_top[raw_col],
            normalized_column: df_top[raw_col],  # start as identity mapping
            "notes": "",
        }
    )

    template.to_csv(mapping_path, index=False)
    return mapping_path


def load_mapping(field_name: str, normalized_column: str = "normalized_value") -> pd.DataFrame:
    """
    Load a mapping table for a given field.

    Expected columns:
        raw_value, <normalized_column>, notes
    """
    path = get_mapping_path(field_name)
    if not path.exists():
        raise FileNotFoundError(f"Mapping file not found for '{field_name}': {path}")
    df = pd.read_csv(path)
    if "raw_value" not in df.columns or normalized_column not in df.columns:
        raise ValueError(
            f"Mapping file {path} must contain 'raw_value' and '{normalized_column}' columns."
        )
    return df


def normalize_series_with_mapping(
    series: pd.Series,
    mapping_df: pd.DataFrame,
    normalized_column: str = "normalized_value",
    policy: Literal["keep_raw", "set_nan", "flag"] = "keep_raw",
) -> pd.Series:
    """
    Normalize a pandas Series based on a mapping table.

    Parameters
    ----------
    series : pd.Series
        Series of raw values (e.g., Material).
    mapping_df : pd.DataFrame
        DataFrame with 'raw_value' and <normalized_column>.
    normalized_column : str
        Column in mapping_df that contains the normalized values.
    policy : {"keep_raw", "set_nan", "flag"}
        How to handle values not found in the mapping:
          - "keep_raw": return original value
          - "set_nan": return NaN
          - "flag": return f"UNMAPPED::{raw_value}"

    Returns
    -------
    pd.Series
        Series of normalized values.
    """
    mapping = mapping_df.set_index("raw_value")[normalized_column]

    def _normalize(val):
        if pd.isna(val):
            return val
        val_str = str(val)
        if val_str in mapping.index:
            return mapping[val_str]
        if policy == "keep_raw":
            return val_str
        if policy == "set_nan":
            return pd.NA
        if policy == "flag":
            return f"UNMAPPED::{val_str}"
        return val_str

    return series.map(_normalize)
