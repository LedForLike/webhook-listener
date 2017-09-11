from flask import Flask
app = Flask(__name__)

from flask import request
import paho.mqtt.client as paho


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/webhoo", methods=['POST'])
def webhook():
    mqttc = paho.Client()
    mqttc.connect()
    print(request.is_json)
    content = request.get_json()
    mqttc.publish('topic', content)
    print(content)
    return 'JSON posted'
