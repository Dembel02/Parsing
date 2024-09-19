import requests

url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(url=url).json()
for item in response:
    print(item["userId"], item["title"])