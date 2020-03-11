import urllib.request
import aiohttp
import asyncio
import logging
import time

logger_sync = logging.getLogger('urllib_logger')
logger_sync.setLevel(logging.INFO)
fh_sync = logging.FileHandler("1_2_urllib_log.log")
form_sync = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh_sync.setFormatter(form_sync)
logger_sync.addHandler(fh_sync)

resources = [
    'https://jsonplaceholder.typicode.com/todos/1',
    'http://example.com',
    'https://github.com',
    'https://jsonplaceholder.typicode.com/posts/1',
]

logger_async = logging.getLogger('aiohttp_logger')
logger_async.setLevel(logging.INFO)
fh_async = logging.FileHandler("1_2_aiohttp_log.log")
form_async = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh_async.setFormatter(form_async)
logger_async.addHandler(fh_async)


async def fetch_url(url):
    """
    Асинзронный HTTP-клиент для выполнения запросов к серверу.
    """
    logger_async.info(f'Start request to {url}')

    async with aiohttp.request('get', url) as request:
        logger_async.info(f'Takes request with status {request.status}')

        return url, await request.text()



async def async_main():
    """
    Асинхронная корутина для выполнения запросов, она генерирует список корутин
    и выоплняет fetch_url.
    """
    tasks = [
        asyncio.ensure_future(fetch_url(url))
        for url in resources
    ]

    started = time.time()

    for future in asyncio.as_completed(tasks):
        url, _ = await future
        print(url)

    print('Async spent time: {:.2f}'.format(time.time() - started))


def sync_main():

    started = time.time()

    for url in resources:
        # начало запроса
        logger_sync.info(f'Start request to {url}')

        resp = urllib.request.urlopen(url)
        code = str(resp.getcode())

        # конец запроса со статусом 200
        logger_sync.info(f'Takes request with status {code}')

    print('Sync spent time:  {:.2f}'.format(time.time() - started))


sync_main()
event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(async_main())