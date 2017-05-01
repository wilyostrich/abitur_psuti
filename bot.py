import telebot
from telebot import types
import configparser

config = configparser.ConfigParser()
config.read('config.ini', encoding = 'UTF-8')


bot = telebot.TeleBot(config["DEFAULT"]["Token"])

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, 'Привет! Здесь собрана достоверная информация о Поволжском государственном '
                                      'университете телекоммуникаций и информатики', reply_markup=markup)
    help_message(message)


@bot.message_handler(commands=['help'])
def help_message(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, 'Я помогу тебе узнать немного больше о нашем ВУЗе! Воспользуйся простыми '
                                      'командами, чтобы узнать интересующую тебя информацию!\n'
                                      '/openday - День открытых дверей\n'
                                      '/course - Курсы для абитуриентов\n'
                                      '/specialties - Направления подготовки\n'
                                      '/guide - Руководство по поступлению\n'
                                      '/rating - Узнай свой рейтинг\n'
                                      '/contacts - Контактая информация\n'
                                      '/calculator - Подсчитай свои баллы и узнай на какую спецальность ты проходишь\n'
                                      '/studorganizations - внеучебная деятельность\n'
                                      '/excursion - интерактивная экскурсия по университету\n'
                                      '/about - О разработчитах', reply_markup=markup)


@bot.message_handler(commands=['openday'])
def openday(message):
    bot.send_message(message.chat.id, 'Приглашаем всех желающих (абитуриентов, школьников и их родителей) на День '
                                      'открытых дверей в ПГУТИ. Экскурсии по вузу, презентации направлений подготовки, '
                                      'ответы на всевозможные вопросы по процессу обучения в университете - всё это и '
                                      'многое другое ждёт вас на днях открытых дверей в Самаре\n\n'
                                      'Ближайший День открытых дверей в ПГУТИ состоится {} года по '
                                      'адресу: Московское шоссе, д. 77 (2-й корпус ПГУТИ). \n'
                                      'Начало в 10:00 по самарскому времени.\n'
                                      'Актуальную и подробную информацию Вы можете узнать на сайте '
                                      'https://abitur.psuti.ru/ и в группе ВК https://vk.com/abiturpsuti'
                     .format(config["OPENDAY"]["data"]), disable_web_page_preview=True)


@bot.message_handler(commands=['course'])
def course(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.row('Инженерный лицей', 'Школа программистов')
    keyboard.row('Подготовка к ЕГЭ и внутренним экзаменам')
    keyboard.row('Меню')
    msg = bot.send_message(message.chat.id, 'Выберите интересующий вас курс!', reply_markup=keyboard)
    bot.register_next_step_handler(msg, course_info)


def course_info(message):
    if message.text == 'Подготовка к ЕГЭ и внутренним экзаменам':
        bot.send_message(message.chat.id, text=config["COURSE"]["ege"], parse_mode='HTML')
        msg_exam = bot.send_message(message.chat.id, 'Получить более подробную информаци, а также записаться на курсы,'
                                          ' можно перейдя по ссылке: http://abitur.psuti.ru/center/podgotovitelnye-kursy-k-ege-i-vnutrennim-ekzamenam/', disable_web_page_preview=True)
        bot.register_next_step_handler(msg_exam, course_info)
    elif message.text == 'Школа программистов':
        bot.send_message(message.chat.id, '<b>Школа программистов</b>\n'
                                          'Обучение платное для учащихся 8-х, 9-х, 10-х и 11-х классов, проводится в 3 этапа:\n'
                                          '1. Информатика;\n'
                                          '2. Программирование;\n'
                                          '3. Информационные системы и технологии.\n'
                                          'Срок обучения в школе – 5 месяцев.\n'
                                          'Окончившим Школу программистов выдается «Свидетельство об окончании», которое дает право преимущественного зачисления в ПГУТИ.\n'
                                          'Справки по телефону: (846) 228-00-51,  (846) 228-00-58.', parse_mode='HTML')
        msg_school = bot.send_message(message.chat.id, 'Получить более подробную информаци, а также записаться в школу программистов,'
                                          ' можно перейдя по ссылке: http://abitur.psuti.ru/center/shkola-programmistov/', disable_web_page_preview=True, parse_mode='HTML')
        bot.register_next_step_handler(msg_school, course_info)
    elif message.text == 'Инженерный лицей':
        bot.send_message(message.chat.id, text=config["COURSE"]["engineer"], parse_mode='HTML')
        msg_engineer = bot.send_message(message.chat.id, 'Получить более подробную информаци, а также записаться на занятия,'
                                          ' можно перейдя по ссылке: http://abitur.psuti.ru/center/inzhenernyy-litsey/',
                         disable_web_page_preview=True, parse_mode='HTML')
        bot.register_next_step_handler(msg_engineer, course_info)
    elif message.text == 'Меню':
        help_message(message)
    else:
        msg_understand = bot.send_message(message.chat.id, 'Я Вас не понял, выберите раздел из меню '
                                          'или используйте кнопку Меню для выхода в меню')
        bot.register_next_step_handler(msg_understand, course_info)


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
        bot.send_message(message.chat.id, '<b>Академический бакалавриат</b>\n'
                                          'Срок обучения - 4 года\n'
                                          '<b>Направления подготовки:</b>\n', parse_mode='HTML')
        bot.send_message(message.chat.id, '02.03.03 - Математическое обеспечение и администрирование информационных систем\n'
                                          '<b>Профиль:</b>\n'
                                          '<a href="http://abitur.psuti.ru/napravleniya-podgotovki/profili/'
                                          'tekhnologiya-programmirovaniya/">Технология программирования</a>\n'
                                          '<b>Вступительные испытания:</b> Русский язык, Математика, Физика\n'
                                          '<b>Число бюджетных мест:</b> 0\n'
                                          '<b>Коммерческкое обучение:</b> \n'
                                          '<b>Число конкратных мест:</b> 25\n'
                                          '<b>Стоимость обучений(за один семестр):</b> 34000 р', parse_mode='HTML')
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
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add('IT-клуб ПГУТИ')
    keyboard.add('РСО', 'Профком', 'СМЦ')
    keyboard.add('Спортивные секции')
    keyboard.add('Меню')
    msg_org = bot.send_message(message.chat.id, 'Про каждую организация можно узнать, перейдя в '
                                      'интересующий раздел.', reply_markup=keyboard)
    bot.register_next_step_handler(msg_org, org_info)

def org_info(message):
    if message.text == 'IT-клуб ПГУТИ':
        keyboard = types.InlineKeyboardMarkup()
        vk_button = types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/itclub_psuti")
        inst_button = types.InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/itclub_psuti/")
        keyboard.add(vk_button, inst_button)
        bot.send_message(message.chat.id, text=config["ORG_INFORMATION"]["itclub"], parse_mode='HTML',
                         reply_markup=keyboard)
        msg_itclub = bot.send_photo(message.chat.id, photo="https://pp.userapi.com/c623223/v623223296/234e/vqj_1H5X-Bs.jpg")
        bot.register_next_step_handler(msg_itclub, org_info)
    elif message.text == 'Профком':
        keyboard = types.InlineKeyboardMarkup()
        vk_button = types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/profkom_psuti")
        inst_button = types.InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/profkompguti/")
        keyboard.add(vk_button, inst_button)
        bot.send_message(message.chat.id, text=config["ORG_INFORMATION"]["profkom"], parse_mode='HTML',
                         reply_markup=keyboard)
        msg_profkom = bot.send_photo(message.chat.id, photo="https://pp.userapi.com/c11086/v11086252/59/ALr9Fe6aJX4.jpg")
        bot.register_next_step_handler(msg_profkom, org_info)
    elif message.text == 'СМЦ':
        keyboard = types.InlineKeyboardMarkup()
        vk_button = types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/smcpsuti")
        keyboard.add(vk_button)
        bot.send_message(message.chat.id, text=config["ORG_INFORMATION"]["smc"], parse_mode='HTML',
                         reply_markup=keyboard)
        msg_smc = bot.send_photo(message.chat.id, photo="https://pp.userapi.com/c624423/v624423730/46ffb/o64s1rt7Sds.jpg")
        bot.register_next_step_handler(msg_smc, org_info)
    elif message.text == 'РСО':
        msg_rso = bot.send_message(message.chat.id, 'Разнорабочие')
        bot.register_next_step_handler(msg_rso, org_info)
    elif message.text == 'Спортивные секции':
        keyboard = types.InlineKeyboardMarkup()
        site_btn = types.InlineKeyboardButton(text="Перейти на сайт", url="http://sport.psuti.ru/")
        keyboard.add(site_btn)
        bot.send_message(message.chat.id, text=config["ORG_INFORMATION"]["sport"], parse_mode='HTML',
                         reply_markup=keyboard)
        msg_sport = bot.send_photo(message.chat.id, photo="http://sport.psuti.ru/doc/Ovg56tNXoFE.jpg")
        bot.register_next_step_handler(msg_sport, org_info)
    elif message.text == 'Меню':
        help_message(message)
    else:
        msg_understand = bot.send_message(message.chat.id, 'Я Вас не понял, выберите раздел из меню '
                                                           'или используйте кнопку Меню для выхода в меню')
        bot.register_next_step_handler(msg_understand, course_info)


'''    
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
        keyboard = types.InlineKeyboardMarkup()
        site_btn = types.InlineKeyboardButton(text="Перейти на сайт", url="http://sport.psuti.ru/")
        keyboard.add(site_btn)
        bot.send_message(c.message.chat.id, text=config["ORG_INFORMATION"]["sport"], parse_mode='HTML', reply_markup=keyboard)
        bot.send_photo(c.message.chat.id, photo="http://sport.psuti.ru/doc/Ovg56tNXoFE.jpg")
'''


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
    bot.send_message(message.chat.id, 'Перейдите по ссылке чтобы поетить наш университет онлайн!\n'
                                      'Рекомендуется открывать через браузер компьютера.')
    bot.send_photo(message.from_user.id, photo="https://pp.vk.me/c629125/v629125487/21029/Qd9czt4U02E.jpg", reply_markup=keyboard)


if __name__ == '__main__':
    bot.polling(none_stop=True)
