from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from handlers.users.w_users import r_users, r_message_users, r_users_id, w_user_id
from loader import dp
from state.personalData import PersonalData

lan = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='uz'),
     KeyboardButton(text='ru')]
], resize_keyboard=True)


@dp.message_handler(commands=['start'], state='*')
async def cm_start(message: types.Message):
    if str(message.from_user.id) in r_users_id():
        return await message.answer("Ro'yxatdan o'tkansiz")
    else:
        w_user_id(message.from_user.id)
        await message.answer(text='Til tanlang: ',
                             reply_markup=lan)
        await PersonalData.language.set()


@dp.message_handler(commands=['users'], state='*')
async def cm_users(message: types.Message):
    user_count = r_users()
    await message.answer(text=user_count)


@dp.message_handler(commands=['users_message'], state='*')
async def cm_users_message(message: types.Message):
    message_list = r_message_users()
    for i in range(len(message_list)):
        await message.answer(text=message_list[i])
