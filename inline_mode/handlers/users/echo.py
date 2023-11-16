from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(text='#01 KERAKLI DASTURLAR darsiga link: https://python.sariq.dev/ilk-qadamlar/01-software')
async def bot_echo(message: types.Message):
    await message.delete()
    await message.answer('Inline iwga tushdi')
