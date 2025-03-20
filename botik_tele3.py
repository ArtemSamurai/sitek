import telebot
import requests
import json

TOKEN = "7721361070:AAHMO6LC2EjtmpqsifsSkcMU4fgtDNErtvc"
bot = telebot.TeleBot(TOKEN)
API = 'a0936aa71a2230c2f2e9a564fc4ea5da'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, рад тебя видеть! Введи название города")
    

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
    if weather.status_code == 200:
        data = json.loads(weather.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода: {temp}')

        image = 'sun-flare.jpg' if temp > 5 else 'storm-clouds.jpg'
        file = open('D:\\python\\Telegram_bot\\' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f'Город указан не верно')
bot.polling(none_stop=True)