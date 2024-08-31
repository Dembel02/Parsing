import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/table/1/index.html'

response = requests.get(url=url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')
total = set()

table = soup.find('table')
rows = soup.find_all('tr')[1:]

for row in rows:
    values = row.text.strip().split('\n')
    for value in values:
        total.add(float(value))
sum_total = sum(total)
print(sum_total)