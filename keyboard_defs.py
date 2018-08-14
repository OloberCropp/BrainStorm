import telebot
from telebot import types
import const
import texts

bot = telebot.TeleBot(const.token)

#Главные клавиатуры

def start_keyboard(message):
    murkup = types.ReplyKeyboardMarkup(True, False)
    murkup.row('Заработать', 'На интерес')
    murkup.row('Кошелёк')
    murkup.row('Райтинг', 'About')
    bot.send_message(message.chat.id, '', reply_markup=murkup)

def paymenu_keyboard(message):
    murkup = types.ReplyKeyboardMarkup(True, False)
    murkup.row('игра', 'Кошелёк')
    murkup.row('Назад')
    bot.send_message(message.chat.id, '', reply_markup=murkup)

def freemenu_keyboard(message):
    murkup = types.ReplyKeyboardMarkup(True, False)
    murkup.row('Игра', 'Убрать рекламу')
    murkup.row('Назад')
    bot.send_message(message.chat.id, '', reply_markup=murkup)

def rating_keyboard(message):
    murkup = types.ReplyKeyboardMarkup(True, False)
    murkup.row('Моя позиция')
    murkup.row('Назад')
    bot.send_message(message.chat.id, '', reply_markup=murkup)

def about_keyboard(message):
    murkup = types.ReplyKeyboardMarkup(True, False)
    murkup.row('Приласить друга')
    murkup.row('Назад')
    bot.send_message(message.chat.id, '', reply_markup=murkup)

#Клавиатуры >2 ветви

def paygame_keyboard(message):
    murkup = types.ReplyKeyboardMarkup(True, False)
    murkup.row('Cтавка', 'Поиск')
    murkup.row('Назад')
    bot.send_message(message.chat.id, '', reply_markup=murkup)

def freegame_keyboard(message):
    murkup = types.ReplyKeyboardMarkup(True, False)
    murkup.row('Поиск игры')
    murkup.row('Назад')
    bot.send_message(message.chat.id, '', reply_markup=murkup)

def wallet_keyboard(message):
    murkup = types.ReplyKeyboardMarkup(True, False)
    murkup.row('Ввести', 'Вывести')
    murkup.row('Бесплатная валюта')
    murkup.row('Назад')
    bot.send_message(message.chat.id, '', reply_markup=murkup)



##################
#######
###
#
# Для тех, кто убрал рекламу
def freemenu2_keyboard(message):
    murkup = types.ReplyKeyboardMarkup(True, False)
    murkup.row('Игра')
    murkup.row('Назад')
    bot.send_message(message.chat.id, '', reply_markup=murkup)
#
###
#######
##################
