"""This module exposes a class that handles all MQTT interactions"""
import logging
import datetime
import json
import paho.mqtt.client as paho
import settings as Config
from common.msg import Msg

# pylint: disable=too-few-public-methods


class MqttClient:
    """A facade api to  MQTT client"""

    def __init__(self):
        self.mqttc = paho.Client()
        self.mqttc.on_message = self.on_message
        self.mqttc.username_pw_set(Config.MQTT_USER, Config.MQTT_PWD)
        self.callback = None

        logging.warning('Trying to establish connection to ' +
                        Config.MQTT_HOST)
        try:
            self.mqttc.connect(Config.MQTT_HOST, Config.MQTT_PORT)
        except ValueError:
            logging.critical(
                "Oops!  connection to '%s' couldn't be established",
                Config.MQTT_HOST)
        self.mqttc.loop_start()  #start the loop
        self.mqttc.subscribe('posts')

    def reg(self, callback):
        """register a callback method to dlegate when topic updated"""
        self.callback = callback

    def publish(self, topic: str, message: Msg):
        """Publishes a new message to a topic"""
        return self.mqttc.publish(topic, json.dumps(message.__dict__))

    # pylint: disable=unused-argument
    def on_message(self, client, userdata, message):
        """callback"""
        self.callback("Thanks! " + datetime.datetime.now())
        logging.info("got message!" + message + userdata)
