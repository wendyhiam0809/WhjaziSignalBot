import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from price_fetcher import get_binance_price, get_coingecko_price

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome Wendy! 👋\nSend /signal BTC/USDT or /signal PEPE/USDT to get a real live price."
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args:
        await update.message.reply_text("Usage: /signal <COIN/PAIR> (e.g. /signal BTC/USDT or /signal PEPE/USDT)")
        return

    symbol = args[0].upper()

    # Try Binance first
    price = get_binance_price(symbol)
    if not price:
        cg_map = {
            "BTC/USDT": "bitcoin",
            "ETH/USDT": "ethereum",
            "BNB/USDT": "binancecoin",
            "SOL/USDT": "solana",
            "PEPE/USDT": "pepe",
            "FLOKI/USDT": "floki",
            "WIF/USDT": "dogwifhat",
            "BONK/USDT": "bonk",
            "SHIB/USDT": "shiba-inu",
            "DOGE/USDT": "dogecoin",
            "MEME/USDT": "memecoin",
            # Add more as needed!
        }
        cg_symbol = cg_map.get(symbol)
        if cg_symbol:
            price = get_coingecko_price(cg_symbol)

    if price:
        await update.message.reply_text(
            f"📊 Signal Alert: {symbol}\n"
            f"Entry: {price}\n"
            f"Source: Binance or CoinGecko"
        )
    else:
        await update.message.reply_text(f"❌ Could not fetch price for {symbol}. Try another coin or check mapping.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()




