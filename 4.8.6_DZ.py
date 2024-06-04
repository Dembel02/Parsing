import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/table/6/index.html'

response = requests.get(url=url)
response.encoding = 'utf-7'

soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')
total_sum = 1
rows = table.find_all('tr')

for i in rows:
    columns = i.find_all('td')
    orange_value = i.find_all('td', class_='orange')
    for i, j in zip(columns[0:], orange_value):
        total_sum += float(j.text) * int(i.text)
        print(j.text)
        print(i.text)

print(total_sum)