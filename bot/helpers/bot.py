from queue import Queue
from threading import Thread

from telegram import Bot
from telegram.ext import Dispatcher

from ..config import config


def setup(token):
    bot = Bot(token)
    update_queue = Queue()
    bot.set_webhook(config['webhook_url'])

    dispatcher = Dispatcher(bot, update_queue)

    thread = Thread(target=dispatcher.start, name='dispatcher')
    thread.start()

    return dispatcher
