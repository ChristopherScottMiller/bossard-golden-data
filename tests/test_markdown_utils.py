import pandas as pd
from golden_data.markdown_utils import df_to_markdown


def test_df_to_markdown_basic():
    df = pd.DataFrame({"A": [1, 2], "B": ["x", "y"]})
    md = df_to_markdown(df, max_rows=10)

    # Should include headers
    assert "| A | B |" in md

    # Should include values
    assert "1" in md
    assert "x" in md

    # Should not crash on small DataFrame
    assert md.count("\n") >= 4


def test_df_to_markdown_empty():
    df = pd.DataFrame()
    md = df_to_markdown(df)
    assert "(no data)" in md