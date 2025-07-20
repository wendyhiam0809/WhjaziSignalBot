import ccxt
from pycoingecko import CoinGeckoAPI

def get_binance_price(symbol="BTC/USDT"):
    binance = ccxt.binance()
    ticker = binance.fetch_ticker(symbol)
    return ticker['last']

def get_coingecko_price(symbol="bitcoin"):
    cg = CoinGeckoAPI()
    data = cg.get_price(ids=symbol, vs_currencies='usd')
    return data[symbol]['usd']
