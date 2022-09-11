from requests import request
import telebot
from flask import Flask, request
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ForceReply
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


        

API_TOKEN  = '5526189505:AAGV3T6-SIgRa_mo1JrZsMkmdV5wjakklLM'
bot = telebot.TeleBot(API_TOKEN)
server = Flask(__name__)
usuarios = {}

@bot.message_handler(commands=['start'])
def send_welkome(message):
    markup = ReplyKeyboardRemove()
    bot.reply_to(message, "Hola, soy un 🤖ChatBot informativo de la Universidad Gran Asuncion. Presiona el comando /inicio o /carreras para conocer los detalles de cada una de las carreras de grado habilitadas por la Cones y acreditadas por Aneaes. Tambien el comando /botones si deseas conocer un poco más acerca de la Universidad", reply_markup=markup)

@bot.message_handler(commands=['inicio'])
def bot_inicio(message):
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, "¿Como te llamas?", reply_markup=markup)
    bot.register_next_step_handler(msg, preguntar_edad)

def preguntar_edad(message):
    usuarios[message.chat.id] = {}
    usuarios[message.chat.id]["nombre"] = message.text
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, "¿Cuantos años tienes?", reply_markup=markup)
    bot.register_next_step_handler(msg, preguntar_sexo)

def preguntar_sexo(message):
    if not message.text.isdigit():
        markup = ForceReply()
        msg = bot.send_message(message.chat.id, 'Error: indicar nro \n¿Cuantos años tienes?')
        bot.register_next_step_handler(msg, preguntar_sexo)
    else:
        usuarios[message.chat.id]["edad"] = int(message.text)
        markup = ReplyKeyboardMarkup(
            one_time_keyboard=True,
            input_field_placeholder="Pulsa un boton",
            resize_keyboard=True
            )
        markup.add("hombre", "mujer")
        msg = bot.send_message(message.chat.id, '¿Cual es tu sexo?', reply_markup=markup)
        bot.register_next_step_handler(msg, guardar_datos_usuario)

def guardar_datos_usuario(message):
    if message.text != "hombre" and message.text != "mujer":
        msg = bot.send_message(message.chat.id, 'Error: sexo no valido. \n Pulsa un boton')
        bot.register_next_step_handler(msg, guardar_datos_usuario)
    else:
        usuarios[message.chat.id]["sexo"] = message.text
        texto = 'Datos introducidos:\n'
        texto+= f'<code>Nombre:</code> {usuarios[message.chat,id]["nombre"]}\n'
        texto+= f'<code>Edad..:</code> {usuarios[message.chat,id]["edad"]}\n'
        texto+= f'<code>Sexo..:</code> {usuarios[message.chat,id]["sexo"]}\n'
        bot.send_message(message.chat.id, texto, parse_mode="html")
        print(usuarios)
        del usuarios[message.chat.id]

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
