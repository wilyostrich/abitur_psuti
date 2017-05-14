import telebot
from telebot import types
import configparser
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Specialty

config = configparser.ConfigParser()
config.read('config.ini', encoding = 'UTF-8')

engine = create_engine("postgresql://postgres:1234@localhost/abitur")
Session = sessionmaker(bind=engine)
session = Session()
fields = session.query(Specialty)
numb_fields = fields.count()


bot = telebot.TeleBot(config["DEFAULT"]["Token"])

def pages_keyboard(numb):
    """Формируем Inline-кнопки для перехода по страницам.
    """
    keyboard = types.InlineKeyboardMarkup()
    btns = []
    if numb > 1: btns.append(types.InlineKeyboardButton(
        text='<', callback_data='to_{}'.format(numb - 1)))
    if numb < numb_fields: btns.append(types.InlineKeyboardButton(
        text='>', callback_data='to_{}'.format(numb + 1)))
    keyboard.add(*btns)
    return keyboard # возвращаем объект клавиатуры

@bot.message_handler(commands=['start'])
def start(m):
    """Отвечаем на команду /start
    """
    spec = session.query(Specialty).filter_by(id_spec=1).first()
    bot.send_message(m.chat.id, 'Название: {}\nЭкзамены: {}\nСсылка на профиль: {}?'
                                '\nБюджетные места: {}\nКонтрактные места: {}'
                                '\nЦена контракт: {}'.format(spec.name,spec.examinations,
                                                                    spec.prof_link,spec.budgetary_place,
                                                                    spec.contract_places,spec.cost),
                     parse_mode='Markdown',disable_web_page_preview=True,reply_markup=pages_keyboard(1))

@bot.callback_query_handler(func=lambda c: c.data)
def pages(c):
    """Редактируем сообщение каждый раз, когда пользователь переходит по
    страницам.
    """
    print(c.data[3:])
    print(numb_fields)
    if int(c.data[3:]) <= numb_fields:
        spec = session.query(Specialty).filter_by(id_spec=c.data[3:]).first()
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            disable_web_page_preview=True,
            text='Название: {}\nЭкзамены: {}\nСсылка на профиль: {}\nБюджетные места: {}\nКонтрактные места: {}'
                                    '\nЦена контракт: {}'.format(spec.name,spec.examinations,spec.prof_link,
                                                                 spec.budgetary_place,spec.contract_places,spec.cost),
            parse_mode='Markdown',
            reply_markup=pages_keyboard(int(c.data[3:])))
    elif int(c.data[3:]) > numb_fields:
        start()

bot.polling()