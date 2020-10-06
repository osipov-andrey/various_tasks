import sys
import asyncio
from aiohttp import web

from charfinder import UnicodeNameIndex


TEMPLATE_NAME = 'http_charfinder.html'
CONTENT_TYPE = 'text/html'
SAMPLE_WORDS = ('bismillah chess cat circled Malayalam digit'
                ' Roman face Ethiopic black mark symbol dot'
                ' operator Braille hexagram').split()

ROW_TPL = '<tr><td>{code_str}</td><th>{char}</th><td>{name}</td></tr>'
LINK_TPL = '<a href="/?query={0}" title="find &quot;{0}&quot;">{0}</a>'
LINKS_HTML = ', '.join(LINK_TPL.format(word) for word in
                       sorted(SAMPLE_WORDS, key=str.upper))


index = UnicodeNameIndex()
with open(TEMPLATE_NAME) as tpl:
    template = tpl.read()
template = template.replace('{links}', LINKS_HTML)


# BEGIN HTTP_CHARFINDER_HOME
def home(request):  # <1>
    try:
        query = request.query['query']  # <2>
        print('Query: {!r}'.format(query))  # <3>
        descriptions = list(index.find_descriptions(query))
        res = '\n'.join(ROW_TPL.format(**descr._asdict())
                        for descr in descriptions)
        msg = index.status(query, len(descriptions))
    except KeyError:
        query = ''
        descriptions = []
        res = ''
        msg = 'Enter words describing characters.'

    html = template.format(query=query, result=res,  # <5>
                           message=msg)
    print('Sending {} results'.format(len(descriptions)))  # <6>
    return web.Response(content_type=CONTENT_TYPE, text=html) # <7>
# END HTTP_CHARFINDER_HOME


def init_app():
    app = web.Application()
    app.router.add_route('GET', '/', home)
    return app


def main(address="127.0.0.1", port=8888):
    port = int(port)
    loop = asyncio.get_event_loop()
    app = init_app()
    web.run_app(app, host=address, port=port)

    print('Server shutting down.')
    loop.close()  # <9>


if __name__ == '__main__':
    main(*sys.argv[1:])
# END HTTP_CHARFINDER_SETUP