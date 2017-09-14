"""Worker that register to post topic """
from services.facebook_service import FacebookService

# pylint: disable=too-few-public-methods
class Worker(object):
    """Service Worker"""

    def __init__(self, mqtt):
        self.mqtt = mqtt
        self.facebook = FacebookService()
        self.mqtt.reg(self.post_to_page)

    def post_to_page(self, msg):
        """facebook page post api"""
        self.facebook.post_to_page(msg)
