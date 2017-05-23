import telebot
import configparser
DATABASE_URI = "postgresql://postgres:1234@localhost/abitur"
config = configparser.ConfigParser()
config.read('config.ini', encoding='UTF-8')
bot = telebot.TeleBot(config["DEFAULT"]["Token"])
