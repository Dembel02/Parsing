import requests

url = 'https://parsinger.ru/downloads/get_json/res.json'

response = requests.get(url=url).json()
watch = 0
mobile = 0
mouse = 0
hdd = 0
headphones = 0

for item in response:
    if item["categories"] == 'watch':
        watch += 1
    elif item["categories"] == 'mobile':
        mobile += 1
    elif item["categories"] == 'mouse':
        mouse += 1
    elif item["categories"] == 'hdd':
        hdd += 1
    elif item["categories"] == 'headphones':
        headphones += 1
print(watch)
