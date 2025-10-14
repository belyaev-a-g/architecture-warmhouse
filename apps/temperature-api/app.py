from flask import Flask, request, jsonify
import random

app = Flask(__name__)

def get_default_location(sensor_id):
    """Получить местоположение по умолчанию на основе sensorId"""
    print("sensor_id = ", sensor_id)
    if sensor_id == "1":
        return "Living Room"
    elif sensor_id == "2":
        return "Bedroom"
    elif sensor_id == "3":
        return "Kitchen"
    else:
        return "Unknown"

def get_default_sensor_id(location):
    """Получить sensorId по умолчанию на основе местоположения"""
    if location == "Living Room":
        return "1"
    elif location == "Bedroom":
        return "2"
    elif location == "Kitchen":
        return "3"
    else:
        return "0"

@app.route('/temperature', methods=['GET'])
def get_temperature():
    """Обработчик для получения температуры"""
    # Получаем параметры из запроса
    location = request.args.get('location', '').strip()
    sensor_id = request.args.get('sensor_id', '').strip()
    
    # Если location не указан, используем значение по умолчанию на основе sensorId
    if not location and sensor_id:
        location = get_default_location(sensor_id)
    
    # Если sensorId не указан, генерируем на основе location
    if not sensor_id and location:
        sensor_id = get_default_sensor_id(location)
    
    # Если оба параметра не указаны, используем случайные значения
    if not location and not sensor_id:
        #locations = ["Living Room", "Bedroom", "Kitchen", "Bathroom", "Office"]
        #location = random.choice(locations)
        #sensor_id = get_default_sensor_id(location)
        sensor_id = 0
    
    # Генерируем случайную температуру в диапазоне 15-30 градусов
    temperature = random.randint(0, 30)

    location = get_default_location(sensor_id)
    
    # Формируем ответ
    response = {
        "location": location,
        "sensorId": sensor_id,
        "temperature": temperature,
        "unit": "Celsius"
    }
    
    return jsonify(response)

@app.route('/health', methods=['GET'])
def health_check():
    """Проверка здоровья сервиса"""
    return jsonify({"status": "healthy", "service": "temperature-api"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
