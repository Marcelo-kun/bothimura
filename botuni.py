from requests import request
import telebot #para manejar la API de Telegram
from flask import Flask, request #para crear el srvidor web
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton #para crrear botones inline y para definir botones inline
from telebot.types import ForceReply
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove #para crear botones y para eliminar botones


        

API_TOKEN  = '5526189505:AAGV3T6-SIgRa_mo1JrZsMkmdV5wjakklLM'
bot = telebot.TeleBot(API_TOKEN)
#instancia de bot de Telegram
server = Flask(__name__)
#varaible global donde se guardaran los datos del usuario 
usuarios = {} #se crea un diccionario vacio

#responde al comando /start
@bot.message_handler(commands=['start'])
def send_welkome(message):
    markup = ReplyKeyboardRemove() #se remueven botones despues de darle un click
    #acontinuacion el bot saluda
    bot.reply_to(message, "Hola, soy un 🤖ChatBot informativo de la Universidad Gran Asuncion. Para conocer un poco más de lo que puedes hacer con este bot te invitamos a darle click al Menu de comandos ubicado en la parte inferior izquierdo de tu pantalla, allí se desplegaran una lista de comandos con una breve descripcion de las acciones que relizan cada una de ellas.", reply_markup=markup)



@bot.message_handler(commands=['inicio'])
def bot_inicio(message):
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, "¿Como te llamas?", reply_markup=markup) #pregunta el nombre del usuario
    bot.register_next_step_handler(msg, preguntar_carrera) #se registra respuesta en una funcion
###codigo de prueba sin botones#############

def preguntar_carrera(message): 
    usuarios[message.chat.id] = {} #se utiliza el diccionario usuarios y como clave el chat.id y dentro de esta clave vamos a guardar un diccionario vacio 
    usuarios[message.chat.id]["nombre"] = message.text #se guarda nombre dentro del diccionario vacio
    markup = ReplyKeyboardMarkup(
        input_field_placeholder="Pulsa un boton",
        resize_keyboard=True,
        row_width=2
        )
    markup.add("Ing. Informática", "Ing. Comercial", "Ing. en Marketing y Publicidad", "Lic. en Ciencias Contables", "Lic. en Ciencias de la Educación", "Lic. en Enfermería", "Lic. en Psicología", "Derecho")
    msg = bot.send_message(message.chat.id, "¿Cual es tu Carrera?", reply_markup=markup)
    bot.register_next_step_handler(msg, preguntar_curso) #se registra respuesta en una funcion

def preguntar_curso(message):
    usuarios[message.chat.id]["carrera"] = message.text #se guarda curso dentro del diccionario vacio
    markup = ReplyKeyboardMarkup(
        input_field_placeholder="Pulsa un boton",
        resize_keyboard=True,
        row_width=5
        )
    markup.add("1er Curso", "2do Curso", "3er Curso", "4to Curso", "5to Curso")
    msg = bot.send_message(message.chat.id, "¿Cual es tu Curso?", reply_markup=markup)
    bot.register_next_step_handler(msg, guardar_datos_usuario) #se registra respuesta en una funcion

def guardar_datos_usuario(message):
    usuarios[message.chat.id]["curso"] = message.text #se guarda curso dentro del diccionario vacio
    #guardamos los datos introducidos por el usuario
    #si la carrera introducida no es valido
    if usuarios[message.chat.id]["carrera"] == "Ing. Informática":
        
        if usuarios[message.chat.id]["curso"] == "1er Curso":
            usuarios[message.chat.id]["cuota"] = "12 Cuotas de 500.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "50.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<u>Nombre:</u> \n{usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso:</u> \n{usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> \n{usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<u>Cuotas:</u> \n{usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> \n{usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
            
        elif usuarios[message.chat.id]["curso"] == "2do Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
        
        elif usuarios[message.chat.id]["curso"] == "3er Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "4to Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "5to Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        else: 
            msg = bot.send_message(message.chat.id, "Error: Curso no valido.\n Pulsa un boton")
            #se vuelve a ejecutar la funcion
            bot.register_next_step_handler(msg, preguntar_curso)
            #se informa del error y se vuelve a preguntar
#####################################################Ing. Comercial######################################################################################
    elif usuarios[message.chat.id]["carrera"] == "Ing. Comercial":
        if usuarios[message.chat.id]["curso"] == "1er Curso":
            usuarios[message.chat.id]["cuota"] = "500.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
            
        elif usuarios[message.chat.id]["curso"] == "2do Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
        
        elif usuarios[message.chat.id]["curso"] == "3er Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "4to Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "5to Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        else: 
            msg = bot.send_message(message.chat.id, "Error: Curso no valido.\n Pulsa un boton")
            #se vuelve a ejecutar la funcion
            bot.register_next_step_handler(msg, preguntar_curso)
            #se informa del error y se vuelve a preguntar
#####################################################Ing. en Marketing y Publicidad##########################################################################
    elif usuarios[message.chat.id]["carrera"] == "Ing. en Marketing y Publicidad":
        if usuarios[message.chat.id]["curso"] == "1er Curso":
            usuarios[message.chat.id]["cuota"] = "500.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
            
        elif usuarios[message.chat.id]["curso"] == "2do Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
        
        elif usuarios[message.chat.id]["curso"] == "3er Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "4to Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "5to Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
        else: 
            msg = bot.send_message(message.chat.id, "Error: Curso no valido.\n Pulsa un boton")
            #se vuelve a ejecutar la funcion
            bot.register_next_step_handler(msg, preguntar_curso)
            #se informa del error y se vuelve a preguntar
#####################################################Lic. en Ciencias Contables######################################################################################
    elif usuarios[message.chat.id]["carrera"] == "Lic. en Ciencias Contables":
        if usuarios[message.chat.id]["curso"] == "1er Curso":
            usuarios[message.chat.id]["cuota"] = "500.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
            
        elif usuarios[message.chat.id]["curso"] == "2do Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
        
        elif usuarios[message.chat.id]["curso"] == "3er Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "4to Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "5to Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        else: 
            msg = bot.send_message(message.chat.id, "Error: Curso no valido.\n Pulsa un boton")
            #se vuelve a ejecutar la funcion
            bot.register_next_step_handler(msg, preguntar_curso)
            #se informa del error y se vuelve a preguntar
#####################################################Lic. en Ciencias de la Educación######################################################################################
    elif usuarios[message.chat.id]["carrera"] == "Lic. en Ciencias de la Educación":
        if usuarios[message.chat.id]["curso"] == "1er Curso":
            usuarios[message.chat.id]["cuota"] = "500.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
            
        elif usuarios[message.chat.id]["curso"] == "2do Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
        
        elif usuarios[message.chat.id]["curso"] == "3er Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "4to Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "5to Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        else: 
            msg = bot.send_message(message.chat.id, "Error: Curso no valido.\n Pulsa un boton")
            #se vuelve a ejecutar la funcion
            bot.register_next_step_handler(msg, preguntar_curso)
            #se informa del error y se vuelve a preguntar
#####################################################Lic. en Enfermería######################################################################################
    elif usuarios[message.chat.id]["carrera"] == "Lic. en Enfermería":
        if usuarios[message.chat.id]["curso"] == "1er Curso":
            usuarios[message.chat.id]["cuota"] = "500.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
            
        elif usuarios[message.chat.id]["curso"] == "2do Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
        
        elif usuarios[message.chat.id]["curso"] == "3er Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "4to Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "5to Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        else: 
            msg = bot.send_message(message.chat.id, "Error: Curso no valido.\n Pulsa un boton")
            #se vuelve a ejecutar la funcion
            bot.register_next_step_handler(msg, preguntar_curso)
            #se informa del error y se vuelve a preguntar
#####################################################Lic. en Psicología######################################################################################
    elif usuarios[message.chat.id]["carrera"] == "Lic. en Psicología":
        if usuarios[message.chat.id]["curso"] == "1er Curso":
            usuarios[message.chat.id]["cuota"] = "500.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
            
        elif usuarios[message.chat.id]["curso"] == "2do Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
        
        elif usuarios[message.chat.id]["curso"] == "3er Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "4to Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "5to Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        else: 
            msg = bot.send_message(message.chat.id, "Error: Curso no valido.\n Pulsa un boton")
            #se vuelve a ejecutar la funcion
            bot.register_next_step_handler(msg, preguntar_curso)
            #se informa del error y se vuelve a preguntar
#####################################################Derecho######################################################################################
    elif usuarios[message.chat.id]["carrera"] == "Derecho":
        if usuarios[message.chat.id]["curso"] == "1er Curso":
            usuarios[message.chat.id]["cuota"] = "500.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
            
        elif usuarios[message.chat.id]["curso"] == "2do Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
        
        elif usuarios[message.chat.id]["curso"] == "3er Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "4to Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "5to Curso":
            usuarios[message.chat.id]["cuota"] = "600.000Gs"
            texto = 'Datos introducidos:\n'
            texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
            texto+= f'<code>Cuota..:</code> {usuarios[message.chat.id]["cuota"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        else: 
            msg = bot.send_message(message.chat.id, "Error: Curso no valido.\n Pulsa un boton")
            #se vuelve a ejecutar la funcion
            bot.register_next_step_handler(msg, preguntar_curso)
            #se informa del error y se vuelve a preguntar

    else: 
        msg = bot.send_message(message.chat.id, "Error: Carrera no valida.\n Pulsa un boton")
    #se vuelve a ejecutar la funcion
        bot.register_next_step_handler(msg, bot_inicio)
        #se informa del error y se vuelve a preguntar

#codigo con botones################################
"""def preguntar_curso(message): 
    usuarios[message.chat.id] = {} #se utiliza el diccionario usuarios y como clave el chat.id y dentro de esta clave vamos a guardar un diccionario vacio 
    usuarios[message.chat.id]["nombre"] = message.text #se guarda nombre dentro del diccionario vacio
    markup = ReplyKeyboardMarkup(
        input_field_placeholder="Pulsa un boton",
        resize_keyboard=True,
        row_width=5
        )
    markup.add("1er Curso", "2do Curso", "3er Curso", "4to Curso", "5to Curso")
    msg = bot.send_message(message.chat.id, "¿Curso?", reply_markup=markup)
    bot.register_next_step_handler(msg, preguntar_carrera)

def preguntar_carrera(message):#esta funcion contiene la respuesta anterior
    if  message.text.isdigit(): #el metodo isdigit nos devuelve un True si el contenido es un nro
        #informar del error
        markup = ForceReply()
        msg = bot.send_message(message.chat.id, "Error: No indicar en nros \n¿Curso?")
        #se vuelve a ejecutar la funcion
        bot.register_next_step_handler(msg, preguntar_carrera)
    else: #si se introdujo el curso correcto
        #se definiran botones
        usuarios[message.chat.id]["curso"] = message.text #en la clave curso se guarda los datos introducidos
        markup = ReplyKeyboardMarkup( 
            input_field_placeholder="Pulsa un boton", #argumento que indicara la accion que se debe realizar
            resize_keyboard=True, #argumento para reescalar el teclado
            row_width=2 # nro de botones en cada fila
            )
        #añadir botones
        markup.add("Ing. Informatica", "Ing. Comercial", "Ing. en Marketing y Publicidad", "Lic. en Ciencias Contables", "Lic. en Ciencias de la Educación", "Lic. en Enfermería", "Lic. en Psicología", "Derecho" )
        #se pregunta por el curso
        msg = bot.send_message(message.chat.id, "¿Que Carrera?", reply_markup=markup)
        bot.register_next_step_handler(msg, guardar_datos_usuario) #se guaradaran los datos en una funcion con este nombre"""


"""def guardar_datos_usuario(message):
    #guardamos los datos introducidos por el usuario
    #si la carrera introducida no es valido
    if message.text != "Ing. Informatica" and message.text != "Ing. Comercial" and message.text != "Ing. en Marketing y Publicidad" and message.text != "Lic. en Ciencias Contables" and message.text != "Lic. en Ciencias de la Educación" and message.text != "Lic. en Enfermería" and message.text != "Lic. en Psicología" and message.text != "Derecho":
        #se informa del error y se vuelve a preguntar
        msg = bot.send_message(message.chat.id, "Error: Carrera no valida.\n Pulsa un boton")
        #se vuelve a ejecutar la funcion
        bot.register_next_step_handler(msg, guardar_datos_usuario)
    else: #si la cerrrera introducida es valida
        usuarios[message.chat.id]["carrera"] = message.text
        #se crea una variable tipo string donde se guarda una cadena de texto en la que se indica los datos introducidos formateando la salida
        texto = 'Datos introducidos:\n'
        texto+= f'<code>Nombre.:</code> {usuarios[message.chat.id]["nombre"]}\n'
        texto+= f'<code>Curso..:</code> {usuarios[message.chat.id]["curso"]}\n'
        texto+= f'<code>Carrera:</code> {usuarios[message.chat.id]["carrera"]}\n'
        markup = ReplyKeyboardRemove()
        bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
        print(usuarios) #para que se vea en terminal
        del usuarios[message.chat.id] #se elimina los datos del diccinario"""

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
    markup = InlineKeyboardMarkup(row_width = 2) # nro de botones en cada fila
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
    bot.remove_webhook() #pequeña pausa para que se elimine el webhook
    bot.set_webhook(url='https://bothimura.herokuapp.com/' + API_TOKEN)
    return "!", 200
#Menu ###############################################################################################################
if __name__ + '__main__':
    bot.set_my_commands([
        # se crea un menu en la parte inferior izquierdo de la interfaz de Telegram
        telebot.types.BotCommand("/start", "Da inicio al bot"),
        telebot.types.BotCommand("/inicio", "Breve presentacion del Usuario al bot"),
        telebot.types.BotCommand("/carreras", "Lista de carreras que ofrece la Universidad"),
        telebot.types.BotCommand("/botones", "Enlaces de interes"),
    ])
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
