import telebot
from telebot import types
 
TOKEN = "7721361070:AAHMO6LC2EjtmpqsifsSkcMU4fgtDNErtvc"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton(text='Перейти на сайт')
    markup.row(btn1)
    btn2 = types.KeyboardButton(text='Удалить фото')
    btn3 = types.KeyboardButton(text='/help')
    markup.row(btn2, btn3)
    file = open('D:\python\Telegram_bot\papich maniakich.jpg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)    
    #bot.send_message(message.chat.id, "Привет!", reply_markup=markup)
    bot.register_next_step_handler(message, on_click)
    
def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, "WebSite is open!")
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, "Фото удалено!")

@bot.message_handler(commands=['help'])
def help(message):
    kaka = types.ReplyKeyboardMarkup()
    bitin1 = types.KeyboardButton(text='Кто создал бота?')
    kaka.row(bitin1)
    bot.send_message(message.chat.id, "Это бот, который поможет вам во всем!", reply_markup=kaka)

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Перейти на сайт', url='https://www.google.com')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton(text='Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton(text='изменить текст', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, "Крутая фотка!", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_massege(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text("Edit text", callback.message.chat.id, callback.message.message_id) 
        
@bot.message_handler()
def kaka(message):
    if message.text.lower() == 'кто создал бота?':
        bot.send_message(message.chat.id, "Бота создал @Bountyhunterdo")
        
bot.polling(none_stop=True)