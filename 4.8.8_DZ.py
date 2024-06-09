import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/4.8/7/index.html'

response = requests.get(url=url)
response.encoding = 'utf-8'
result = []
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find_all('tr')
for i in table:
    table_i = i.find_all('td')
    for i in table_i:
        j = int(i.text)
        if j % 3 == 0:
            result.append(j)
            
print(sum(result))