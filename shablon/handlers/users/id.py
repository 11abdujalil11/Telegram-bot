from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

superusers = [1329197690]
blacklist = []


@dp.message_handler(filters.IDFilter(chat_id=superusers))
@dp.message_handler(chat_id=superusers, text='secret')
async def id_filter_users(message: types.Message):
    await message.answer('nima gap superuser')



