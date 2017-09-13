"""rest apis routes"""
import logging
from flask import request
from flask import Flask
from lib.mqtt_client import MqttClient
import settings as Config


class Server(object):
    """Server class"""
    app = Flask(__name__)

    def __init__(self):
        self.mqttc = MqttClient()

    @app.route("/")
    # pylint: disable=no-method-argument
    def hello():
        """default"""
        return "Hello World!"

    @app.route("/webhook", methods=['POST'])
    def webhook(self):
        """webhook api"""
        content = request.get_json()
        self.mqttc.publish(Config.MQTT_FB_WEBHOOK_TOPIC_NAME, str(content))
        logging.info('Handled webhook request ' + str(content))
        return ''
