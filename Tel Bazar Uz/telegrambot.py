import logging
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode
from buttons import *
import requests
from bs4 import BeautifulSoup as BS
from aiogram.dispatcher.filters.builtin import CommandStart, Command
from aiogram import types

BOT_TOKEN = "6227637752:AAGN7NDCf_phkh0mvc1uwsoKiojYKGEpVOg"


async def on_startup(dispatcher):
    print("Bot ishlavotti")


bot = Bot(BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

t = requests.get('https://sinoptik.ua/погода-ташкент')
html_t = BS(t.content, 'html.parser')

for el in html_t.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    t_min = min[4:]
    t_max = max[5:]
    print(t_min, t_max)


@dp.message_handler(text='Toshkent')
async def enter_test(message: types.Message):
    await message.answer(
        f"Bugun Toshkentda havo {t_min} dan {t_max} gacha bo'lishi kuzatilmoqda",

        reply_markup=havvo)


@dp.message_handler(Command('start'))
async def enter_test(message: types.Message):
    await message.answer(
        f"Assslomu aleykum {message.from_user.full_name,}!",

        reply_markup=havvo)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
