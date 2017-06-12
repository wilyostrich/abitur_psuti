import configparser
import telebot
import dependency_injector as di

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from di_configuration import DIConfige, DIBot

from views import handlers, specialty
from views.specialty import call_back_handlers
from config import DATABASE_URI

config = configparser.ConfigParser()
config.read('text_config.ini', encoding='UTF-8')

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

bot = telebot.TeleBot(config["DEFAULT"]["Token"])

db_session_prv = di.Object(session)
specialty.DIService.db_session.override(db_session_prv)

config_prv = di.Object(config)
DIConfige.config_ini.override(config_prv)

bot_prv = di.Object(bot)
DIBot.di_bot.override(bot_prv)

# Добавляем обработчики
for name, func in handlers.items():
    bot.message_handler(commands=[name])(
        lambda massage, func=func: func(massage)
    )

for arg_dec, dec_func in call_back_handlers.values():
    bot.callback_query_handler(arg_dec)(dec_func)


if __name__ == '__main__':
    bot.polling(none_stop=True)
