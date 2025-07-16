from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Отправь мне ссылку на видео или название музыки.")

app = ApplicationBuilder().token("8052314993:AAFRhqOhhEW6uGFuAdhNnNLM4pay-m9zXgE").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
