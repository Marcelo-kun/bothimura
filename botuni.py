from ast import pattern
from asyncore import dispatcher
from cgitb import text
from email.message import Message
from tkinter import Button
from click import command
from requests import request
from setuptools import Command
import telebot
from flask import Flask, request
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove



        

API_TOKEN  = '5526189505:AAGV3T6-SIgRa_mo1JrZsMkmdV5wjakklLM'

bot = telebot.TeleBot(API_TOKEN)
server = Flask(__name__)

button1 = KeyboardButton('Hello')
button2 = KeyboardButton('Youtube')
keyboard1=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button1, button2)

button3 = KeyboardButton('Hello' , request_contact=True)
button4 = KeyboardButton('Youtube', request_contact=True)
keyboard2=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button3, button4)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    message.reply("Resultado 1", reply_markup=keyboard1)

@bot.message_handler(commands=['info'])
def info(message):
    message.reply("Resultado 2 ", reply_markup=keyboard2)


"""@bot.message_handler(commands=['start'])
def send_welkome(message):
    bot.reply_to(message, "Hola, soy un 🤖ChatBot informativo de la Universidad Gran Asuncion")"""
    


"""def comand_callback_handler(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text='Te envio un texto'
    )
    return INPUT_TEXT


    button1 = InlineKeyboardButton(
        text = 'Sobre el autor',
        url = 'https://www.youtube.com/watch?v=DBoWGTO4TaU&t=824s'
    )

    update.message.reply.text(
        text='Haz click en un boton',
        reply_markup=InlineKeyboardMarkup([
            [button1]
        ])
    )"""

    

@bot.message_handler(commands=['botones'])
def cmd_botones(message):
    """Muestra un mensaje con botones inline (a continuacion del mensaje)"""
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("UGA Radio", url="http://ugaradio.com.py/")
    b2 = InlineKeyboardButton("UNIGRAN WEB", url="https://www.unigran.edu.py/")
    b3 = InlineKeyboardButton("UNIGRAN FACEBOOK", url="https://www.facebook.com/unigranparaguay?_rdc=1&_rdr")
    markup.add(b1, b2, b3)
    bot.send_message(message.chat.id, "Enlaces que pueden intereasarte 🎓Haz click en el botón", reply_markup=markup)

"""@bot.message_handler(commands=['consulta'])
def consulta_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row = ('Carreras')
    bot.send_message(message.chat.id, 'Consulta1', reply_markup=keyboard)"""



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
