from telebot import types
from models import Academic
import dependency_injector as di


class DIService(di.AbstractCatalog):
    db_session = di.Provider()


def first_msg(message, bot):
    """Отвечаем на команду /start
    """
    session = DIService.db_session()
    spec = session.query(Academic).filter_by(id_spec=1).first()
    bot.send_message(message.chat.id,
                     'Название: {}\nЭкзамены: {}\nСсылка на профиль: {}?'
                     '\nБюджетные места: {}\nКонтрактные места: {}'
                     '\nЦена контракт: {}'.format(spec.name, spec.examinations,
                                                  spec.prof_link,
                                                  spec.budgetary_place,
                                                  spec.contract_places,
                                                  spec.cost),
                     parse_mode='Markdown', disable_web_page_preview=True,
                     reply_markup=pages_keyboard(1))

def pages_keyboard(numb):
    """Формируем Inline-кнопки для перехода по страницам.
    """
    session = DIService.db_session()
    numb_fields = session.query(Academic).count()
    keyboard = types.InlineKeyboardMarkup()
    btns = []
    btns.append(types.InlineKeyboardButton(text='Меню', callback_data='help'))
    if numb > 1: btns.append(types.InlineKeyboardButton(
        text='<', callback_data='to_{}'.format(numb - 1)))
    if numb < numb_fields: btns.append(types.InlineKeyboardButton(
        text='>', callback_data='to_{}'.format(numb + 1)))
    keyboard.add(*btns)
    return keyboard  # возвращаем объект клавиатуры



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
#         spec = session.query(Academic).filter_by(id_spec=c.data[3:]).first()
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


def specialties(message, bot):
    print('specialties')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                         one_time_keyboard=True)
    keyboard.add('Академический бакалавриат')
    keyboard.add('Прикладной бакалавриат')
    keyboard.add('Специалитет')
    msg = bot.send_message(
        message.chat.id, 'Выберите необходимую степень!', reply_markup=keyboard
    )
    bot.register_next_step_handler(
        msg, lambda massage: specialties_info(massage, bot)
    )


def specialties_info(message, bot):
    if message.text == 'Академический бакалавриат':
        first_msg(message, bot)
    elif message.text == 'Прикладной бакалавриат':
        session = DIService.db_session()
        spec = session.query(Academic).filter_by(id_spec=1).first()
        bot.send_message(
            message.chat.id, 'Прикладной бакалавриат {}'.format(spec.name)
        )
    elif message.text == 'Специалитет':
        bot.send_message(message.chat.id, 'Специалитет')


handlers = {'specialties': specialties}
