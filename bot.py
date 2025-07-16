from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, filters

TOKEN = "YOUR_BOT_TOKEN"

bot = Bot(token=TOKEN)
app = Flask(__name__)

dispatcher = Dispatcher(bot, None, workers=0)

def start(update, context):
    update.message.reply_text("Привет! Отправь мне ссылку на видео или название музыки.")

dispatcher.add_handler(CommandHandler("start", start))

def echo(update, context):
    text = update.message.text
    update.message.reply_text(f"Ты написал: {text}")

dispatcher.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK"

@app.route("/")
def index():
    return "Bot is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
