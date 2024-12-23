import psycopg2
from bs4 import BeautifulSoup
import requests
import lxml
import time
from datetime import datetime

# Подключение к PostgreSQL
conn = psycopg2.connect(
    dbname="your_database",
    user="your_user",
    password="your_password",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# # Создание таблицы, если она не существует
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS weather_data (
#     id SERIAL PRIMARY KEY,
#     timestamp TIMESTAMP NOT NULL,
#     temperature TEXT,
#     wind_speed TEXT,
#     term_value TEXT
# )
# ''')
# conn.commit()

# Функция для парсинга HTML и получения данных
def fetch_weather_data():
    with open('Pogoda.html', 'r', encoding='utf-8') as file:
        soup2 = BeautifulSoup(file, 'lxml')

        try:
            temp_text = soup2.find('span', class_='temp__value temp__value_with-unit').text
        except AttributeError:
            temp_text = None

        try:
            wind_speed = soup2.find('span', class_='wind-speed').text
        except AttributeError:
            wind_speed = None

        try:
            term_value = soup2.find('div', class_='term__value').text
        except AttributeError:
            term_value = None

        return temp_text, wind_speed, term_value

# Запись данных в PostgreSQL через определенные промежутки времени
try:
    while True:
        # Получение данных
        temp_text, wind_speed, term_value = fetch_weather_data()
        timestamp = datetime.now()

        # Запись данных в таблицу
        cursor.execute('''
        INSERT INTO weather_data (timestamp, temperature, wind_speed, term_value)
        VALUES (%s, %s, %s, %s)
        ''', (timestamp, temp_text, wind_speed, term_value))
        conn.commit()

        print(f"Данные записаны: {timestamp} | Температура: {temp_text} | Скорость ветра: {wind_speed} | Влажность: {term_value}")

        # Интервал записи данных (например, каждые 10 минут)
        time.sleep(600)  # 600 секунд = 10 минут

except KeyboardInterrupt:
    print("Программа остановлена пользователем.")
finally:
    cursor.close()
    conn.close()
