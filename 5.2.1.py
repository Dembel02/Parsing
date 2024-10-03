# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# with webdriver.Chrome(ChromeDriverManager().install()) as driver:
#     driver.get("https://stepik.org/course/104774")
#     time.sleep(5)

# Или

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.service import Service as ChromiumService

with webdriver.Chrome(
        service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())) as driver:
    driver.get("https://stepik.org/course/104774")
    time.sleep(5)

# from webdriver_manager.chrome import ChromeDriverManager
# from selenium import webdriver

# # Initialize the ChromeDriver with the installed executable
# driver = webdriver.Chrome(ChromeDriverManager().install())

# # You can use the driver now
# with driver:
#     # Your code here
#     driver.get("https://www.google.com")