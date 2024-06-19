# import csv
import requests
from bs4 import BeautifulSoup

#1 --------------------------------------------------------------
# with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow([
#         'Наименование', 'Артикул', 'Бренд', 'Модель', 
#         'Тип', 'Игровая', 'Размер', 'Разрешение', 'Подсветка',
#         'Сайт производителя', 'В наличии', 'Цена'])
#1 ---------------------------------------------------------------

#2 ----------------------------------------------------------------
url = 'http://parsinger.ru/html/mouse/3/3_11.html'

response = requests.get(url = url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
#2 ---------------------------------------------------------------

#3 ---------------------------------------------------------------
name = soup.find('p', id = 'p_header').text
article = soup.find('p', class_ = 'article').text.split(': ')[1]
#brand =
#model
# type
# purpose
# light
# size
# dpi
# site
# in_stock
# price

print(article)