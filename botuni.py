from requests import request
import telebot
from flask import Flask, request
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


        

API_TOKEN  = '5526189505:AAGV3T6-SIgRa_mo1JrZsMkmdV5wjakklLM'
bot = telebot.TeleBot(API_TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welkome(message):
    bot.reply_to(message, "Hola, soy un 🤖ChatBot informativo de la Universidad Gran Asuncion. Presiona el comando /carreras para conocer los detalles de cada una de las carreras de grado habilitadas por la Cones y acreditadas por Aneaes. Tambien el comando /botones si deseas conocer un poco más acerca de la Universidad")


@bot.message_handler(commands=['carreras'])
def carreras_command(message):
   keyboard = telebot.types.InlineKeyboardMarkup()
   keyboard.add(
       telebot.types.InlineKeyboardButton(
           "Pagina Web Oficial 🎓", url='https://www.unigran.edu.py/'
       )
   )
   bot.send_message(
       message.chat.id,
       '1) Derecho \n' +
       '2) Ingeniería Comercial \n' +
       '3) Ingeniería en Informática \n' +
       '4) Ingeniería en Marketing y Publicidad \n' +
       '5) Licenciatura en Ciencias Contables \n' +
       '6) Licenciatura en Ciencias de la Educación \n' +
       '7) Licenciatura en Enfermería \n' +
       '8) Licenciatura en Psicología',
       reply_markup=keyboard
   )


@bot.message_handler(commands=['botones'])
def cmd_botones(message):
    """Muestra un mensaje con botones inline (a continuacion del mensaje)"""
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("UGA Radio", url="http://ugaradio.com.py/")
    b2 = InlineKeyboardButton("Aula Virtual", url="https://grado.unigran.edu.py/")
    b3 = InlineKeyboardButton("UNIGRAN FACEBOOK", url="https://www.facebook.com/unigranparaguay?_rdc=1&_rdr")
    b4 = InlineKeyboardButton("UNIGRAN INSTAGRAM", url="https://instagram.com/unigranpy?igshid=YmMyMTA2M2Y=")
    markup.add(b1, b2, b3, b4)
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
