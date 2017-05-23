from config import bot
from views import general

def open_menu(message):
    if message.text == 'Меню':
        general.help_message(message,bot)
    else:
        test = message.text
        print(test)
        msg_understand = bot.send_message(
            message.chat.id,
            'Я Вас не понял, повторите попытку или используйте кнопку Меню для выхода в меню')
        bot.register_next_step_handler(msg_understand, open_menu)