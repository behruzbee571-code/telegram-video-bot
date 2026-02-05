import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import yt_dlp

TOKEN = ("8555844711:AAHbGtRaM3FkwDszbrTzZVCXwV-m3wx4uAI")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Salom!\n\n"
        "🎬 YouTube link yuboring,\n"
        "men uni video holatida yuboraman."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if (
        "youtube.com" in text or
        "youtu.be" in text or
        "instagram.com" in text
    ):
        await update.message.reply_text("🎬 Video yuklanmoqda, biroz kuting...")

        ydl_opts = {
            'outtmpl': 'video.%(ext)s',
            'format': 'mp4'
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(text, download=True)
                filename = ydl.prepare_filename(info)

            await update.message.reply_video(video=open(filename, 'rb'))
            os.remove(filename)

        except Exception as e:
            await update.message.reply_text(
                "❌ Video yuklab bo‘lmadi.\n"
                "Ehtimol post private yoki bloklangan."
            )
            print(e)
    else:
        await update.message.reply_text(
            "📎 YouTube yoki Instagram link yuboring"
        )


        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(text, download=True)
                filename = ydl.prepare_filename(info)

            await update.message.reply_video(video=open(filename, 'rb'))
            os.remove(filename)

        except Exception as e:
            await update.message.reply_text("❌ Xatolik yuz berdi!")
            print(e)
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot ishga tushdi...")
    app.run_polling()


from telegram.ext import CommandHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Salom!\n\n"
        "🎬 YouTube link yuboring,\n"
        "men uni video holatida yuboraman."
    )
