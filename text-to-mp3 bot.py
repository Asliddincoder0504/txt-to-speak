#Kod    python telegram-bot==13.15   kutubxonasida    yozilgan.
import logging    #Xatolikni  ushlash   uchun  yozganman
import os    #  Fayllarni  o'qitish uchun
import asyncio
import edge_tts   #bu  modullarni   albatta   o'rnating
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "7652520907:AAHV39uWrqDoJyPZShOxlGqE11feO5BHhHY"


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Salom meni   Asliddin  Coder   dasturlagan! Matnni ovozga aylantirish uchun menga yozing.")


def text_to_speech(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    if not text:
        update.message.reply_text("Iltimos, matn yuboring!")
        return

    voice = "uz-UZ-MadinaNeural"
    output_file = "output.mp3"


    async def generate_speech():
        tts = edge_tts.Communicate(text, voice)
        await tts.save(output_file)

    asyncio.run(generate_speech())

    with open(output_file, "rb") as voice_file:
        update.message.reply_audio(voice_file)

    os.remove(output_file)


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, text_to_speech))

    updater.start_polling()
    updater.idle()

print("Bot ishladi")
if __name__ == "__main__":
    main()
