from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ЗАМЕНИ ЭТОТ ТОКЕН НА СВОЙ
TOKEN = "8052314993:AAFRhqOhhEW6uGFuAdhNnNLM4pay-m9zXgE"

app = Flask(__name__)
telegram_app = ApplicationBuilder().token(TOKEN).build()


@app.route('/')
def home():
    return "Bot is running!"


@app.route('/webhook', methods=['POST'])
async def webhook():
    if request.method == "POST":
        update = Update.de_json(request.get_json(force=True), telegram_app.bot)
        await telegram_app.process_update(update)
        return "OK", 200


# /start команда
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Отправь мне ссылку на видео или название музыки.")


telegram_app.add_handler(CommandHandler("start", start))
