from __future__ import annotations

import json
from collections import Counter, defaultdict

import pandas as pd
from rich.console import Console
from rich.table import Table

from golden_data.config import get_raw_data_path, DATA_INTERIM

console = Console()


def parse_cf_cell(cell):
    """
    Parse a single 'Custom Fields' cell from BigCommerce into a list of (name, value) pairs.
    """
    if pd.isna(cell) or cell == "":
        return []
    try:
        parsed = json.loads(str(cell))
    except Exception:
        return []

    out: list[tuple[str, str | None]] = []
    if isinstance(parsed, list):
        for item in parsed:
            if isinstance(item, dict):
                name = item.get("name")
                value = item.get("value")
                if name:
                    out.append(
                        (str(name).strip(), str(value).strip() if value is not None else None)
                    )
    return out


def scan_custom_fields(max_rows: int | None = 5000, show_table: bool = False) -> pd.DataFrame:
    """
    Scan 'Custom Fields' for products and return a summary DataFrame.

    Returns a DataFrame with:
      - Field_Name
      - Product_Count
      - Usage_Percent
      - Example_Values
    """
    path = get_raw_data_path()
    df = pd.read_csv(path, low_memory=False)

    # Try to isolate product rows, but fall back gracefully
    if "Item" in df.columns:
        products = df[df["Item"] == "Product"].copy()
        if products.empty:
            products = df.copy()
    else:
        products = df.copy()

    if max_rows is not None:
        products = products.head(max_rows)

    total_products = len(products)
    field_usage: Counter[str] = Counter()
    samples: dict[str, Counter[str]] = defaultdict(Counter)

    for _, row in products.iterrows():
        for name, value in parse_cf_cell(row.get("Custom Fields")):
            field_usage[name] += 1
            if value and len(samples[name]) < 50:
                samples[name][value] += 1

    rows: list[dict[str, object]] = []
    for name, cnt in field_usage.most_common():
        usage_pct = 100.0 * cnt / total_products if total_products else 0.0
        example_vals = ", ".join(v for v, _ in samples[name].most_common(5))
        rows.append(
            {
                "Field_Name": name,
                "Product_Count": cnt,
                "Usage_Percent": round(usage_pct, 2),
                "Example_Values": example_vals,
            }
        )

    summary_df = pd.DataFrame(rows)

    # Save to interim for inspection
    DATA_INTERIM.mkdir(parents=True, exist_ok=True)
    summary_df.to_csv(DATA_INTERIM / "custom_field_summary.csv", index=False)

    if show_table:
        table = Table(title="Custom Field Summary (subset)")
        for col in ["Field_Name", "Product_Count", "Usage_Percent", "Example_Values"]:
            table.add_column(col)

        for _, r in summary_df.head(25).iterrows():
            table.add_row(
                str(r["Field_Name"]),
                str(r["Product_Count"]),
                f'{r["Usage_Percent"]}%',
                str(r["Example_Values"]),
            )

        console.print(table)

    # 🔥 CRITICAL: ALWAYS return the DataFrame
    return summary_df


def main():
    console.print("[bold green]Running custom field scan...[/bold green]")
    summary_df = scan_custom_fields(max_rows=5000, show_table=True)
    console.print(f"[bold]Rows:[/bold] {len(summary_df)}")


if __name__ == "__main__":
    main()