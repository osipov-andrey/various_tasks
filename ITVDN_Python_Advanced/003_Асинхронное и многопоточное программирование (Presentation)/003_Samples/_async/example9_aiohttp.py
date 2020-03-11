import asyncio
import time
import aiohttp
import requests

resources = [
    'https://jsonplaceholder.typicode.com/todos/1',
    'http://example.com',
    'https://github.com',
    'https://jsonplaceholder.typicode.com/posts/1',
]


async def fetch_url(url):
    """
    Асинзронный HTTP-клиент для выполнения запросов к серверу.
    """
    async with aiohttp.request('get', url) as request:
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
    """
    Синхронная функция для выполнения запросов, она подсчитывает время,
    затраченное на выполнение всех запросов и получение ответа.
    Сравниваем асинхронный и синхронный примеры.
    """
    started = time.time()
    for url in resources:
        requests.get(url)
        print(url)
    print('Sync spent time:  {:.2f}'.format(time.time() - started))


sync_main()
event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(async_main())
