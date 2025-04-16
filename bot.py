import os
import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from gtts import gTTS
from uuid import uuid4

from dotenv import load_dotenv
load_dotenv()

# Load environment variables
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# Gemini config
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

# Define Gemini-based AI responder
def ask_gemini(user_input):
    prompt = f"""
You are a wise, compassionate mentor based on the teachings of the Bhagavad Gita.
Understand the user's language and respond in the same language.
If they speak in Marathi, reply in Marathi.
If they speak in English, reply in English.
If in Hindi, reply in Hindi.

User: {user_input}
Answer:
    """
    try:
        print("🧠 Prompt sent to Gemini...")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print("❌ Gemini error:", e)
        return "क्षम करा, उत्तर मिळण्यात अडचण आली आहे. पुन्हा प्रयत्न करा."


# Text-to-speech
def generate_voice(text):
    tts = gTTS(text=text, lang="hi")
    filename = f"{uuid4()}.mp3"
    tts.save(filename)
    return filename

# Handler function
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    print(f"\n👤 USER TEXT:\n{user_text}")
    
    ai_reply = ask_gemini(f"तुम भगवद्गीतेवर आधारित एक ज्ञानी आणि प्रेमळ मार्गदर्शक आहात. वापरकर्त्याच्या भावना समजून, त्यांना प्रेमळ आणि प्रभावी उत्तर द्या.\n\nप्रश्न: {user_text}\n\nउत्तर:")
    
    print(f"🤖 AI REPLY:\n{ai_reply}")
    await update.message.reply_text(ai_reply)

    voice_file = generate_voice(ai_reply)
    with open(voice_file, "rb") as voice:
        await update.message.reply_voice(voice)
    os.remove(voice_file)

# Main
def main():
    print("📿 Gita Wisdom Gemini Bot is running...")
    print("🤖 BOT TOKEN:", TELEGRAM_BOT_TOKEN)
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.run_polling()

if __name__ == "__main__":
    main()
