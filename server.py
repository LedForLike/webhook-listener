import paho.mqtt.client as paho
import os

from flask import Flask
app = Flask(__name__)

from flask import request

mqttc = paho.Client()
mqtt_host = os.environ["mqtt-host"]
mqtt_user = os.environ["mqtt-user"]
mqtt_pwd = os.environ["mqtt-pwd"]
mqtt_port = os.environ["mqtt-port"]
print(mqtt_host)
mqttc.username_pw_set(mqtt_user, mqtt_pwd)
mqttc.connect(mqtt_host,mqtt_port)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/webhook", methods=['POST'])
def webhook():
    print(request.is_json)
    content = request.get_json()
    mqttc.publish('fb-posts-updates', content)
    print(content)
    return 'ok'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
