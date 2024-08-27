# Сбор данных со всех карточек товара
# Соберите данные всех карточек товара всех категорий и со всех страниц тренажера 
# (всего 160шт).
# Не "проваливайтесь" внутрь каждой карточки. Соберите только информацию из превью.
# Сохраните данные в JSON файл с использованием указанных параметров.
# json.dump(res, file, indent=4, ensure_ascii=False)
# Отправьте готовый JSON файл в валидатор, для успешной валидации файла, необходимо сохранить порядок объектов JSON:
# Порядок сбора категорий;
# Часы
# Телефоны
# Мыши
# HDD
# Наушники
# Имя файла произвольное.
# Удалите все лишние пробелы из данных. методом .strip().
# Если файл совпадает с эталоном на сервере, вы получите код. Этот код необходимо будет вставить в поле ответа.
# Используйте этот сервис для проверки разности строк. 

import requests
from bs4 import BeautifulSoup
import json

url = 'https://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

name = [x.text.strip() for x in soup.find_all('a', class_ = 'name_item')]
description = [x.text.strip().split('\n') for x in soup.find_all('div', class_ = 'description')]
price = [x.text.strip() for x in soup.find_all('p', class_ = 'price')]

result_json = []

for list_item, price_item, name in zip (description, price, name):
    result_json.append({
        "Наименование": name,
        "Бренд": [x.split(':')[1].strip() for x in list_item][0],
        "Тип подключения": [x.split(':')[1].strip() for x in list_item][1],
        "Цвет": [x.split(':')[1].strip() for x in list_item][2],
        "Тип наушников": [x.split(':')[1].strip() for x in list_item][3],
        "Цена": price_item
    })

with open('res_4.10.5.json', 'w', encoding= 'UTF-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)

print(result_json)