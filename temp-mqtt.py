#!/usr/bin/python3
# Import package
import os
import glob
import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publishpython
import click
import yaml

def loadConfig(path):
    with open(path, 'r') as ymlfile:
        config = yaml.load(ymlfile)
    return config
def read_temp_raw(path):
    sensor_file = open(path, 'r') # Opens the temperature device file
    raw_data = sensor_file.readlines() # Returns the text
    sensor_file.close()
    sensor_data = raw_data[1].split("t=") # split the second line output at t=
    temp_c = float(sensor_data[1]) / 1000.0 # convert value of t= to calcius
    return temp_c

@click.command()
@click.option('--config', '-c', help='path to your config file i.e. sensors.yml')
def main(config):
    # Initialize the mqtt connection
    config_yaml = loadConfig(config)
    client = mqtt.Client()
    client.username_pw_set(config_yaml['mqtt']['username'], config_yaml['mqtt']['password'])
    client.connect(config_yaml['mqtt']['broker'])
    client.loop_start()
    while True:
        for sensor in config_yaml['sensors']:
            sensor_value = read_temp_raw(sensor['path'])
            sensor_name = sensor['friendly']
            friendly_name = "home-assistant/{}/temperature".format(sensor_name)
            client.publish(friendly_name, sensor_value)
            print(friendly_name, sensor_value)
        time.sleep(int(config_yaml['mqtt']['interval_seconds']))
main()
