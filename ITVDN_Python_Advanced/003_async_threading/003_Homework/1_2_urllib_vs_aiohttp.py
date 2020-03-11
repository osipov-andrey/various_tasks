import urllib.request
import aiohttp
import logging


logging.basicConfig(filename='urllib.log', level=logging.INFO)
logger = logging.getLogger('urllib_logger')

resources = [
    'https://jsonplaceholder.typicode.com/todos/1',
    # 'http://example.com',
    # 'https://github.com',
    # 'https://jsonplaceholder.typicode.com/posts/1',
]

for url in resources:
    logger.info('GET')
    resp = urllib.request.urlopen(url)
    code = str(resp.getcode())
    logger.info(code)