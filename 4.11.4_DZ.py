import requests

url = 'https://parsinger.ru/downloads/get_json/res.json'

response = requests.get(url=url).json()


# Создаем пустой словарь для хранения сумм по категориям
categories = {}

# Подсчитываем общее количество товаров в каждой категории
for item in response:
    category = item['categories']
    count = int(item['count'])
    price = int(item['price'].split()[0])
    
    # Если категория уже есть в словаре, добавляем к её значению count
    if category in categories:
        categories[category] += (count * price)
    else:
        # Если категории ещё нет, создаём её и присваиваем ей count
        categories[category] = (count * price)
    # print(price)

# Выводим результат
print(categories)