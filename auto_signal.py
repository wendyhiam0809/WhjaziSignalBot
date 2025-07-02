import os
import requests
import time
from datetime import datetime
import pytz
from telegram import Bot

# Get secrets from environment
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

COINS = ["bitcoin", "ethereum", "ripple", "cardano", "solana"]
URL_TEMPLATE = "https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies=usd"

def get_prices():
    ids = ",".join(COINS)
    url = URL_TEMPLATE.format(ids)
    try:
        res = requests.get(url)
        return res.json()
    except Exception as e:
        print("Error fetching prices:", e)
        return {}

def is_new_york_open():
    ny = datetime.now(pytz.timezone('America/New_York'))
    return ny.hour == 9 and ny.minute == 30

def send_auto_signal():
    prices = get_prices()
    for coin, data in prices.items():
        price = data['usd']
        target = round(price * 1.05, 2)
        stop = round(price * 0.97, 2)
        msg = f"📈 *Auto Signal: {coin.upper()}/USDT*\nPrice: ${price}\n🎯 Target: ${target}\n🛑 Stop Loss: ${stop}"
        bot.send_message(chat_id=CHAT_ID, text=msg, parse_mode='Markdown')

if __name__ == "__main__":
    sent_today = False
    while True:
        if is_new_york_open() and not sent_today:
            send_auto_signal()
            sent_today = True
        if datetime.now(pytz.timezone('America/New_York')).hour == 0:
            sent_today = False
        time.sleep(30)
