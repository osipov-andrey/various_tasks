import asyncio


@asyncio.coroutine
def test_cor(cor_index, number):
    result = 0
    for i in range(number):
        result += i
        yield from asyncio.sleep(0)
        # yield
        print('Index: {} -> {}'.format(cor_index, i))
    return result


event_loop = asyncio.get_event_loop()
tasks = asyncio.wait([
    event_loop.create_task(test_cor(1, 3)),
    event_loop.create_task(test_cor(2, 4))
])
event_loop.run_until_complete(tasks)
event_loop.close()
