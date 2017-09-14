"""Main entry point"""

import logging
import settings as Config 
from web.server import Server
from services.worker import Worker
from services.mqtt_client import MqttClient

logging.basicConfig(level=logging.DEBUG)

# pylint: disable=invalid-name
mqttc = MqttClient()
server = Server(mqttc)
worker = Worker(mqttc)
if __name__ == '__main__':
    server.app.run(host='0.0.0.0', port=Config.WEB_PORT)
