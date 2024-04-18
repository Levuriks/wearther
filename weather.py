# 1bfae7afb33453eee3a7ae1466d1a2f6
# https://api.openweathermap.org/data/2.5/weather?q=Воронеж&appid=1bfae7afb33453eee3a7ae1466d1a2f6&units=metric

import requests


def get_weather(home,api_key):
  print("запущено")
  print(f"Ваше местоположение: {home}. Ваш ключ: {api_key}")

  url = "https://api.openweathermap.org/data/2.5/weather?"
  complete_url = f"{url}q={home}&appid={api_key}&units=metric"
  print (complete_url)
  
  r =  requests.get(complete_url)
  print(r)

  data = r.json()
  print(type(data))

  temp = data["main"]["temp"]
  print(f"Температура: {temp}°C")
  
  weather = data["weather"][0]["description"]
  print(f"описание: {weather}")

  wind_speed = data["wind"]["speed"]
  print(f"Скорость ветра: {wind_speed} м/с")

  name = data["name"]
  print(f"Ваш город: {name}")

  temp_min = data["main"]["temp_min"]
  print(f"минимальная температура: {temp_min}°C")

  temp_max = data["main"]["temp_min"]
  print(f"максимальная температура: {temp_max}°C")

  clouds = data["clouds"]["all"]
  print(f"заполненность облаками: {clouds}%")

  visibility = data["visibility"]
  print(f"видимость: {visibility} м")

def main():
  print("Здравствуйте,это 'Погода'")
  home = input("Введите ваше местоположение:")
  api_key = "1bfae7afb33453eee3a7ae1466d1a2f6"
  get_weather(home,api_key)  



main() 

# Добавить больше информации в приложение Погода.

# Скорость ветра, страна, влажность, заполненность неба облаками и т.д. на свой вкус.






































