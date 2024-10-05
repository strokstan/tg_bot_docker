import datetime

import requests
from aiogram import types
from config import OPEN_WEATHER_TOKEN

# Processing  city request
async def start_weather(message: types.Message):
    await message.reply('Hi! What city do you watch the weather in?')


# Getting the weather in the city
async def get_weather(message: types.Message):
    # Making an emoji dictionary for the output
    code_to_icons = {
        'Clear': 'Clear \U00002600',
        'Rain': 'Rain \U00002614',
        'Clouds': 'Clouds \U00002601',
        'Drizzle': 'Drizzle \U00002614',
        'Snow': 'Snow \U00002744',
        'Mist': 'Mist \U0001F32B',
        'Thunderstorm': 'Thunderstorm \U0001F329',
    }
    # Get the weather data
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={OPEN_WEATHER_TOKEN}&units=metric'
        )
        data = r.json()

        city = data['name']
        description = data['weather'][0]['main']

        # Emoji output condition
        if description in code_to_icons:
            wd = code_to_icons[description]
        else:
            wd = "It's unclear, look out the window!"

        # Select the data we need
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        feels_like = data['main']['feels_like']
        sunrise_time = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_time = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(
            data['sys']['sunrise'])

        # Output formatted data
        await message.reply(f'*** {datetime.datetime.now().strftime("%d-%m-%Y %H:%M")} ***\n'
                            f'Weather in the city: {city}\n'
                            f'{wd}\n'
                            f'Temperature: {temp} °C\n'
                            f'Humidity: {humidity} %\n'
                            f'Wind: {wind} м/c\n'
                            f'Feels like: {feels_like} °C\n'
                            f'Sunrise time: {sunrise_time.strftime("%d-%m-%Y %H:%M")}\n'
                            f'Sunset time: {sunset_time.strftime("%d-%m-%Y %H:%M")}\n'
                            f'Length day: {length_day}\n'
                            )
    # Processing incorrect input
    except:
        await message.reply('Check the city name!')
