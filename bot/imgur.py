import json
from random import choice
from time import time
from urllib.request import Request, urlopen

from . import env


class ImgurCache:
    def __init__(self, loop, refresh_time=900):
        self.gallery = None
        self.refresh_time = refresh_time
        self.last_refresh = time()
        self.loop = loop

        loop.create_task(self.update_gallery())

    async def update_gallery(self):
        req = Request('https://api.imgur.com/3/gallery/r/katebeckinsale/time', headers={
            'Authorization': f'Client-ID {env.IMGUR_TOKEN}'
        })

        res = await self.loop.run_in_executor(None, urlopen, req)
        res = res.read().decode('utf-8')
        res = json.loads(res)

        self.gallery = res['data']

    async def get_pic(self):
        now = time()
        delta = now - self.last_refresh
        if delta > self.refresh_time:
            await self.update_gallery()
            self.last_refresh = now

        return choice(self.gallery)
