"""FB Service Module"""
import settings as Config
import facebook

# pylint: disable=too-few-public-methods
class FacebookService(object):
    """FB Service"""

    def __init__(self):
        self.graph = facebook.GraphAPI(Config.PAGE_ACCESS_TOKEN)

    def post_to_page(self, msg):
        """facebook page post api"""
        self.graph.put_object(Config.FB_PAGE_ID, "feed", message=msg)
