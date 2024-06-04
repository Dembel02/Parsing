import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/4.8/7/index.html'

response = requests.get(url=url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find_all('tr')
for i in table:
    print(i)