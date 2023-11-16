from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

inline = types.InlineKeyboardMarkup(inline_keyboard=[
    [types.InlineKeyboardButton(text='rasm', switch_inline_query_current_chat='rasm')]
])


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",
                         reply_markup=inline)
