import pyowm

owm = pyowm.OWM('92a039b2f5b82f5ef1267a5892016c2b', language = "ru")


place = input('Введите в каком городе/стране?: ')

observation = owm.weather_at_place(place)
w = observation.get_weather()

temp = w.get_temperature('celsius')['temp']

print('В городе ' + place + ' сейчас ' + w.get_detailed_status())
print('Температура сейчас в районе ' + str(temp))

if temp < 15:
	print('Прохладно, конечно. Накинь что-нибудь потеплее!')
elif temp < 20:
	print('Вечная мерзлота...')
elif temp < 30:
	print('Ядерная зима!')
else:
	print('Температура норм. Одевай что угодно')

print()