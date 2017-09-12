"""rest apis routes"""
from flask import request
from webhook.MqttClient import MqttClient
mqttc = MqttClient()

from flask import Flask
app = Flask(__name__)

FB_WEBHOOK_TOPIC_NAME = 'fb-posts-updates'


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/webhook", methods=['POST'])
def webhook():
    content = request.get_json()
    mqttc.publish(FB_WEBHOOK_TOPIC_NAME, str(content))
    print('Handled webhook request ' + str(content))
    return 'ok'
