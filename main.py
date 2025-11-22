import os
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

TOKEN = os.getenv("BOT_TOKEN")
bot = TeleBot(TOKEN)

# ---------------- MENU ----------------

@bot.message_handler(commands=['start', 'menu'])
def main_menu(msg):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(
        KeyboardButton("📝 Nový záznam"),
        KeyboardButton("📊 Moje hodiny")
    )
    bot.send_message(msg.chat.id, "Vyber akci:", reply_markup=markup)

# ---------------- NOVÝ ZÁZNAM ----------------

@bot.message_handler(func=lambda m: m.text == "📝 Nový záznam")
def start_new(msg):
    start_markup = InlineKeyboardMarkup()

    start_markup.row(
        InlineKeyboardButton("6:00", callback_data="start_6"),
        InlineKeyboardButton("6:30", callback_data="start_630")
    )
    start_markup.row(
        InlineKeyboardButton("7:00", callback_data="start_7"),
        InlineKeyboardButton("7:30", callback_data="start_730")
    )

    bot.send_message(msg.chat.id, "Vyber čas začátku:", reply_markup=start_markup)

# ---------------- CALLBACK ----------------

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, f"Zaznamenáno: {call.data}")

# ---------------- START BOT ----------------

if __name__ == "__main__":
    print("Bot běží…")
    bot.infinity_polling()
