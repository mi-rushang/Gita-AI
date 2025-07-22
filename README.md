Gita Wisdom Gemini Bot

A Telegram bot that provides wisdom and guidance based on the teachings of the Bhagavad Gita, powered by Google's Gemini API. The bot can understand and respond in English, Marathi, and Hindi, and it provides answers with relevant chapter and verse numbers from the Bhagavad Gita. It also features text-to-speech functionality to deliver the responses in a voice format.

About The Project

This project is a Telegram bot designed to act as a wise and compassionate mentor, drawing its knowledge from the sacred text of the Bhagavad Gita. It leverages the power of the Google Gemini API to understand user queries and generate insightful responses. Whether you are seeking guidance on life's challenges or wish to understand the philosophical teachings of the Gita, this bot is here to help.

The bot is designed to be multilingual and can interact with users in English, Marathi, and Hindi. It also converts the generated text response into an audio file, making the wisdom of the Gita more accessible.

Features

Multi-language Support: The bot can understand and respond in English, Marathi, and Hindi.

Contextual Responses: Provides answers based on the user's query with relevant chapter and verse numbers from the Bhagavad Gita.

Philosophical Guidance: Offers insights into life's questions based on the teachings of the Gita.

Text-to-Speech: Converts the AI-generated response into a voice message for a more immersive experience.

Easy to Set Up: The bot can be easily set up and deployed with a few simple steps.

Getting Started

To get a local copy up and running follow these simple steps.

Prerequisites

You need to have Python installed on your system. You will also need to have a Telegram bot token and a Google Gemini API key.

Python 3.x

Telegram Bot Token

Google Gemini API Key

Installation

Clone the repo

Generated sh
git clone https://github.com/your_username/gita-wisdom-gemini-bot.git


Navigate to the project directory

Generated sh
cd gita-wisdom-gemini-bot
```3.  **Install the required packages**
```sh
pip install -r requirements.txt
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Sh
IGNORE_WHEN_COPYING_END

Create a .env file in the root of the project and add your Telegram Bot Token and Gemini API Key.

Generated env
TELEGRAM_BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Env
IGNORE_WHEN_COPYING_END
Usage

To start the bot, run the following command in your terminal:

Generated sh
python main.py
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Sh
IGNORE_WHEN_COPYING_END

Once the bot is running, you can interact with it on Telegram by sending it messages. The bot will respond with a text message and a voice note containing the wisdom of the Bhagavad Gita.

How It Works

The bot uses the python-telegram-bot library to interact with the Telegram API. When a user sends a message, the handle_text function is triggered. This function sends the user's message to the Google Gemini API, which generates a response based on the Bhagavad Gita. The response is then sent back to the user as a text message.

The bot also uses the gTTS (Google Text-to-Speech) library to convert the text response into an audio file. This audio file is then sent to the user as a voice message.

Acknowledgments

Google Gemini

python-telegram-bot

gTTS

Bhagavad Gita
