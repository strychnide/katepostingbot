import os
import logging

import bjoern

from .helpers.bot import setup
from .helpers.router import Router
from .config import config


logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

router = Router()
bot, queue = setup(config['telegram_token'])

from . import routes


def app(environ, start_response):
    path = environ['PATH_INFO'].replace(config['base_address'], '')
    method = environ['REQUEST_METHOD']
    return router(path, method)(environ, start_response)


port = int(os.environ.get('PORT', '8443'))
bjoern.run(app, '0.0.0.0', port)
