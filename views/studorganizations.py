from telebot import types
from di_configuration import DIConfige, DIBot
from views import general


def studorganizations(message):
    bot = DIBot.di_bot()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add('IT-клуб ПГУТИ')
    keyboard.add('РСО', 'Профком', 'СМЦ')
    keyboard.add('Спортивные секции')
    keyboard.add('Меню')
    msg_org = bot.send_message(
        message.chat.id,
        'Про каждую организация можно узнать, перейдя в интересующий раздел.',
        reply_markup=keyboard)
    bot.register_next_step_handler(msg_org, org_info)


def org_info(message):
    bot = DIBot.di_bot()
    config = DIConfige.config_ini()
    if message.text == 'IT-клуб ПГУТИ':
        keyboard = types.InlineKeyboardMarkup()
        vk_button = types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/itclub_psuti")
        inst_button = types.InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/itclub_psuti/")
        keyboard.add(vk_button, inst_button)
        msg_itclub = bot.send_message(
            message.chat.id,
            text=config["ORG_INFORMATION"]["itclub"],
            disable_web_page_preview=False,
            parse_mode='HTML',
            reply_markup=keyboard)
        bot.register_next_step_handler(msg_itclub, org_info)
    elif message.text == 'Профком':
        keyboard = types.InlineKeyboardMarkup()
        vk_button = types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/profkom_psuti")
        inst_button = types.InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/profkompguti/")
        keyboard.add(vk_button, inst_button)
        msg_profkom = bot.send_message(
            message.chat.id,
            text=config["ORG_INFORMATION"]["profkom"],
            disable_web_page_preview=False,
            parse_mode='HTML',
            reply_markup=keyboard)
        bot.register_next_step_handler(msg_profkom, org_info)
    elif message.text == 'СМЦ':
        keyboard = types.InlineKeyboardMarkup()
        vk_button = types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/smcpsuti")
        keyboard.add(vk_button)
        msg_smc = bot.send_message(
            message.chat.id,
            text=config["ORG_INFORMATION"]["smc"],
            disable_web_page_preview=False,
            parse_mode='HTML',
            reply_markup=keyboard)
        bot.register_next_step_handler(msg_smc, org_info)
    elif message.text == 'РСО':
        keyboard = types.InlineKeyboardMarkup()
        vk_button = types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/smcpsuti")
        keyboard.add(vk_button)
        msg_rso = bot.send_message(
            message.chat.id,
            text=config["ORG_INFORMATION"]["rso"],
            disable_web_page_preview=False,
            parse_mode='HTML',
            reply_markup=keyboard)
        bot.register_next_step_handler(msg_rso, org_info)
    elif message.text == 'Спортивные секции':
        keyboard = types.InlineKeyboardMarkup()
        site_btn = types.InlineKeyboardButton(text="Перейти на сайт", url="http://sport.psuti.ru/")
        keyboard.add(site_btn)
        msg_sport = bot.send_message(
            message.chat.id,
            text=config["ORG_INFORMATION"]["sport"],
            disable_web_page_preview=False,
            parse_mode='HTML',
            reply_markup=keyboard)
        bot.register_next_step_handler(msg_sport, org_info)
    elif message.text == 'Меню':
        general.help_message(message)
    else:
        msg_understand = bot.send_message(
            message.chat.id,
            'Я Вас не понял, выберите раздел из меню или используйте кнопку Меню для выхода в меню')
        bot.register_next_step_handler(msg_understand, org_info)

handlers = {'studorganizations': studorganizations}