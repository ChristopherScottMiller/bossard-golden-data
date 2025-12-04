# src/golden_data/quick_stats.py
import duckdb
from config import get_raw_data_path
from rich import print


def quick_stats():
    path = get_raw_data_path()
    con = duckdb.connect()

    # Read directly from CSV
    con.execute(f"""
        CREATE OR REPLACE TABLE raw_products AS
        SELECT * FROM read_csv_auto('{path}', header=True);
    """)

    # How many product vs image rows, etc.
    result = con.execute("""
        SELECT Item, COUNT(*) AS cnt
        FROM raw_products
        GROUP BY Item
        ORDER BY cnt DESC;
    """).fetchdf()

    print("[bold]Row counts by Item:[/bold]")
    print(result)


if __name__ == "__main__":
    quick_stats()
