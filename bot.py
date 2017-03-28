import telebot
from telebot import types


bot = telebot.TeleBot("370462510:AAElsbNsJwqO9P0Ucuv6XHJQc7AH-5Xjw68")


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id,
                     "\nХочешь стать крутым IT-специалистом или cвязистом? Тогда тебе к нам!")
    bot.send_message(message.chat.id, "Я помогу тебе узнать немного больше о нашем ВУЗе! Воспользуйся простыми "
                                      "командами чтобы узнать интересующую тебя информацию!\n"
                                      "/course - Наши курсы для абитуриентов\n"
                                      "/specialties - Направления подготовки\n"
                                      "/guide - Руководство по поступлению\n"
                                      "/rating - Узнай свой рейтинг\n"
                                      "/contacts - Контактая информация\n"
                                      "/calculator - Подсчитай свои баллы и узнай на какую спецальноть ты проходишь\n"
                                      "/studorganizations - внеучебная деятельность\n"
                                      "/about - О разработчитах\n"
                                      "/excursion - интерактивная экскурсия по университету")


@bot.message_handler(commands=['course'])
def course(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    keyboard.row('Подготовка к ЕГЭ и внутренним экзаменам','Школа программистов')
    keyboard.row('Инженерный лицей','Контактная информация')
    msg = bot.send_message(message.chat.id, "Тест!",reply_markup=keyboard)
    bot.register_next_step_handler(msg, process_step)

def process_step(message):
    if message.text == 'Подготовка к ЕГЭ и внутренним экзаменам':
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, 'К ЕГЭ!', reply_markup=markup)


@bot.message_handler(commands=['specialties'])
def specialties(message):
    bot.send_message(message.chat.id, "Тест!")


@bot.message_handler(commands=['guide'])
def guide(message):
    bot.send_message(message.chat.id, "Тест!")


@bot.message_handler(commands=['rating'])
def rating(message):
    bot.send_message(message.chat.id, "Тест!")


@bot.message_handler(commands=['contacts'])
def contacts(message):
    bot.send_message(message.chat.id, "Тест!")


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
        keyboard.add(vk_button,inst_button)
        bot.send_message(c.message.chat.id, text='<b>Студенческий ИТ-клуб Поволжского Государственного'
                                                 ' Университета Телекоммуникаций и Информатики</b>\n\n'
                                                 'Основными направлениями деятельности клуба являются:\n'
                                                 '• Научно–исследовательская работа студентов;\n'
                                                 '• Организация мероприятий;\n'
                                                 '• Работа со школьниками и абитуриентами;\n'
                                                 '• Студенческие мастерские\n\n'
                                                 'На счету студенческого ИТ–клуба сотрудничество с ведущими IT-компаниями '
                                                 'области и региона.\n\n'
                                                 'Члены клуба успешно представляют университет на разных уровнях. Они '
                                                 'являются участниками, призерами и победителями Межвузовских, Областных и '
                                                 'Международных Олимпиад и Конференций.\n\n'
                                                 'Представители студенческого ИТ­ Клуба «IN-­IT with ПГУТИ» с удовольствием '
                                                 'делятся своими навыками и всегда готовы к обмену опытом. Благодаря этому, '
                                                 'при клубе существуют мастерские, организованные студентами по актуальным '
                                                 'ИТ направлениям. ИТ–Клуб дает студентам возможность проявить себя в самых '
                                                 'различных направлениях,что немаловажно для будущей профессиональной '
                                                 'карьеры. Умение работать в команде, возможность проявить себя, как '
                                                 'начинающего ученого, творческий подход к сложным задачам, опыт организации'
                                                 ' мероприятий в ВУЗе и за его пределами, возможность развить педагогический'
                                                 ' талант – это неполный список качеств, которые студент может открыть в '
                                                 'себе, работая совместно с ИТ–клубом.\n'
                                                 'Вы всегда можете найти нас в социальных сетях! #itclub_psuti',
                         parse_mode='HTML',reply_markup=keyboard)
        bot.send_photo(c.message.chat.id, photo="https://pp.userapi.com/c623223/v623223296/234e/vqj_1H5X-Bs.jpg")
    elif c.data == 'Профком':
        keyboard = types.InlineKeyboardMarkup()
        vk_button = types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/profkom_psuti")
        inst_button = types.InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/profkompguti/")
        keyboard.add(vk_button, inst_button)
        bot.send_message(c.message.chat.id, '<b>Студенческий профсоюз | ПГУТИ</b> – это явление сравнительно молодое, но уже '
                                            'сейчас сумевшее объединить в себе большинство обучающихся в университете.\n\n '
                                            'Это организация, которой студент не безразличен, где он — личность, '
                                            'которая стремится наполнить событиями окружающую действительность, сделать'
                                            ' её более интересной. Он существует для того, чтобы объединить свои силы и'
                                            ' способности, чтобы сделать студенческую жизнь по-настоящему интересной и'
                                            ' увлекательной.\n\n '
                                            'Этот мощный механизм, запущенный с помощью администрации ПГУТИ, сумел '
                                            'вовлечь в свою работу самых активных, талантливых студентов. Преодолевая '
                                            'определённые трудности, наша организация достигает поставленных целей: '
                                            'проведение различных творческих вечеров, конференций, спортивных '
                                            'мероприятий. Всё это вряд ли стало бы возможным без сильной поддержки '
                                            'администрации ПГУТИ, которая идёт навстречу организаторам, воспитателям, '
                                            'одним словом, всем тем, кто работает на благо студентов.\n\n'
                                            'Основными сферами деятельности профсоюза являются постановка и реализация'
                                            ' самых различных задач социального характера, спортивно-оздоровительные '
                                            'мероприятия. Каждый проект обсуждается и согласуется, в результате этого '
                                            'каждый может внести свои изменения, сделать замечания. Открытость, '
                                            'возможность влиять на события студенческой жизни в университете – именно '
                                            'по такому принципу организует свою деятельность профсоюз ПГУТИ. И этому '
                                            'способствует сотрудничество с СМЦ, студ.городком, редакцией газеты '
                                            '«Академия связи». Из её публикаций и статей можно почерпнуть сведения о '
                                            'деятельности профсоюза. По заранее утверждённой комплексной программе '
                                            'работы профком проводит различные мероприятия.',
                         parse_mode='HTML',reply_markup=keyboard)
        bot.send_photo(c.message.chat.id, photo="https://pp.userapi.com/c11086/v11086252/59/ALr9Fe6aJX4.jpg")
    elif c.data == 'СМЦ':
        bot.send_message(c.message.chat.id, 'Песни-пляски')
    elif c.data == 'РСО':
        bot.send_message(c.message.chat.id, 'Разнорабочие')
    elif c.data == 'Спортивные секции':
        bot.send_message(c.message.chat.id, 'ЗОЖ')


@bot.message_handler(commands=['about'])
def about_dev(message):
    bot.send_message(message.chat.id, text="Чат-бот разработан студентами <b>ИТ-клуба ПГУТИ</b> для будующих студентов.\n"
                                      "Будем рады увидеть Вас в наших рядах!", parse_mode='HTML')
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
