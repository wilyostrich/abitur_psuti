import telebot
from telebot import types
from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData

TOKEN = '370462510:AAElsbNsJwqO9P0Ucuv6XHJQc7AH-5Xjw68'
bot = telebot.TeleBot(TOKEN)
engine = create_engine("postgresql://postgres:1234@localhost/abitur")
meta = MetaData(bind=engine, reflect=True)
table = meta.tables['balls']
for i in range(1,3):
    res = []
    res.append(list(engine.execute(table.select(table.c.code == i))))
    print(res)


def pages_keyboard(start, stop):
    """Формируем Inline-кнопки для перехода по страницам.
    """
    keyboard = types.InlineKeyboardMarkup()
    btns = []
    if start > 0: btns.append(types.InlineKeyboardButton(
        text='Назад', callback_data='to_{}'.format(start - 900)))
    if stop < len(lis): btns.append(types.InlineKeyboardButton(
        text='Дальше', callback_data='to_{}'.format(stop)))
    keyboard.add(*btns)
    return keyboard # возвращаем объект клавиатуры

@bot.message_handler(commands=['start'])
def start(m):
    """Отвечаем на команду /start
    """
    bot.send_message(m.chat.id, '{0} {1}'.format(lis[0][1],lis[0][2]), parse_mode='Markdown',
        reply_markup=pages_keyboard(0, 900))

@bot.callback_query_handler(func=lambda c: c.data)
def pages(c):
    """Редактируем сообщение каждый раз, когда пользователь переходит по
    страницам.
    """
    bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=BOOK[int(c.data[3:]):int(c.data[3:]) + 900],
        parse_mode='Markdown',
        reply_markup=pages_keyboard(int(c.data[3:]),
            int(c.data[3:]) + 900))




bot.polling()