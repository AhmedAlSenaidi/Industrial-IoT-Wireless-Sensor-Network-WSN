import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient
import re

# Connect to InfluxDB
client_influx = InfluxDBClient(host="localhost", port=8086, username="admin", password="admin123", database="sensors")

# On MQTT connection
def on_connect(client, userdata, flags, rc):
    print("MQTT connected with result code", rc)
    # Subscribe to all relevant topics
    client.subscribe("wsn/+/temperature")
    client.subscribe("wsn/+/humidity")
    client.subscribe("wsn/+/air_quality")
    client.subscribe("wsn/+/light_intensity")

# On receiving MQTT message
def on_message(client, userdata, msg):
    # Extract zone and metric from topic
    match = re.match(r"wsn/([^/]+)/([^/]+)", msg.topic)
    if not match:
        return
    
    zone, metric = match.groups()  # Extract zone and metric (e.g., "zone1", "temperature")
    value = float(msg.payload.decode())  # Parse the value from payload

    # Create the InfluxDB JSON body
    json_body = [
        {
            "measurement": metric,  # Metric as the measurement name (e.g., "temperature", "humidity")
            "tags": {
                "zone": zone  # Zone as a tag
            },
            "fields": {
                "value": value  # Value of the measurement
            }
        }
    ]

    # Write data to InfluxDB
    client_influx.write_points(json_body)
    print(f"Wrote to InfluxDB: zone={zone}, metric={metric}, value={value}")

# Initialize MQTT client and set callbacks
client_mqtt = mqtt.Client()
client_mqtt.on_connect = on_connect
client_mqtt.on_message = on_message

# Connect to the MQTT broker and start the loop
client_mqtt.connect("localhost", 1883, 60)
client_mqtt.loop_forever()
