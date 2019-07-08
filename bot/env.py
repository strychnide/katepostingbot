import hashlib
from os import environ


TELEGRAM_TOKEN = environ['TELEGRAM_TOKEN']
URL = environ['URL']
IMGUR_TOKEN = environ['IMGUR_TOKEN']
PORT = environ['PORT']

WEBHOOK_PATH = f'/{hashlib.sha256(TELEGRAM_TOKEN.encode()).hexdigest()}'
WEBHOOK_URL = f'{URL}{WEBHOOK_PATH}'
