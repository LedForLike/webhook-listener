"""This module exposes a class that handles all MQTT interactions"""
import logging
import paho.mqtt.client as paho
import webhook.config as Config


class MqttClient:
    """A facade api to  MQTT client"""

    def __init__(self):
        self.mqttc = paho.Client()
        self.mqttc.username_pw_set(Config.MQTT_USER, Config.MQTT_PWD)

        logging.warning(
            'Trying to establish connection to ' + Config.MQTT_HOST)
        try:
            self.mqttc.connect(Config.MQTT_HOST, Config.MQTT_PORT)
        except ValueError:
            logging.critical(
                "Oops!  connection to '%s' couldn't be established", Config.MQTT_HOST)

    def publish(self, topic: str, message: str):
        """Publishes a new message to a topic"""
        return self.mqttc.publish(topic, message)