# Telegram BTC bot
This is a simple telegram bot that can be used to get the current price of bitcoin in USD. The bot uses my own API price, on [btc-api.borisquiroz.dev](https://btc-api.borisquiroz.dev/btc).

This work was part of my regular "weekend projects".

## How to use - The real bot
It's available at [https://t.me/fc83c928_bot](https://t.me/fc83c928_bot)

## How to use - Requirements
- Python 3.6 or higher
- A Telegram bot token, you can get one by talking to the [BotFather](https://t.me/botfather)
- A server to run the bot. I use Kubernetes (see "deployment" below)

## How to use - Deployment
If you're using Kubernetes, you can deploy the bot using the following command:

```bash
kubectl apply -f deployment/deployment.yaml
```
