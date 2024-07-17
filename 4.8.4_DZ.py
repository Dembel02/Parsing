import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/table/3/index.html'

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
sum_value = 0
table = soup.find('table')
rows = table.find_all('td')
for row in rows:
    value_ = row.find('b')
    if value_:
        sum_value += float(value_.text)

print(sum_value)