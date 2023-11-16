from aiogram import types

from loader import dp


@dp.message_handler(hashtags='money')
@dp.message_handler(cashtags=['eur', 'usd'])
async def hashtags_example(message: types.Message):
    await message.answer('akang kuchaydi')
