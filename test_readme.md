# Unit Test – Validation of the `fetch_stock_data` Function Using yfinance

## ✅ Pre-Checklist

- I have read the project’s contribution guidelines.
- I have installed the required dependencies:
  - `pytest`
  - `yfinance`
  - `pytest-mock`
- I have tested the `fetch_stock_data()` function locally.

## 🎯 Objective

Validate that the `fetch_stock_data()` function:

- Correctly retrieves valid stock data from Yahoo Finance.
- Returns a non-empty pandas DataFrame.
- Includes essential columns: `Open`, `Close`, and `Volume`.

## 📌 Tasks to Complete

1. **Create test file**:  
   `tests/test_stock_ingestion.py`

2. **Write a unit test that:**
   - Calls `fetch_stock_data("AAPL")`.
   - Asserts the return is a non-empty `pandas.DataFrame`.
   - Checks for the presence of the columns: `Open`, `Close`, `Volume`.

3. **Add a test with mocking:**
   - Use `pytest-mock` to mock the call to `yfinance.Ticker().history()`.
   - This avoids live API calls during CI/CD runs.

4. **Run tests:**
   - Use `pytest` to execute and ensure all tests pass.

## 🛠️ Technologies Used

- Test framework: [pytest](https://docs.pytest.org/)
- Data ingestion library: [yfinance](https://pypi.org/project/yfinance/)
- Mocking framework: [pytest-mock](https://pypi.org/project/pytest-mock/)

## 📁 Recommended Project Structure

financelake/
├── stock_ingestion.py # Contains the fetch_stock_data() function
├── tests/
│ └── test_stock_ingestion.py # Contains the unit tests
└── requirements.txt # Lists the project dependencies


