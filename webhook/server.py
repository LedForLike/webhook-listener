"""rest apis routes"""
import logging
from flask import request
from flask import Flask
from webhook.MqttClient import MqttClient
import webhook.config as Config

mqttc = MqttClient()

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/webhook", methods=['POST'])
def webhook():
    content = request.get_json()
    mqttc.publish(Config.MQTT_FB_WEBHOOK_TOPIC_NAME, str(content))
    logging.info('Handled webhook request ' + str(content))
    return ''
