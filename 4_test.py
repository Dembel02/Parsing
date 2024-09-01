import requests
from bs4 import BeautifulSoup

base_url = 'https://parsinger.ru/html/index1_page_'
all_links = []
list_href = []

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
    print(href)