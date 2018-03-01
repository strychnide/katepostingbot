import ujson

from telegram import Update

from . import dispatcher, router
from .config import config


@router.route(f'/{config["telegram_token"]}', methods=['POST'])
def webhook(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    try:
        size = int(environ.get('CONTENT_LENGTH', 0))
    except ValueError:
        size = 0
    req = environ['wsgi.input'].read(size)
    req = ujson.loads(req)

    update = Update.de_json(req, dispatcher.bot)
    dispatcher.update_queue.put(update)

    return [b'Online']