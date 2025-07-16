from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask
import threading

# Telegram bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Отправь мне ссылку на видео или название музыки.")

telegram_app = ApplicationBuilder().token("8052314993:AAFRhqOhhEW6uGFuAdhNnNLM4pay-m9zXgE").build()
telegram_app.add_handler(CommandHandler("start", start))

# Flask app
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Bot is running"

# Запускаем Flask в отдельном потоке, чтобы не блокировать Telegram-бота
def run_flask():
    flask_app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    import threading
    # Запускаем Flask
    threading.Thread(target=run_flask).start()
    # Запускаем Telegram бота (основной поток)
    telegram_app.run_polling()
