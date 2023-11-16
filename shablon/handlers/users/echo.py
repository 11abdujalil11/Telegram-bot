from aiogram import types
from filters.IsGroupFilter import IsGroupFilter
from loader import dp


# Echo bot
@dp.message_handler(IsGroupFilter(),state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)
