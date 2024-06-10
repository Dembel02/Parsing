import requests
from bs4 import BeautifulSoup
url = 'https://parsinger.ru/4.8/8/index.html'

response = requests.get(url=url)
response.encoding = 'utf-8'
result = []
soup = BeautifulSoup(response.text, 'html.parser')
vol_1 = soup.find_all('th',{'colspan':True})
for i in vol_1:
    cleaned_text = i.text.replace(' ', '').strip()  # Очищаем текст от лишних символов
    if cleaned_text.isdigit():  # Проверяем, состоит ли текст только из цифр
        result.append(int(cleaned_text))
    # result.append(int(i.text))
vol_2 = soup.find_all('td',{'colspan':True})
for i in vol_2:
    cleaned_text = i.text.replace(' ', '').strip()  # Очищаем текст от лишних символов
    if cleaned_text.isdigit():  # Проверяем, состоит ли текст только из цифр
        result.append(int(cleaned_text))
print(sum(result))