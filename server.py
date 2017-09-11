import paho.mqtt.client as paho
import os

from flask import Flask
app = Flask(__name__)

from flask import request

mqttc = paho.Client()
mqttc.connect(os.environ["mqtt-host"])


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/webhook", methods=['POST'])
def webhook():
    print(request.is_json)
    content = request.get_json()
    mqttc.publish('topic', content)
    print(content)
    return 'ok'
