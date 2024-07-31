# 1 -------------------------------------------------------------------
from bs4 import BeautifulSoup
import requests
import csv
# 1 -------------------------------------------------------------------

# 2 -------------------------------------------------------------------
with open('rezult.csv', 'w', encoding='utf-8-sig',newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип', 
        'Технология экрана', 'Материал корпуса', 'Материал браслета', 
        'Размер', 'Сайт производителя', 'Наличие', 'Цена', 'Старая цена',
        'Ссылка на карточку с товаром'
    ])

# 3 -------------------------------------------------------------------
url = 'https://parsinger.ru/html/index1_page_1.html'

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
#print(soup)
# 3 -------------------------------------------------------------------

# 4 -------------------------------------------------------------------
pagen = int(soup.find('div', class_ = 'pagen').find_all('a')[-1].text)
# В переменную pagen спарсим количесто страниц 
# for i in range(1, pagen + 1):
#     url = f'https://parsinger.ru/html/index1_page_{i}.html'
#     response = requests.get(url=url)
#     response.encoding = 'utf-8'
#     soup = BeautifulSoup(response.text, 'lxml')
#     print(url)
item_card = soup.find_all('div', class_ = 'img_box')
# card_href = item_card.find_all('a')
for i in item_card:
    print(i)
url = 'https://parsinger.ru/html/watch/1/1_1.html'
response_1 = requests.get(url=url)
response_1.encoding = 'utf-8'
soup = BeautifulSoup(response_1.text, 'lxml')

name = soup.find('p', id = 'p_header').text
article = soup.find('p', class_ = 'article').text.split()[1]
description = [x.text.split('\n') for x in soup.find('ul', id = 'description')]
in_stock = int(soup.find('span', id = 'in_stock').text.split(':')[1])
price = soup.find('span', id = 'price').text.split()[0]
old_price = soup.find('span', id = 'old_price').text.split()[0]
# print(old_price)