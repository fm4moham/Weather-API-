import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = INSERT_KEY
CITY = "London"


def kel_to_celsius_fahrenheit (kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * 1.8 + 32
    return celsius, fahrenheit

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

temp_kelvin = response["main"]["temp"]
temp_celsius , temp_fahrenheit = kel_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response ["main"]["feels_like"]
feels_like_celsius, feels_like_kelvin = kel_to_celsius_fahrenheit(feels_like_kelvin)
wind_speed = response["wind"]["speed"]
humidity = response["main"]["humidity"]
description = response["weather"][0]["description"]
sunrise_timestamp = response["sys"]["sunrise"] + response["timezone"]
sunrise_time = dt.datetime.fromtimestamp( sunrise_timestamp, dt.timezone.utc)
sunset_timestamp = response["sys"]["sunset"] + response["timezone"]
sunset_time = dt.datetime.fromtimestamp( sunset_timestamp, dt.timezone.utc)

print(f"Temperature in {CITY}: {temp_celsius:.2f}C or {temp_fahrenheit:.2f}F")
print(f"Temperature in {CITY} feels like: {feels_like_celsius:.2f}C or {feels_like_kelvin:.2f}F")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind Speed in {CITY}: {wind_speed} m/s")
print(f"General Weather in {CITY}: {description}")
print(f"Sun rises in {CITY} at  {sunrise_time} local time.")
print(f"Sun sets in {CITY} at  {sunset_time} local time.")







