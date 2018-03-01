import os

_url = os.environ.get('URL')  # url of the application
_telegram_token = os.environ.get('TELEGRAM_TOKEN')  # telegram token
_imgur_token = os.environ.get('IMGUR_TOKEN')  # client id assigned by imgur

config = {
    'webhook_url': f'{_url}{_telegram_token}',
    'imgur_api_headers': {
        'Authorization': f'Client-ID {_imgur_token}'
    },
    'telegram_token': _telegram_token
}