# tests/test_basic_loading.py
import pandas as pd
from golden_data.config import get_raw_data_path

def test_raw_file_loads():
    path = get_raw_data_path()
    df = pd.read_csv(path, low_memory=False)

    # Basic sanity checks
    assert len(df) > 0, "Raw CSV appears to be empty."

    # Expect these columns to exist in this project
    expected_cols = {"Item", "ID", "Name", "SKU"}
    missing = expected_cols - set(df.columns)
    assert not missing, f"Missing expected columns: {missing}"