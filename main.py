import telebot

# TVŮJ TOKEN
bot = telebot.TeleBot("8547107810:AAFgSVRtmEFAhj3ux7vDfqK-xwQVEYKFfSs")

@bot.message_handler(commands=['start'])
def start(msg):
bot.reply_to(msg, "👋 Bot běží!\nPoužij příkazy:\n/startwork – začít práci\n/endwork – ukončit práci")

@bot.message_handler(commands=['startwork'])
def startwork(msg):
bot.reply_to(msg, "🏁 Začal jsi pracovat.")

@bot.message_handler(commands=['endwork'])
def endwork(msg):
bot.reply_to(msg, "⛔ Ukončil jsi práci.")

print("BOT BĚŽÍ…")
bot.infinity_polling()
