import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Wendy! 🚀 The bot is working again.")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 Signal feature is coming soon.")

async def track(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📈 Track feature is coming soon.")

async def strategy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧠 Strategy feature is coming soon.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))
    app.add_handler(CommandHandler("track", track))
    app.add_handler(CommandHandler("strategy", strategy))

    print("Launching bot...")
    app.run_polling()

if __name__ == "__main__":
    main()





