from aiogram import types

from loader import dp
from state.personalData import PersonalData


@dp.message_handler(commands=['help'], state=PersonalData.fullName)
async def help_state(message: types.Message):
    await message.answer("royxatdan otish uchun ism familiyangizni kiriitng: ")
