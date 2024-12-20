import sqlite3
from sense_hat import SenseHat
from datetime import datetime
import time
import requests

# Создание подключения к базе данных
conn = sqlite3.connect('sensor_data.db')
cursor = conn.cursor()

# Создание таблицы для записи данных
cursor.execute('''
CREATE TABLE IF NOT EXISTS sensor_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    temperature REAL NOT NULL,
    humidity REAL NOT NULL,
    pressure REAL NOT NULL,
    weather_temp REAL,
    weather_humidity REAL
)
''')
conn.commit()

# Инициализация Sense HAT
sense = SenseHat()

# Настройки интервала записи данных (в секундах)
data_logging_interval = 60  # Запись каждые 60 секунд

# Функция для получения данных с сайта погоды
def fetch_weather_data():
    try:
        # URL и параметры запроса (пример: OpenWeatherMap API)
        api_key = "your_api_key"
        city = "your_city"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={Ufa}&appid={6b15a37d0da96063028015d10ff67873}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_temp = data['main']['temp']
            weather_humidity = data['main']['humidity']
            return weather_temp, weather_humidity
        else:
            print(f"Ошибка при получении данных с сайта погоды: {response.status_code}")
            return None, None
    except Exception as e:
        print(f"Ошибка: {e}")
        return None, None

try:
    while True:
        # Получение данных с датчиков
        temperature = sense.get_temperature()
        humidity = sense.get_humidity()
        pressure = sense.get_pressure()

        # Получение данных о погоде
        weather_temp, weather_humidity = fetch_weather_data()

        # Получение текущего времени
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Запись данных в базу данных
        cursor.execute('''
        INSERT INTO sensor_data (timestamp, temperature, humidity, pressure, weather_temp, weather_humidity)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (timestamp, temperature, humidity, pressure, weather_temp, weather_humidity))
        conn.commit()

        print(f"Данные записаны: {timestamp} | Температура: {temperature:.2f}°C | Влажность: {humidity:.2f}% | Давление: {pressure:.2f} гПа")
        if weather_temp is not None and weather_humidity is not None:
            print(f"Погода: Температура: {weather_temp:.2f}°C | Влажность: {weather_humidity:.2f}%")

        # Интервал записи данных
        time.sleep(data_logging_interval)

except KeyboardInterrupt:
    print("\nПрограмма завершена пользователем.")

finally:
    # Закрытие соединения с базой данных
    conn.close()
