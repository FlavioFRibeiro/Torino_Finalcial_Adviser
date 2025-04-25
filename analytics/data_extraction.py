def data_extraction(ticker, period="6mo"):
    import yfinance as yf

    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)
    hist.reset_index(inplace=True)
    
    return hist