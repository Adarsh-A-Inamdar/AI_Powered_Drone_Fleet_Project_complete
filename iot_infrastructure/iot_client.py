
import paho.mqtt.client as mqtt
import json
import time

class IoTClient:
    def __init__(self, broker_address="localhost", port=1883):
        self.client = mqtt.Client("Drone_Client")
        self.broker_address = broker_address
        self.port = port

    def connect(self):
        self.client.connect(self.broker_address, self.port)

    def publish(self, topic, payload):
        self.client.publish(topic, payload)

    def run(self, drone):
        self.connect()
        while True:
            drone.collect_data()
            payload = json.dumps({'drone_id': drone.drone_id, 'data': drone.data})
            self.publish(f"environment/drone/{drone.drone_id}", payload)
            time.sleep(5)
