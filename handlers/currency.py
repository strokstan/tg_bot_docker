import requests
from aiogram import types
from config import EXCHANGERATE_TOKEN
from create_bot import dp

# Get the courses from the API
def get_exchange_rate(from_currency, to_currency):
    url = f'https://v6.exchangerate-api.com/v6/{EXCHANGERATE_TOKEN}/latest/{from_currency}'
    response = requests.get(url)
    data = response.json()
    exchange_rate = data['conversion_rates'][to_currency]
    return exchange_rate


@dp.message_handler(commands=['exchange'])
async def process_exchange_command(message: types.Message):
    try:
        # Get the currencies from the command
        currencies = message.get_args().upper().split()

        # Checking for two currencies
        if len(currencies) != 2:
            raise ValueError

        # Get currency values
        from_currency, to_currency = currencies

        # Get the exchange rate
        exchange_rate = get_exchange_rate(from_currency, to_currency)

        # Send the result to the user
        await message.reply(f"1 {from_currency} = {exchange_rate} {to_currency}")
    except:
        # Process possible errors and inform about the input
        await message.reply('To receive the course, enter: /exchange FROM_CURRENCY TO_CURRENCY '
                            '(For example /exchange USD EUR)')
