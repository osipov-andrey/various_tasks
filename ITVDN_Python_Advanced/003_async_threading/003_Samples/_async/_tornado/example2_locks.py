from tornado import gen
from tornado.ioloop import IOLoop
from tornado.locks import Event

event = Event()


async def consumer():
    print('Waiting for product')

    # ожидаем события
    await event.wait()
    print('Product was found')

    # очистка события, для нового ожидания
    event.clear()
    # ожидание повторного возникновения события
    await event.wait()
    print('Product was found twice')

    return 1


async def producer():
    print("About to set the event")

    # засыпаем на 5сек
    await gen.sleep(5)
    print('Set Event')

    # установка события
    event.set()
    # засыпаем на 5сек снова
    await gen.sleep(5)

    print('Set Event')
    # и снова устанавливаем событие
    event.set()

    return 2


async def runner():
    results = await gen.multi([
        producer(),
        consumer()
    ])
    print(results)


IOLoop.current().run_sync(runner)
