from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

API_TOKEN="5149342417:AAFVp3Tb4umE1mYtQ0Pmfa2AUVSkVgxN9Ig"

bot=Bot(API_TOKEN)
dp=Dispatcher(bot)

as1=KeyboardButton("🛍 Buyurtma berish")
as2=KeyboardButton("🎉 Aksiya")
as3=KeyboardButton("ℹ️ Biz haqimizda")
as4=KeyboardButton("📞 Biz bilan bog'laning")
as5=KeyboardButton("⚙️ Sozlamalar")
as6=KeyboardButton("🏠 Mening manzillarim")
natija3=ReplyKeyboardMarkup(resize_keyboard=True).add(as1,as2,as3,as4,as5,as6)

men1=KeyboardButton("🥪🍟🥤Макси бокс")
men2=KeyboardButton("🥪 Клаб-сендвич")
men3=KeyboardButton("🌯Лаваш")
men4=KeyboardButton("🌮Шаурма")
men5=KeyboardButton("🍱Донар кебаб")
men6=KeyboardButton("🥖Шаурма Баггет (хагги)")
but1=KeyboardButton("➡️Keyingisi")
bosh=KeyboardButton("🏠Bosh Menyu")
natija1=ReplyKeyboardMarkup(resize_keyboard=True).add(men1,men2,men3,men4,men5,men6,but1,bosh)

men7=KeyboardButton("🍔Бургер")
men8=KeyboardButton("🌭Хот-дог")
men9=KeyboardButton("🍟Снеки")
men10=KeyboardButton("🍚Гарниры")
men11=KeyboardButton("🥫Соусы")
men12=KeyboardButton("🥤Напитки")
men13=KeyboardButton("🍰Десерты")
but2=KeyboardButton("⬅️Orqaga")
natija2=ReplyKeyboardMarkup(resize_keyboard=True).add(men7,men8,men9,men10,men11,men12,men13,but2,bosh)

box1=KeyboardButton("Макси Бокс Популярный")
box2=KeyboardButton("Макси бокс Ретро")
box3=KeyboardButton("макси Бокс Тренд")
box4=KeyboardButton("Макси Бокс Традиция")
boxreply=ReplyKeyboardMarkup(resize_keyboard=True).add(box1,box2,box3,box4)

sen1=KeyboardButton("Клаб Сэндвич куриный")
sen2=KeyboardButton("Сэндвич Classic")
sen3=KeyboardButton("Сэндвич Classic острый")
senreply=ReplyKeyboardMarkup(resize_keyboard=True).add(sen1,sen2,sen3)

law1=KeyboardButton("Лаваш Куриный Standart Classic")
law2=KeyboardButton("Лаваш Standart classic")
law3=KeyboardButton("Лаваш мясной Standart острый")
law4=KeyboardButton("Лаваш Куриный Standart Cheese")
law5=KeyboardButton("Лаваш Standart Cheese")
law6=KeyboardButton("Лаваш куриный Standart острый")
law7=KeyboardButton("Лаваш Куриный Mini")
law8=KeyboardButton("Лаваш Mini")
law9=KeyboardButton("Лаваш Куриный Mini Cheese")
law10=KeyboardButton("Лаваш Mini Cheese")
lawreply=ReplyKeyboardMarkup(resize_keyboard=True).add(law1,law2,law3,law4,law5,law6,law7,law8,law9,law10)

sh1=KeyboardButton("Шаурма Big")
sh2=KeyboardButton("Шаурма Standart")
sh3=KeyboardButton("Шаурма Куриная Big")
sh4=KeyboardButton("Шаурма Куриная Standart")
shreply=ReplyKeyboardMarkup(resize_keyboard=True).add(sh1,sh2,sh3,sh4)

keb1=KeyboardButton("Донар Кебаб мясной")
keb2=KeyboardButton("Донар Кебаб куриный")
keb3=KeyboardButton("Турецский хлеб")
kebreply=ReplyKeyboardMarkup(resize_keyboard=True).add(keb1,keb2,keb3)

bag1=KeyboardButton("Шаурма Баггет мясной")
bag2=KeyboardButton("Шаурма Баггет куриный")
bagreply=ReplyKeyboardMarkup(resize_keyboard=True).add(bag1,bag2)

bur1=KeyboardButton("Гамбургер")
bur2=KeyboardButton("Чизбургер")
bur3=KeyboardButton("Дабл Бургер")
bur4=KeyboardButton("Дабл Чиз")
burreply=ReplyKeyboardMarkup(resize_keyboard=True).add(bur1,bur2,bur3,bur4)

xot1=KeyboardButton("Хот Дог")
xot2=KeyboardButton("Кинг Дог")
xotreply=ReplyKeyboardMarkup(resize_keyboard=True).add(xot1,xot2)

snk1=KeyboardButton("Наггетсы L (20 шт)")
snk2=KeyboardButton("Байтсы большой 270 гр")
snk3=KeyboardButton("Наггетс бокс")
snk4=KeyboardButton("Картофель Фри Большой 150 гр")
snk5=KeyboardButton("Нагетсы M (10шт)")
snk6=KeyboardButton("Байтсы средний 130гр")
snk7=KeyboardButton("Микс Бокс")
snk8=KeyboardButton("Нагетсы S (6шт)")
snk9=KeyboardButton("Байтсы малый 90гр")
snk10=KeyboardButton("Картофель Фри Средний 100 гр")
snk11=KeyboardButton("Картофель Фри малый 60 гр")
snk12=KeyboardButton("Картофель по-деревенски 110 гр")
snkreply=ReplyKeyboardMarkup(resize_keyboard=True).add(snk1,snk2,snk3,snk4,snk5,snk6,snk7,snk8,snk9,snk10,snk11,snk12)



@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Asosiy menyu!",reply_markup=natija3)

@dp.message_handler()
async def agar(message: types.Message):
    if message.text == "🛍 Buyurtma berish":
        await message.answer("Tanlang!",reply_markup=natija1)

    elif message.text == "➡️Keyingisi":
        await message.answer("Tanlang!",reply_markup=natija2) 

    elif message.text == "⬅️Orqaga":
        await message.answer("Tanlang!",reply_markup=natija1) 

    elif message.text == "🎉 Aksiya":
        await message.answer("Xozirda xech qanday aksiya yo'q!!! ")  

    elif message.text == "ℹ️ Biz haqimizda":
        await message.answer("🍟 Max Way\n"
        "☎️ Aloqa markazi: +998712005400")  

    elif message.text == "🏠Bosh Menyu":
        await message.answer("Bosh Menyu!",reply_markup=natija3) 

    elif message.text == "📞 Biz bilan bog'laning":
        await message.answer("Biz bilan @MaxWaySupport_bot orqali bog'laning yoki\n"
        "+998712005400 raqamiga qo'ng'iroq qiling.")  






































if __name__ == '__main__':
        executor.start_polling(dp, skip_updates=True)