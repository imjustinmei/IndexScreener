import yfinance as yf
import pandas as pd


# Extract only close prices

def getClose(data, tickers, out):
    # clean up data
    data = data.reset_index().T.reset_index()
    data = data.drop(data.columns[[0, 1]], axis=1)
    data.loc[0] = pd.to_datetime(data.loc[0]).dt.strftime("%m/%d/%Y")
    data.insert(loc=0, column="0", value="")
    data.at[0, "0"] = "Ticker"

    # format and drop all except close
    for index, value in enumerate(tickers):
        data.drop([index * 6 + 1, index * 6 + 2, index * 6 + 3, index * 6 + 5, index * 6 + 6], inplace=True)
        data.at[index * 6 + 4, "0"] = value

    # export as .xlsx
    data.to_excel(out, index=False, header=False)
