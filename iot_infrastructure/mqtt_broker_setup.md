
# MQTT Broker Setup

To set up an MQTT broker locally, follow these steps:

### Install Mosquitto (Ubuntu)
```bash
sudo apt-get update
sudo apt-get install mosquitto mosquitto-clients
```

### Start Mosquitto Service
```bash
sudo systemctl start mosquitto
sudo systemctl enable mosquitto
```

Once installed, you can test publishing and subscribing using:
```bash
mosquitto_sub -t "environment/drone/#"
mosquitto_pub -t "environment/drone/test" -m "Test message"
```
