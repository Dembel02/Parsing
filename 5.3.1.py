import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options_chrome = webdriver.ChromeOptions()

# Используем WebDriverManager для автоматического скачивания и установки драйвера
service = Service(ChromeDriverManager().install())

options_chrome.add_extension('coordinates.crx')

with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://stepik.org/course/104774'
    browser.get(url)
    time.sleep(15)