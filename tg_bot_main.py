from aiogram import executor, types

from create_bot import dp
from handlers import weather, currency, cute_cat, cute_dog

# Create a keyboard with buttons
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Weather')
btn2 = types.KeyboardButton('Exchange rates')
btn3 = types.KeyboardButton('Cute cat pictures')
btn4 = types.KeyboardButton('Cute dog pictures')
keyboard.add(btn1, btn2, btn3, btn4)


# Process the greeting via the /start handler
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
        await message.reply("Hi, I'm a bot that can help you find out currency rates, the weather, send "
                           " cute cat or dog pics. Choose what you want from the menu below:", reply_markup=keyboard)


# Create handlers for keyboard commands and weather processing
dp.register_message_handler(weather.start_weather, lambda message: message.text == 'Weather')
dp.register_message_handler(currency.process_exchange_command, lambda message: message.text == 'Exchange rates')
dp.register_message_handler(cute_cat.get_cat_pic, lambda message: message.text == 'Cute cat pictures')
dp.register_message_handler(cute_dog.get_dog_pic, lambda message: message.text == 'Cute dog pictures')
dp.register_message_handler(weather.get_weather)

# Start the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
