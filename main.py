import os
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

TOKEN = os.getenv("BOT_TOKEN")
bot = TeleBot(TOKEN)

async def start(update, context):
    await update.message.reply_text(
        "👋 Vítej v Hodinovka_bot!\n\n"
        "/startwork – začít měřit\n"
        "/endwork – ukončit měření\n"
        "/today – dnešní hodiny\n"
        "/week – týdenní přehled\n"
        "/month – měsíční přehled\n"
        "/year – roční přehled"
    )

async def startwork(update, context):
    uid = str(update.effective_user.id)
    msg = start_session(uid)
    await update.message.reply_text(msg)

async def endwork(update, context):
    uid = str(update.effective_user.id)
    msg = end_session(uid)
    await update.message.reply_text(msg)

async def today(update, context):
    uid = str(update.effective_user.id)
    msg = get_today(uid)
    await update.message.reply_text(msg)

async def week(update, context):
    uid = str(update.effective_user.id)
    msg = get_week(uid)
    await update.message.reply_text(msg)

async def month(update, context):
    uid = str(update.effective_user.id)
    msg = get_month(uid)
    await update.message.reply_text(msg)

async def year(update, context):
    uid = str(update.effective_user.id)
    msg = get_year(uid)
    await update.message.reply_text(msg)

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("startwork", startwork))
    app.add_handler(CommandHandler("endwork", endwork))
    app.add_handler(CommandHandler("today", today))
    app.add_handler(CommandHandler("week", week))
    app.add_handler(CommandHandler("month", month))
    app.add_handler(CommandHandler("year", year))

    print("Bot běží…")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
