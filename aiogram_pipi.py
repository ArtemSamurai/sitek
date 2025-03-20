from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('7721361070:AAHMO6LC2EjtmpqsifsSkcMU4fgtDNErtvc')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def kaka(message: types.Message):
    kaka = types.ReplyKeyboardMarkup()
    file = open('D:\python\Telegram_bot\papich maniakich.jpg')
    kaka.add(types.KeyboardButton('Открыть веб-страницу', web_app=WebAppInfo(url='https://itproger.com/')))
    await message.answer('Привет и иди нахуй))', reply_markup=kaka)

executor.start_polling(dp)