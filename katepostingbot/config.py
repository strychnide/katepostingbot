import os

_imgur_token = os.environ.get('IMGUR_TOKEN')
_address = os.environ.get('ADDRESS')
_telegram_token = os.environ.get('TELEGRAM_TOKEN')

config = {
    'base_address': _address,
    'webhook_url': f'{_address}{_telegram_token}',
    'imgur_api_headers': {
        'Authorization': f'Client-ID {_imgur_token}'
    },
    'telegram_token': _telegram_token,
}