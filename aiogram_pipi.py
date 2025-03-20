from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('7721361070:AAFSBMU41Alz2423lGH1RznrBnUvpzJGKls')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def kaka(message: types.Message):
    kaka = types.ReplyKeyboardMarkup()
    kaka.add(types.KeyboardButton('Открыть веб-страницу', web_app=WebAppInfo(url='https://artemsamurai.github.io/sitek/')))
    await message.answer('Привет и иди нахуй))', reply_markup=kaka)

executor.start_polling(dp)
