from telebot import types
from di_configuration import DIBot

def start_message(message):
    bot = DIBot.di_bot()
    print('start')
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(
        message.chat.id,
        'Привет! Здесь собрана достоверная информация о Поволжском '
        'государственном университете телекоммуникаций и информатики',
        reply_markup=markup
    )
    help_message(message)


def help_message(message):
    bot = DIBot.di_bot()
    print('help')
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(
        message.chat.id,
        'Я помогу тебе узнать немного больше о нашем ВУЗе! Воспользуйся простыми '
        'командами, чтобы узнать интересующую тебя информацию!\n'
        '/openday - День открытых дверей\n'
        '/course - Курсы для абитуриентов\n'
        '/specialties - Направления подготовки\n'
        '/guide - Руководство по поступлению\n'
        '/contacts - Контактая информация\n'
        '/calculator - Подсчитай свои баллы и узнай на какую спецальность ты проходишь\n'
        '/studorganizations - внеучебная деятельность\n'
        '/excursion - интерактивная экскурсия по университету\n'
        '/about - О разработчитах',
        reply_markup=markup
    )


handlers = {
    'start': start_message,
    'help': help_message
}
