import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from indicators import get_live_price

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome Wendy! Send /signal BTC/USDT (or any mapped coin) to get a real price signal.")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args:
        await update.message.reply_text("Usage: /signal BTC/USDT")
        return
    symbol = args[0].upper()
    price = get_live_price(symbol)
    if price:
        await update.message.reply_text(
            f"📊 Signal Alert: {symbol}\n"
            f"Entry: {price}\n"
            f"Source: Binance or CoinGecko"
        )
    else:
        await update.message.reply_text(f"❌ Could not fetch price for {symbol}. Try another coin.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()



