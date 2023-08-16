import pandas as pd
from pathlib import Path
import extract
from get import *


def main():
    start = "2018-7-27"
    end = "2023-7-27"
    data = Path('.') / 'data'
    raw = data / 'raw'

    try:
        # extract tickers from .xlsx
        tickers = extract.extractStocks(data / 'input' / 'Stocks.xlsx')

        # get current market caps, 5 years of trading and close-only data
        market_caps.getCaps(tickers, raw / 'Market Cap.xlsx')
        data = trading_data.getTrading(tickers, raw / 'Trading Data.xlsx', start, end)
        closing_prices.getClose(data, tickers, raw / 'Close.xlsx')
    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    main()
