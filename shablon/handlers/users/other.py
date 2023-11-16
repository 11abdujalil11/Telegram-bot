from aiogram import types
from filters.AdminFilter import AdminFilter
from aiogram.dispatcher import filters

from loader import dp


# isReplyFilter  -- javob qaytarilgan message tekshirish
@dp.message_handler(AdminFilter(),is_reply=True, commands='user_id')
async def relpy_filter(message: types.Message):
    await message.answer(message.reply_to_message.from_user.id)


# isSenderContact -- jonatilgan contact ozinikiligini tekshirish
@dp.message_handler(content_types=['contact'], is_sender_contact=True)
async def sender_contact(message: types.Message):
    await message.answer('Raxmat qabul qilindi')


# forwardedMessage -- jonatilgan messageligini tekshirish
@dp.message_handler(is_forwarded=True)
async def forwarded(message: types.Message):
    await message.answer("sani sms mas bu")


# ChatTypeFilter -- chat turini tekshiruvchi filter
@dp.message_handler(chat_type='private', commands='is_pm')
@dp.message_handler(filters.ChatTypeFilter(types.ChatType.PRIVATE), commands=['shaxsiy'])
async def chat_type(message: types.Message):
    await message.answer('Bu shaxsiy chat')
