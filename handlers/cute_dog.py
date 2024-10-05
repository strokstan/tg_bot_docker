import requests
from aiogram import types
from create_bot import bot


# Getting a picture of the dogs from the API
async def get_dog_pic(message: types.Message):
    response = requests.get('https://api.thedogapi.com/v1/images/search')
    cat_url = response.json()[0]['url']
    await bot.send_photo(chat_id=message.chat.id, photo=cat_url)
