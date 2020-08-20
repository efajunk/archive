import pyowm
import time
import os 
from colorama import * 
from pyowm.exceptions import OWMError

init(autoreset = True)

print(Fore.BLACK + Back.WHITE + 'Let`s go')



owm = pyowm.OWM('bbc3649126d17d7bb4111c44c6a562d5')
place = input("Place you find: ")

main = owm.weather_at_place(place)
weather = main.get_weather()
maxtemp = weather.get_temperature("celsius")["temp_max"] 
midtemp =  weather.get_temperature("celsius")["temp"]
mintemp = weather.get_temperature("celsius")["temp_min"]
speedwind = weather.get_wind()["speed"]
status = weather.get_detailed_status()
azimuth = weather.get_wind()["deg"]
humidity = weather.get_humidity()

try:
    owm.weather_at_place(place)
except api_response_error.NotFoundError:
    print('Wrong information, try again and find out mistakes please')
    time.sleep(10)