from telebot import types


#@bot.message_handler(commands=['start'])
def start_message(message, bot):
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, 'Привет! Здесь собрана достоверная информация о Поволжском государственном '
                                      'университете телекоммуникаций и информатики', reply_markup=markup)
    #help_message(message)

handlers = {'start': start_message}