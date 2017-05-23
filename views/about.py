from telebot import types
from views import open_menu as menu #возможный костыль

#@bot.message_handler(commands=['about'])
def about_dev(message, bot):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.row('Меню')
    inline_key = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="ПРИСОЕДИНЯЙСЯ!", url="https://vk.com/itclub_psuti")
    inline_key.add(url_button)
    about_msg = bot.send_message(message.chat.id, text='Чат-бот разработан студентами <b>ИТ-клуба ПГУТИ</b> для будующих студентов.'
                                      '\nБудем рады увидеть Вас в наших рядах! '
                                      '\nhttps://pp.vk.me/c629125/v629125487/21029/Qd9czt4U02E.jpg',
                     parse_mode='HTML',reply_markup=inline_key)
    #keyboard = types.InlineKeyboardMarkup()
    #url_button = types.InlineKeyboardButton(text="ПРИСОЕДИНЯЙСЯ!", url="https://vk.com/itclub_psuti")
    #keyboard.add(url_button)
    #bot.send_photo(message.from_user.id, photo="https://pp.vk.me/c629125/v629125487/21029/Qd9czt4U02E.jpg", )
    bot.register_next_step_handler(about_msg, menu.open_menu)


handlers = {'about': about_dev}