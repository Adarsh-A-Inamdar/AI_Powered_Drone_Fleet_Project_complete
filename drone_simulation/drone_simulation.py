
import random
import time
import json
from tensorflow import lite

class Drone:
    def __init__(self, drone_id, location):
        self.drone_id = drone_id
        self.location = location
        self.data = {
            'temperature': 0,
            'humidity': 0,
            'air_quality': 0,
            'co2_levels': 0,
            'water_level': 0
        }
        self.model = lite.Interpreter(model_path="models/anomaly_detection.tflite")
        self.model.allocate_tensors()

    def collect_data(self):
        self.data['temperature'] = round(random.uniform(20.0, 35.0), 2)
        self.data['humidity'] = round(random.uniform(30.0, 90.0), 2)
        self.data['air_quality'] = random.randint(0, 500)
        self.data['co2_levels'] = round(random.uniform(300, 400), 2)
        self.data['water_level'] = round(random.uniform(1.0, 10.0), 2)

    def detect_anomaly(self):
        input_data = [self.data['temperature'], self.data['humidity'], self.data['air_quality']]
        self.model.set_tensor(self.model.get_input_details()[0]['index'], [input_data])
        self.model.invoke()
        output = self.model.get_tensor(self.model.get_output_details()[0]['index'])
        return output[0] > 0.5

    def send_data(self):
        payload = {
            'drone_id': self.drone_id,
            'location': self.location,
            'data': self.data,
            'anomaly': self.detect_anomaly()
        }
        print(json.dumps(payload))

    def run(self):
        while True:
            self.collect_data()
            self.send_data()
            time.sleep(5)

if __name__ == "__main__":
    drone_fleet = [Drone(f'drone_{i}', {'lat': random.uniform(-90, 90), 'long': random.uniform(-180, 180)}) for i in range(5)]
    for drone in drone_fleet:
        drone.run()
