from requests import request
import telebot
from flask import Flask, request
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ForceReply
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


        

API_TOKEN  = '5526189505:AAGV3T6-SIgRa_mo1JrZsMkmdV5wjakklLM'
bot = telebot.TeleBot(API_TOKEN)
server = Flask(__name__)
usuarios = {}


@bot.message_handler(commands=['start'])
def send_welkome(message):
    markup = ReplyKeyboardRemove()
    bot.reply_to(message, "Hola, soy un 🤖ChatBot informativo de la Universidad Gran Asuncion. Para conocer un poco más de lo que puedes hacer con este bot te invitamos a darle click al Menu de comandos ubicado en la parte inferior izquierdo de tu pantalla, allí se desplegaran una lista de comandos con una breve descripcion de las acciones que relizan cada una de ellas.", reply_markup=markup)



@bot.message_handler(commands=['inicio'])
def bot_inicio(message):
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, "¿Como te llamas?", reply_markup=markup)
    bot.register_next_step_handler(msg, preguntar_curso)

def preguntar_curso(message):
    usuarios[message.chat.id] = {}
    usuarios[message.chat.id]["nombre"] = message.text
    markup = ReplyKeyboardMarkup(
        input_field_placeholder="Pulsa un boton",
        resize_keyboard=True,
        row_width=5
        )
    markup.add("1er Curso", "2do Curso", "3er Curso", "4to Curso", "5to Curso")
    """markup = ForceReply()"""
    msg = bot.send_message(message.chat.id, "¿Curso?", reply_markup=markup)
    bot.register_next_step_handler(msg, preguntar_carrera)

def preguntar_carrera(message):
    if  message.text.isdigit():
        markup = ForceReply()
        msg = bot.send_message(message.chat.id, "Error: No indicar en nros \n¿Curso?")
        bot.register_next_step_handler(msg, preguntar_carrera)
    else:
        usuarios[message.chat.id]["curso"] = message.text
        markup = ReplyKeyboardMarkup( 
            input_field_placeholder="Pulsa un boton",
            resize_keyboard=True, 
            row_width=2
            )
        markup.add("Ing. Informatica", "Ing. Comercial", "Ing. en Marketing y Publicidad", "Lic. en Ciencias Contables", "Lic. en Ciencias de la Educación", "Lic. en Enfermería", "Lic. en Psicología", "Derecho" )
        msg = bot.send_message(message.chat.id, "¿Que Carrera?", reply_markup=markup)
        bot.register_next_step_handler(msg, guardar_datos_usuario)

"""def guardar_datos_usuario(message):
    if message.text != "Ing. Informatica" and message.text != "Ing. Comercial" and message.text != "Ing. en Marketing y Publicidad" and message.text != "Lic. en Ciencias Contables" and message.text != "Lic. en Ciencias de la Educación" and message.text != "Lic. en Enfermería" and message.text != "Lic. en Psicología" and message.text != "Derecho":
        msg = bot.send_message(message.chat.id, "Error: Carrera no valida.\n Pulsa un boton")
        bot.register_next_step_handler(msg, guardar_datos_usuario)"""

def guardar_datos_usuario(message):
    if message.text == "Ing. Informatica" and message.text == "1er Curso":
        carre = bot.send_message(message.chat.id, "Error: Carrera no valida.\n Pulsa un boton")
        bot.register_next_step_handler(carre, guardar_datos_usuario)
    else:
        usuarios[message.chat.id]["carrera"] = message.text
        texto = 'Datos introducidos:\n'
        texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
        texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
        texto+= f'<code>Carrera:</code> {usuarios[message.chat.id][carre]}\n'
        markup = ReplyKeyboardRemove()
        bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
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
    bot.set_my_commands([
        telebot.types.BotCommand("/start", "Da inicio al bot"),
        telebot.types.BotCommand("/inicio", "Breve presentacion del Usuario al bot"),
        telebot.types.BotCommand("/carreras", "Lista de carreras que ofrece la Universidad"),
        telebot.types.BotCommand("/botones", "Enlaces de interes"),
    ])
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
