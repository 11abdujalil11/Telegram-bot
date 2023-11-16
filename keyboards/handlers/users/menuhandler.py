import logging

from keyboards.inline.callback_data import course_callback, book_callback
from keyboards.inline.productsKeyboard import categoryMenu, coursesMenu, booksMenu
from aiogram.dispatcher.filters import Text
from aiogram import types

from loader import dp


@dp.message_handler(Text(equals='Mahsulotlar'))
async def select_category(message: types.Message):
    await message.answer('Mahsulot tanlang', reply_markup=categoryMenu)


@dp.callback_query_handler(text='courses')
async def buy_courses(callback: types.CallbackQuery):
    await callback.message.answer('Kursni tanlang', reply_markup=coursesMenu)
    await callback.answer(cache_time=60)


@dp.callback_query_handler(text='books')
async def buy_books(callback: types.CallbackQuery):
    await callback.message.answer('Kitoboblar', reply_markup=booksMenu)
    await callback.message.delete()
    await callback.answer(cache_time=3600)


@dp.callback_query_handler(course_callback.filter(item_name='python'))
async def wive_python(callback: types.CallbackQuery, callback_data: dict):
    logging.info(callback_data)
    await callback.answer('ok', show_alert=True)


@dp.callback_query_handler(book_callback.filter(item_name='cpp_book'))
async def wive_book(call: types.CallbackQuery):
    await call.answer('ok', show_alert=True)
