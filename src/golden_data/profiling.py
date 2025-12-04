import pandas as pd
from rich import print
from rich.console import Console
from rich.table import Table

from config import get_raw_data_path, DATA_INTERIM, DATA_RAW

console = Console()

def profile_raw_data():
    csv_path = get_raw_data_path()
    console.rule(f"[bold blue]Profiling raw data: {csv_path.name}[/bold blue]")

    # Load
    df = pd.read_csv(csv_path, low_memory=False)
    rows, cols = df.shape
    console.print(f"[green]Loaded[/green] {rows} rows, {cols} columns")

    # Basic info
    console.print("[bold]Column dtypes:[/bold]")
    dtypes_table = Table(show_header=True, header_style="bold magenta")
    dtypes_table.add_column("Column")
    dtypes_table.add_column("Dtype")

    for col, dt in df.dtypes.items():
        dtypes_table.add_row(col, str(dt))

    console.print(dtypes_table)

    # Null counts (top 15 by nulls)
    console.print("\n[bold]Null counts (top 15):[/bold]")
    null_counts = df.isna().sum().sort_values(ascending=False).head(15)
    null_table = Table(show_header=True, header_style="bold magenta")
    null_table.add_column("Column")
    null_table.add_column("Nulls")

    for col, cnt in null_counts.items():
        null_table.add_row(col, str(cnt))

    console.print(null_table)

    # Value counts for a few important columns, if they exist
    for col in ["Item", "Type", "Brand ID", "Categories"]:
        if col in df.columns:
            console.print(f"\n[bold]Value counts for '{col}' (top 10):[/bold]")
            vc = df[col].value_counts(dropna=False).head(10)
            vc_table = Table(show_header=True, header_style="bold magenta")
            vc_table.add_column(f"{col}")
            vc_table.add_column("Count")
            for val, cnt in vc.items():
                vc_table.add_row(str(val), str(cnt))
            console.print(vc_table)

    # Save a small sample for quick inspection
    sample_path = DATA_INTERIM / "raw_sample_head50.csv"
    DATA_INTERIM.mkdir(parents=True, exist_ok=True)
    df.head(50).to_csv(sample_path, index=False)
    console.print(f"\n[cyan]Saved sample to[/cyan] {sample_path}")


if __name__ == "__main__":
    profile_raw_data()