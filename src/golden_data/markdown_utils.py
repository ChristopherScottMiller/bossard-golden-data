from __future__ import annotations
import pandas as pd


def df_to_markdown(df: pd.DataFrame, max_rows: int = 30) -> str:
    """
    Convert a DataFrame to a simple Markdown table string.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.
    max_rows : int
        Maximum number of rows to convert.

    Returns
    -------
    str
        A Markdown-formatted table.
    """
    # Handle empty DataFrame
    if df is None or df.empty:
        return "| (no data) |\n| --- |\n"

    # Limit rows
    df = df.head(max_rows)

    # Prepare header
    columns = df.columns.tolist()
    header = "| " + " | ".join(columns) + " |\n"
    separator = "| " + " | ".join(["---"] * len(columns)) + " |\n"

    # Prepare rows
    rows = ""
    for _, row in df.iterrows():
        vals = [str(row[col]) for col in columns]
        rows += "| " + " | ".join(vals) + " |\n"

    return header + separator + rows