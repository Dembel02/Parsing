from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options_chrome = webdriver.ChromeOptions()

# Используем WebDriverManager для автоматического скачивания и установки драйвера
service = Service(ChromeDriverManager().install())

with webdriver.Chrome(service=service, options=options_chrome) as browser:
    # ваш код здесь
# with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://stepik.org/a/104774'
    browser.get(url)
    
    # Ищем элемент по тегу 'a' (ссылку)
    a = browser.find_element(By.TAG_NAME, 'a')
    
    # Выводим атрибут 'href' найденного элемента (URL ссылки)
    print(a.get_attribute('href'))