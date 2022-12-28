import requests
from pprint import pprint

API_Key = '4c6502785275d54936da696ad9774f22'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" + city

weather_data = requests.get(base_url).json()

pprint(weather_data)