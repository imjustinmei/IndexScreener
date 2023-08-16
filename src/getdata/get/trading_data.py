import pandas as pd
import yfinance as yf


# Request weekly trading data (High, Low, Close, Volume)

def getTrading(tickers, out, start, end):
    # request data
    data = yf.download(tickers, start=start,
                       end=end, interval="1wk", rounding=True, group_by="tickers", progress=False)
    copy = data.copy(deep=True)

    # clean up + remove unnecessary data
    data = data.reset_index().T.reset_index()
    data = data.drop(data.columns[[0, 1]], axis=1)

    # format data
    data.loc[0] = pd.to_datetime(data.loc[0]).dt.strftime("%m/%d/%Y")
    data.insert(loc=0, column="0", value="")
    data.at[0, "0"] = "Ticker"

    for index, value in enumerate(tickers):
        data.drop([index * 6 + 1, index * 6 + 5], inplace=True)
        data.at[index * 6 + 2, "0"] = value

    # export as .xlsx
    data.to_excel(out, index=False, header=False)

    return copy
