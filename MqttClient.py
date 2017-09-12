"""This module exposes a class that handles all MQTT interactions"""
import os
import paho.mqtt.client as paho


class MqttClient:
    """A facade api to  MQTT client"""

    def __init__(self):
        self.mqttc = paho.Client()
        mqtt_host = os.environ.get("mqtt-host", '')
        mqtt_user = os.environ.get("mqtt-user", '')
        mqtt_pwd = os.environ.get("mqtt-pwd", '')
        mqtt_port = int(os.environ.get("mqtt-port", 5001))
        self.mqttc.username_pw_set(mqtt_user, mqtt_pwd)

        print('Trying to establish connection to ' + mqtt_host)
        try:
            self.mqttc.connect(mqtt_host, mqtt_port)
        except ValueError:
            print("Oops!  connection to '%s' couldn't be established" %
                  (mqtt_host))

    def publish(self, topic: str, message: str):
        """Publishes a new message to a topic"""
        return self.mqttc.publish(topic, message)
