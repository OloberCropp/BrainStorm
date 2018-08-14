import keyboard_defs
import telebot

def pay_def(message):
    if message.text == 'Заработать!':
        keyboard_defs.paymenu_keyboard(message)

def free_def(message):
    if message.text == 'На интерес':
        keyboard_defs.freemenu_keyboard(message)

def rating_def(message):
    if message.text == 'Рэйтинг':
        keyboard_defs.rating_keyboard(message)

def about_def(message):
    if message.text == 'Рэйтинг':
        keyboard_defs.about_keyboard(message)