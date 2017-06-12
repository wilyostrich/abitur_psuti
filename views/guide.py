from telebot import types
from di_configuration import DIBot
from .open_menu import open_menu as menu


def guide(message):
    bot = DIBot.di_bot()
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True
    )
    keyboard.add('Список документов')
    keyboard.add('Меню')
    guide_msg = bot.send_message(
        message.chat.id,
        '<b>Шаг 1:</b> До 22.07 подать заявление в ПГУТИ одним из способов:\n'
        '       1) В приемную коммисию, по адресу Московское шоссе, 77\n'
        '       <b>График работы:</b> с 9 до 16 в будние дни\n'
        '       2) На почту abitur@psuti.ru\n'
        'Необходимы документы можно просмотреть перейдя в раздел "Список документов"\n\n'
        '<b>Шаг 2:</b> Следи на сайте за своим рейтингов среди абитуриентов\n'
        'https://abitur.psuti.ru/rating/\n\n'
        '<b>Шаг 3:</b> Принеси оригинал документов\n\n'
        '<b>Шаг 4:</b> Приходи на линейку 1 сентября!',
        parse_mode='HTML',
        reply_markup=keyboard)
    bot.register_next_step_handler(guide_msg, open_menu)


def open_menu(message):
    bot = DIBot.di_bot()
    if message.text == 'Меню':
        menu(message)
    elif message.text == 'Список документов':
        keyboard = types.InlineKeyboardMarkup()
        url_questionnaire = types.InlineKeyboardButton(
            text='Заявление анкета',
            url='https://abitur.psuti.ru/documents/priemnaya-kampaniya-2016/'
                '2016-%D0%97%D0%B0%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B0%D0%BD%D0%BA%D0%B5%D1%82%D0%B0.docx')
        url_statement = types.InlineKeyboardButton(
            text='Заявления о согласии на зачисление',
            url='https://abitur.psuti.ru/documents/priemnaya-kampaniya-2016/2016-%D0%97%D0%B0%D1%8F%D0%B2%D0%BB%D0%B5'
                '%D0%BD%D0%B8%D1%8F%20%D0%BE%20%D1%81%D0%BE%D0%B3%D0%BB%D0%B0%D1%81%D0%B8%D0%B8%20%D0%BD%D0%B0%20%D0'
                '%B7%D0%B0%D1%87%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5.docx')
        url_compliance = types.InlineKeyboardButton(
            text='Cогласие на обработку ПДн',
            url='https://abitur.psuti.ru/documents/priemnaya-kampaniya-2016/2016-%D0%A1%D0%BE%D0%B3%D0%BB%D0%B0'
                '%D1%81%D0%B8%D0%B5%20%D0%BD%D0%B0%20%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82'
                '%D0%BA%D1%83%20%D0%9F%D0%94%D0%BD.docx')
        keyboard.add(url_questionnaire)
        keyboard.add(url_statement)
        keyboard.add(url_compliance)
        bot.send_message(
            message.chat.id,
            'Поступающие в университет подают в приемную комиссию следующие документ\n'
            '1. <b>заявление</b> на имя ректора (заполняется на месте через автоматизированную систему);\n'
            '2. 4 фотографии размером 3х4 см <b>(после зачисления)</b> для личного дела, 1 фотография  '
            'делается бесплатно для нашей электронной базы у нас - будьте готовы (фото пойдет в зачетку);\n'
            '3. копию документа, удостоверяющего личность и гражданство; \n'
            '4. <b>согласие</b> на обработку персональных данных;\n'
            '5. <b>согласие на зачисление</b> по направлению.\n'
            '6. информацию о результатах единых государственных экзаменов (данные проверяются при поступающем '
            'через федеральную информационную базу);\n'
            '7. документы, дающие право на льготы, установленные законодательством Российской Федерации '
            '(для лиц, претендующих при поступлении на указанные льготы);\n'
            '8. документ (копия/оригинал), удостоверяющий образование соответствующего уровня\n',
            reply_markup=keyboard,
            parse_mode='HTML'
        )

handlers = {'guide': guide}

