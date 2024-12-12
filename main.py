from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from datetime import datetime
import requests
import json
import os
import time


price_url = "https://btc-api.borisquiroz.dev/btc"
data_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

# get token from env variable
BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")
CMC_TOKEN = os.getenv("CMC_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id
    price(f"Chat ID: {chat_id}")

    await update.message.reply_text("Hello! I'm a bot!")


async def price(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id

    response = requests.get(price_url)
    r = response.json()
    value = r["price"]

    data_request = requests.get(data_url, headers={"X-CMC_PRO_API_KEY": CMC_TOKEN})
    data = data_request.json()
    percent_change_24h = data["data"][0]["quote"]["USD"]["percent_change_24h"]
    percent_change_7d = data["data"][0]["quote"]["USD"]["percent_change_7d"]
    percent_change_30d = data["data"][0]["quote"]["USD"]["percent_change_30d"]
    percent_change_60d = data["data"][0]["quote"]["USD"]["percent_change_60d"]
    percent_change_90d = data["data"][0]["quote"]["USD"]["percent_change_90d"]

    gmtime_struct = time.gmtime()
    now = datetime(*gmtime_struct[:6])


    print(f"Chat ID: {chat_id} | BTC price: ${value} USD | Updated on {now} UTC.")

    await update.message.reply_text(f"Current BTC price is ${value} USD.\nUpdated on {now} UTC.\n\nPercent change:\n24h: {percent_change_24h:.2f}%\n7d: {percent_change_7d:.2f}%\n30d: {percent_change_30d:.2f}%\n60d: {percent_change_60d:.2f}%\n90d: {percent_change_90d:.2f}%")


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("price", price))

    print("Bot started! Send /start to the bot to retrieve the chat ID.")
    application.run_polling()


if __name__ == "__main__":
    main()

