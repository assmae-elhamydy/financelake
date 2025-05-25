Unit Test – Validation of the fetch_stock_data Function Using yfinance

Closes #57

✅ Pre‑Checklist

I have read the project’s contribution guidelines.

I have installed the required dependencies (pytest, yfinance, pytest-mock).

I have tested the fetch_stock_data() function locally.

🎯 Objective

Validate that the fetch_stock_data() function correctly retrieves valid stock data from Yahoo Finance, returning a DataFrame with essential columns: Open, Close, and Volume.

📌 Tasks to Complete

Create the test file: tests/test_stock_ingestion.py

Write a unit test that:

Calls fetch_stock_data("AAPL")

Asserts the return is a non-empty pandas.DataFrame

Checks for the presence of the columns: Open, Close, Volume

Add a test using mocking for the call to yfinance.Ticker().history() (with pytest-mock) to avoid live calls during CI/CD

Run the tests with pytest and ensure they pass

🛠️ Technologies Used

Test framework: pytest

Ingestion library: yfinance

Mocking (optional): pytest-mock

📁 Recommended Structure

financelake/
├── stock_ingestion.py # Contains the fetch_stock_data() function
├── tests/
│ └── test_stock_ingestion.py # Contains the unit tests
└── requirements.txt # Lists the project dependencies

