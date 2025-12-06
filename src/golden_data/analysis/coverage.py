from __future__ import annotations

from typing import Iterable

import pandas as pd

from golden_data.normalization.mapping_utils import mapping_coverage_report


def attribute_health_report(
    df: pd.DataFrame,
    field_to_mapping: dict[str, pd.DataFrame] | None = None,
    id_col: str | None = None,
) -> pd.DataFrame:
    """
    Build a simple health table across multiple attributes.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the raw and/or normalized attribute columns.
    field_to_mapping : dict
        Optional, mapping of field name -> mapping_df
        Example:
            {
              "Material": material_mapping,
              "Finish": finish_mapping,
            }
    id_col : str, optional
        Product identifier column. Used to compute non-null coverage.

    Returns
    -------
    pd.DataFrame with columns:
        - Attribute
        - NonNull_Count
        - NonNull_Percent
        - Unique_Values
        - Mapped_Unique_Values (if mapping given)
        - Unmapped_Unique_Values (if mapping given)
        - Mapping_Coverage_Percent (if mapping given)
    """
    rows: list[dict[str, object]] = []

    if id_col is None:
        # fallback: count over all rows
        total_rows = len(df)
    else:
        total_rows = df[id_col].nunique()

    field_to_mapping = field_to_mapping or {}

    for col in df.columns:
        if col == id_col:
            continue

        series = df[col]
        non_null = series.dropna()
        nn_count = non_null.shape[0]
        uniq_vals = non_null.astype(str).nunique()
        nn_pct = 100.0 * nn_count / total_rows if total_rows else 0.0

        row = {
            "Attribute": col,
            "NonNull_Count": nn_count,
            "NonNull_Percent": round(nn_pct, 2),
            "Unique_Values": uniq_vals,
        }

        if col in field_to_mapping:
            cov = mapping_coverage_report(
                series=series,
                mapping_df=field_to_mapping[col],
            ).iloc[0]

            row.update(
                {
                    "Mapped_Unique_Values": cov["mapped_unique_values"],
                    "Unmapped_Unique_Values": cov["unmapped_unique_values"],
                    "Mapping_Coverage_Percent": cov["coverage_percent"],
                }
            )

        rows.append(row)

    return pd.DataFrame(rows).sort_values("Attribute")