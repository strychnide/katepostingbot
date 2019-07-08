import json

from . import env
from .globals import bot


async def app(scope, receive, send):
    assert scope['type'] == 'http'

    if scope['path'] == env.WEBHOOK_PATH and scope['method'] == 'POST':

        body = []
        more_body = True

        while more_body:
            message = await receive()
            body.append(message.get('body', b'').decode('utf-8'))
            more_body = message.get('more_body', False)

        body = ''.join(body)
        body = json.loads(body)
        bot.push_update(body)

    await send({
        'type': 'http.response.start',
        'status': 204,
        'headers': [
            [b'content-type', b'text/plain'],
        ]
    })
    await send({
        'type': 'http.response.body'
    })
