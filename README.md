# Index Screener - Career Explorers Capstone

This project filters securities by using capitalization weighing and moving averages as metrics. 
- Retrieves trading data from Yahoo Finance API via ``yfinance``
- Reads/writes to .xlsx via ``pandas``

## Prerequisites
Install requirements via ``pip install -r requirements.txt`` or ``make install``

## Usage
```
# get current market caps, trading and close-only data
make get

# filter top 20/3 securities by weighted performance, performance against moving average
make process

# does both
make main
```