from telebot import types
from views import general
from di_configuration import DIConfige, DIBot

def course(message):
    bot = DIBot.di_bot()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.row('Инженерный лицей', 'Школа программистов')
    keyboard.row('Подготовка к ЕГЭ и внутренним экзаменам')
    keyboard.row('Меню')
    msg = bot.send_message(message.chat.id, 'Выберите интересующий вас курс!', reply_markup=keyboard)
    bot.register_next_step_handler(msg,course_info)


def course_info(message):
    config = DIConfige.config_ini()
    bot = DIBot.di_bot()
    if message.text == 'Подготовка к ЕГЭ и внутренним экзаменам':
        bot.send_message(message.chat.id, text=config["COURSE"]["ege"], parse_mode='HTML')
        msg_exam = bot.send_message(message.chat.id, 'Получить более подробную информаци, а также записаться на курсы,'
                                                     ' можно перейдя по ссылке: http://abitur.psuti.ru/'
                                                     'center/podgotovitelnye-kursy-k-ege-i-vnutrennim-ekzamenam/',
                                    disable_web_page_preview=True)
        bot.register_next_step_handler(msg_exam, course_info)
    elif message.text == 'Школа программистов':
        bot.send_message(message.chat.id, '<b>Школа программистов</b>\n'
                                          'Обучение платное для учащихся 8-х, 9-х, 10-х и 11-х классов, проводится '
                                          'в 3 этапа:\n'
                                          '1. Информатика;\n'
                                          '2. Программирование;\n'
                                          '3. Информационные системы и технологии.\n'
                                          'Срок обучения в школе – 5 месяцев.\n'
                                          'Окончившим Школу программистов выдается «Свидетельство об окончании», '
                                          'которое дает право преимущественного зачисления в ПГУТИ.\n'
                                          'Справки по телефону: (846) 228-00-51,  (846) 228-00-58.', parse_mode='HTML')
        msg_school = bot.send_message(message.chat.id, 'Получить более подробную информаци, а также записаться в школу '
                                                       'программистов, можно перейдя по ссылке: '
                                                       'http://abitur.psuti.ru/center/shkola-programmistov/',
                                      disable_web_page_preview=True, parse_mode='HTML')
        bot.register_next_step_handler(msg_school, course_info)
    elif message.text == 'Инженерный лицей':
        bot.send_message(message.chat.id, text=config["COURSE"]["engineer"], parse_mode='HTML')
        msg_engineer = bot.send_message(message.chat.id, 'Получить более подробную информаци, а также '
                                                         'записаться на занятия, можно перейдя по ссылке: '
                                                         'http://abitur.psuti.ru/center/inzhenernyy-litsey/',
                                        disable_web_page_preview=True, parse_mode='HTML')
        bot.register_next_step_handler(msg_engineer, course_info)
    elif message.text == 'Меню':
        general.help_message(message)
    else:
        try:
            if message.text == 'Меню':
                general.help_message(message)
        except:
            print('ERROR')

handlers = {'course': course}