"""Application Config"""
import os

MQTT_HOST = os.environ.get("mqtt-host", '')
MQTT_USER = os.environ.get("mqtt-user", '')
MQTT_PWD = os.environ.get("mqtt-pwd", '')
MQTT_PORT = int(os.environ.get("mqtt-port", ))
MQTT_FB_WEBHOOK_TOPIC_NAME = 'fb-posts-updates'
WEB_PORT = int(os.environ.get("PORT", ))
PAGE_ACCESS_TOKEN = os.environ.get("PAGE_ACCESS_TOKEN",
 "")
FB_PAGE_ID = os.environ.get("FB_PAGE_ID", "")

