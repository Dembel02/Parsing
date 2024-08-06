# 1 -------------------------------------------------------------
import csv
from bs4 import BeautifulSoup
import requests
# 1 -------------------------------------------------------------

# 2 -------------------------------------------------------------
with open ('rez_1.csv', w, encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    