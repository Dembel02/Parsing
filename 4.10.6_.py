import requests
from bs4 import BeautifulSoup
import json

base_url = 'https://parsinger.ru/html/index2_page_1.html'

response = requests.get(url=base_url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

result_json = []

for i in range(1, 33):  # Достаточно до 32 включительно
    url = f'https://parsinger.ru/html/mobile/2/2_{i}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    
    name = soup.find('p', id='p_header').text.strip()
    article = soup.find('p', class_='article').text.strip()
    in_stock = soup.find('span', id='in_stock').text.strip()
    price = soup.find('span', id='price').text.strip()
    old_price_element = soup.find('span', id='old_price')
    old_price = old_price_element.text.strip() if old_price_element else None

    description = [li.text.strip() for li in soup.find('ul', id='description').find_all('li')] 

    result_json.append({
        
        'Наименование': name,
        'article': article.split(':')[1].strip(),
        'description': description,
        'count': in_stock.split(':')[1].strip(),
        'price': price,
        'old_price': old_price,
        'link': url
    })

with open('4.10.6.json', 'w', encoding='UTF-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)

print(result_json)