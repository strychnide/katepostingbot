import secrets
from uuid import uuid4

from telegram import InlineQueryResultPhoto
from telegram.ext import InlineQueryHandler
from telegram.ext.dispatcher import run_async

from . import imgur_cache, dispatcher
from .helpers.handlers import add_handler


@add_handler(dispatcher, InlineQueryHandler)
@run_async
def katepost(bot, update):
    data = imgur_cache.kb_gallery_json
    random = secrets.randbelow(len(data))

    url = f'{data[random]["link"]}'
    thumb_url = f'{url}?maxwidth=64&shape=thumb&fidelty=low'

    results = [
        InlineQueryResultPhoto(
            id=uuid4(),
            photo_url=url,
            thumb_url=thumb_url)
    ]

    update.inline_query.answer(results, cache_time=0)