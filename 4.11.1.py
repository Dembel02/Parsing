import requests
<<<<<<< HEAD

url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(url=url).json()
for item in response:
    print(item["userId"], item["title"])
=======
from bs4 import BeautifulSoup
import json
>>>>>>> cab4a85ac61ded13a3a698e1155df7fb3d663cc1
