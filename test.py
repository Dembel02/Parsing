import requests
from bs4 import BeautifulSoup
import json

base_url = 'https://parsinger.ru/html/index1_page_'
all_links = []
list_href = []

# Получаем номер последней страницы
response = requests.get(url=f'{base_url}1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
pagen = int(soup.find('div', class_='pagen').find_all('a')[-1].text)
types_href = soup.find_all('div', class_ = 'nav_menu') #.split()
for i in types_href:
    print(i)
    list_href.append(i.find('a').get('href'))
# Перебираем все страницы товаров
for page in range(1, pagen + 1):
    response = requests.get(url=f'{base_url}{page}.html')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    # Получаем все ссылки на товары на текущей странице
    product_links = soup.find_all('a', class_='name')
    for link in product_links:
        href = link.get('href')
        all_links.append(href)

# # Сохраняем данные в JSON-файл
# with open('product_links.json', 'w', encoding='utf-8') as f:
#     json.dump(all_links, f, ensure_ascii=False, indent=4)

# print(types_href)