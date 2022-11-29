# -*- coding: utf-8 -*-
import telebot
import time

# NlpYoutube 
bot = telebot.TeleBot("token:token")

# Comandos
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        bot.reply_to(message, "Hola")
# echo
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    time.sleep(3)
    print(message.text)
    if message.text.find("A") >= 0:
        bot.reply_to(message, "12346")

bot.polling()