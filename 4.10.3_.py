import requests
from bs4 import BeautifulSoup

response = requests.get('http://parsinger.ru/html/watch/1/1_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
description = soup.find('ul', id='description').find_all('li')
li_id = [x['id'] for x in description]
print(li_id)