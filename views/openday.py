from telebot import types
#from views import general
from config import config
from views import open_menu as menu #возможный костыль

def openday(message, bot):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.row('Меню')
    open_d = bot.send_message(
        message.chat.id,
        'Приглашаем всех желающих (абитуриентов, школьников и их родителей) на День открытых дверей в ПГУТИ.'
        ' Экскурсии по вузу, презентации направлений подготовки, ответы на всевозможные вопросы по'
        ' процессу обучения в университете - всё это и многое другое ждёт вас на днях открытых дверей в Самаре\n\n'
        'Ближайший День открытых дверей в ПГУТИ состоится {} года по адресу:'
        ' Московское шоссе, д. 77 (2-й корпус ПГУТИ). \nНачало в 10:00 по самарскому времени.\n'
        'Актуальную и подробную информацию Вы можете узнать на сайте '
        'https://abitur.psuti.ru/ и в группе ВК https://vk.com/abiturpsuti'.format(config["OPENDAY"]["data"]),
        disable_web_page_preview=True,
        reply_markup=keyboard)
    bot.register_next_step_handler(open_d, menu.open_menu)

# def open_menu(message):
#     if message.text == 'Меню':
#         general.help_message(message,bot)
#     else:
#         test = message.text
#         print(test)
#         msg_understand = bot.send_message(
#             message.chat.id,
#             'Я Вас не понял, повторите попытку или используйте кнопку Меню для выхода в меню')
#         bot.register_next_step_handler(msg_understand, open_menu)

handlers = {'openday': openday}
