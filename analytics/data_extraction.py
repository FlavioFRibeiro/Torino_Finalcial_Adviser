import yfinance as yf

def data_extraction(ticker, period="6mo"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)
    hist.reset_index(inplace=True)
    return hist