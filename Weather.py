import requests
from config import omg
import obuna
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove
from button import check_button
API_TOKEN="5065496513:AAGfJFGnLjJthV__vuWwRR6_YPKvSJ4V4Rs"

bot=Bot(API_TOKEN)
dp=Dispatcher(bot)

tash=KeyboardButton("Tashkent")
sam=KeyboardButton("Samarkand")
bukh=KeyboardButton("Bukhara")
nam=KeyboardButton("Namangan")
djiz=KeyboardButton("Jizzakh")
sirdar=KeyboardButton("Syrdarya")
xorezm=KeyboardButton("Khorezm")
navoi=KeyboardButton("Navoi")
natija=ReplyKeyboardMarkup().add(tash,sam,bukh,nam,djiz,sirdar,xorezm,navoi)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    channele_format = str()
    full_name = message.from_user.full_name
    for channel in omg:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        channels_format += f"👉🏻 <a href='{invite_link}'> {chat.title}</a>\n"
    await message.answer("Assalomu aleykum!{}. Botdan foydalanish uchun , quyidagi kanallarga obuna bo'ling: \n"
                        f"{channels_format}", reply_markup=check_button, disable_web_page_preview=True,pase_mode='HTML')




@dp.message_handler()
async def start(message: types.Message):
    if message.text == "Tashkent":
        url=f"https://goweather.herokuapp.com/weather/{message.text}"
        response=requests.get(url)
        gradus=response.json()['temperature']
        shamol=response.json()['wind']
        await message.answer(f"{message.text}da {gradus}🌡 .Shamol {shamol}💨 esyapti!")
    elif message.text == "Samarkand":
        url=f"https://goweather.herokuapp.com/weather/{message.text}"
        response=requests.get(url)
        gradus=response.json()['temperature']
        shamol=response.json()['wind']
        await message.answer(f"{message.text}da {gradus}🌡 .Shamol {shamol}💨 esyapti!")
    elif message.text == "Bukhara":
        url=f"https://goweather.herokuapp.com/weather/{message.text}"
        response=requests.get(url)
        gradus=response.json()['temperature']
        shamol=response.json()['wind']
        await message.answer(f"{message.text}da {gradus}🌡 .Shamol {shamol}💨 esyapti!")
    elif message.text == "Namangan":
        url=f"https://goweather.herokuapp.com/weather/{message.text}"
        response=requests.get(url)
        gradus=response.json()['temperature']
        shamol=response.json()['wind']
        await message.answer(f"{message.text}da {gradus}🌡 .Shamol {shamol}💨 esyapti!")
    elif message.text == "Jizzakh":
        url=f"https://goweather.herokuapp.com/weather/{message.text}"
        response=requests.get(url)
        gradus=response.json()['temperature']
        shamol=response.json()['wind']
        await message.answer(f"{message.text}da {gradus}🌡 .Shamol {shamol}💨 esyapti!")
        
    
    elif message.text == "Syrdarya":
        url=f"https://goweather.herokuapp.com/weather/{message.text}"
        response=requests.get(url)
        gradus=response.json()['temperature']
        shamol=response.json()['wind']
        await message.answer(f"{message.text}da {gradus}🌡 .Shamol {shamol}💨 esyapti!")
    
    elif message.text == "Khorezm":   
        url=f"https://goweather.herokuapp.com/weather/{message.text}"
        response=requests.get(url)
        gradus=response.json()['temperature']
        shamol=response.json()['wind']
        await message.answer(f"{message.text}da {gradus}🌡 .Shamol {shamol}💨 esyapti!")
    elif message.text == "Navoi":
        url=f"https://goweather.herokuapp.com/weather/{message.text}"
        response=requests.get(url)
        gradus=response.json()['temperature']
        shamol=response.json()['wind']
        await message.answer(f"{message.text}da {gradus}🌡 .Shamol {shamol}💨 esyapti!")
       


    




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
