import requests

from katepostingbot.config import config


def imgur_get(url):
    req = requests.get(url, headers=config['imgur_api_headers'])
    return req
