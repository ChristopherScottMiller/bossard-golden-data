from __future__ import annotations

import pandas as pd
from rich.console import Console
from rich.table import Table

from .config import get_raw_data_path, DATA_INTERIM

console = Console()


def profile_raw_data(save_sample: bool = True) -> pd.DataFrame:
    """
    Load and lightly profile the raw BigCommerce export.

    - Reads the CSV at the configured raw data path
    - Prints basic info (rows, columns, first N column names)
    - Optionally saves a small sample to data/interim
    - RETURNS the full DataFrame
    """
    raw_path = get_raw_data_path()
    df = pd.read_csv(raw_path, low_memory=False)

    # Console summary
    console.print(f"[bold cyan]Profiling raw dataset: {raw_path}[/bold cyan]")
    console.print(f"Rows: {len(df)}, Columns: {len(df.columns)}")

    table = Table(title="Raw Data Overview")
    table.add_column("Metric")
    table.add_column("Value", overflow="fold")

    table.add_row("Rows", str(len(df)))
    table.add_row("Columns", str(len(df.columns)))
    col_preview = ", ".join(df.columns[:15]) + (" ..." if len(df.columns) > 15 else "")
    table.add_row("First columns", col_preview)

    console.print(table)

    # Save a small sample for inspection
    if save_sample:
        DATA_INTERIM.mkdir(parents=True, exist_ok=True)
        df.head(50).to_csv(DATA_INTERIM / "raw_sample_head50.csv", index=False)

    # 🔥 CRITICAL: always return the DataFrame
    return df