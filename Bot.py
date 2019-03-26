#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

from telegram.ext import Updater, CommandHandler

updater = Updater(token='776802578:AAEzq0Gzd1mPdXgBLHYMcINEwL_UIdVjOF4')
dispatcher = updater.dispatcher

def saluda(bot, update):
    missatge = 'Sóc aquí :)'
    bot.send_message(chat_id=update.message.chat_id, text=missatge)

def saluda_nom(bot, update, args):
    missatge = 'Hola '+args[0]+'!'
    bot.send_message(chat_id=update.message.chat_id, text=missatge)

def imagen(bot, update):
    bot.send_photo(chat_id=update.message.chat_id, photo='https://pbs.twimg.com/media/DwFIu6-WkAAfJda.jpg')

numero=random.randint(1,100)
cont = 0

def jugar(bot, update, args):
    global numero
    global cont
    user = args[0]
    bot.send_message(chat_id=update.message.chat_id, text=numero)

    if user == str(user):
	bot.send_message(chat_id=update.message.chat_id, text='Introduce un numero')

    if numero < int(user):
	cont = cont+1
	missatge = 'Intentos '+str(cont)
	bot.send_message(chat_id=update.message.chat_id, text='El numero es mas pequeño')
	bot.send_message(chat_id=update.message.chat_id, text=missatge)

    if numero > int(user):
	cont = cont+1
	missatge = 'Intentos '+str(cont)
	bot.send_message(chat_id=update.message.chat_id, text='El numero es mas grande')
	bot.send_message(chat_id=update.message.chat_id, text=missatge)

    if numero == int(user):
	cont = cont+1
	missatge = 'Felicidades, has acertado con un numero de intentos de '+str(cont)
	bot.send_message(chat_id=update.message.chat_id, text=missatge)
	cont = 0
	numero=random.randint(1,100)



handlers = [CommandHandler('saluda', saluda),
	    CommandHandler('imagen', imagen),
            CommandHandler('saluda_nom', saluda_nom, pass_args=True),
	    CommandHandler('jugar', jugar, pass_args=True)]

for handler in handlers:
    dispatcher.add_handler(handler)

updater.start_polling()
