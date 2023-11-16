import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State

API_KEY = 'ab96c832590aa3876667ad16'

token = '6002308972:AAFn5mmiJReNOUmHuyBvWMpZGllAJQ1qLNs'

storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot=bot, storage=storage)


class Money(StatesGroup):
    step1 = State()
    step2 = State()


markup = ReplyKeyboardMarkup(resize_keyboard=True)
usd = KeyboardButton(text='USD')
uzs = KeyboardButton(text='UZS')
rus = KeyboardButton(text='RUB')
markup.add(usd, rus).add(uzs)


async def on_startup(_):
    print('Bot ishga tushdi')


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(text='Pul birligini tanlang: ',
                         reply_markup=markup)
    await Money.step1.set()


@dp.message_handler(lambda message: message.text in ['USD', 'UZS', 'RUB'], state=Money.step1)
async def cmd_currency(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['step1'] = message.text
    await message.answer('Pul birligini tanlang: ',
                         reply_markup=markup)
    await Money.next()


@dp.message_handler(lambda message: message.text in ['USD', 'UZS', 'RUB'], state=Money.step2)
async def cmd_money(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['step2'] = message.text
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{data['step1']}/{data['step2']}"
    respond = requests.get(url)
    await message.answer(text=f"{data['step1']} ==> {data['step2']} = {(respond.json()['conversion_rate'])}")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
