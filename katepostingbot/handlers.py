import ujson
import secrets
from uuid import uuid4

from telegram import InlineQueryResultPhoto
from telegram.ext import InlineQueryHandler
from telegram.ext.dispatcher import run_async

from .helpers.imgur import imgur_get


def handlers(dispatcher):
    dispatcher.add_handler(InlineQueryHandler(katepost))


@run_async
def katepost(bot, update):
    url = 'https://api.imgur.com/3/gallery/r/katebeckinsale/time'

    req = imgur_get(url)
    req = ujson.loads(req.text)

    data = req['data']
    random = secrets.randbelow(len(data))

    url = f'{data[random]["link"]}'
    thumb_url = f'{url}?maxwidth=64&shape=thumb'

    results = [
        InlineQueryResultPhoto(
            id=uuid4(),
            photo_url=url,
            thumb_url=thumb_url)
    ]

    update.inline_query.answer(results, cache_time=0)
