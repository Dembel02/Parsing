# 1 -------------------------------------------------------------
import csv
from bs4 import BeautifulSoup
import requests
# 1 -------------------------------------------------------------

# 2 -------------------------------------------------------------
with open ('res_1.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    # writer.writerow('')
# 2 -------------------------------------------------------------

# 3 -------------------------------------------------------------
url = 'https://parsinger.ru/html/index1_page_1.html'

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

# 3 -------------------------------------------------------------

# 4 -------------------------------------------------------------
# pagen = int(soup.find('div', class_ = 'pagen').find_all('a')[-1].text)
# for i in range(1, pagen + 1):
#     url = f'https://parsinger.ru/html/index1_page_{i}.html'
#     response = requests.get(url=url)
#     response.encoding = 'utf-8'
#     soup = BeautifulSoup(response.text, 'lxml')
#     name = soup.find_all('a', class_ = 'name_item')
#     for i in name:
#         # j = i.find_all('a', class_ = 'name_item')
#         print(i.find('a').text)
    
#     print(name)
name = soup.find_all('a', class_ = 'name_item')
for i in name:
    i.find('a', [f'name_{j}' for j in range(1, 8)])
    print(i.find('a'))