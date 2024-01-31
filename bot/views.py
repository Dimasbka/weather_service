from django.shortcuts import HttpResponse
import telebot
from telebot.util import quick_markup
import logging

from django.conf import settings

import json
from django.views.decorators.csrf import csrf_exempt

from geo.models import City

from geo.yandex_weather import get_yandex_weather


BOT_TOKEN    = getattr( settings, 'BOT_TOKEN', False )
BOT_URL      = getattr( settings, 'BOT_URL', False )

BOT_WEBHOOK  = getattr( settings, 'BOT_WEBHOOK', False )

GET_CITY_NAME_TEXT ='Веедите название города'

BOT_MENY = telebot.types.InlineKeyboardMarkup(row_width=1)
BOT_MENY.add(telebot.types.InlineKeyboardButton(
    text='Узнать погоду', 
    callback_data='get_city_name'
))



bot = telebot.TeleBot(BOT_TOKEN)
if BOT_WEBHOOK:
    bot.set_webhook( BOT_WEBHOOK )


@csrf_exempt
def index(request):
    if request.method == "POST":
        update = telebot.types.Update.de_json(request.body.decode('utf-8'))
        bot.process_new_updates([update])
    return HttpResponse(f'<h1>Бот серверe погоды <a href="{BOT_URL}">https://{BOT_URL}</a>!</h1>')


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    print(f'/start')
    name = f'{message.from_user.first_name}'
    text = f'Привет {name}!\n'\
           f'Я бот, который будет показывать погоду :)\n\n'

    bot.send_message(
        message.chat.id, 
        text, 
        reply_markup=BOT_MENY)


# https://github.com/eternnoir/pyTelegramBotAPI?tab=readme-ov-file#callback-query-handler
@bot.callback_query_handler(func=lambda call: True)
def get_city_name(callback: telebot.types.CallbackQuery ):
    if callback.data == 'get_city_name':
        markup = telebot.types.ForceReply( )
        bot.send_message(
            callback.message.chat.id, 
            GET_CITY_NAME_TEXT, 
            reply_markup=markup 
        )

@bot.message_handler(func=lambda message: True)
def weather(message: telebot.types.Message):

    if message.reply_to_message \
            and message.reply_to_message.text == GET_CITY_NAME_TEXT:
        city_name = message.text.capitalize()
        city = City.objects.filter( name__iexact=city_name ).first()

        if city == None:
            bot.send_message(
                message.chat.id, 
                f"Город '{city_name}' не найден",
                reply_markup=BOT_MENY
            )
            return

        data = get_yandex_weather(
                city.name, 
                (city.latitude, city.longitude) 
            )

        text =  f"Погода в городе {city.name}:\n\n" \
                f"температура {data['temp']}℃\n" \
                f"атмосферное давление {data['pressure_mm']}мм рт.ст.\n" \
                f"скорость ветра {data['wind_speed']}м/с\n"

        bot.send_message(
            message.chat.id,
            text,
            reply_markup=BOT_MENY
        )

