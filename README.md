# DS18B20-mqtt
Send sensor data from DS18B20 to MQTT (works with home-assistant).

## Config
Edit sensors.yml with your home-assistant info.

## home-assistant
Update your home-assistant sensors.yml or sensors section in configuration.yml with the new mqtt topics, for example:
```
- platform: mqtt
  state_topic: "home-assistant/balcony/temperature"
  name: "Balcony Temperature"
  unit_of_measurement: "°C"
- platform: mqtt
  state_topic: "home-assistant/livingroom/temperature"
  name: "Living Room Temperature"
  unit_of_measurement: "°C"
```

## Setup
On your Pi or device that has the sensors attached, we'll get things going.

Ubuntu:
```bash
sudo apt-get install python3 python3-virtualenv
virtualenv -p /usr/bin/python3 temp-mqtt
cd temp-mqtt
source bin/activate
git clone https://github.com/ngonzal/DS18B20-mqtt.git
cd DS18B20-mqtt
pip install -r requirements.txt
python temp-mqtt.py -c sensors.yml
```
