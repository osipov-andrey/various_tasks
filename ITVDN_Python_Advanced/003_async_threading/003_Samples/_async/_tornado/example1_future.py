from tornado import gen
from tornado.ioloop import IOLoop

# создание фУтура
future = gen.Future()
future = gen.Task()


async def consumer():
    print('Waiting for boss')
    # дожидаемся результата от future, без блокировки потока
    product = await future
    print('Product was found: {}'.format(product))


async def producer():
    print('Produces is boss, please wait when boss will get up')
    # засыпаем на 5сек, после чего устанавливаем результат нашему футуру
    # после установки результата, consumer продолжит выполнение
    await gen.sleep(5)
    future.set_result({
        'id': 10,
        'name': 'Mobile Phone'
    })


async def run_tasks():
    await gen.multi([
        producer(),
        consumer()
    ])


IOLoop.current().run_sync(run_tasks)
