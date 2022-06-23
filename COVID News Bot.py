import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import  InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove
API_TOKEN="5268927824:AAHGhxq7LtsnnvwY9nLBeNsbAefBk1WtXoA"

bot=Bot(API_TOKEN)
dp=Dispatcher(bot)

uzb=KeyboardButton("Uzbekistan")
rus=KeyboardButton("Russia")
kaz=KeyboardButton("Kazakhstan")
avganistan=KeyboardButton("Afghanistan")
uk=KeyboardButton("Ukraine")
belarus=KeyboardButton("Belarus")
china=KeyboardButton("China")
natija=ReplyKeyboardMarkup().add(uzb,rus,kaz,avganistan,uk,belarus,china)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Assalomu aleykum😄!!! Siz qayer xaqida ma'lumot olmoqchisiz?🤨", reply_markup=natija)



@dp.message_handler()
async def start(message: types.Message):
    if message.text == "Uzbekistan":
        url=f"https://covid-api.mmediagroup.fr/v1/cases?country={message.text}"
        response=requests.get(url)
        kasal=response.json()["All"]["confirmed"]
        tuzal=response.json()["All"]["recovered"]
        olim=response.json()["All"]["deaths"]
        await message.answer(f"{message.text}da {kasal} ta odam kasallandi😮‍💨 {tuzal} ta odam tuzaldi😄 {olim} ta odam oldi😥😱")
        
    elif message.text == "Russia":
        url=f"https://covid-api.mmediagroup.fr/v1/cases?country={message.text}"
        response=requests.get(url)
        kasal=response.json()["All"]["confirmed"]
        tuzal=response.json()["All"]["recovered"]
        olim=response.json()["All"]["deaths"]
        await message.answer(f"{message.text}da {kasal} ta odam kasallandi😮‍💨 {tuzal} ta odam tuzaldi😄 {olim} ta odam oldi😥😱")
        
    elif message.text == "Kazakhstan":
        url=f"https://covid-api.mmediagroup.fr/v1/cases?country={message.text}"
        response=requests.get(url)
        kasal=response.json()["All"]["confirmed"]
        tuzal=response.json()["All"]["recovered"]
        olim=response.json()["All"]["deaths"]
        await message.answer(f"{message.text}da {kasal} ta odam kasallandi😮‍💨 {tuzal} ta odam tuzaldi😄 {olim} ta odam oldi😥😱")
        
    elif message.text == "Afghanistan":
        url=f"https://covid-api.mmediagroup.fr/v1/cases?country={message.text}"
        response=requests.get(url)
        kasal=response.json()["All"]["confirmed"]
        tuzal=response.json()["All"]["recovered"]
        olim=response.json()["All"]["deaths"]
        await message.answer(f"{message.text}da {kasal} ta odam kasallandi😮‍💨 {tuzal} ta odam tuzaldi😄 {olim} ta odam oldi😥😱")
        
    elif message.text == "Ukraine":
        url=f"https://covid-api.mmediagroup.fr/v1/cases?country={message.text}"
        response=requests.get(url)
        kasal=response.json()["All"]["confirmed"]
        tuzal=response.json()["All"]["recovered"]
        olim=response.json()["All"]["deaths"]
        await message.answer(f"{message.text}da {kasal} ta odam kasallandi😮‍💨 {tuzal} ta odam tuzaldi😄 {olim} ta odam oldi😥😱")
        
    elif message.text == "Belarus":
        url=f"https://covid-api.mmediagroup.fr/v1/cases?country={message.text}"
        response=requests.get(url)
        kasal=response.json()["All"]["confirmed"]
        tuzal=response.json()["All"]["recovered"]
        olim=response.json()["All"]["deaths"]
        await message.answer(f"{message.text}da {kasal} ta odam kasallandi😮‍💨 {tuzal} ta odam tuzaldi😄 {olim} ta odam oldi😥😱")
    elif message.text == "China":
        url=f"https://covid-api.mmediagroup.fr/v1/cases?country={message.text}"
        response=requests.get(url)
        kasal=response.json()["All"]["confirmed"]
        tuzal=response.json()["All"]["recovered"]
        olim=response.json()["All"]["deaths"]
        await message.answer(f"{message.text}da {kasal} ta odam kasallandi😮‍💨 {tuzal} ta odam tuzaldi😄 {olim} ta odam oldi😥😱")    












if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
