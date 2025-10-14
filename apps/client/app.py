import requests
import time
import random
import os
from datetime import datetime

# Список из 5 локаций
locations = ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань"]
base_url = "http://localhost:8085/temperature"

def make_requests():
    """Функция для выполнения запросов каждую секунду"""
    
    while True:
        try:
            # Выбираем случайную локацию и sensor_id
            location = random.choice(locations)
            sensor_id = random.randint(1, 5)
            
            params = {
                'sensor_id': sensor_id
            }
            
            # Выполняем GET запрос
            response = requests.get(base_url, params=params)
            
            # Выводим результат
            if response.status_code == 200:
                data = response.json()
                print("data", data)
            else:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] "
                      f"Ошибка: {response.status_code} - {response.json().get('error', 'Unknown error')}")
            
        except requests.exceptions.RequestException as e:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Ошибка соединения: {e}")
        
        # Ждем 1 секунду перед следующим запросом
        time.sleep(1)

if __name__ == '__main__':
    print("Запуск клиента...")
    print("Запросы выполняются каждую секунду...")
    API_URL = os.getenv('API_URL', 'http://localhost:8085')
    print("API_URL = ", API_URL)
    base_url = API_URL + "/temperature"
    print("base_url = ", base_url)
    make_requests()
