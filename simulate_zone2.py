import time, random
import paho.mqtt.publish as publish

broker = "localhost"

while True:
    # Simulate metrics
    temperature = round(random.uniform(20, 30), 2)
    humidity = round(random.uniform(40, 60), 2)
    air_quality = round(random.uniform(100, 200), 2)
    light_intensity = round(random.uniform(300, 800), 2)

    # Publish data to MQTT topics
    publish.single("wsn/zone2/temperature", str(temperature), hostname=broker)
    publish.single("wsn/zone2/humidity", str(humidity), hostname=broker)
    publish.single("wsn/zone2/air_quality", str(air_quality), hostname=broker)
    publish.single("wsn/zone2/light_intensity", str(light_intensity), hostname=broker)
    
    time.sleep(5)  # Publish every 5 seconds
