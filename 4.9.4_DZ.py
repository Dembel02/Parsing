import csv
import requests
from bs4 import BeautifulSoup

# 1 -----------------------------------------------------------
with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость', 'Объем буферной памяти', 'Цена'
    ])
# 1 ------------------------------------------------------------

# 2 ------------------------------------------------------------

url ='https://parsinger.ru/html/index4_page_1.html'

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
# 2 ------------------------------------------------------------
pagen = int(soup.find('div', 'pagen').find_all('a')[-1].text)
print(pagen)
for i in range (1, pagen+1):
    url = f'https://parsinger.ru/html/index4_page_{i}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    #print(url)
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
    with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for item, price, descr in zip(name, price, description):
            
            # Формируем строку для записи
            flatten = item, *[x.split(':')[1].strip() for x in descr if x], price
            writer.writerow(flatten)

print('Файл res.csv создан')