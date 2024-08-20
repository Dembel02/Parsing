# 1 -------------------------------------------------------------
import csv
from bs4 import BeautifulSoup
import requests
# 1 -------------------------------------------------------------

# 2 -------------------------------------------------------------
with open ('res_1.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    # writer.writerow('')
# 2 -------------------------------------------------------------

# 3 -------------------------------------------------------------
url = 'https://parsinger.ru/html/index1_page_1.html'

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

# 3 -------------------------------------------------------------

# 4 -------------------------------------------------------------
pagen = int(soup.find('div', class_ = 'pagen').find_all('a')[-1].text)
for i in range(1, pagen + 1):
    url = f'https://parsinger.ru/html/index1_page_{i}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    names = soup.find_all('a', class_ = 'name_item')
    prices = [x.text for x in soup.find_all('p', class_ = 'price')]
    description_list = [x.text.split('\n') for x in soup.find('div', class_ = 'description')]
    for i, description, price in zip (names, description_list, prices):
        name = i.text

        description = [item for sublist in description_list for item in sublist]
           
        print(name, *[x.split(':')[1].strip() for x in description if ':' in x], price)
        # Находим все товары на странице
        # names = soup.find_all('a', class_='name_item')
        # descriptions = soup.find_all('div', class_='description')
        # prices = soup.find_all('p', class_='price')











        # # Обрабатываем каждый товар
        # for name, price in zip(names, prices):
        #     name_text = name.text.strip()
        #     # description_text = description.text.strip().replace('\n', ' ')
        #     price_text = price.text.strip()
        #     print(name_text, *[x.split(':')[1].strip() for x in description if ':' in x], price_text)
        #     # Записываем данные в CSV
        #     writer.writerow([name_text, description_text, price_text])