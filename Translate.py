import requests
import json
from aiogram import Bot, Dispatcher, types, executor

API_TOKEN="5337981171:AAFLyoyjShPlAeWxKRk791tCPFTX3RMME7c"

bot=Bot(API_TOKEN)
dp=Dispatcher(bot)



app_id = "c37d0857"
app_key = "ae5aa86fc54845a9e38bc5c14bde18cb"
language = "en-ru"
source= "en"
target= "ru"
@dp.message_handler()
async def echo(message: types.Message):
    word_id = message.text
    url1 = 'https://od-api.oxforddictionaries.com:443/api/v2/translations/' + source + '/' + target + '/' + word_id.lower()

    r = requests.get(url1, headers = {'app_id': app_id, 'app_key': app_key}).json()
    await message.answer(r['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['translations'][0]['text'])



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)