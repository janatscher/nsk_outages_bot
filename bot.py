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
    bot.send_message(chat_id, f'Здравствуйте, {user_name}', reply_markup=main_keyboard, parse_mode='HTML')

all_data = {} #parsed[0]
dist_list = [] #parsed[1]
info_list = [1] #для замены в 59 строке и тд; parsed[2]

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
            btn_dist1 = telebot.types.InlineKeyboardButton(text=dist_list[0], callback_data='dist1_hw')
            list_keyboard.add(btn_dist1)
        if len(dist_list) > 1:
            btn_dist2 = telebot.types.InlineKeyboardButton(text=dist_list[1], callback_data='dist2_hw')
            list_keyboard.add(btn_dist2)
        if len(dist_list) > 2:
            btn_dist3 = telebot.types.InlineKeyboardButton(text=dist_list[2], callback_data='dist3_hw')
            list_keyboard.add(btn_dist3)
        if len(dist_list) > 3:
            btn_dist3 = telebot.types.InlineKeyboardButton(text=dist_list[3], callback_data='dist4_hw')
            list_keyboard.add(btn_dist3)
        if len(dist_list) > 4:
            btn_dist3 = telebot.types.InlineKeyboardButton(text=dist_list[4], callback_data='dist5_hw')
            list_keyboard.add(btn_dist3)
        if len(dist_list) > 5:
            btn_dist3 = telebot.types.InlineKeyboardButton(text=dist_list[5], callback_data='dist6_hw')
            list_keyboard.add(btn_dist3)
        if len(dist_list) > 6:
            btn_dist3 = telebot.types.InlineKeyboardButton(text=dist_list[6], callback_data='dist7_hw')
            list_keyboard.add(btn_dist3)
        if len(dist_list) > 7:
            btn_dist3 = telebot.types.InlineKeyboardButton(text=dist_list[7], callback_data='dist8_hw')
            list_keyboard.add(btn_dist3)
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
            btn_dist1 = telebot.types.InlineKeyboardButton(text=dist_list[0], callback_data='dist1_cw')
            list_keyboard.add(btn_dist1)
        if len(dist_list) > 1:
            btn_dist2 = telebot.types.InlineKeyboardButton(text=dist_list[1], callback_data='dist2_cw')
            list_keyboard.add(btn_dist2)
        if len(dist_list) > 2:
            btn_dist3 = telebot.types.InlineKeyboardButton(text=dist_list[2], callback_data='dist3_cw')
            list_keyboard.add(btn_dist3)
        if len(dist_list) > 3:
            btn_dist3 = telebot.types.InlineKeyboardButton(text=dist_list[3], callback_data='dist4_cw')
            list_keyboard.add(btn_dist3)
        if len(dist_list) > 4:
            btn_dist3 = telebot.types.InlineKeyboardButton(text=dist_list[4], callback_data='dist5_cw')
            list_keyboard.add(btn_dist3)
        if len(dist_list) > 5:
            btn_dist3 = telebot.types.InlineKeyboardButton(text=dist_list[5], callback_data='dist6_cw')
            list_keyboard.add(btn_dist3)
        if len(dist_list) > 6:
            btn_dist3 = telebot.types.InlineKeyboardButton(text=dist_list[6], callback_data='dist7_cw')
            list_keyboard.add(btn_dist3)
        if len(dist_list) > 7:
            btn_dist3 = telebot.types.InlineKeyboardButton(text=dist_list[7], callback_data='dist8_cw')
            list_keyboard.add(btn_dist3)

        bot.send_message(chat_id, title, reply_markup=list_keyboard)
    if message.text == '♨️ Теплоснабжение':

        parsed = parse('heat')
        dist_list = parsed[1]

        chat_id = message.chat.id
        list_keyboard = telebot.types.InlineKeyboardMarkup()

        if dist_list[0] == '':
            title = 'Информация об отключениях теплоснабжения отсутствует ❌'
        else:
            title = '🏙Выберите район:'
        if len(dist_list) > 0:
            btn_dist1 = telebot.types.InlineKeyboardButton(text=dist_list[0], callback_data='dist1_heat')
            list_keyboard.add(btn_dist1)
        if len(dist_list) > 1:
            btn_dist2 = telebot.types.InlineKeyboardButton(text=dist_list[1], callback_data='dist2_heat')
            list_keyboard.add(btn_dist2)
        if len(dist_list) > 2:
            btn_dist3 = telebot.types.InlineKeyboardButton(text=dist_list[2], callback_data='dist3_heat')
            list_keyboard.add(btn_dist3)
        if len(dist_list) > 3:
            btn_dist3 = telebot.types.InlineKeyboardButton(text=dist_list[3], callback_data='dist4_heat')
            list_keyboard.add(btn_dist3)
        if len(dist_list) > 4:
            btn_dist3 = telebot.types.InlineKeyboardButton(text=dist_list[4], callback_data='dist5_heat')
            list_keyboard.add(btn_dist3)
        if len(dist_list) > 5:
            btn_dist3 = telebot.types.InlineKeyboardButton(text=dist_list[5], callback_data='dist6_heat')
            list_keyboard.add(btn_dist3)
        if len(dist_list) > 6:
            btn_dist3 = telebot.types.InlineKeyboardButton(text=dist_list[6], callback_data='dist7_heat')
            list_keyboard.add(btn_dist3)
        if len(dist_list) > 7:
            btn_dist3 = telebot.types.InlineKeyboardButton(text=dist_list[7], callback_data='dist8_heat')
            list_keyboard.add(btn_dist3)

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
            btn_dist1 = telebot.types.InlineKeyboardButton(text=dist_list[0], callback_data='dist1_el')
            list_keyboard.add(btn_dist1)
        if len(dist_list) > 1:
            btn_dist2 = telebot.types.InlineKeyboardButton(text=dist_list[1], callback_data='dist2_el')
            list_keyboard.add(btn_dist2)
        if len(dist_list) > 2:
            btn_dist3 = telebot.types.InlineKeyboardButton(text=dist_list[2], callback_data='dist3_el')
            list_keyboard.add(btn_dist3)
        if len(dist_list) > 3:
            btn_dist3 = telebot.types.InlineKeyboardButton(text=dist_list[3], callback_data='dist4_el')
            list_keyboard.add(btn_dist3)
        if len(dist_list) > 4:
            btn_dist3 = telebot.types.InlineKeyboardButton(text=dist_list[4], callback_data='dist5_el')
            list_keyboard.add(btn_dist3)
        if len(dist_list) > 5:
            btn_dist3 = telebot.types.InlineKeyboardButton(text=dist_list[5], callback_data='dist6_el')
            list_keyboard.add(btn_dist3)
        if len(dist_list) > 6:
            btn_dist3 = telebot.types.InlineKeyboardButton(text=dist_list[6], callback_data='dist7_el')
            list_keyboard.add(btn_dist3)
        if len(dist_list) > 7:
            btn_dist3 = telebot.types.InlineKeyboardButton(text=dist_list[7], callback_data='dist8_el')
            list_keyboard.add(btn_dist3)

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
link_heat_keyboard = telebot.types.InlineKeyboardMarkup()
btn_link_heat = telebot.types.InlineKeyboardButton(text='↪️ Перейти на сайт', url=link_heat)
link_heat_keyboard.add(btn_link_heat)

@bot.callback_query_handler(func=lambda call: call.data in ['dist1_hw', 'dist1_cw', 'dist1_heat', 'dist1_el'])
def save_btn(call):
    if call.data == 'dist1_hw':
        parsed = parse('hw')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(1, dist_list, info_list)
        link_keyboard = link_hw_keyboard
    if call.data == 'dist1_cw':
        parsed = parse('cw')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(1, dist_list, info_list)
        link_keyboard = link_cw_keyboard
    if call.data == 'dist1_heat':
        parsed = parse('heat')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(1, dist_list, info_list)
        link_keyboard = link_heat_keyboard
    if call.data == 'dist1_el':
        parsed = parse('el')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(1, dist_list, info_list)
        link_keyboard = link_heat_keyboard

    message = call.message
    chat_id = message.chat.id
    bot.send_message(chat_id, message_formatted, parse_mode='HTML', reply_markup=link_keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ['dist2_hw', 'dist2_cw', 'dist2_heat', 'dist2_el'])
def save_btn(call):
    if call.data == 'dist2_hw':
        parsed = parse('hw')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(2, dist_list, info_list)
        link_keyboard = link_hw_keyboard
    if call.data == 'dist2_cw':
        parsed = parse('cw')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(2, dist_list, info_list)
        link_keyboard = link_cw_keyboard
    if call.data == 'dist2_heat':
        parsed = parse('heat')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(2, dist_list, info_list)
        link_keyboard = link_heat_keyboard
    if call.data == 'dist2_el':
        parsed = parse('el')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(2, dist_list, info_list)
        link_keyboard = link_heat_keyboard

    message = call.message
    chat_id = message.chat.id
    bot.send_message(chat_id, message_formatted, parse_mode='HTML', reply_markup=link_keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ['dist3_hw', 'dist3_cw', 'dist3_heat', 'dist3_el'])
def save_btn(call):
    if call.data == 'dist3_hw':
        parsed = parse('hw')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(3, dist_list, info_list)
        link_keyboard = link_hw_keyboard
    if call.data == 'dist3_cw':
        parsed = parse('cw')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(3, dist_list, info_list)
        link_keyboard = link_cw_keyboard
    if call.data == 'dist3_heat':
        parsed = parse('heat')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(3, dist_list, info_list)
        link_keyboard = link_heat_keyboard
    if call.data == 'dist3_el':
        parsed = parse('el')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(3, dist_list, info_list)
        link_keyboard = link_heat_keyboard

    message = call.message
    chat_id = message.chat.id
    bot.send_message(chat_id, message_formatted, parse_mode='HTML', reply_markup=link_keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ['dist4_hw', 'dist4_cw', 'dist4_heat', 'dist4_el'])
def save_btn(call):
    if call.data == 'dist4_hw':
        parsed = parse('hw')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(4, dist_list, info_list)
        link_keyboard = link_hw_keyboard
    if call.data == 'dist4_cw':
        parsed = parse('cw')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(4, dist_list, info_list)
        link_keyboard = link_cw_keyboard
    if call.data == 'dist4_heat':
        parsed = parse('heat')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(4, dist_list, info_list)
        link_keyboard = link_heat_keyboard
    if call.data == 'dist4_el':
        parsed = parse('el')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(4, dist_list, info_list)
        link_keyboard = link_heat_keyboard

    message = call.message
    chat_id = message.chat.id
    bot.send_message(chat_id, message_formatted, parse_mode='HTML', reply_markup=link_keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ['dist5_hw', 'dist5_cw', 'dist5_heat', 'dist5_el'])
def save_btn(call):
    if call.data == 'dist5_hw':
        parsed = parse('hw')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(5, dist_list, info_list)
        link_keyboard = link_hw_keyboard
    if call.data == 'dist5_cw':
        parsed = parse('cw')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(5, dist_list, info_list)
        link_keyboard = link_cw_keyboard
    if call.data == 'dist5_heat':
        parsed = parse('heat')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(5, dist_list, info_list)
        link_keyboard = link_heat_keyboard
    if call.data == 'dist5_el':
        parsed = parse('el')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(5, dist_list, info_list)
        link_keyboard = link_heat_keyboard

    message = call.message
    chat_id = message.chat.id
    bot.send_message(chat_id, message_formatted, parse_mode='HTML', reply_markup=link_keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ['dist6_hw', 'dist6_cw', 'dist6_heat', 'dist6_el'])
def save_btn(call):
    if call.data == 'dist6_hw':
        parsed = parse('hw')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(6, dist_list, info_list)
        link_keyboard = link_hw_keyboard
    if call.data == 'dist6_cw':
        parsed = parse('cw')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(6, dist_list, info_list)
        link_keyboard = link_cw_keyboard
    if call.data == 'dist6_heat':
        parsed = parse('heat')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(6, dist_list, info_list)
        link_keyboard = link_heat_keyboard
    if call.data == 'dist6_el':
        parsed = parse('el')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(6, dist_list, info_list)
        link_keyboard = link_heat_keyboard

    message = call.message
    chat_id = message.chat.id
    bot.send_message(chat_id, message_formatted, parse_mode='HTML', reply_markup=link_keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ['dist7_hw', 'dist7_cw', 'dist7_heat', 'dist7_el'])
def save_btn(call):
    if call.data == 'dist7_hw':
        parsed = parse('hw')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(7, dist_list, info_list)
        link_keyboard = link_hw_keyboard
    if call.data == 'dist7_cw':
        parsed = parse('cw')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(7, dist_list, info_list)
        link_keyboard = link_cw_keyboard
    if call.data == 'dist7_heat':
        parsed = parse('heat')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(7, dist_list, info_list)
        link_keyboard = link_heat_keyboard
    if call.data == 'dist7_el':
        parsed = parse('el')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(7, dist_list, info_list)
        link_keyboard = link_heat_keyboard

    message = call.message
    chat_id = message.chat.id
    bot.send_message(chat_id, message_formatted, parse_mode='HTML', reply_markup=link_keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ['dist8_hw', 'dist8_cw', 'dist8_heat', 'dist8_el'])
def save_btn(call):
    if call.data == 'dist8_hw':
        parsed = parse('hw')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(8, dist_list, info_list)
        link_keyboard = link_hw_keyboard
    if call.data == 'dist8_cw':
        parsed = parse('cw')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(8, dist_list, info_list)
        link_keyboard = link_cw_keyboard
    if call.data == 'dist8_heat':
        parsed = parse('heat')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(8, dist_list, info_list)
        link_keyboard = link_heat_keyboard
    if call.data == 'dist8_el':
        parsed = parse('el')
        dist_list = parsed[1]
        info_list[0] = parsed[2]
        message_formatted = format_message(8, dist_list, info_list)
        link_keyboard = link_heat_keyboard

    message = call.message
    chat_id = message.chat.id
    bot.send_message(chat_id, message_formatted, parse_mode='HTML', reply_markup=link_keyboard)

bot.infinity_polling()