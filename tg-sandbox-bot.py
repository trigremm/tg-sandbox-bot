import logging
import os

import aiohttp
from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, ContentType

# set logging to info level
logging.basicConfig(level=logging.INFO)
# set logging to debug leve
# logging.basicConfig(level=logging.DEBUG)

# import telegram bot token
# TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
from TELEGRAM_BOT_TOKEN import TELEGRAM_BOT_TOKEN

# set proxy config
# PROXY_URL = os.getenv("TELEGRAM_PROXY_URL")
# PROXY_AUTH = aiohttp.BasicAuth(
#   login=os.getenv("TELEGRAM_PROXY_LOGIN"),
#   password=os.getenv("TELEGRAM_PROXY_PASSWORD")
# )

# declare who can access to telegram bot
# ACCESS_ID = os.getenv("TELEGRAM_ACCESS_ID")
from TELEGRAM_ACCESS_ID import TELEGRAM_ACCESS_ID

# init bot with given options, what else can i do here?
# bot = Bot(token=API_TOKEN, proxy=PROXY_URL, proxy_auth=PROXY_AUTH)
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# init dispatcher - what is dispatcher
dp = Dispatcher(bot)

# design new keyboard markup
markup_request = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(
    KeyboardButton('send my contact ☎️', request_contact=True)
)

# here we start catching commands
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """Greeting and help message"""
    await message.answer(
        "bot to test features\n"
        "/phone_number to return phone number\n"
        "/id to return id\n"
        "/ip for ip\n"
        "/hostmane to show hostname\n"
        "/todo to show todo list\n"
        "/state to show state\n"
        "/uptime show uptime\n"
        )


#bot.py
@dp.message_handler(commands=['phone_number'])
async def process_hi6_command(message: types.Message):
    await message.reply("cusom keyboard", reply_markup=markup_request)


@dp.message_handler(commands=['/user'])
async def process_hi6_command(message: types.Message):
    user = types.User.get_current()
    await message.reply(user)


@dp.message_handler(commands=['id'])
async def process_hi6_command(message: types.Message):
    user = types.User.get_current()
    await message.reply(user["id"])


@dp.message_handler(commands=['todo'])
async def process_hi6_command(message: types.Message):
    await message.reply('this is /todo option')


@dp.message_handler(commands=['state'])
async def process_hi6_command(message: types.Message):
    await message.reply('this is /state option')


@dp.message_handler(commands=['ip'])
async def process_hi6_command(message: types.Message):
    await message.reply('this is /ip option')


# what other types can i use ?
@dp.message_handler(content_types=ContentType.CONTACT)
async def echo2(message: types.Message):
    """ echo """
    await message.answer(message.contact["phone_number"])


@dp.message_handler()
async def echo(message: types.Message):
    """ echo """
    user = types.User.get_current()
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
