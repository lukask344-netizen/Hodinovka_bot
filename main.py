import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

# ----- /start -----
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Vítej v Hodinovka_bot!\n\n"
        "/startwork – začít měřit\n"
        "/endwork – ukončit měření\n"
        "/today – dnešní hodiny\n"
        "/week – týdenní přehled\n"
        "/month – měsíční přehled\n"
        "/year – roční přehled"
    )

# ----- Placeholder funkce -----
async def startwork(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🟢 Začal jsi měřit čas.")

async def endwork(update: Update, Context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔴 Ukončil jsi měření.")

async def today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📅 Dnes: 0 hodin (zatím neimplementováno).")

async def week(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📆 Tento týden: 0 hodin (zatím neimplementováno).")

async def month(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📅 Tento měsíc: 0 hodin (zatím neimplementováno).")

async def year(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📅 Tento rok: 0 hodin (zatím neimplementováno).")

# ----- spuštění aplikace -----
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