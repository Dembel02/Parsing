import requests
from bs4 import BeautifulSoup
import json

base_url = 'https://parsinger.ru/html/index1_page_'
all_links = []
list_href = []
result_json = []

# Получаем номер последней страницы
response = requests.get(url=f'{base_url}1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

# Проверяем наличие элемента с номером страницы
pagen_element = soup.find('div', class_='pagen')
if pagen_element:
    pagen = int(pagen_element.find_all('a')[-1].text)
else:
    print("Не удалось найти элемент с номером страницы.")
    pagen = 1  # или другое значение по умолчанию

# Извлечение ссылок из nav_menu
types_href = soup.find_all('div', class_='nav_menu')
for nav_menu in types_href:
    links = nav_menu.find_all('a')  # Находим все теги <a> в nav_menu
    for link in links:
        href = link.get('href')  # Получаем значение атрибута href
        if href:  # Проверяем, что href не None
            list_href.append(href)  # Добавляем ссылку в список

# Выводим собранные ссылки
print("Собранные ссылки:")
for href in list_href:
        url_1 = f'https://parsinger.ru/html/{href}'
        response_1 = requests.get(url=url_1)
        response_1.encoding = 'utf-8'
        soup = BeautifulSoup(response_1.text, 'lxml')
        pagen = int(soup.find('div', class_ = 'pagen').find_all('a')[-1].text)
        index_ = int(href.strip()[5])
        for i in range(1, pagen + 1):
            url = f'https://parsinger.ru/html/index{index_}_page_{i}.html'
            response = requests.get(url=url)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')
            name = [x.text.strip() for x in soup.find_all('a', class_ = 'name_item')]
            description = [x.text.strip().split('\n') for x in soup.find_all('div', class_ = 'description')]
            price = [x.text.strip() for x in soup.find_all('p', class_ = 'price')]
            
            for list_item, price_item, name in zip (description, price, name):
                result_json.append({
                    "Наименование": name,
                    [x.split(':')[0].strip() for x in list_item][0] : [x.split(':')[1].strip() for x in list_item][0],
                    [x.split(':')[0].strip() for x in list_item][1] : [x.split(':')[1].strip() for x in list_item][1],
                    [x.split(':')[0].strip() for x in list_item][2] : [x.split(':')[1].strip() for x in list_item][2],
                    [x.split(':')[0].strip() for x in list_item][3] : [x.split(':')[1].strip() for x in list_item][3],
                    "Цена": price_item
                })

            with open('4.10.5.json', 'w', encoding= 'UTF-8') as file:
                    json.dump(result_json, file, indent=4, ensure_ascii=False)
            print(description)