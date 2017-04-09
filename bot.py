import telebot
from telebot import types
import configparser

config = configparser.ConfigParser()
config.read('config.ini', encoding = 'UTF-8')


bot = telebot.TeleBot(config["DEFAULT"]["Token"])


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Хочешь стать крутым IT-специалистом или cвязистом? Тогда тебе к нам!')
    bot.send_message(message.chat.id, 'Я помогу тебе узнать немного больше о нашем ВУЗе! Воспользуйся простыми '
                                      'командами чтобы узнать интересующую тебя информацию!\n'
                                      '/course - Курсы для абитуриентов\n'
                                      '/specialties - Направления подготовки\n'
                                      '/guide - Руководство по поступлению\n'
                                      '/rating - Узнай свой рейтинг\n'
                                      '/contacts - Контактая информация\n'
                                      '/calculator - Подсчитай свои баллы и узнай на какую спецальность ты проходишь\n'
                                      '/studorganizations - внеучебная деятельность\n'
                                      '/about - О разработчитах\n'
                                      '/excursion - интерактивная экскурсия по университету')


@bot.message_handler(commands=['course'])
def course(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.row('Инженерный лицей', 'Школа программистов')
    keyboard.row('Подготовка к ЕГЭ и внутренним экзаменам')
    msg = bot.send_message(message.chat.id, 'Выберите интересующий вас курс!', reply_markup=keyboard)
    bot.register_next_step_handler(msg, course_info)


def course_info(message):
    if message.text == 'Подготовка к ЕГЭ и внутренним экзаменам':
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, text=config["COURSE"]["ege"], parse_mode='HTML', reply_markup=markup)
        #link = types.InlineKeyboardMarkup()
        #url_button = types.InlineKeyboardButton(text="Записаться на курсы!",
                                                #url="http://abitur.psuti.ru/center/podgotovitelnye-kursy-k-ege-i-vnutrennim-ekzamenam/")
        #link.add(url_button)
        #bot.send_message(message.chat.id, "Получить более подробную информаци, а также записаться на курсы,"
                                          #" можно перейдя по кнопке.",reply_markup=link)
        bot.send_message(message.chat.id, 'Получить более подробную информаци, а также записаться на курсы,'
                                          ' можно перейдя по ссылке: http://abitur.psuti.ru/center/podgotovitelnye-kursy-k-ege-i-vnutrennim-ekzamenam/', disable_web_page_preview=True)
    elif message.text == 'Школа программистов':
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, '<b>Школа программистов</b>\n'
                                          'Обучение платное для учащихся 8-х, 9-х, 10-х и 11-х классов, проводится в 3 этапа:\n'
                                          '1. Информатика;\n'
                                          '2. Программирование;\n'
                                          '3. Информационные системы и технологии.\n'
                                          'Срок обучения в школе – 5 месяцев.\n'
                                          'Окончившим Школу программистов выдается «Свидетельство об окончании», которое дает право преимущественного зачисления в ПГУТИ.\n'
                                          'Справки по телефону: (846) 228-00-51,  (846) 228-00-58.', reply_markup=markup, parse_mode='HTML')
        bot.send_message(message.chat.id, 'Получить более подробную информаци, а также записаться в школу программистов,'
                                          ' можно перейдя по ссылке: http://abitur.psuti.ru/center/shkola-programmistov/', disable_web_page_preview=True, parse_mode='HTML')
    elif message.text == 'Инженерный лицей':
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, text=config["COURSE"]["engineer"], reply_markup=markup, parse_mode='HTML')
        bot.send_message(message.chat.id, 'Получить более подробную информаци, а также записаться на занятия,'
                                          ' можно перейдя по ссылке: http://abitur.psuti.ru/center/inzhenernyy-litsey/',
                         disable_web_page_preview=True, parse_mode='HTML')
    else:
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, 'Я Вас не понял, попробуйте еще раз /course '
                                          'или воспользуйтесь /help для справки.', reply_markup=markup)


@bot.message_handler(commands=['specialties'])
def specialties(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add('Академический бакалавриат')
    keyboard.add('Прикладной бакалавриат')
    keyboard.add('Специалитет')
    msg = bot.send_message(message.chat.id, 'Выберите необходимую степень!', reply_markup=keyboard)
    bot.register_next_step_handler(msg, specialties_info)


def specialties_info(message):
    if message.text == 'Академический бакалавриат':
        bot.send_message(message.chat.id, 'Академический бакалавриат')
    elif message.text == 'Прикладной бакалавриат':
        bot.send_message(message.chat.id, 'Прикладной бакалавриат')
    elif message.text == 'Специалитет':
        bot.send_message(message.chat.id, 'Специалитет')


@bot.message_handler(commands=['guide'])
def guide(message):
    bot.send_message(message.chat.id, "Тест!")


@bot.message_handler(commands=['rating'])
def rating(message):
    bot.send_message(message.chat.id, "Тест!")


@bot.message_handler(commands=['contacts'])
def contacts(message):
    bot.send_message(message.chat.id, text='<b>Контактная информация</b>\n\n'
                                           '<b>Телефоны:</b> '
                                           '(846)228-00-51, '
                                           '(846)228-00-58\n'
                                           '<b>Email:</b> '
                                           'cdou@psati.ru\n'
                                           '<b>Проезд:</b> '
                                           'остановка "Телецентр"\n'
                                           '• автобусами (1, 23, 30, 37, 47, 56),\n'
                                           '• троллейбусами (2, 4, 12, 17, 19),\n'
                                           '• маршрутными такси (1, 1к, 4 (216), 21м, 23, 37, 47, 67, 91, 110, 257д, 259, 269, 373, 392, 392а, 410а, 492).', parse_mode='HTML')
    bot.send_venue(message.chat.id, 53.2256561, 50.1949533, 'Физический адрес:', '443090, г. Самара, ул.Московское шоссе, 77, комн.201')


@bot.message_handler(commands=['calculator'])
def calculator(message):
    bot.send_message(message.chat.id, "Тест!")


@bot.message_handler(commands=['studorganizations'])
def studorganizations(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(text=orgname, callback_data=orgname)
                   for orgname in ['РСО', 'Профком', 'СМЦ',
                                   'IT-клуб ПГУТИ', 'Спортивные секции']])
    bot.send_message(message.chat.id, 'Про каждую организация можно узнав перейдя в '
                                      'интересующий раздел.', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    if c.data == 'IT-клуб ПГУТИ':
        keyboard = types.InlineKeyboardMarkup()
        vk_button = types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/itclub_psuti")
        inst_button = types.InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/itclub_psuti/")
        keyboard.add(vk_button, inst_button)
        bot.send_message(c.message.chat.id, text=config["ORG_INFORMATION"]["itclub"], parse_mode='HTML',reply_markup=keyboard)
        bot.send_photo(c.message.chat.id, photo="https://pp.userapi.com/c623223/v623223296/234e/vqj_1H5X-Bs.jpg")
    elif c.data == 'Профком':
        keyboard = types.InlineKeyboardMarkup()
        vk_button = types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/profkom_psuti")
        inst_button = types.InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/profkompguti/")
        keyboard.add(vk_button, inst_button)
        bot.send_message(c.message.chat.id, text=config["ORG_INFORMATION"]["profkom"], parse_mode='HTML',reply_markup=keyboard)
        bot.send_photo(c.message.chat.id, photo="https://pp.userapi.com/c11086/v11086252/59/ALr9Fe6aJX4.jpg")
    elif c.data == 'СМЦ':
        keyboard = types.InlineKeyboardMarkup()
        vk_button = types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/smcpsuti")
        keyboard.add(vk_button)
        bot.send_message(c.message.chat.id, text=config["ORG_INFORMATION"]["smc"], parse_mode='HTML',
                         reply_markup=keyboard)
        bot.send_photo(c.message.chat.id, photo="https://pp.userapi.com/c624423/v624423730/46ffb/o64s1rt7Sds.jpg")
    elif c.data == 'РСО':
        bot.send_message(c.message.chat.id, 'Разнорабочие')
    elif c.data == 'Спортивные секции':
        bot.send_message(c.message.chat.id, 'ЗОЖ')


@bot.message_handler(commands=['about'])
def about_dev(message):
    bot.send_message(message.chat.id, text='Чат-бот разработан студентами <b>ИТ-клуба ПГУТИ</b> для будующих студентов.\n'
                                      'Будем рады увидеть Вас в наших рядах!', parse_mode='HTML')
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="ПРИСОЕДИНЯЙСЯ!", url="https://vk.com/itclub_psuti")
    keyboard.add(url_button)
    bot.send_photo(message.from_user.id, photo="https://pp.vk.me/c629125/v629125487/21029/Qd9czt4U02E.jpg", reply_markup=keyboard)


@bot.message_handler(commands=['excursion'])
def excursion(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="ЭКСКУРСИЯ!", url="https://abitur.psuti.ru/priemnaya-kampaniya/interaktivnaya-ekskursiya-po-psuti/psuti_webgl.html")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Перейдите по ссылке чтобы поетить наш университет онлайн!", reply_markup=keyboard)


if __name__ == '__main__':
    bot.polling(none_stop=True)
