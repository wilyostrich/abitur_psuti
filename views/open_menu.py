from di_configuration import DIBot
from .general import help_message

def open_menu(message):
    bot = DIBot.di_bot()
    try:
        if message.text == 'Меню':
            help_message(message)
    except:
        print('ERROR')
        # else:
        # test = message.text
        # print(test)
        # msg_understand = bot.send_message(
        #     message.chat.id,
        #     'Я Вас не понял, повторите попытку или используйте кнопку Меню для вызова справки')
        # bot.register_next_step_handler(msg_understand, open_menu)