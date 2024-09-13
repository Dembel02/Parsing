# Соберите данные из категории mobile  (всего 32 карточки).
# "Провалитесь" в каждую карточку и соберите необходимую информацию.
# Сохраните данные в JSON файл с использованием указанных параметров.
# json.dump(res, file, indent=4, ensure_ascii=False)
# Отправьте готовый JSON файл в валидатор, для успешной валидации файла, необходимо сохранить порядок объектов JSON:
# Ключи словаря должны быть собраны из id в тегах  li;
import requests
from bs4 import BeautifulSoup
import json

base_url = 'https://parsinger.ru/html/index2_page_1.html'

response = requests.get(url=base_url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

list_href = []
result_json = []
for i in range(1, 32 + 1):
    url = f'https://parsinger.ru/html/mobile/2/2_{i}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    name = soup.find('p', id = 'p_header' ).text
    article = soup.find('p', class_ = 'article').text
    in_stock = soup.find('span', id = 'in_stock').text
    price = soup.find('span', id = 'price').text
    old_price = soup.find('span', id = 'old_price')

    description = [x.text.strip().split('\n') for x in soup.find_all('ul', id = 'description')]

    for nane, list_item in zip(name, description):
                result_json.append({
                    'Наименование' : name,
                    'article' : article.split(':')[1].strip(),
                    'description' : description,
                    'count' : in_stock.split(':')[1].strip(),
                    'price' : price,
                    'old_price' : old_price,
                    'link' : url
                    })
    with open('4.10.6.json', 'w', encoding= 'UTF-8') as file:
        json.dump(result_json, file, indent=4, ensure_ascii=False)
print(result_json)