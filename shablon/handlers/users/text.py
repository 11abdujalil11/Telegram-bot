from aiogram import types

from aiogram.dispatcher.filters import Text

from loader import dp

"""equals - tenglik , contains - ichida bolsa , startswith - boshida bolsa , endswith -oxirida bolsa"""


@dp.message_handler(Text(equals='Nima gap', ignore_case=True))
@dp.message_handler(Text(contains='nima gap', ignore_case=True))
@dp.message_handler(Text(startswith='nima gap', ignore_case=True))
@dp.message_handler(Text(endswith='nima gap', ignore_case=True))
async def text(message: types.Message):
    await message.answer('tinchku')
