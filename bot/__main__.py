import asyncio
import logging

from .globals import bot, loop, server

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

from . import trigger  # noqa: F401, E402, I100, I202

loop.run_until_complete(asyncio.gather(
    bot.start(),
    server.serve(),
    loop=loop
))
