import requests

def get_live_price(symbol):
    pair = symbol.replace("/", "")
    # Binance (most blue chips, some memes)
    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={pair}"
        r = requests.get(url, timeout=3)
        if r.ok and 'price' in r.json():
            return float(r.json()['price'])
    except Exception:
        pass
    # CoinGecko fallback for meme/ICO
    try:
        cgids = {
            "BTC/USDT": "bitcoin",
            "ETH/USDT": "ethereum",
            "BNB/USDT": "binancecoin",
            "SOL/USDT": "solana",
            "DOGE/USDT": "dogecoin",
            "PEPE/USDT": "pepe",
            "FLOKI/USDT": "floki",
            "WIF/USDT": "dogwifhat",
            "BONK/USDT": "bonk",
            "SHIB/USDT": "shiba-inu",
            "MEME/USDT": "memecoin",
            # Add more mappings here as you wish!
        }
        if symbol in cgids:
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={cgids[symbol]}&vs_currencies=usd"
            r = requests.get(url, timeout=3)
            price = r.json()[cgids[symbol]]["usd"]
            return float(price)
    except Exception:
        pass
    return None
