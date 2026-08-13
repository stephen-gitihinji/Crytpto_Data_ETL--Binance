import requests as req 
import json

exchange_info_url = "https://api.binance.com/api/v3/exchangeInfo"
trading_day_url = "https://api.binance.com/api/v3/ticker/tradingDay"

def extract_market_data():
    #getting general information of the tickers(symbols)
    symbols_info = req.get(exchange_info_url).json()['symbols']
    #extracting 100 tickers
    tickers = [symbol_info['symbol']for symbol_info in symbols_info][:100]

    #using the extracted tickers to get their market data.
    parameters = {"symbols":json.dumps(tickers, separators=(",", ":"))}
    market_data = req.get(trading_day_url, params=parameters).json()
    return market_data