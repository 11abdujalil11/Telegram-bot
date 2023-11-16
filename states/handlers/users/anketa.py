from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Regexp

from loader import dp
from state.personalData import PersonalData

EMAIL_REGEX = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
PHONE_NUM = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'


@dp.message_handler(Command('anketa'))
async def enter_test(message: types.Message):
    await message.answer("To'li'g ismingizni kiriting: ")
    await PersonalData.fullName.set()


@dp.message_handler(state=PersonalData.fullName)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    # 1 chi usul
    # await state.update_data(fullname=fullname)
    # 2 chi usul
    await state.update_data(
        {"fullname": fullname}
    )
    # 3 chi uslul
    # async with state.proxy() as data:
    #     data['fullname'] = fullname
    await message.answer('email manzil kiriting: ')
    await PersonalData.next()


@dp.message_handler(Regexp(EMAIL_REGEX), state=PersonalData.email)
async def answer_email(message: types.Message, state: FSMContext):
    email = message.text
    # await state.update_data(email=email)
    await state.update_data(
        {"email": email}
    )
    await message.answer('Telefon nomeringizni kiriting: ')
    await PersonalData.next()


@dp.message_handler(lambda x: x != Regexp(EMAIL_REGEX), state=PersonalData.email)
async def answer_email(message: types.Message, state: FSMContext):
    await message.answer('Email xato')


@dp.message_handler(Regexp(PHONE_NUM), state=PersonalData.phoneNum)
async def answer_email(message: types.Message, state: FSMContext):
    phone = message.text
    # await state.update_data(phone=phone)
    await state.update_data(
        {"phone": phone}
    )
    # data = await state.get_data()
    async with state.proxy() as data:
        name = data.get('fullname')
        email = data.get('email')
        phone = data.get('phone')

        await message.answer(f'{name} {email} {phone}')
    await state.finish()
    # await state.reset_state(with_data=False)


@dp.message_handler(lambda x: x != Regexp(PHONE_NUM), state=PersonalData.phoneNum)
async def answer_email(message: types.Message):
    await message.answer('Nomeri togri kiriting: ')
