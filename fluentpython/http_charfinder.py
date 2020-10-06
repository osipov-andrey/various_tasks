import sys
import asyncio
import aiohttp_cors
from aiohttp import web

from charfinder import UnicodeNameIndex


TEMPLATE_NAME = 'http_charfinder.html'
CONTENT_TYPE = 'text/html'
SAMPLE_WORDS = ('bismillah chess cat circled Malayalam digit'
                ' Roman face Ethiopic black mark symbol dot'
                ' operator Braille hexagram').split()
LINK_TPL = '/?query={0}'

LINKS_JSON = [
    {'href': LINK_TPL.format(word), 'text': word}
    for word in sorted(SAMPLE_WORDS, key=str.upper)
]

index = UnicodeNameIndex()


class GetExamples(web.View):

    async def get(self):
        return web.json_response(LINKS_JSON)


class GetChars(web.View):
    chars_cache = dict()

    async def get(self):
        url_params = self.request.query
        char_query = url_params['query']
        page = int(url_params['page'])
        page_size = int(url_params['per_page'])

        descriptions = self.chars_cache.setdefault(
            char_query,
            list(index.find_descriptions(char_query))
        )

        descriptions_page = descriptions[page * page_size - page_size: page * page_size]
        res = [descr._asdict() for descr in descriptions_page]

        print('Sending {} results'.format(len(res)))
        return web.json_response(res)


def init_app():
    app = web.Application()
    cors = aiohttp_cors.setup(app)
    resource = cors.add(app.router.add_resource('/'))
    resource2 = cors.add(app.router.add_resource('/examples'))

    cors.add(resource.add_route("GET", GetChars), {
        "*":
            aiohttp_cors.ResourceOptions(allow_credentials=True),
    })
    cors.add(resource2.add_route("GET", GetExamples), {
        "*":
            aiohttp_cors.ResourceOptions(allow_credentials=True),
    })

    return app


def main(address="127.0.0.1", port=8888):
    port = int(port)
    loop = asyncio.get_event_loop()
    app = init_app()
    web.run_app(app, host=address, port=port)

    print('Server shutting down.')
    loop.close()


if __name__ == '__main__':
    main(*sys.argv[1:])
