from pathlib import Path
from weighted import *
from average import *


def main():
    data = Path(".") / "data"
    raw = data / "raw"
    processed = data / "processed"

    try:
        # filter top 20 securities by weighted performance
        weight_adjusted.calcPerformance(raw / "Market Cap.xlsx", raw / "Close.xlsx", data / "processed/Weighted.xlsx")
        # filter top 3 securities by performance against moving average
        moving_average.calcPerformance(processed / "Weighted.xlsx", processed / "Averaged.xlsx")
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()
