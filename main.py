import os
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

TOKEN = os.getenv("BOT_TOKEN")
bot = TeleBot(TOKEN)

# -------------------- MENU --------------------

@bot.message_handler(commands=['start', 'menu'])
def main_menu(msg):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(
        KeyboardButton("📝 Nový záznam"),
        KeyboardButton("📊 Moje hodiny")
    )
    bot.send_message(msg.chat.id, "Vyber akci:", reply_markup=markup)

# -------------------- NOVÝ ZÁZNAM --------------------

@bot.message_handler(func=lambda m: m.text == "📝 Nový záznam")
def start_new(msg):

    start_markup = InlineKeyboardMarkup()

    start_markup.row(
        InlineKeyboardButton("6:00", callback_data="start_6:00"),
        InlineKeyboardButton("6:30", callback_data="start_6:30"),
    )

    start_markup.row(
        InlineKeyboardButton("7:00", callback_data="start_7:00"),
        InlineKeyboardButton("7:30", callback_data="start_7:30"),
    )

    start_markup.row(
        InlineKeyboardButton("Vlastní čas", callback_data="start_custom"),
    )

    bot.send_message(msg.chat.id, "⏱ Vyber začátek práce:", reply_markup=start_markup)

# -------------------- CALLBACK --------------------

@bot.callback_query_handler(func=lambda call: call.data.startswith("start_"))
def handle_start_time(call):
    selected = call.data.replace("start_", "")

    if selected == "custom":
        bot.send_message(call.message.chat.id, "Napiš vlastní čas ve formátu HH:MM")
        bot.register_next_step_handler(call.message, save_custom_start)
        return

    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, f"🕒 Začátek práce: {selected}")

def save_custom_start(msg):
    custom_time = msg.text.strip()
    bot.send_message(msg.chat.id, f"🕒 Začátek práce: {custom_time}")

# -------------------- SPUŠTĚNÍ BOTA --------------------

if __name__ == "__main__":
    print("Bot běží…")
    bot.infinity_polling()
