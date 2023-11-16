from aiogram import Bot, Dispatcher, executor, types
import wikipedia

wikipedia.set_lang('uz')
token = '6002308972:AAFn5mmiJReNOUmHuyBvWMpZGllAJQ1qLNs'


bot = Bot(token=token)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(text='Wikipedia botimizga xush kelibsiz')


@dp.message_handler()
async def send_wikipedia(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(text=respond)
    except Exception as err:
        await message.answer(text=f'{message.text} ga malumot topilmadi')
        print(err)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)
