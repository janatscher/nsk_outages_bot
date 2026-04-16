import telebot
from telebot import types
from parser import *
from format import *
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    user_name = message.from_user.first_name
    main_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, )
    btn_query1 = telebot.types.KeyboardButton(text='🔴 Горячее водоснабжение')
    btn_query2 = telebot.types.KeyboardButton(text='🔵 Холодное водоснабжение')
    btn_query3 = telebot.types.KeyboardButton(text='♨️ Теплоснабжение')
    btn_query4 = telebot.types.KeyboardButton(text='💡 Электроснабжение')
    main_keyboard.row(btn_query1)
    main_keyboard.row(btn_query2)
    main_keyboard.row(btn_query3)
    main_keyboard.row(btn_query4)
    bot.send_message(chat_id, f'Здравствуйте, {user_name}. Для просмотра информации об отключениях нажмите на одну из кнопок ниже ⬇', reply_markup=main_keyboard, parse_mode='HTML')

all_data = {} #parsed[0]
dist_list = [] #parsed[1]
info_list = [1] #индекс для замены; parsed[2]

@bot.message_handler(func=lambda message: True)
def reply(message):
    if message.text == '🔴 Горячее водоснабжение':

        parsed = parse('hw')
        dist_list = parsed[1]
        chat_id = message.chat.id
        list_keyboard = telebot.types.InlineKeyboardMarkup()

        if dist_list[0] == '':
            title = 'Информация об отключениях горячего водоснабжения отсутствует ❌'
        else:
            title = '🏙Выберите район:'

        if len(dist_list) > 0:
            list_len = len(dist_list)
            for i in range(list_len):
                list_keyboard.add(telebot.types.InlineKeyboardButton(text=dist_list[i], callback_data=f'dist{i+1}_hw'))

        bot.send_message(chat_id, title, reply_markup=list_keyboard)
    if message.text == '🔵 Холодное водоснабжение':

        parsed = parse('cw')
        dist_list = parsed[1]
        chat_id = message.chat.id
        list_keyboard = telebot.types.InlineKeyboardMarkup()

        if dist_list[0] == '':
            title = 'Информация об отключениях холодного водоснабжения отсутствует ❌'
        else:
            title = '🏙Выберите район:'

        if len(dist_list) > 0:
            list_len = len(dist_list)
            for i in range(list_len):
                list_keyboard.add(telebot.types.InlineKeyboardButton(text=dist_list[i], callback_data=f'dist{i+1}_cw'))

        bot.send_message(chat_id, title, reply_markup=list_keyboard)
    if message.text == '♨️ Теплоснабжение':

        parsed = parse('ht')
        dist_list = parsed[1]
        chat_id = message.chat.id
        list_keyboard = telebot.types.InlineKeyboardMarkup()

        if dist_list[0] == '':
            title = 'Информация об отключениях теплоснабжения отсутствует ❌'
        else:
            title = '🏙Выберите район:'

        if len(dist_list) > 0:
            list_len = len(dist_list)
            for i in range(list_len):
                list_keyboard.add(telebot.types.InlineKeyboardButton(text=dist_list[i], callback_data=f'dist{i+1}_ht'))

        bot.send_message(chat_id, title, reply_markup=list_keyboard)
    if message.text == '💡 Электроснабжение':

        parsed = parse('el')
        dist_list = parsed[1]
        chat_id = message.chat.id
        list_keyboard = telebot.types.InlineKeyboardMarkup()

        if dist_list[0] == '':
            title = 'Информация об отключениях электроснабжения отсутствует ❌'
        else:
            title = '🏙Выберите район:'

        if len(dist_list) > 0:
            list_len = len(dist_list)
            for i in range(list_len):
                list_keyboard.add(telebot.types.InlineKeyboardButton(text=dist_list[i], callback_data=f'dist{i+1}_el'))

        bot.send_message(chat_id, title, reply_markup=list_keyboard)

#горячая вода
link_hw_keyboard = telebot.types.InlineKeyboardMarkup()
btn_link_hw = telebot.types.InlineKeyboardButton(text='↪️ Перейти на сайт', url=link_hw)
link_hw_keyboard.add(btn_link_hw)
#холодная вода
link_cw_keyboard = telebot.types.InlineKeyboardMarkup()
btn_link_cw = telebot.types.InlineKeyboardButton(text='↪️ Перейти на сайт', url=link_cw)
link_cw_keyboard.add(btn_link_cw)
#теплоснабжение
link_ht_keyboard = telebot.types.InlineKeyboardMarkup()
btn_link_ht = telebot.types.InlineKeyboardButton(text='↪️ Перейти на сайт', url=link_ht)
link_ht_keyboard.add(btn_link_ht)
#электроснабжение
link_el_keyboard = telebot.types.InlineKeyboardMarkup()
btn_link_el = telebot.types.InlineKeyboardButton(text='↪️ Перейти на сайт', url=link_el)
link_el_keyboard.add(btn_link_el)

def info_message(dist_num_utility):
    utility = dist_num_utility[-2:]
    num = int(dist_num_utility[4])
    parsed = parse(utility)
    dist_list = parsed[1]
    info_list[0] = parsed[2]
    message_formatted = format_message(num, dist_list, info_list)
    if utility == 'el': link_keyboard = link_el_keyboard
    elif utility == 'ht': link_keyboard = link_ht_keyboard
    elif utility == 'hw': link_keyboard = link_hw_keyboard
    else: link_keyboard = link_cw_keyboard
    return message_formatted, link_keyboard

@bot.callback_query_handler(func=lambda call: call.data)
def save_btn(call):
    dist_num_utility = call.data
    message = call.message
    chat_id = message.chat.id
    bot.send_message(chat_id, info_message(dist_num_utility)[0], parse_mode='HTML', reply_markup=info_message(dist_num_utility)[1])

bot.infinity_polling()