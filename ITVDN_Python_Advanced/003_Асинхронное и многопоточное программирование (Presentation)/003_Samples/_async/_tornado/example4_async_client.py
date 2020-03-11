from tornado import gen
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop


@gen.coroutine
def fetch1(url):
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch(url)
    return response.body


# пример идентичен примеру fetch1, но используем async/await
async def fetch2(url):
    http_client = AsyncHTTPClient()
    response = await http_client.fetch(url)
    return response.body


# пример идентичен примеру fetch2, но используем callback-подход
@gen.coroutine
def fetch3(url):
    http_client = AsyncHTTPClient()
    fetch_future = http_client.fetch(url)
    future = gen.Future()

    def callback(f):
        result = f.result().body
        print('Done: ', future.done())
        future.set_result(result)
        print('Done: ', future.done())

    fetch_future.add_done_callback(callback)
    return (
        yield future
    )


# выполнение нескольких запросов в цикле for
@gen.coroutine
def fetch4(url):
    http_client = AsyncHTTPClient()
    responses = [
        http_client.fetch(url),
        http_client.fetch(url)
    ]
    results = []
    for i in (yield responses):
        print('-', i.body)
        results.append(i.body)
    return results


@gen.coroutine
def run_tasks():
    tasks = [
        fetch1('http://example.com'),
        fetch2('http://example.com'),
        fetch3('http://example.com'),
        fetch4('http://example.com'),
    ]
    for r in (yield gen.multi(tasks)):
        print(r)
    print('done')


IOLoop.current().run_sync(run_tasks)
