Пример тестирования моей ручки:
(venv) alex@ub:~/projects$ curl -X GET "http://localhost:8085/temperature?location=Bedroom"
{
  "location": "Bedroom",
  "sensorId": "2",
  "temperature": 8,
  "unit": "Celsius"
}
(venv) alex@ub:~/projects$ curl -X GET "http://localhost:8085/temperature?sensor_id=1"
{
  "location": "Living Room",
  "sensorId": "1",
  "temperature": 27,
  "unit": "Celsius"
}

