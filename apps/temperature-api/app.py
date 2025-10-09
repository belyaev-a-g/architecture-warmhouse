from flask import Flask, request, jsonify
import random
from datetime import datetime

app = Flask(__name__)

# Mapping between location names and sensor IDs
LOCATION_TO_SENSOR_ID = {
    "Living Room": "1",
    "Bedroom": "2",
    "Kitchen": "3"
}

SENSOR_ID_TO_LOCATION = {
    "1": "Living Room",
    "2": "Bedroom",
    "3": "Kitchen"
}


def generate_random_temperature():
    """Generate a random temperature between 18 and 28 degrees Celsius"""
    return round(random.uniform(18.0, 28.0), 2)


@app.route('/temperature', methods=['GET'])
def get_temperature_by_location():
    """
    Get temperature by location query parameter
    Example: /temperature?location=Living Room
    """
    location = request.args.get('location', '')
    sensor_id = request.args.get('sensorId', '')
    
    # If no location is provided, use a default based on sensor ID
    if location == "" and sensor_id != "":
        location = SENSOR_ID_TO_LOCATION.get(sensor_id, "Unknown")
    
    # If no sensor ID is provided, generate one based on location
    if sensor_id == "" and location != "":
        sensor_id = LOCATION_TO_SENSOR_ID.get(location, "0")
    
    # If both are empty, use defaults
    if location == "" and sensor_id == "":
        location = "Unknown"
        sensor_id = "0"
    
    temperature = generate_random_temperature()
    
    response = {
        "value": temperature,
        "unit": "°C",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "location": location,
        "status": "active",
        "sensor_id": sensor_id,
        "sensor_type": "temperature",
        "description": f"Temperature reading for {location}"
    }
    
    return jsonify(response), 200


@app.route('/temperature/<sensor_id>', methods=['GET'])
def get_temperature_by_id(sensor_id):
    """
    Get temperature by sensor ID
    Example: /temperature/1
    """
    location = SENSOR_ID_TO_LOCATION.get(sensor_id, "Unknown")
    temperature = generate_random_temperature()
    
    response = {
        "value": temperature,
        "unit": "°C",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "location": location,
        "status": "active",
        "sensor_id": sensor_id,
        "sensor_type": "temperature",
        "description": f"Temperature reading for {location}"
    }
    
    return jsonify(response), 200


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "ok"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=False)

