# -*- coding: utf-8 -*-
# se añade @BotFather en telegran
# se le manda el comando: /start
# se le manda el comando: /newbot

import telebot
import time
#from ia import prediceToxico
import nltk
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pickle
from ia import *


# NlpYouTubeBot 
bot = telebot.TeleBot("token")

# Comandos.
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        bot.reply_to(message, "Ayuda")
        print(message, "Iefre: ¿En que puedo ayudar?" )

# Echo
@bot.message_handler(func=lambda message: True)
def echo_all(message):
   estatus = prediceToxico(message.text)
   bot.reply_to(message, message.text  )
   time.sleep(3)
   if estatus == 1:
      print(f're: {estatus}',message.text)
      bot.reply_to(message, message.text)
   else:
      print(f're: {estatus}',message.text)
      bot.reply_to(message, message.text)
   
bot.polling()