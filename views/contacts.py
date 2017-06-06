from telebot import types
from di_configuration import DIBot
from .open_menu import open_menu as menu

def contacts(message):
    bot = DIBot.di_bot()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.row('Меню')
    bot.send_message(
        message.chat.id,
        text='<b>Контактная информация</b>\n\n'
             '<b>Телефоны:</b> (846)228-00-51, (846)228-00-58\n'
             '<b>Email:</b> cdou@psati.ru\n'
             '<b>Проезд:</b> остановка "Телецентр"\n'
             '• автобусами (1, 23, 30, 37, 47, 56),\n'
             '• троллейбусами (2, 4, 12, 17, 19),\n'
             '• маршрутными такси (1, 1к, 4 (216), 21м, 23, 37, 47, 67, 91, 110, 257д, '
             '259, 269, 373, 392, 392а, 410а, 492).',
        parse_mode='HTML')
    contact_msg = bot.send_venue(
        message.chat.id,
        53.2256561, 50.1949533,
        'Физический адрес:',
        '443090, г. Самара, ул.Московское шоссе, 77, комн.201',
        reply_markup=keyboard)
    bot.register_next_step_handler(contact_msg, open_menu)

def open_menu(message):
    menu(message)

handlers = {'contacts': contacts}