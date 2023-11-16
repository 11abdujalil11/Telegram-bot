from aiogram import types

from aiogram.dispatcher import FSMContext

from loader import dp


@dp.message_handler(commands='xarid')
async def set_state(message: types.Message, state: FSMContext):
    await state.set_state('xarid_state')
    await message.answer('Nahsulot tanlang: ')


@dp.message_handler(state='xarid_state')
async def state_example(message: types.Message, state: FSMContext):
    await message.answer('raxmat')
    await state.finish()




















