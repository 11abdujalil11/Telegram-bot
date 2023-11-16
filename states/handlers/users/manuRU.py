from state.personalData import PersonalData
from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp


@dp.message_handler(text='ru', state=PersonalData.language)
async def lan_uz(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['lan'] = message.text
    await message.answer(text='Введите свое имя:')
    await PersonalData.fullName_ru.set()


@dp.message_handler(state=PersonalData.fullName_ru)
async def state_ful_ru(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fullname_ru'] = message.text
    await message.answer(text='Введите Email')
    await PersonalData.email_ru.set()


@dp.message_handler(state=PersonalData.email_ru)
async def state_email_ru(message: types.Message, state: FSMContext):
    await state.update_data(email_ru=message.text)
    await message.answer(text='введите номер телефона')
    await PersonalData.phoneNum_ru.set()


@dp.message_handler(state=PersonalData.phoneNum_ru)
async def state_phone_ru(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_ru'] = message.text
        name = data.get('fullname_ru')
        email = data.get('email_ru')
        phone = data.get('phone_ru')

    await message.answer(text=f'{name}\n{email}\n{phone}')
    await state.finish()
