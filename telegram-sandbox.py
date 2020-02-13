"""Сервер Telegram бота, запускаемый непосредственно"""
import logging
import os

import aiohttp
from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, ContentType


#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
#PROXY_URL = os.getenv("TELEGRAM_PROXY_URL")
#PROXY_AUTH = aiohttp.BasicAuth(
#   login=os.getenv("TELEGRAM_PROXY_LOGIN"),
#   password=os.getenv("TELEGRAM_PROXY_PASSWORD")
#)
# ACCESS_ID = os.getenv("TELEGRAM_ACCESS_ID")

# bot = Bot(token=API_TOKEN, proxy=PROXY_URL, proxy_auth=PROXY_AUTH)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

markup_request = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(
    KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """Отправляет приветственное сообщение и помощь по боту"""
    await message.answer(
        "Бот для тестов\n"
        "/phone_number для отправки номера телефона\n"
        "/id для отправки id\n"
        )


#bot.py
@dp.message_handler(commands=['phone_number'])
async def process_hi6_command(message: types.Message):
    await message.reply("кастомная клавиатура", reply_markup=markup_request)

@dp.message_handler(commands=['id'])
async def process_hi6_command(message: types.Message):
    user = types.User.get_current()
    await message.reply(user["id"])



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
