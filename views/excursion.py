from telebot import types
from di_configuration import DIBot

def excursion(message):
    print('excursion')
    bot = DIBot.di_bot()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(
        text='Перейти к экскурсии',
        url='https://abitur.psuti.ru/priemnaya-kampaniya/interaktivnaya-ekskursiya-po-psuti/psuti_webgl.html')
    keyboard.add(url_button)
    bot.send_photo(
        message.from_user.id,
        caption='Перейдите по ссылке чтобы поетить наш университет онлайн!\nРекомендуется открывать через браузер компьютера.',
        photo='https://pp.userapi.com/c637325/v637325686/4df76/BFvXI7PDeTw.jpg',
        reply_markup=keyboard)

handlers = {'excursion': excursion}