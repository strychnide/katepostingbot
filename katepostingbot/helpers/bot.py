from queue import Queue
from threading import Thread

from telegram import Bot
from telegram.ext import Dispatcher

from katepostingbot.config import config
from katepostingbot.handlers import handlers


def setup(token):
    bot = Bot(token)
    update_queue = Queue()
    # bot.set_webhook(config['webhook_address'])

    dispatcher = Dispatcher(bot, update_queue)

    handlers(dispatcher)

    thread = Thread(target=dispatcher.start, name='dispatcher')
    thread.start()

    return bot, update_queue

