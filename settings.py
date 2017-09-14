"""Application Config"""
import os

MQTT_HOST = os.environ.get("mqtt-host", 'm21.cloudmqtt.com')
MQTT_USER = os.environ.get("mqtt-user", 'vhxoajqj')
MQTT_PWD = os.environ.get("mqtt-pwd", 'K0oIgMwjl93S')
MQTT_PORT = int(os.environ.get("mqtt-port", 13143))
MQTT_FB_WEBHOOK_TOPIC_NAME = 'fb-posts-updates'
WEB_PORT = int(os.environ.get("PORT", 5000))
PAGE_ACCESS_TOKEN = os.environ.get("PAGE_ACCESS_TOKEN",
 "EAACEdEose0cBAHCT4rmoZBdDxGB5HxyEOSGwnQkRelZAitLObpZAoZCzhu7imogQg8RGGvYUQv1ahkKQquqLA4gR0ZBZBPbnbiI6zwcwsC9FO8FSoLV44eaqb7pBtPPoQvugkiZAB8DmXeJQEsI1JZCKtK8OQgZAFCaqwCzapN8VZA7AmaISJgUfzjCdqJlxOy1uYZD")
FB_PAGE_ID = os.environ.get("FB_PAGE_ID", "1948455872076947")

