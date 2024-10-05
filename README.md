
# AI-Powered Autonomous Drone Fleet for Environmental Monitoring

## Project Overview
This project aims to monitor ecosystems by deploying a fleet of AI-powered drones with IoT infrastructure, providing real-time data collection, anomaly detection, and wildlife monitoring through AI models and computer vision.

### Key Features:
- Anomaly detection using AI models.
- Real-time video streaming from drones.
- Edge computing for faster local drone processing.
- React.js for the frontend visualization.

## Installation and Setup

### Step 1: Install Backend Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Install Frontend Dependencies
```bash
cd frontend
npm install
```

### Step 3: Setup MQTT Broker
Follow the instructions in `iot_infrastructure/mqtt_broker_setup.md` to set up your broker.

### Step 4: Train AI Models
Use the models in `ai_models`. To train anomaly detection, run:
```bash
python anomaly_detection.py
```

### Step 5: Run the Simulation and Backend
```bash
python drone_simulation.py
python iot_client.py
python app.py
```

### Step 6: Start Frontend (React.js)
```bash
cd frontend
npm start
```

