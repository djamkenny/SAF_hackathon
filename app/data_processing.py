import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_dht  # Updated import statement
import paho.mqtt.client as mqtt

# importation from my app folder
from analysis_algorithms import process_soil_data, decision_support_system
from mongo_connector import log_sensor_data

# Initialize MQTT client (example)
# mqtt_client = mqtt.Client(callback_api_version=mqtt.MQTTv31)
# mqtt_client.connect("mqtt.eclipse.org", 1883, 60)


# || HAVE TO GET THE RIGHT VALUE FROM THE SENSORS ||

# Placeholder values for testing
MOCK_SENSOR_VALUES = {
    'moisture': 50.0,
    'ph': 6.5,
    'nutrient': 150.0,
    'temperature': 25.0,
    'crop_health': [0.8, 0.6, 0.95]  # Placeholder values for chlorophyll, leaf moisture, disease presence
}

def read_soil_moisture():
    # Replace with actual soil moisture sensor reading logic
    # Example using a hypothetical analog soil moisture sensor
    analog_in = AnalogIn(ADS.ADS1115(busio.I2C(board.SCL, board.SDA)))
    moisture = analog_in.value * (100.0 / 32767.0)
    return moisture

def read_ph_sensor():
    # Replace with actual pH sensor reading logic
    # Example using a hypothetical analog pH sensor
    analog_in = AnalogIn(ADS.ADS1115(board.I2C()))
    ph = analog_in.value * (14.0 / 32767.0)
    return ph

def read_nutrient_sensor():
    # Replace with actual nutrient sensor reading logic
    # Example using a hypothetical analog nutrient sensor
    analog_in = AnalogIn(ADS.ADS1115(board.I2C()))
    nutrient = analog_in.value * (200.0 / 32767.0)
    return nutrient

def read_temperature_sensor():
    # Replace with actual temperature sensor reading logic using adafruit_dht
    pin = 4  # Pin 4 on Raspberry Pi
    dht = adafruit_dht.DHT22(board.D4)  # Use board.D4 instead of pin for DHT22
    temperature = dht.temperature
    return temperature

def read_crop_health_sensors():
    # Replace with actual crop health sensor reading logic
    # Example using placeholder values for chlorophyll, leaf moisture, disease presence
    return MOCK_SENSOR_VALUES['crop_health']

def publish_sensor_data(data):
    # Replace with actual MQTT publishing logic
    topic = "sensor_data"
    payload = ','.join(map(str, data))
    mqtt_client.publish(topic, payload)

def read_sensor_data():
    moisture = read_soil_moisture()
    ph = read_ph_sensor()
    nutrients = read_nutrient_sensor()
    temperature = read_temperature_sensor()
    crop_health_data = read_crop_health_sensors()

    return moisture, ph, nutrients, temperature, crop_health_data

def process_and_publish_data():
    moisture, ph, nutrients, temperature, crop_health_data = read_sensor_data()

    processed_data = process_soil_data(moisture, ph, nutrients, temperature)
    decision = decision_support_system(processed_data)

    log_sensor_data([moisture, ph, nutrients, temperature, *crop_health_data, decision])
    publish_sensor_data([moisture, ph, nutrients, temperature, *crop_health_data, decision])


# Other functions (process_soil_data, decision_support_system, log_sensor_data, etc.) go here.
