import time
import pandas as pd
import yfinance as yf


# Request current market caps

def getCaps(tickers, out):
    data = pd.DataFrame(columns=["Ticker", "Market Cap"])

    # request and extract market cap
    for ticker in tickers:
        info = yf.Ticker(ticker).info
        data.loc[data.size] = [ticker, info["marketCap"]]
        time.sleep(1)

    # export as .xlsx
    data.to_excel(out, index=False)
