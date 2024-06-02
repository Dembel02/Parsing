import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/table/5/index.html'

response = requests.get(url=url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')
total_sum = [0] * 15
result = {}
rows = table.find_all('tr')
for row in rows:
    columns = row.find_all('td')
    for j, column in enumerate(columns):
        total_sum[j] += float(column.text)
for i, sum_j in enumerate(total_sum):
    result[f"{i+1} column"] = round(sum_j, 3)

print(result)
