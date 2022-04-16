import yfinance as yf
from datetime import date

# The function loops though a list of tickers and obtains dictionaries of info from Yahoo Finance
# It then obtains the relevent values from the dictionary and appends a new line with symbol, price and a daily change calculation to the stock_data string
 
def get_market_data():
    tickers = ("SPY","QQQ","MDY","IWM","^VIX","SVIX","BTC-USD","ETH-USD","DOGEC-USD")
    stock_data =""

    for ticker in tickers:
        ticker = yf.Ticker(ticker)
        info = ticker.info
        symbol = info.get("symbol")
        price = info.get("regularMarketPrice")
        previous = info.get("regularMarketPreviousClose")
        stock_data = f"{stock_data}{symbol}: {price} | Daily Change: {(price/previous-1)*100: .2f}%\n"

    return stock_data