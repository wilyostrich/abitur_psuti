from telebot import types
from di_configuration import DIBot
from .open_menu import open_menu as menu


def about_dev(message):
    bot = DIBot.di_bot()
    inline_key = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="ПРИСОЕДИНЯЙСЯ!", url="https://vk.com/itclub_psuti")
    inline_key.add(url_button)
    about_msg = bot.send_message(
        message.chat.id,
        text='Чат-бот разработан студентами <b>ИТ-клуба ПГУТИ</b> для будующих студентов.'
             '\nБудем рады увидеть Вас в наших рядах!'
             '\nhttps://pp.vk.me/c629125/v629125487/21029/Qd9czt4U02E.jpg',
        parse_mode='HTML',
        reply_markup=inline_key)
    bot.register_next_step_handler(about_msg, open_menu)


def open_menu(message):
    menu(message)

handlers = {'about': about_dev}


