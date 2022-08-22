"""from crypt import methods"""
from requests import post, request
import telebot
from flask import Flask, request
import os
"""from telebot.types import InlinekeyboardMarkup
from telebot.types import InlinekeyboardButton"""""


API_TOKEN  = '5526189505:AAGV3T6-SIgRa_mo1JrZsMkmdV5wjakklLM'

bot = telebot.TeleBot(API_TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welkome(message):
    bot.reply_to(message, "Bienvenido/a al Bot")

@bot.message_handler(commands=['Hola'])
def send_welkome(message):
    bot.reply_to(message, "Hola, soy un ChatBot informativo de la Universidad Gran Asuncion, en que puedo ayudarte?")

"""@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'hola':
        bot.send_message(message.chat.id, 'Hola, en que puedo ayudarte?')
    elif message.text.lower() == 'Gracias':
        bot.send_message(message.chat.id, 'Gracias a usted por utilizar el sistema de consulta Bot de Telegram!')"""

"""@bot.message_handler(commands=['botones'])
def cmd_botones(message):"""
"""Muestra un mensaje con botones inline (a continuacion del mensaje)"""
""" markup = InlinekeyboardMarkup(row_width = 2)
    b1 = InlinekeyboardButton("UGA Radio", url="http://ugaradio.com.py/")
    b2 = InlinekeyboardButton("UNIGRAN WEB", url="https://www.unigran.edu.py/")
    b3 = InlinekeyboardButton("UNIGRAN FACEBOOK", url="https://www.facebook.com/unigranparaguay?_rdc=1&_rdr")
    markup.add(b1, b2, b3)
    bot.send_message(message.chat.id, "Enlaces que pueden intereasarte", reply_markup=markup)"""

@server.route('/' + API_TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode('utf-8'))])
    return "!", 200

@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://bothimura.herokuapp.com/' + API_TOKEN)
    return "!", 200

if __name__ + '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))