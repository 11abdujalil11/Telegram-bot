from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

""" types.ContentTypes.PHOTO -- message turi rasmligini anglatadi """


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_handler(message: types.Message):
    await message.answer('sanga oxwidi')
