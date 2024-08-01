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
list_href = []
for i in range(1, pagen + 1):
    url = f'https://parsinger.ru/html/index1_page_{i}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
#     print(url)
    item_card = soup.find_all('div', class_ = 'img_box')
    # card_href = item_card.find_all('a')
    
    for i in item_card:
        list_href.append(i.find('a').get('href'))
        y = i.find('a').get('href')
# print(list_href)
        url_1 = f'https://parsinger.ru/html/{y}'
        response_1 = requests.get(url=url_1)
        response_1.encoding = 'utf-8'
        soup = BeautifulSoup(response_1.text, 'lxml')

        name = soup.find('p', id = 'p_header').text
        article = soup.find('p', class_ = 'article').text.split()[1]
        description = [x.text.split('\n') for x in soup.find('ul', id = 'description')]
        in_stock = int(soup.find('span', id = 'in_stock').text.split(':')[1])
        price = soup.find('span', id = 'price').text.split()[0]
        old_price = soup.find('span', id = 'old_price').text.split()[0]
        # print(name)
# 4 ---------------------------------------------------------------------

# 5 --------------------------------------------------------------------
        with open('rezult.csv', 'a', encoding = 'utf-8-sig', newline = '') as file:
            writer = csv.writer('file', delimiter=';')
            for item, article, description, in_stock, price, old_price, y in zip(name, article, description, in_stock, price, old_price, y):
                # формируем строку для записи
                flatten = item, article, *[x.split(':')[1].strip() for x in description if x], in_stock, price, old_price, y
                writer.writerow(flatten)
                print(flatten)