import types
from requests import post, request
import telebot
from flask import Flask, request, request_started
import os
from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from logging import logger

        

API_TOKEN  = '5526189505:AAGV3T6-SIgRa_mo1JrZsMkmdV5wjakklLM'

bot = telebot.TeleBot(API_TOKEN)
server = Flask(__name__)

button1 = KeyboardButton('Hello')
button2 = KeyboardButton('Youtube')
keyboard1=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1).add(button2)

button3 = KeyboardButton('Hello', request_contact=True)
button4 = KeyboardButton('Youtube', request_contact=True)
keyboard2=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button3).add(button4)

@bot.message_handler(commands=['start'])
def send_welkome(message):
    bot.reply_to(message, "Hola, soy un 🤖ChatBot informativo de la Universidad Gran Asuncion")

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, "Informacion sobre ti:", reply_markup=keyboard2)

@bot.message_handler()
def kb_answer(message):
    if message.text == 'Hello':
        message.answer('Hola, sigue asi')
    elif message.text == 'Youtube':
        message.answer('mira mas tutoriales')
    else:
        message.answer(f' Your message is: {message.text}')

def Menu(update, context):
    bot = context.bot
    resize_keyboard=True
    ChatId = update.message.chat_id
    userName = update.effective_user["first_name"]
    logger.info(f'El Usuario {userName} Id:{ChatId} ah accedido al menu')
    keyboard = []
    keyboard.append([KeyboardButton(f'Informacion sobre el bot', callback_data='1')])
    keyboard.append([KeyboardButton(f'Mi WhatsApp', callback_data='2')])
    keyboard.append([KeyboardButton(f'Lista', callback_data='3')])
    keyboard.append([KeyboardButton(f'Bot para WA', callback_data='4')])
    keyboard.append([KeyboardButton(f'Redes Sociales', callback_data='5')])
    keyboard.append([KeyboardButton(f'Cafe?', callback_data='6')])
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('*****Menu*****\nElige una de las siguientes opciones:',  reply_markup=reply_markup)


@bot.message_handler(commands=['botones'])
def cmd_botones(message):
    """Muestra un mensaje con botones inline (a continuacion del mensaje)"""
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("UGA Radio", url="http://ugaradio.com.py/")
    b2 = InlineKeyboardButton("UNIGRAN WEB", url="https://www.unigran.edu.py/")
    b3 = InlineKeyboardButton("UNIGRAN FACEBOOK", url="https://www.facebook.com/unigranparaguay?_rdc=1&_rdr")
    markup.add(b1, b2, b3)
    bot.send_message(message.chat.id, "Enlaces que pueden intereasarte 🎓Haz click en el botón", reply_markup=markup)

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