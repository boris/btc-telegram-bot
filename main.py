from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from datetime import datetime
import requests
import json
import os
import time


url = "https://btc-api.borisquiroz.dev/btc"

# get token from env variable
BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id
    price(f"Chat ID: {chat_id}")

    await update.message.reply_text("Hello! I'm a bot!")


async def price(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id

    response = requests.get(url)
    r = response.json()
    value = r["price"]

    gmtime_struct = time.gmtime()
    now = datetime(*gmtime_struct[:6])
    print(f"Chat ID: {chat_id} | BTC price: ${value} USD | Updated on {now} UTC.")

    await update.message.reply_text(f"Current BTC price is ${value} USD.\nUpdated on {now} UTC.")


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("price", price))

    print("Bot started! Send /start to the bot to retrieve the chat ID.")
    application.run_polling()


if __name__ == "__main__":
    main()

