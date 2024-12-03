# OpenAI-Powered Telegram Bot

This project is a Telegram bot that integrates with OpenAI's GPT-3.5-turbo model to provide AI-powered conversational capabilities. Users can interact with the bot to get answers, reset chat memory, and receive assistance in a conversational manner.

---

## Features

- **OpenAI Integration**: Uses GPT-3.5-turbo for intelligent conversational responses.
- **Memory Management**: Maintains conversation history with a memory limit to ensure efficient performance.
- **Command Handlers**:
  - `/start`: Begin a conversation with the bot.
  - `/help`: List available commands.
  - `/info`: Learn more about the bot.
  - `/clear`: Reset the bot's memory to start a new conversation.
- **Echo Responses**: Replies to user messages with AI-generated responses.

---

## Prerequisites

Before running the bot, ensure you have the following installed:

- Python 3.9 or higher
- Telegram Bot API token
- OpenAI API key
- `dotenv` for environment variable management
- `aiogram` for Telegram bot handling

---

## Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:NandhuGB/Telebot.git
   cd Telebot

2. Install required Python packages:
     
   ```bash
   pip install -r requirements.txt

3. Create a .env file in the project root directory and add the following keys:

   ```env
   TELEBOT_API_KEY = your_telegram_bot_token
   OPENAI_API_KEY = your_openai_api_key


## Usage

1. Run the bot using:

   ```bash
   python bot.py

2. Interact with the bot via Telegram:

   * Start a conversation using /start.
   * Clear chat memory using /clear.
   * Get help with /help.
   * Learn more about the bot with /info.
   * Send any message to receive an AI-generated response.


## Project Structure

   * bot.py: Main script to initialize and run the bot.
   * OpenAiBot: A class to handle OpenAI API interactions, including memory management and response   generation.

* Handlers:
   *  Command handlers for /start, /help, /info, and /clear.
   *  General message handler to process user inputs and return AI-generated responses.

## Acknowledgments

    OpenAI for their powerful language models.
    Telegram for their API and platform.
    Aiogram for the Telegram bot framework.


