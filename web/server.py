"""rest apis routes"""
import logging
from flask import request
from flask import Flask
from lib.mqtt_client import MqttClient
import settings as Config

MQTTC = MqttClient()
# pylint: disable=no-method-argument
class Server(object):
    """Server class"""
    app = Flask(__name__)

    @app.route("/")
    def hello():
        """default"""
        return "Hello World!"

    @app.route("/webhook", methods=['GET'])
    def verify():
        """webhook api"""
        return request.args.get('hub.challenge')

    @app.route("/webhook", methods=['POST'])
    def webhook():
        """webhook api"""
        logging.debug('Handling webhook request!!')
        content = request.get_json()
        MQTTC.publish(Config.MQTT_FB_WEBHOOK_TOPIC_NAME, str(content))
        logging.info('Handled webhook request ' + str(content))
        return ''
