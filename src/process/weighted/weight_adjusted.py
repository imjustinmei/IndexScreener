import pandas as pd


# calculate performance of weighted stocks against index and filter top twenty

def calcPerformance(caps, close, out):
    # read data
    caps = pd.read_excel(caps)
    close = pd.read_excel(close)

    # combine caps, weights, and close
    weights = caps["Market Cap"].div(caps["Market Cap"].sum())
    caps.insert(2, "Weight", weights)
    caps = pd.concat([caps, close.iloc[:, 1:]], axis=1)

    # calculate weighted prices and index percent change
    caps.iloc[:, 3:] = caps.iloc[:, 3:].multiply(caps.iloc[:, 2], axis=0)
    sums = caps.sum(numeric_only=True)
    change = sums[2:].pct_change()

    # combine raw and processed data
    sums = pd.concat([sums, change], axis=1).T
    sums.insert(0, "Ticker", ["Total", ""])
    caps = pd.concat([caps, sums], ignore_index=True)

    # calculate performance against index and top twenty
    caps.insert(3, "Weeks > index", caps.iloc[:-2, 3:].apply(lambda x: (x.pct_change() > change).sum(), axis=1))
    twenty = caps.nlargest(20, ["Weeks > index", "Weight"]).drop("Weeks > index", axis=1)
    caps = caps.fillna("")

    # setup .xlsx file writer
    writer = pd.ExcelWriter(out, engine="xlsxwriter")
    caps.to_excel(writer, sheet_name="Weighted", startrow=1, index=False, header=False)
    twenty.to_excel(writer, sheet_name="Twenty", startrow=1, index=False, header=False)

    workbook = writer.book

    number = workbook.add_format({"num_format": "#,##0"})
    price = workbook.add_format({"num_format": "0.00000"})
    percent = workbook.add_format({"num_format": "0.0000%"})

    # format weighted sheet
    worksheet = writer.sheets["Weighted"]
    for idx, val in enumerate(caps.columns):
        worksheet.write(0, idx, val)

    worksheet.set_column(0, 0, 7.71)
    worksheet.set_column(1, 1, 17, number)
    worksheet.set_column(2, 2, 10.43, percent)
    worksheet.set_column(3, 3, 13.29, number)
    worksheet.set_column(4, caps.shape[0] - 1, 11.43, price)
    worksheet.set_row(len(close) + 2, None, percent)

    # format twenty sheet
    worksheet = writer.sheets["Twenty"]
    for idx, val in enumerate(twenty.columns):
        worksheet.write(0, idx, val)

    worksheet.set_column(0, 0, 7.71)
    worksheet.set_column(1, 1, 17, number)
    worksheet.set_column(2, 2, 10.43, percent)
    worksheet.set_column(3, twenty.shape[0] - 1, 11.43, price)

    writer.close()
