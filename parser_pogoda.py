from bs4 import BeautifulSoup
import requests
import lxml

with open('Pogoda.html', 'r', encoding='utf-8') as file:
    soup2 = BeautifulSoup(file, 'lxml')
   
    temp_text = soup2.find('span',class_='temp__value temp__value_with-unit').text
    print("Температура наружняя:\n", temp_text)

    wind_speed = soup2.find('span', class_='wind-speed').text
    print("Скорость ветра:\n", wind_speed)

    