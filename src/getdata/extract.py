import pandas as pd


def extractStocks(sheet):
    tickers = []

    # read spreadsheet
    stocks = pd.read_excel(sheet)
    for stock in stocks["Stock"]:
        tickers.append(stock.split(' ')[0].replace('/', '-'))

    return tickers
