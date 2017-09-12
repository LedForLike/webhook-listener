"""Main entry point"""

import logging
import settings as Config
from web.server import Server

logging.basicConfig(level=logging.DEBUG)

# pylint: disable=invalid-name
server = Server()
if __name__ == '__main__':
    server.app.run(host='0.0.0.0', port=Config.WEB_PORT)
