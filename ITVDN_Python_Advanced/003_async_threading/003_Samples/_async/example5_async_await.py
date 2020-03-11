import asyncio


async def async_worker(number, divider):
    """
    вместо yield/yield from используем синтаксис async/await.
    """
    print('Worker {} started'.format(number))
    await asyncio.sleep(2)
    print(number / divider)
    return number / divider


async def gather_worker():
    # выполнение нескольких задач и получение результата от каждой из них
    # в результате выполнения мы получим список результатов в том же порядке,
    # в котором передавали сопрограммы.
    result = await asyncio.gather(
        async_worker(50, 10),
        async_worker(60, 10),
        async_worker(70, 10),
        async_worker(80, 10),
        async_worker(90, 10),
    )
    print(result)


event_loop = asyncio.get_event_loop()
task_list = [
    # async_worker(30, 10),
    # asyncio.ensure_future(async_worker(30, 10)),
    event_loop.create_task(gather_worker())
]
tasks = asyncio.wait(task_list)
event_loop.run_until_complete(tasks)
event_loop.close()
