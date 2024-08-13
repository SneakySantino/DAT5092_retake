import pytest
import pandas as pd
from DAT5092_retake import load_csv

def sample_data_COL():
    data_COL = {
        "Country": ["Switzerland", "Bahamas", "Iceland", "Singapore", "Barbados"],
        "Cost of Living Index": [101.1, 85.0, 83.0, 76.7, 76.6],
    }
    return pd.DataFrame(data_COL)

def sample_data_SDG():
    data_SDG = {
        "Country": ["Finland", "Sweden", "Denmark", "Germany", "France"],
        "Cost of Living Index": [86.35, 85.70, 85.00, 83.45, 82.76],
    }
    return pd.DataFrame(data_SDG)

def test_load_csv(tmpdir):
    file_path = tmpdir.join("test.csv")
    data = "Country,Cost of Living Index\nSwitzerland,101.1\nBahamas,85.0\nIceland,83.0\nSingapore,76.7\nBarbados,76.6\n"
    file_path.write(data)

    df = load_data(str(file_path))

    assert len(df) == 5
    assert list(df.columns) == ["Country", "Cost of Living Index"]
