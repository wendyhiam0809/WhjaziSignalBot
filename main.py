import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

import os
BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 Hello Wendy! Your bot is live and ready.")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
    "📊 *Signal Alert: BTC/USDT*\n"
    "Action: BUY\n"
    "Entry: 60,800\n"
    "Target: 63,000\n"
    "Stop-Loss: 59,500\n"
    "Timeframe: 15m",
    parse_mode='Markdown'
)


async def track(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 Tracking portfolio performance... (Sample response)")

async def strategy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧠 Strategy tip: Always use a stop-loss. Risk management first!")

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

# /send BTC BUY 62800 65500 61500
async def send_signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        symbol, action, entry, target, stop = context.args
        response = (
            f"📊 *Signal Alert: {symbol}/USDT*\n"
            f"Action: {action.upper()}\n"
            f"Entry: {entry}\n"
            f"Target: {target}\n"
            f"Stop-Loss: {stop}\n"
            f"Timeframe: 15m"
        )
        await update.message.reply_text(response, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(
            "⚠️ Invalid format. Please use:\n/send BTC BUY 62800 65500 61500"
        )


if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))
    app.add_handler(CommandHandler("track", track))
    app.add_handler(CommandHandler("strategy", strategy))
    app.add_handler(CommandHandler("send", send_signal))
    app.run_polling()


