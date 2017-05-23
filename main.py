import configparser
import telebot
import dependency_injector as di

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from views import handlers, specialty
from config import DATABASE_URI

from config import bot
# config = configparser.ConfigParser()
# config.read('config.ini', encoding='UTF-8')

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()
#bot = telebot.TeleBot(config["DEFAULT"]["Token"])

db_session_prv = di.Object(session)
specialty.DIService.db_session.override(db_session_prv)

# Добавляем обработчики
for name, func in handlers.items():
    bot.message_handler(commands=[name])(
        lambda massage, func=func: func(massage, bot=bot)
    )

#
# @bot.message_handler(commands=['openday'])
# def openday(message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#     keyboard.row('Меню')
#     open_d = bot.send_message(message.chat.id, 'Приглашаем всех желающих (абитуриентов, школьников и их родителей) на День '
#                                       'открытых дверей в ПГУТИ. Экскурсии по вузу, презентации направлений подготовки, '
#                                       'ответы на всевозможные вопросы по процессу обучения в университете - всё это и '
#                                       'многое другое ждёт вас на днях открытых дверей в Самаре\n\n'
#                                       'Ближайший День открытых дверей в ПГУТИ состоится {} года по '
#                                       'адресу: Московское шоссе, д. 77 (2-й корпус ПГУТИ). \n'
#                                       'Начало в 10:00 по самарскому времени.\n'
#                                       'Актуальную и подробную информацию Вы можете узнать на сайте '
#                                       'https://abitur.psuti.ru/ и в группе ВК https://vk.com/abiturpsuti'
#                      .format(config["OPENDAY"]["data"]), disable_web_page_preview=True, reply_markup=keyboard)
#     bot.register_next_step_handler(open_d, open_menu)
#
# def open_menu(message):
#     if message.text == 'Меню':
#         help_message(message)
#     else:
#         msg_understand = bot.send_message(message.chat.id, 'Я Вас не понял, повторите попытку '
#                                           'или используйте кнопку Меню для выхода в меню')
#         bot.register_next_step_handler(msg_understand, open_menu)
#
#
# @bot.message_handler(commands=['course'])
# def course(message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#     keyboard.row('Инженерный лицей', 'Школа программистов')
#     keyboard.row('Подготовка к ЕГЭ и внутренним экзаменам')
#     keyboard.row('Меню')
#     msg = bot.send_message(message.chat.id, 'Выберите интересующий вас курс!', reply_markup=keyboard)
#     bot.register_next_step_handler(msg, course_info)
#
#
# def course_info(message):
#     if message.text == 'Подготовка к ЕГЭ и внутренним экзаменам':
#         bot.send_message(message.chat.id, text=config["COURSE"]["ege"], parse_mode='HTML')
#         msg_exam = bot.send_message(message.chat.id, 'Получить более подробную информаци, а также записаться на курсы,'
#                                                      ' можно перейдя по ссылке: http://abitur.psuti.ru/'
#                                                      'center/podgotovitelnye-kursy-k-ege-i-vnutrennim-ekzamenam/',
#                                     disable_web_page_preview=True)
#         bot.register_next_step_handler(msg_exam, course_info)
#     elif message.text == 'Школа программистов':
#         bot.send_message(message.chat.id, '<b>Школа программистов</b>\n'
#                                           'Обучение платное для учащихся 8-х, 9-х, 10-х и 11-х классов, проводится '
#                                           'в 3 этапа:\n'
#                                           '1. Информатика;\n'
#                                           '2. Программирование;\n'
#                                           '3. Информационные системы и технологии.\n'
#                                           'Срок обучения в школе – 5 месяцев.\n'
#                                           'Окончившим Школу программистов выдается «Свидетельство об окончании», '
#                                           'которое дает право преимущественного зачисления в ПГУТИ.\n'
#                                           'Справки по телефону: (846) 228-00-51,  (846) 228-00-58.', parse_mode='HTML')
#         msg_school = bot.send_message(message.chat.id, 'Получить более подробную информаци, а также записаться в школу '
#                                                        'программистов, можно перейдя по ссылке: '
#                                                        'http://abitur.psuti.ru/center/shkola-programmistov/',
#                                       disable_web_page_preview=True, parse_mode='HTML')
#         bot.register_next_step_handler(msg_school, course_info)
#     elif message.text == 'Инженерный лицей':
#         bot.send_message(message.chat.id, text=config["COURSE"]["engineer"], parse_mode='HTML')
#         msg_engineer = bot.send_message(message.chat.id, 'Получить более подробную информаци, а также '
#                                                          'записаться на занятия, можно перейдя по ссылке: '
#                                                          'http://abitur.psuti.ru/center/inzhenernyy-litsey/',
#                                         disable_web_page_preview=True, parse_mode='HTML')
#         bot.register_next_step_handler(msg_engineer, course_info)
#     elif message.text == 'Меню':
#         help_message(message)
#     else:
#         msg_understand = bot.send_message(message.chat.id, 'Я Вас не понял, выберите раздел из меню '
#                                           'или используйте кнопку Меню для выхода в меню')
#         bot.register_next_step_handler(msg_understand, course_info)
#
#
#
# def first_msg(message):
#     """Отвечаем на команду /start
#     """
#     spec = session.query(Specialty).filter_by(id_spec=1).first()
#     bot.send_message(message.chat.id, 'Название: {}\nЭкзамены: {}\nСсылка на профиль: {}?'
#                                 '\nБюджетные места: {}\nКонтрактные места: {}'
#                                 '\nЦена контракт: {}'.format(spec.name, spec.examinations,
#                                                              spec.prof_link, spec.budgetary_place,
#                                                              spec.contract_places, spec.cost),
#                      parse_mode='Markdown', disable_web_page_preview=True, reply_markup=pages_keyboard(1))
#
#
# def pages_keyboard(numb):
#     """Формируем Inline-кнопки для перехода по страницам.
#     """
#     keyboard = types.InlineKeyboardMarkup()
#     btns = []
#     btns.append(types.InlineKeyboardButton(text='Меню',callback_data='help'))
#     if numb > 1: btns.append(types.InlineKeyboardButton(
#         text='<', callback_data='to_{}'.format(numb - 1)))
#     if numb < numb_fields: btns.append(types.InlineKeyboardButton(
#         text='>', callback_data='to_{}'.format(numb + 1)))
#     keyboard.add(*btns)
#     return keyboard  # возвращаем объект клавиатуры
#
#
# @bot.callback_query_handler(func=lambda c: c.data)
# def pages(c):
#     """Редактируем сообщение каждый раз, когда пользователь переходит по
#     страницам.
#     """
#     print(c.data)
#     print(numb_fields)
#     if c.data=='help':
#         help_message(c.message)
#     elif int(c.data[3:]) <= numb_fields:
#         spec = session.query(Specialty).filter_by(id_spec=c.data[3:]).first()
#         bot.edit_message_text(
#             chat_id=c.message.chat.id,
#             message_id=c.message.message_id,
#             disable_web_page_preview=True,
#             text='Название: {}\nЭкзамены: {}\nСсылка на профиль: {}\nБюджетные места: {}\nКонтрактные места: {}'
#                  '\nЦена контракт: {}'.format(spec.name, spec.examinations, spec.prof_link,
#                                               spec.budgetary_place, spec.contract_places, spec.cost),
#             parse_mode='Markdown',
#             reply_markup=pages_keyboard(int(c.data[3:])))
#     elif int(c.data[3:]) > numb_fields:
#         first_msg()
#
#
# @bot.message_handler(commands=['specialties'])
# def specialties(message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#     keyboard.add('Академический бакалавриат')
#     keyboard.add('Прикладной бакалавриат')
#     keyboard.add('Специалитет')
#     msg = bot.send_message(message.chat.id, 'Выберите необходимую степень!', reply_markup=keyboard)
#     bot.register_next_step_handler(msg, specialties_info)
#
#
# def specialties_info(message):
#     if message.text == 'Академический бакалавриат':
#         first_msg(message)
#
#
# #--------------------------------------------------------------------------------------------
#     elif message.text == 'Прикладной бакалавриат':
#         spec = session.query(Specialty).filter_by(id_spec=1).first()
#         bot.send_message(message.chat.id, 'Прикладной бакалавриат {}'.format(spec.name))
#
#
#     elif message.text == 'Специалитет':
#         bot.send_message(message.chat.id, 'Специалитет')
#
#
# @bot.message_handler(commands=['guide'])
# def guide(message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#     keyboard.row('Меню')
#     guide_msg = bot.send_message(message.chat.id, 'Не реализовано!', reply_markup=keyboard)
#     bot.register_next_step_handler(guide_msg, open_menu)
#
# @bot.message_handler(commands=['rating'])
# def rating(message):
#     bot.send_message(message.chat.id, "Тест!")
#
#
# @bot.message_handler(commands=['contacts'])
# def contacts(message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#     keyboard.row('Меню')
#     bot.send_message(message.chat.id, text='<b>Контактная информация</b>\n\n'
#                                            '<b>Телефоны:</b> '
#                                            '(846)228-00-51, '
#                                            '(846)228-00-58\n'
#                                            '<b>Email:</b> '
#                                            'cdou@psati.ru\n'
#                                            '<b>Проезд:</b> '
#                                            'остановка "Телецентр"\n'
#                                            '• автобусами (1, 23, 30, 37, 47, 56),\n'
#                                            '• троллейбусами (2, 4, 12, 17, 19),\n'
#                                            '• маршрутными такси (1, 1к, 4 (216), 21м, 23, 37, 47, 67, 91, 110, 257д, 259, 269, 373, 392, 392а, 410а, 492).', parse_mode='HTML')
#     contact_msg = bot.send_venue(message.chat.id, 53.2256561, 50.1949533, 'Физический адрес:', '443090, г. Самара, ул.Московское шоссе, 77, комн.201')
#     bot.register_next_step_handler(contact_msg, open_menu)
#
# @bot.message_handler(commands=['calculator'])
# def calculator(message):
#     bot.send_message(message.chat.id, "Тест!")
#
#
# @bot.message_handler(commands=['studorganizations'])
# def studorganizations(message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#     keyboard.add('IT-клуб ПГУТИ')
#     keyboard.add('РСО', 'Профком', 'СМЦ')
#     keyboard.add('Спортивные секции')
#     keyboard.add('Меню')
#     msg_org = bot.send_message(message.chat.id, 'Про каждую организация можно узнать, перейдя в '
#                                       'интересующий раздел.', reply_markup=keyboard)
#     bot.register_next_step_handler(msg_org, org_info)
#
# def org_info(message):
#     if message.text == 'IT-клуб ПГУТИ':
#         keyboard = types.InlineKeyboardMarkup()
#         vk_button = types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/itclub_psuti")
#         inst_button = types.InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/itclub_psuti/")
#         keyboard.add(vk_button, inst_button)
#         msg_itclub = bot.send_message(message.chat.id, text=config["ORG_INFORMATION"]["itclub"], disable_web_page_preview=False, parse_mode='HTML',
#                          reply_markup=keyboard)
#         #msg_itclub = bot.send_photo(message.chat.id, photo="https://pp.userapi.com/c623223/v623223296/234e/vqj_1H5X-Bs.jpg")
#         bot.register_next_step_handler(msg_itclub, org_info)
#     elif message.text == 'Профком':
#         keyboard = types.InlineKeyboardMarkup()
#         vk_button = types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/profkom_psuti")
#         inst_button = types.InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/profkompguti/")
#         keyboard.add(vk_button, inst_button)
#         msg_profkom = bot.send_message(message.chat.id, text=config["ORG_INFORMATION"]["profkom"], disable_web_page_preview=False, parse_mode='HTML',
#                          reply_markup=keyboard)
#         #msg_profkom = bot.send_photo(message.chat.id, photo="https://pp.userapi.com/c11086/v11086252/59/ALr9Fe6aJX4.jpg")
#         bot.register_next_step_handler(msg_profkom, org_info)
#     elif message.text == 'СМЦ':
#         keyboard = types.InlineKeyboardMarkup()
#         vk_button = types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/smcpsuti")
#         keyboard.add(vk_button)
#         msg_smc = bot.send_message(message.chat.id, text=config["ORG_INFORMATION"]["smc"], disable_web_page_preview=False, parse_mode='HTML',
#                          reply_markup=keyboard)
#         #msg_smc = bot.send_photo(message.chat.id, photo="https://pp.userapi.com/c624423/v624423730/46ffb/o64s1rt7Sds.jpg")
#         bot.register_next_step_handler(msg_smc, org_info)
#     elif message.text == 'РСО':
#         keyboard = types.InlineKeyboardMarkup()
#         vk_button = types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/smcpsuti")
#         keyboard.add(vk_button)
#         msg_rso = bot.send_message(message.chat.id, text=config["ORG_INFORMATION"]["rso"], disable_web_page_preview=False, parse_mode='HTML',
#                          reply_markup=keyboard)
#         bot.register_next_step_handler(msg_rso, org_info)
#     elif message.text == 'Спортивные секции':
#         keyboard = types.InlineKeyboardMarkup()
#         site_btn = types.InlineKeyboardButton(text="Перейти на сайт", url="http://sport.psuti.ru/")
#         keyboard.add(site_btn)
#         msg_sport = bot.send_message(message.chat.id, text=config["ORG_INFORMATION"]["sport"], disable_web_page_preview=False, parse_mode='HTML',
#                          reply_markup=keyboard)
#         #msg_sport = bot.send_photo(message.chat.id, photo="http://sport.psuti.ru/doc/Ovg56tNXoFE.jpg")
#         bot.register_next_step_handler(msg_sport, org_info)
#     elif message.text == 'Меню':
#         help_message(message)
#     else:
#         msg_understand = bot.send_message(message.chat.id, 'Я Вас не понял, выберите раздел из меню '
#                                                            'или используйте кнопку Меню для выхода в меню')
#         bot.register_next_step_handler(msg_understand, course_info)
#
#
# @bot.message_handler(commands=['about'])
# def about_dev(message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#     keyboard.row('Меню')
#     inline_key = types.InlineKeyboardMarkup()
#     url_button = types.InlineKeyboardButton(text="ПРИСОЕДИНЯЙСЯ!", url="https://vk.com/itclub_psuti")
#     inline_key.add(url_button)
#     about_msg = bot.send_message(message.chat.id, text='Чат-бот разработан студентами <b>ИТ-клуба ПГУТИ</b> для будующих студентов.'
#                                       '\nБудем рады увидеть Вас в наших рядах! '
#                                       '\nhttps://pp.vk.me/c629125/v629125487/21029/Qd9czt4U02E.jpg',
#                      parse_mode='HTML',reply_markup=inline_key)
#     #keyboard = types.InlineKeyboardMarkup()
#     #url_button = types.InlineKeyboardButton(text="ПРИСОЕДИНЯЙСЯ!", url="https://vk.com/itclub_psuti")
#     #keyboard.add(url_button)
#     #bot.send_photo(message.from_user.id, photo="https://pp.vk.me/c629125/v629125487/21029/Qd9czt4U02E.jpg", )
#     bot.register_next_step_handler(about_msg, open_menu)
#
# @bot.message_handler(commands=['excursion'])
# def excursion(message):
#     keyboard = types.InlineKeyboardMarkup()
#     url_button = types.InlineKeyboardButton(text="ЭКСКУРСИЯ!", url="https://abitur.psuti.ru/priemnaya-kampaniya/interaktivnaya-ekskursiya-po-psuti/psuti_webgl.html")
#     keyboard.add(url_button)
#     bot.send_message(message.chat.id, 'Перейдите по ссылке чтобы поетить наш университет онлайн!\n'
#                                       'Рекомендуется открывать через браузер компьютера.')
#     bot.send_photo(message.from_user.id, photo="https://pp.vk.me/c629125/v629125487/21029/Qd9czt4U02E.jpg", reply_markup=keyboard)


if __name__ == '__main__':
    bot.polling(none_stop=True)
