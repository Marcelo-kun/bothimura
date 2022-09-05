from requests import request
import telebot
from flask import Flask, request
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove



        

API_TOKEN  = '5526189505:AAGV3T6-SIgRa_mo1JrZsMkmdV5wjakklLM'

bot = telebot.TeleBot(API_TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['botones'])
def cmd_botones(message):
    """Muestra un mensaje con botones inline (a continuacion del mensaje)"""
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = KeyboardButton("UGA Radio", text="http://ugaradio.com.py/")
    b2 = InlineKeyboardButton("UNIGRAN WEB", url="https://www.unigran.edu.py/")
    b3 = InlineKeyboardButton("UNIGRAN FACEBOOK", url="https://www.facebook.com/unigranparaguay?_rdc=1&_rdr")
    markup.add(b1, b2, b3)
    bot.send_message(message.chat.id, "Enlaces que pueden intereasarte 🎓Haz click en el botón", reply_markup=markup)


@bot.message_handler(commands=['start'])
def send_welkome(message):
    bot.reply_to(message, "Hola, soy un 🤖ChatBot informativo de la Universidad Gran Asuncion")



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
