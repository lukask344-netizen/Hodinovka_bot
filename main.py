import os
from flask import Flask, request
import telebot

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN, threaded=False)

app = Flask(__name__)

@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    json_str = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

@app.route('/', methods=['GET'])
def index():
    return "Bot běží!", 200

# ----------------- MENU -----------------

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "Bot běží ✔️")

# --------------------- START BOT ---------------------

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"{os.getenv('RENDER_URL')}/{TOKEN}")
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
