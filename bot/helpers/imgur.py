from datetime import datetime

import ujson
import requests

from ..config import config


def imgur_get(url):
    req = requests.get(url, headers=config['imgur_api_headers'])
    return req


class ImgurCache():
    def __init__(self, refresh_time=900):
        self.gallery_json = None
        self.refresh_time = refresh_time
        self.last_refresh = datetime.now()
        self.update_gallery()

    def update_gallery(self):
        url = 'https://api.imgur.com/3/gallery/r/katebeckinsale/time'

        req = imgur_get(url)
        req = ujson.loads(req.text)

        self.gallery_json = req['data']

    def get_gallery_json(self):
        now = datetime.now()
        delta = now - self.last_refresh
        if delta.total_seconds() > self.refresh_time:
            self.update_gallery()
            self.last_refresh = now

        return self.gallery_json
