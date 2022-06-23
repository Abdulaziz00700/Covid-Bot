import requests
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN="5023269838:AAF61kkfgDnSuFE0CCt32TjajFUf-OihdiU"

bot=Bot(API_TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Qale gaplashamizmi!!!")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Pashol naxuy!!!")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

    
