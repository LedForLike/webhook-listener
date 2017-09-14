"""rest apis routes"""
import logging
from flask import request
from flask import Flask
import settings as Config
from common.msg import Msg
from services.facebook_service import FacebookService


# pylint: disable=no-method-argument
class Server(object):
    """Server class"""
    app = Flask(__name__)
    facebook = FacebookService()

    def __init__(self, mqttc):
        Server.MQTTC = mqttc

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
                    int(content['entry'][0]['id']),
                    int(content['entry'][0]['time']), 'LIKE',
                    content['entry'][0]['changes'][0]['value']['user_id']))

        logging.info('Handled webhook request ' + str(content))
        return ''

    @app.route("/postpage", methods=['POST'])
    def post_facebook():
        """facebook page post api for testings only"""
        Server.facebook.post_to_page("yo!")
        return ''
