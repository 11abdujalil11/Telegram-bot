from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.IsPrivate import IsPrivate
from loader import dp

"""deep_link - botni reaklama qilganda qaysi gurgdan qoshilganini bilish"""


# @dp.message_handler(CommandStart(deep_link='kunuz'))
# async def bot_start(message: types.Message):
#     await message.answer(text=f'{message.from_user.full_name} siz '
#                               f'{message.get_args()} kanalidan bizning botimizga qoshildingiz!')


@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
