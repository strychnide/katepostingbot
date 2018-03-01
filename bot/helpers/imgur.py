import threading

import ujson
import requests

from ..config import config
from .threading import ThreadJob


def imgur_get(url):
    req = requests.get(url, headers=config['imgur_api_headers'])
    return req


class ImgurCache():
    def __init__(self, refresh_time=900):
        self.kb_gallery_json = None
        self.get_gallery()

        event = threading.Event()
        update_gallery = ThreadJob(self.get_gallery, event, refresh_time)
        update_gallery.start()

    def get_gallery(self):
        url = 'https://api.imgur.com/3/gallery/r/katebeckinsale/time'

        req = imgur_get(url)
        req = ujson.loads(req.text)

        self.kb_gallery_json = req['data']
