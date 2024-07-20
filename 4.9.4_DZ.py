import csv
import requests
from bs4 import BeautifulSoup

# 1 -----------------------------------------------------------
with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'Наименование', 'Цена', 'Бренд', 'Тип', 'Подключение', 'Игровая'
    ])
# 1 ------------------------------------------------------------

# 2 ------------------------------------------------------------
url ='https://parsinger.ru/html/index4_page_1.html'

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
# 2 ------------------------------------------------------------

# 3 ------------------------------------------------------------
# Извлекаем имена товаров и убираем лишние пробелы
name = [x.text.strip() for x in soup.find_all('a', class_ = 'name_item')]

# Извлекаем описания товаров и разбиваем на строки
description = [x.text.split('\n') for x in soup.find_all('div', class_ = 'description')]

# Извлекаем цены товаров
price = [x.text for x in soup.find_all('p', class_ = 'price')]
# 3 ------------------------------------------------------------

# 4 ------------------------------------------------------------
# Открываем файл для дополнительной записи данных в таблицу
