import yfinance as yf
from datetime import date
from conf import tickers

# The function loops though a list of tickers and obtains dictionaries of info from Yahoo Finance
# It then obtains the relevent values from the dictionary and creates a dictionary with the symbol as the key
# the value is a tuple containing the price at [0] and a caluation at [1] of the % change of today's price compared to yesterday's, rounded to 2 decimal places.
def get_market_data():
    
    stock_dict = {}
    
    for ticker in tickers:
        ticker = yf.Ticker(ticker)
        info = ticker.info
        symbol = info.get("symbol")
        price = info.get("regularMarketPrice")
        previous = info.get("regularMarketPreviousClose")
        stock_dict[symbol] = (price,(str(f'{round((price/previous-1)*100,2)}%'))) 

    return stock_dict
