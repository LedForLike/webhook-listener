"""Application Config"""
import os


MQTT_HOST = os.environ.get("mqtt-host", '')
MQTT_USER = os.environ.get("mqtt-user", '')
MQTT_PWD = os.environ.get("mqtt-pwd", '')
MQTT_PORT = int(os.environ.get("mqtt-port", 5001))
MQTT_FB_WEBHOOK_TOPIC_NAME = 'fb-posts-updates'
