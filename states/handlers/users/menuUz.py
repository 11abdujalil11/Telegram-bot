from aiogram import types
from state.personalData import PersonalData
from aiogram.dispatcher import FSMContext
from .w_users import w_users
from loader import dp


@dp.message_handler(text='uz', state=PersonalData.language)
async def lan_uz(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['lan'] = message.text
    await message.answer(text='Ims kiriting:')
    await PersonalData.fullName_uz.set()


@dp.message_handler(state=PersonalData.fullName_uz)
async def state_ful_ru(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fullname_ru'] = message.text
    await message.answer(text='Email kiriting: ')
    await PersonalData.email_uz.set()


@dp.message_handler(state=PersonalData.email_uz)
async def state_email_ru(message: types.Message, state: FSMContext):
    await state.update_data(email_ru=message.text)
    await message.answer(text='Tel kiriting', )
    await PersonalData.phoneNum_uz.set()


@dp.message_handler(state=PersonalData.phoneNum_uz)
async def state_phone_ru(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_ru'] = message.text
    await w_users(state)
    await message.answer(text=f'tugadi')
    await state.finish()
