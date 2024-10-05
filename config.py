# TOKENS config
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# You should get token from the Telegram BotFather
TG_TOKEN = 'TG token from the BotFather'

# You should get a token from the https://api.openweathermap.org
OPEN_WEATHER_TOKEN = 'Token from api.openweathermap.org'

# You should get a token from the https://v6.exchangerate-api.com
EXCHANGERATE_TOKEN = 'Token from v6.exchangerate-api.com'
