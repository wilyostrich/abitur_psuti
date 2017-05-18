from telebot import types
from main import bot
import main

class Start():
    @bot.message_handler(commands=['start'])
    def start_message(message):
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, 'Привет! Здесь собрана достоверная информация о Поволжском государственном '
                                          'университете телекоммуникаций и информатики', reply_markup=markup)
        main.help_message(message)