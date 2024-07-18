import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/table/2/index.html'

response = requests.get(url=url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')
sum_column = 0
table = soup.find('table')
rows = table.find_all('tr')
for row in rows:
    columns = row.find_all('td')
    if columns:
        sum_column += float(columns[0].text)
print(sum_column)