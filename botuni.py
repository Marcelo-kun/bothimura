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
usuarios = {} #se crea un diccionario vacio para cargar los datos de usuario de manera global

#responde al comando /start
@bot.message_handler(commands=['start'])
def send_welkome(message):
    markup = ReplyKeyboardRemove() #se remueven botones despues de darle un click
    #acontinuacion el bot saluda
    bot.reply_to(message, "Hola, soy un 🤖ChatBot informativo de la Universidad Gran Asuncion. Para conocer un poco más de lo que puedes hacer con este bot te invitamos a darle click al Menu de comandos ubicado en la parte inferior izquierdo de tu pantalla, allí se desplegaran una lista de comandos con una breve descripcion de las acciones que relizan cada una de ellas.", reply_markup=markup)



@bot.message_handler(commands=['infor'])
def bot_inicio(message):
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, "¿Como te llamas?", reply_markup=markup) #pregunta el nombre del usuario
    bot.register_next_step_handler(msg, preguntar_carrera) #se registra respuesta en una funcion

###############botones de seleccion############
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
            

            #se informa del error y se vuelve a preguntar 
    """if usuarios[message.chat.id]["carrera"] != "Ing. Informática" or usuarios[message.chat.id]["carrera"] != "Ing. Comercial"  or usuarios[message.chat.id]["carrera"] != "Ing. en Marketing y Publicidad" or usuarios[message.chat.id]["carrera"] != "Lic. en Ciencias Contables" or usuarios[message.chat.id]["carrera"] != "Lic. en Ciencias de la Educación" or usuarios[message.chat.id]["carrera"] != "Lic. en Enfermería" or usuarios[message.chat.id]["carrera"] != "Lic. en Psicología" or usuarios[message.chat.id]["carrera"] != "Derecho":
        msg = bot.send_message(message.chat.id, "Error: Carrera no valida.\n Pulsa un boton")
        #se vuelve a ejecutar la funcion
        bot.register_next_step_handler(msg, preguntar_carrera)
        #se informa del error y se vuelve a preguntar
    else:
    bot.register_next_step_handler(msg, preguntar_curso) #se registra respuesta en una funcion """

def preguntar_curso(message):#esta funcion contiene la respuesta anterior    
    usuarios[message.chat.id]["carrera"] = message.text #se guarda curso dentro del diccionario vacio
    if usuarios[message.chat.id]["carrera"] != "Ing. Informatica" and usuarios[message.chat.id]["carrera"] != "Ing. Comercial" and usuarios[message.chat.id]["carrera"] != "Ing. en Marketing y Publicidad" and usuarios[message.chat.id]["carrera"] != "Lic. en Ciencias Contables" and usuarios[message.chat.id]["carrera"] != "Lic. en Ciencias de la Educación" and usuarios[message.chat.id]["carrera"] != "Lic. en Enfermería" and usuarios[message.chat.id]["carrera"] != "Lic. en Psicología" and usuarios[message.chat.id]["carrera"] != "Derecho":
        msg = bot.send_message(message.chat.id, "Error: Carrera no valida.\n Pulsa un boton")
        bot.register_next_step_handler(msg, preguntar_carrera)  
    else:
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
            usuarios[message.chat.id]["cuota"] = "12 Cuotas de 300.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "Matrícula Gratuita"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso.....:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera...:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
            
        elif usuarios[message.chat.id]["curso"] == "2do Curso":
            usuarios[message.chat.id]["cuota"] = "350.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso.....:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera...:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
        
        elif usuarios[message.chat.id]["curso"] == "3er Curso":
            usuarios[message.chat.id]["cuota"] = "400.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "4to Curso":
            usuarios[message.chat.id]["cuota"] = "450.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "5to Curso":
            usuarios[message.chat.id]["cuota"] = "500.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
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
            usuarios[message.chat.id]["cuota"] = "12 Cuotas de 300.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "Matrícula Gratuita"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u>  {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
            
        elif usuarios[message.chat.id]["curso"] == "2do Curso":
            usuarios[message.chat.id]["cuota"] = "350.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso.....:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera...:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
        
        elif usuarios[message.chat.id]["curso"] == "3er Curso":
            usuarios[message.chat.id]["cuota"] = "400.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "4to Curso":
            usuarios[message.chat.id]["cuota"] = "450.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "5to Curso":
            usuarios[message.chat.id]["cuota"] = "500.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
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
            usuarios[message.chat.id]["cuota"] = "12 Cuotas de 300.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "Matrícula Gratuita"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u>  {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
            
        elif usuarios[message.chat.id]["curso"] == "2do Curso":
            usuarios[message.chat.id]["cuota"] = "350.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso.....:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera...:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
        
        elif usuarios[message.chat.id]["curso"] == "3er Curso":
            usuarios[message.chat.id]["cuota"] = "400.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "4to Curso":
            usuarios[message.chat.id]["cuota"] = "450.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "5to Curso":
            usuarios[message.chat.id]["cuota"] = "500.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
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
            usuarios[message.chat.id]["cuota"] = "12 Cuotas de 300.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "Matrícula Gratuita"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u>  {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
            
        elif usuarios[message.chat.id]["curso"] == "2do Curso":
            usuarios[message.chat.id]["cuota"] = "350.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso.....:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera...:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
        
        elif usuarios[message.chat.id]["curso"] == "3er Curso":
            usuarios[message.chat.id]["cuota"] = "400.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "4to Curso":
            usuarios[message.chat.id]["cuota"] = "450.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "5to Curso":
            usuarios[message.chat.id]["cuota"] = "500.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
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
            usuarios[message.chat.id]["cuota"] = "12 Cuotas de 300.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "Matrícula Gratuita"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u>  {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
            
        elif usuarios[message.chat.id]["curso"] == "2do Curso":
            usuarios[message.chat.id]["cuota"] = "350.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso.....:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera...:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
        
        elif usuarios[message.chat.id]["curso"] == "3er Curso":
            usuarios[message.chat.id]["cuota"] = "400.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "4to Curso":
            usuarios[message.chat.id]["cuota"] = "450.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "5to Curso":
            usuarios[message.chat.id]["cuota"] = "500.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
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
            usuarios[message.chat.id]["cuota"] = "12 Cuotas de 300.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "Matrícula Gratuita"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u>  {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
            
        elif usuarios[message.chat.id]["curso"] == "2do Curso":
            usuarios[message.chat.id]["cuota"] = "350.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso.....:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera...:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
        
        elif usuarios[message.chat.id]["curso"] == "3er Curso":
            usuarios[message.chat.id]["cuota"] = "400.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "4to Curso":
            usuarios[message.chat.id]["cuota"] = "450.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "5to Curso":
            usuarios[message.chat.id]["cuota"] = "500.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
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
            usuarios[message.chat.id]["cuota"] = "12 Cuotas de 300.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "Matrícula Gratuita"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u>  {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
            
        elif usuarios[message.chat.id]["curso"] == "2do Curso":
            usuarios[message.chat.id]["cuota"] = "350.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso.....:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera...:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
        
        elif usuarios[message.chat.id]["curso"] == "3er Curso":
            usuarios[message.chat.id]["cuota"] = "400.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "4to Curso":
            usuarios[message.chat.id]["cuota"] = "450.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "5to Curso":
            usuarios[message.chat.id]["cuota"] = "500.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
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
            usuarios[message.chat.id]["cuota"] = "12 Cuotas de 300.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "Matrícula Gratuita"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u>  {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
            
        elif usuarios[message.chat.id]["curso"] == "2do Curso":
            usuarios[message.chat.id]["cuota"] = "350.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso.....:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera...:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario
        
        elif usuarios[message.chat.id]["curso"] == "3er Curso":
            usuarios[message.chat.id]["cuota"] = "400.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "4to Curso":
            usuarios[message.chat.id]["cuota"] = "450.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

        elif usuarios[message.chat.id]["curso"] == "5to Curso":
            usuarios[message.chat.id]["cuota"] = "500.000Gs"
            usuarios[message.chat.id]["Derecho de Examen"] = "40.000Gs"
            usuarios[message.chat.id]["Matrícula"] = "350.000Gs"
            texto = '<b>Datos introducidos:</b>\n'
            texto+= f'<u>Nombre.:</u> {usuarios[message.chat.id]["nombre"]}\n'
            texto+= f'<u>Curso..:</u> {usuarios[message.chat.id]["curso"]}\n'
            texto+= f'<u>Carrera:</u> {usuarios[message.chat.id]["carrera"]}\n\n'
            texto+= f'<b>👩‍🎓Resultados👨‍🎓:</b>\n'
            texto+= f'<u>Matrícula:</u> {usuarios[message.chat.id]["Matrícula"]}\n'
            texto+= f'<u>Cuotas:</u> {usuarios[message.chat.id]["cuota"]}\n'
            texto+= f'<u>Derecho de Exámen:</u> {usuarios[message.chat.id]["Derecho de Examen"]}\n'
            markup = ReplyKeyboardRemove()
            bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
            print(usuarios) #para que se vea en terminal
            del usuarios[message.chat.id] #se elimina los datos del diccinario

    else: 
        msg = bot.send_message(message.chat.id, "Error: Carrera no valida.\n Pulsa un boton")
        #se vuelve a ejecutar la funcion
        bot.register_next_step_handler(msg, preguntar_carrera)
        #se informa del error y se vuelve a preguntar


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
        telebot.types.BotCommand("/start", "Inicia el bot con unas recomendaciones"),
        telebot.types.BotCommand("/infor", "Consulta importe de cuotas"),
        telebot.types.BotCommand("/carreras", "Lista de carreras habilitadas"),
        telebot.types.BotCommand("/botones", "Enlace de interes académico"),
    ])
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))