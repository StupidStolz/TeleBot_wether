from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
import telebot

config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here
owm = OWM('2bc4da0ae9b4979d0faaa70a8980655b', config_dict)

bot = telebot.TeleBot("973670127:AAF6oHnSggW0HFhjPG-tJC3xNjOpW-hehTw")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    config_dict = owm.configuration 
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]
    answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
    answer += "Температура сейчас в районе: " + str(temp) + "\n\n"
    if temp < 8:
        answer += 'Сейчас очень холодно, одевайся тепло!'
    elif temp <20:
        answer += 'Сейчас холодно, оденься потеплее.'
    else:
        answer += 'Температура норм, одевайся свободно.'
    bot.send_message(message.chat.id, answer)
bot.polling( none_stop = True )