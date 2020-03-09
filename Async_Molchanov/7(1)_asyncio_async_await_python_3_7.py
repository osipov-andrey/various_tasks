# pip (pip3) install aiohttp
# Python 3.7


import asyncio


async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print("{} seconds have passed".format(count))
        count += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())

    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()
    asyncio.run(main())