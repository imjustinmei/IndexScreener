import pandas as pd


def calcPerformance(weighted, out):
    # read data
    twenty = pd.read_excel(weighted, sheet_name="Twenty")

    # calculate performance against 40-day moving average
    avg = twenty.iloc[:, 3:].apply(lambda x: (x.iloc[7:] > x.rolling(window=8).mean()[7:]).sum(), axis=1).div(twenty.shape[1]-3).rename("> 40day")

    # filter top three and format
    three = pd.concat([twenty["Ticker"], avg], axis=1).iloc[:-2].nlargest(3, "> 40day")
    three["> 40day"] = pd.to_numeric(three["> 40day"]).map("{:.2%}".format)
    three = three.T.reset_index().T

    # export as .xlsx
    three.to_excel(out, index=False, header=False)
