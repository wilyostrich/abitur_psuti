from di_configuration import DIBot
from .general import help_message

def open_menu(message):
    bot = DIBot.di_bot()
    try:
        if message.text == 'Меню':
            help_message(message)
    except:
        print('ERROR')