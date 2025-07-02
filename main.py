import os
import logging
import requests
import datetime
import time
from telegram import Bot

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Get secrets from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

# CoinGecko API URL
COINS = ['bitcoin', 'ethereum', 'ripple', 'cardano', 'solana']
URL_TEMPLATE = "https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies=usd"

def get_prices():
    ids = ",".join(COINS)
    url = URL_TEMPLATE.format(ids)
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        logger.error(f"Failed to fetch prices: {e}")
        return {}

def format_signal(prices):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [f"📊 *Auto Signals* — {now} (NYC Open)\n"]
    for coin, data in prices.items():
        price = data['usd']
        lines.append(f"🔹 *{coin.capitalize()}*: ${price:,}")
    return "\n".join(lines)

def send_signal():
    prices = get_prices()
    if not prices:
        return
    message = format_signal(prices)
    try:
        bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")
        logger.info("✅ Signal sent")
    except Exception as e:
        logger.error(f"Failed to send signal: {e}")

# Run daily at New York market open (9:30 AM EST / 4:30 PM KSA)
while True:
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=3)  # Adjust to KSA time
    if now.hour == 16 and now.minute == 30:
        send_signal()
        time.sleep(60)  # Avoid multiple sends in the same minute
    time.sleep(30)


