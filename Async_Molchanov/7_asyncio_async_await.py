# pip (pip3) install aiohttp
# Python 3.4

# План:
# 1. Asyncio фреймворк для создания событийных циклов
# 2. Пример простой асинхронной программы времен Python 3.4
# 3. Синтаксис Async/await на замену @asyncio.coroutine, yield from
# 4. Пример асинхронного скачивания файлов

import asyncio


@asyncio.coroutine
def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        yield from asyncio.sleep(1)


@asyncio.coroutine
def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print("{} seconds have passed".format(count))
        count += 1
        yield from asyncio.sleep(1)


@asyncio.coroutine
def main():
    task1 = asyncio.ensure_future(print_nums())
    task2 = asyncio.ensure_future(print_time())

    yield from asyncio.gather(task1, task2)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()