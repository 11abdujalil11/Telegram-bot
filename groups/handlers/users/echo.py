import datetime

import asyncio
from aiogram.utils.exceptions import BadRequest
import aiogram
from aiogram import types
from filters import IsPrivate
from aiogram.dispatcher.filters.builtin import Text
import re
from loader import dp

list = ['axmoq', 'jinni', 'qoy', 'mol', 'iflos']


@dp.message_handler(lambda x: any(i in x.text.lower() for i in list))
async def ro_command(message: types.Message):
    member_id = message.from_user.id
    command_parse = re.compile(r"(!ro|/ro) ?(\d+)? ?([\w+\D]+)?")
    parsed = command_parse.match('/ro')
    time = 5
    comment = 'Bizning guruhda axmoq diyish mumkun emas'
    until_date = datetime.datetime.now() + datetime.timedelta(minutes=time)
    try:
        await message.chat.restrict(user_id=member_id, can_send_messages=False, until_date=until_date)
    except aiogram.utils.exceptions.BadRequest as err:
        await message.answer(f"Xatolik! {err.args}")
        return

    await message.answer(
        f"Foydalanuvchi {message.from_user.full_name} {time} minut yozish huquqidan mahrum qilindi.\n"
        f"Sabab: \n<b>{comment}</b>")


# Echo bot
@dp.message_handler(IsPrivate(), state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)
