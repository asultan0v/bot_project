from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

import os

TOKEN = "8052314993:AAFRhqOhhEW6uGFuAdhNnNLM4pay-m9zXgE"
bot = Bot(token=TOKEN)

app = Flask(__name__)
telegram_app = ApplicationBuilder().token(TOKEN).build()

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Отправь мне ссылку или название музыки.")

# Сообщения
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Спасибо! (но обработка пока не реализована)")

telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

@app.route("/")
def home():
    return "Bot is running"

@app.route("/webhook", methods=["POST"])
def webhook():
    if request.method == "POST":
        update = Update.de_json(request.get_json(force=True), bot)
        telegram_app.update_queue.put_nowait(update)
        return "OK", 200

if __name__ == "__main__":
    app.run(debug=True)
