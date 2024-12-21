import requests
from bs4 import BeautifulSoup
import json

url = 'https://yandex.ru/pogoda/ufa?lat=54.738456&lon=55.995403'

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')


print(soup)

