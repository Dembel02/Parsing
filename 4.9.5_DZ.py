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
for i in range(1, pagen + 1):
    url = f'https://parsinger.ru/html/index1_page_{i}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    print(url)
