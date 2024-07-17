import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/table/4/index.html'

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
sum_value = 0
table = soup.find('table')
rows = table.find_all('td', class_='green')
for row in rows:
    sum_value += float(row.text)
    print(row.text)

print(sum_value)