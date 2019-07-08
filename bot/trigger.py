from ubot import Trigger
from ubot.endpoints.inline import AnswerInlineQuery, InlineQueryResultPhoto

from .globals import bot, imgur_cache


@bot.trigger
class Katepost(Trigger):
    @classmethod
    async def match(cls, update, bot):
        bot.get_type_and_flavor(update)
        return update['_type'] == 'inline_query'

    @classmethod
    async def handle(cls, update, bot):
        query_id = update['inline_query']['id']

        pic = await imgur_cache.get_pic()
        url = f'{pic["link"]}'
        thumb_url = f'{url}?maxwidth=64&shape=thumb&fidelty=low'
        result = InlineQueryResultPhoto(url, thumb_url)

        req = AnswerInlineQuery(query_id, [result]).serialize()
        await bot.api_request(req)
