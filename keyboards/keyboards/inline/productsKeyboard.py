from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_data import course_callback, book_callback
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
categoryMenu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='💻 Kurslar', callback_data='courses'),
        InlineKeyboardButton(text='📚 Kitoblar', callback_data='books')
    ],
    [
        InlineKeyboardButton(text='🔗 Bizning sahifamiz', url='https://t.me/fozilovbekzod')
    ],
    [
        InlineKeyboardButton(text='🔎 Qidirish', switch_inline_query_current_chat="")
    ],
    [
        InlineKeyboardButton(text='🚀 Ulashish', switch_inline_query="Zo'r bot ekan")
    ]
]
)

coursesMenu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='🐍 Python Dasturlash Asoslari', callback_data=course_callback.new(item_name='python'))
    ],
    [
        InlineKeyboardButton(text='🌎 Django Web Dasturlash', callback_data=course_callback.new(item_name='django'))
    ],
    [
        InlineKeyboardButton(text='🤖 Mukammal Telegram Bot', callback_data='course:telegram')
    ],
    [
        InlineKeyboardButton(text='📉 Malumotlar Tuzilmasi va Algaritomlar', callback_data='course:algorithm')
    ]
]
)
back_button = InlineKeyboardButton(text='🔙 Ortga', callback_data='cancel')
coursesMenu.add(back_button)

books = {
    'Python. Dasturlash Asoslari': 'python_book',
    'C++. Dasturlsah tili': 'cpp_book',
    'Mukammal Dasturlash. JavaScript': 'js_book'
}

list_time = [
    '7:00', '8:00'
]

booksMenu = InlineKeyboardMarkup()
time_markup = ReplyKeyboardMarkup()
for key, value in books.items():
    booksMenu.add(InlineKeyboardButton(text=key, callback_data=book_callback.new(item_name=value)))
booksMenu.add(back_button)

for i in list_time:
    if i not in list:
        time_markup.add(KeyboardButton(text=i))
