import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🇹🇳 عسلامة! أنا بوت Bac Lettres 2027 📚\n\n"
        "البوت متاعي مازال في مرحلة التجربة، "
        "وقريب نبدأ نخدم معاكم ❤️"
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
