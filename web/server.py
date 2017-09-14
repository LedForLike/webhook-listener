"""rest apis routes"""
import logging
from flask import request
from flask import Flask
import settings as Config
from lib.mqtt_client import MqttClient
from lib.msg import Msg


# pylint: disable=no-method-argument
class Server(object):
    """Server class"""
    app = Flask(__name__)
    MQTTC = MqttClient()

    @app.route("/")
    def hello():
        """default"""
        return "Hello World!"

    @app.route("/webhook", methods=['GET'])
    def verify():
        """webhook api"""
        return request.args.get('hub.challenge')

    @app.route("/webhook", methods=['POST'])
    def fb_feeds_webhook():
        """webhook api"""
        logging.debug('Handling webhook request!!')
        content = request.get_json()
        if content['entry'][0]['changes'][0]['value']['item'] == 'like':
            Server.MQTTC.publish(
                Config.MQTT_FB_WEBHOOK_TOPIC_NAME,
                Msg(
                    int(content['entry'][0]['time']),'LIKE',
                    content['entry'][0]['changes'][0]['value']['user_id']))

        logging.info('Handled webhook request ' + str(content))
        return ''
