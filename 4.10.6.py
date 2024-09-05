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

pages = soup.find('div', class_ = 'pagen')
page = int(pages.find_all('a')[-1].text)
print(page)