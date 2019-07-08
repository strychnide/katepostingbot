import asyncio

from ubot import Bot

import uvicorn

from . import env
from .imgur import ImgurCache

loop = asyncio.new_event_loop()
bot = Bot(env.TELEGRAM_TOKEN, loop=loop)
imgur_cache = ImgurCache(loop=loop)

from .server import app  # noqa: E402, I202

server = uvicorn.Server(uvicorn.Config(
    app=app, host='0.0.0.0', port=int(env.PORT), workers=1, loop='asyncio', http='h11'))
