from asyncore import dispatcher
from itertools import chain
from os import name

import tele as tele
import telepot
#import updater as updater

#from telegram.ext import CommandHandler
#from telegram.ext import *
import re

from nltk import interval_distance
from telepot.exception import TelegramError
import telebot
#import pyTelegramBotAPI
#from win32com.server import dispatcher

import newconstants
import requests as requests
import config
import json
import pprint
import random
import telebot
import sys
import time
import telegram
import requests

#token = '909185060:AAHMMywktcc18wD14yA-jFvJMnSi--S3x7g'
#foto = 'https://api.telegram.org/bot909185060:AAHMMywktcc18wD14yA-jFvJMnSi--S3x7g/sendphoto?chat_id=814781595&photo=AgADAgAD5KwxG-h1wUi3lPTs40-S9tCpwg8ABAEAAwIAA20AA_fjAgABFgQ'

#https://api.telegram.org/bot909185060:AAHMMywktcc18wD14yA-jFvJMnSi--S3x7g/getUpdates

#po2 = 'https://api.telegram.org/bot909185060:AAHMMywktcc18wD14yA-jFvJMnSi--S3x7g/sendphoto?chat_id=814781595&photo=AgADAgADhqwxG4E3yEjqZ7QE3IIZsaYiwQ4ABAEAAwIAA3gAA65MAQABFgQ'
URL = 'https://api.telegram.org/bot909185060:AAHMMywktcc18wD14yA-jFvJMnSi--S3x7g'
#bot.send_photo(chat_id=chat_id, photo='https://telegram.org/img/t_logo.png')
#bot.send_photo(chat_id=chat_id, foto='https://api.telegram.org/bot909185060:AAHMMywktcc18wD14yA-jFvJMnSi--S3x7g/sendphoto?chat_id=814781595&photo=AgADAgAD5KwxG-h1wUi3lPTs40-S9tCpwg8ABAEAAwIAA20AA_fjAgABFgQ')
#chat_id = '814781595'
#message1 = 'hello world!'

#def start_message(message):

chat_id = '814781595'
#po2 ='AgADAgADhqwxG4E3yEjqZ7QE3IIZsaYiwQ4ABAEAAwIAA3gAA65MAQABFgQ'
foto = 'AAQCAAMEBAAC6HXBSFVC4Yyt3bbPC0HKDgAEAQAHbQADuTUAAhYE'
message1 = 'hello world!'
message2 = 'I am Bot, please talk to me!' \
           ' Bots have no online status and no last seen times tamps, the interface shows the label ‘bot’ instead.' \
           ' Bots have limited cloud storage — older messages may be removed by the server shortly after they have been processed.' \
           ' Bots can not initiate conversations with users. A user must either add them to a group or send them a message first.' \
           ' People can use t.me/<bot_username> links or username search to find your bot.' \
           ' Bots never eat, sleep or complain (unless expressly programmed otherwise).'
mebot = 'https://core.telegram.org/file/811140327/1/zlN4goPTupk/9ff2f2f01c4bd1b013'

message3 = 'I am Bot!'
message4 = 'see youuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu'
message5 = 'Thank you for talking to me, bye bye.' \
           ' Obrigada por ter falado comigo, tchau tchau.' \
           ' Спасибо, что поговорили со мной, пока, пока.'

#test = bot.send_audio(chat_id, 'Aperta (BM House feat Ery Stifler) C3 produtions.mp3')
Mygroup_id='-424267332'
#Mygroup_id = https://web.telegram.org/#/im?p=g424267332
#group_id_site = 'https://t.me/joinchat/M30LOw1QkMvusuS9wYV-ug'
group_id_site = 'https://web.telegram.org/#/im?p=s1201883098_18052776823377465520'
#group_id='187864217'
title: "Team Português"
username: "DamiaoPedro"

#807826655
file_id ='AgADAgAD5KwxG-h1wUi3lPTs40-S9tCpwg8ABAEAAwIAA3kAA_XjAgABFgQ'

bot = telebot.TeleBot(newconstants.token)
#bot.config['api_key'] = newconstants.token
#Enviar mensagem no grupooooooooooooooooooooooooooooooooooooooo
#def send_message(group_id, message4):
 #test = bot.send_message(group_id_site, message4)
site = 'https://web.telegram.org/#/im?p=g154513121'
#test = bot.sendMessage(Mygroup_id, message4)
#test = bot.send_message(chat_id, message1)
test = bot.send_message(chat_id, message1)
#test = bot.send_photo(chat_id, foto)
print(bot)

#@bot.message_handler(commands=['start'])
#def handler_text(message):
   # bot.send_message(message.chat.id, message1)

#bot.send_photo(chat_id,'https://yt3.ggpht.com/a/AGF-l79NMNqpULD_ePeyUGPgUSqDbYjus6f3wNtdng=s900-c-k-c0xffffffff-no-rj-mo')
test = bot.send_message(chat_id, 'write hi')
#@bot.message_handler(content_types=['text'])
#def handler_text(message):
 #   print(message)
  #  if message.text == "prin":
     #   bot.send_photo(chat_id,'https://www.google.com/imgres?imgurl=http%3A%2F%2Fwww.prin.ru%2Fimages%2Fnews%2Fprin%2F2019%2F10.17%2Fprin_multicanal.jpg&imgrefurl=http%3A%2F%2Fwww.prin.ru%2Fnews1%2Ftehpodderzhka_prin_stala_multikanalnoj%2F&tbnid=uCkXOGyOouVgeM&vet=10CHMQMyidAWoXChMIuO7tpOP45gIVAAAAAB0AAAAAEBE..i&docid=WJuT_3f3OZWEBM&w=853&h=400&itg=1&q=%D0%BF%D1%80%D0%B8%D0%BD&ved=0CHMQMyidAWoXChMIuO7tpOP45gIVAAAAAB0AAAAAEBE')
    #else:
       # bot.send_message(chat_id, message4)


@bot.message_handler(commands=['mid'])
def handler_text(message):
    bot.send_photo(chat_id, mebot)
    bot.send_message(message.chat.id, message2)


@bot.message_handler(content_types=['text'])
def handler_text(message):
    print(message)
    if message.text == "hi":
        bot.send_message (chat_id, "hi, user")
        test = bot.send_message(chat_id, 'write a/prin')
    elif message.text == "a":
        bot.send_message (chat_id, "do you want to know about meBot????")
        test = bot.send_message(chat_id, 'write yes/not')
    elif message.text == "yes":
        bot.send_message(chat_id, "cool, go start")
        test = bot.send_message(chat_id, 'click in /mid')
    elif message.text == "prin":
        bot.send_photo(chat_id,'https://www.google.com/imgres?imgurl=http%3A%2F%2Fwww.prin.ru%2Fimages%2Fnews%2Fprin%2F2019%2F10.17%2Fprin_multicanal.jpg&imgrefurl=http%3A%2F%2Fwww.prin.ru%2Fnews1%2Ftehpodderzhka_prin_stala_multikanalnoj%2F&tbnid=uCkXOGyOouVgeM&vet=10CHMQMyidAWoXChMIuO7tpOP45gIVAAAAAB0AAAAAEBE..i&docid=WJuT_3f3OZWEBM&w=853&h=400&itg=1&q=%D0%BF%D1%80%D0%B8%D0%BD&ved=0CHMQMyidAWoXChMIuO7tpOP45gIVAAAAAB0AAAAAEBE')
    else:
        bot.send_message(chat_id, message5)

bot.polling(none_stop=True, interval=0)
#message_id":414

#Enviar audiooooooooooooooooooooo0000000
bot.send_audio(chat_id=chat_id, audio=open('tests/test.mp3', 'rb'))
#bot.send_audio(User.id, *args, **kwargs)
#bot.send_audio(chat_id, 'https://www.youtube.com/watch?v=lNHe7dPchwI'

#Enviar mensagem no grupooooooooooooooooooooooooooooooooooooooo
#bot.send_photo(chat_id=chat_id, photo='https://telegram.org/img/t_logo.png')
#bot.send_photo(User.id, *args, **kwargs)

#
#from io import BytesIO
#bio = BytesIO()
#bio.name = 'image.jpeg'
#image.save(bio, 'JPEG')
#bio.seek(0)
#bot.send_photo(chat_id, photo=po)

#Enviar mensagem no grupooooooooooooooooooooooooooooooooooooooo
#def send_message(group_id, message4):
 # bot.send_message(group_id, message4)

##def add_group(update, context):
    #for member in update.message.new_chat_members:
     #   update.message.reply_text("goup_id add group".format(goup_id=member.username))

#add_group_handle = MessageHandler(Filters.status_update.new_chat_members, add_group)
#dispatcher.add_handler(add_group_handle)
#test = bot.send_message(group_id, message3)

#bot = telebot.TeleBot(newconstants.token)

  #Mensagem do usuario (saber quem escreve amensagem)
  #print(bot.get_me())
  #def log (message, answer, from_user=None):
     # from datatime import datatime
     # print(datatime.now())
     # print ("message of(0) (1). (id = (2) \n text - (3)".format(message.from_user.first_name,
                                                                   #   from_user.last_name,
                                                                     # str (message.from_user.id)
                                                                # message.text))


#if __name__ == '__main__':
   # main()

#bot.get_me()


#if __name__ == '__main__':
   # main()

#bot.get_me()
#bot.polling()