from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = "7956930943:AAHl3lCIJ-IiVC2vxhJNeco1YMwNFeW4TTc"

# Fungsi untuk menangani perintah /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Halo! Sayangku Bzirrrr")

# Fungsi untuk menangani pesan teks
async def echo(update: Update, context: CallbackContext):
    await update.message.reply_text(update.message.text)

# Fungsi utama untuk menjalankan bot
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot berjalan...")
    app.run_polling()

if __name__ == "__main__":
    main()
