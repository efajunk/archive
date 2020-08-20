import telebot
import pyowm
import requests

proxies = {
    'http': 'socks5://localhost:9050',
    'https': 'socks5://localhost:9050'
}

url = "https://api.telegram.org"

out = requests.get(url, proxies=proxies).text

owm = pyowm.OWM('92a039b2f5b82f5ef1267a5892016c2b', language = "ru")
bot = telebot.TeleBot ("736407448:AAFT1Mr0v-X36P7Iy7yyW59iVelto_JAqv4")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start! \nВсё что я могу сейчас это подсказать погоду. \nКакой город тебя интересует?')

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place( message.text )
	w = observation.get_weather()
	temp = w.get_temperature('celsius')['temp']

	answer = 'В городе ' + message.text + ' сейчас ' + w.get_detailed_status() + "\n"
	answer += 'Температура сейчас в районе ' + str(temp) + "\n\n"

	if temp < 15:
		answer += 'Прохладно, конечно. Накинь что-нибудь потеплее!'
	elif temp < 20:
		answer += 'Хорошая погода!'
	elif temp < 30:
		answer += 'Жаришка-жаришка. Не забывай пить побольше воды'
	else:
		answer += 'Температура норм. Одевай что угодно'

    #bot.reply_to(message, message.text)
	bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True, interval=0)