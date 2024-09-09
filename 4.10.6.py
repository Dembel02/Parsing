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

# pages = soup.find('div', class_ = 'pagen')
# page = int(pages.find_all('a')[-1].text)
# print(page)
list_href = []
for i in range(1, 32 + 1):
    url = f'https://parsinger.ru/html/mobile/2/2_{i}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    name = soup.find('p', id = 'p_header' ).text
    # ul_description = soup.find('ul', )
    description = [x.text.strip().split('\n') for x in soup.find_all('ul', id = 'description')]
    # print(url)
    # item_card = soup.find_all('div', class_ = 'img_box')
    # card_href = item_card.find_all('a')
    print(description)