import telebot
from dotenv import load_dotenv
import os


TOKEN = os.getenv('TELEGRAM_TOKEN')

bot  = telebot.TeleBot(TOKEN)



# creacion de comandos /start y /help

@bot.message_handler(commands=['start'])
def sen_welcome(message):
    bot.reply_to(message, "Hola, Este bot es Sobre la web Navi Esplore, Software, que te ayudara encontrar mejores lugares en la cuidades del mundo")
    
    
@bot.message_handler(commands=['help'])
def sen_help(message):
    bot.reply_to(message, "Puedes interactuar por comando proximamente")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
if __name__ == '__main__':
    bot.polling(none_stop=True)



