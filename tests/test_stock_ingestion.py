import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from stock_ingestion import fetch_stock_data

def test_fetch_stock_data_mocked(mocker):
    mock_df = pd.DataFrame({
        "Open": [150.0],
        "Close": [155.0],
        "Volume": [1000000],
    })

    mock_ticker = mocker.patch("stock_ingestion.yf.Ticker")
    instance = mock_ticker.return_value
    instance.history.return_value = mock_df

    data = fetch_stock_data("AAPL")

    assert not data.empty, "Le DataFrame retourné est vide"
    for col in ["Open", "Close", "Volume"]:
        assert col in data.columns, f"La colonne '{col}' est absente"
