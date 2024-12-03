# Imports
from aiogram import Bot, Dispatcher, html
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import asyncio
from dotenv import load_dotenv
import logging
import openai
import os
import sys

# Loading dot environment
load_dotenv()


##### Open AI side ######

# setting api key

openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAiBot:
    """
    class which maintains the openai api operation
    """

    def __init__(self):
        """
        Initilising openai chat completion parameters
        """
        self.model_name = "gpt-3.5-turbo"
        self.conversation_history = [{"role":"assistant", "content":"you are AI assistant"}]
        self.max_tokens = 3000
        self.memory_limit = 500

    def update_conversation(self, role, content):
        """
        Keep track of all the conversation. 

        """
        self.conversation_history.append({"role":role, "content":content})
        self.memory_manager()


    def memory_manager(self):
        """
        helps to maintain conversation history under max memory limit
        """
        total_tokens = sum(len(message["content"].split()) for message in self.conversation_history)

        while total_tokens > self.memory_limit:
            self.conversation_history.pop(0)
            total_tokens = sum(len(message.content) for message in self.conversation_history)


    def get_response(self, prompt):
        """
        Getting response from open ai api, updates conversation history
        """

        self.update_conversation(role="user", content=prompt)
        
        try:
            response = openai.ChatCompletion.create(
                model = self.model_name,
                messages = self.conversation_history,
                max_tokens = self.max_tokens
            )
            assistance_message = response.choices[0].message.content
            self.update_conversation(role="assistant", content =assistance_message)
            return assistance_message
        except Exception as e:
            return f"{e} occured!"

    def reset_memory(self):
        """
        Resetting chat memory helps to start new conversation
        """
        self.conversation_history = [{"role":"assistant", "content":"you are AI assistant"}]


# Initilasing the bot
assistant = OpenAiBot()



##### Telegram side #####

# openai_NandhuGB_bot api key

telebot_token = os.getenv("TELEBOT_API_KEY")

dp = Dispatcher()


## Handlers ##

# /start handler
@dp.message(CommandStart())
async def command_start_handler(message:Message):
    """ 
    This handles the first message after the "/start"
    """
    
    assistant.reset_memory()
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}! Im NandhuGB, AI assistant.How can i help you today?")


# /help handler
@dp.message(Command("help"))
async def help_handler(message:Message):
    """ 
    This handles the command /help handled
    """
    text = """
    Here is some usefull commands to get more out this bot:
    /start - start chatting with Ai assistant
    /help -  get all commands
    /clear -  clear previous chats or reset bot memory
    /info - get more information about this bot
    """
    await message.answer(text)


# /info handler
@dp.message(Command("info"))
async def info_handler(message:Message):
    """
    This handles the command "/info"
    """
    text = """ 
    This AI assistant bot powered by open AI. Feel free to ask me anything!
    """
    await message.answer(text)

# /clear handler
@dp.message(Command("clear"))
async def clear_handler(message:Message):
    """ 
    This handler clears all the memory on the  ai assistant
    """
    assistant.reset_memory()
    await message.answer("Memory has been cleared sucessfully!.")


# Echo Handler
@dp.message()
async def echo_handler(message:Message):
    """ 
    This handles any receiving message, except for the first message. This replies the same message back to the user
    """
    try:
        response = assistant.get_response(message.text)
        await message.answer(response)
    except TypeError:
        await message.answer(f"UNSUPPORTED TYPE: {message}, please try again with supported type inputs")


@dp.message()
async def main():
    """ 
    Initilisng bot
    """
    bot = Bot(token = telebot_token, default =DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__=="__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())