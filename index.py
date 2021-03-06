import telebot
import keyboard_defs
import const
import defs
import clases
import texts
import sqlite3
from telebot import types

# Запросы
queries = {
    'table_users_create': "CREATE TABLE IF NOT EXISTS users (id INTEGER, chat_id INTEGER, username INTEGER, money INTEGER, referal VARCHAR(16), rating INTEGER)",
    'table_question_create': "CREATE TABLE IF NOT EXISTS questions (id INTEGER, category VARCHAR(16), question VARCHAR(128))",
        #'update_some_shit': "UPDATE shits SET ",
    'user_insert': "INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)",
    'user_delete': "DELETE FROM users WHERE chat_id = ?",
    'user_get': "SELECT * FROM users WHERE chat_id = ?",
    'users_get': "SELECT * FROM users"
}

DBNAME = 'main.db'


def get_db_connection(dbname):
    """
    :param dbname: <str> name of database (like test.db)
    :return: <sqlite3.connection>
    """
    return sqlite3.connect(dbname)

bot = telebot.TeleBot(const.token)

connection = get_db_connection('main.db')
connection.execute(queries['table_users_create'])
connection.execute(queries['table_question_create'])
connection.commit()
connection.close()


@bot.message_handler(commands=['start'])
def start(message):
    connection = get_db_connection(DBNAME)
    cursor = connection.cursor()
    cursor.execute(queries['user_get'], (message.chat.id,))
    if cursor.fetchone() is None:

        global max_id
        # Создание нумерации пользователей
        cursor.execute('SELECT max(id) FROM users')
        max_id = cursor.fetchone()
        print(max_id)
        try:
            if max_id[0] is None:
                max_id = 0
        except:
            pass

        # Запись пользователя в базу
        money = 0
        rating = 0
        max_id = 0
        referal = "0000000000"
        cursor.execute(queries['user_insert'], (max_id+1, message.chat.id, message.chat.username, money, referal, rating))
        connection.commit()

        print(message.chat.username, ' начал(-ла) игру')
        bot.send_message(message.chat.id, 'Привет, ' + message.chat.username + ', добро пожаловать в BrainStorm Bot.')

    else:
        bot.send_message(message.chat.id, 'Загружаю твой прогресс...')
# Здесь будет переход на кавиатуру
        cursor.close()
        connection.close()
        print(message.chat.username, 'Запустил(-ла ) бота')
    keyboard_defs.start_keyboard(message)

@bot.message_handler(content_types='text')
def start_handler(message):
    if message.text == 'Заработать':
        keyboard_defs.paymenu_keyboard(message)
    elif message.text == 'На интерес':
        keyboard_defs.freemenu_keyboard(message)
    elif message.text == 'Рэйтинг':
        keyboard_defs.rating_keyboard(message)
    elif message.text == 'Рэйтинг':
        keyboard_defs.about_keyboard(message)
    elif message.text == 'Назад':
        keyboard_defs.start_keyboard(message)





"""x = time.time()
if x == 120:
    c = 0
    x = 0
Принцип работы таймеров
"""

if __name__ == '__main__':
    bot.polling(none_stop=True)