import logging
from aiogram.dispatcher.filters import CommandStart
from aiogram import types

from keyboards.default.startMenuKeyboard import menuStart
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    logging.info(message.text)
    await message.answer('Salom dunyo', reply_markup=menuStart)
