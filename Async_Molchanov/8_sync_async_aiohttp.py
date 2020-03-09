import asyncio
import aiohttp
import requests
from time import time


def get_file(url):
    r = requests.get(url, allow_redirects=True)
    return r


def write_file(response):
    # https://loremflickr.com/cache/resized/65535_48847813606_da2a5de6bb_z_320_240_nofilter.jpg
    filename = response.url.split('/')[-1]
    with open(filename, 'wb') as file:
        file.write(response.content)


def main():
    url = 'https://loremflickr.com/320/240'

    t0 = time()

    for i in range(10):
        write_file(get_file(url))

    print(time() - t0)


# if __name__ == '__main__':
#     main()

####################### ASYNC #################################
def write_image(data, filename):
    # Синхронный код может заблокировать поток программы. Поэтому смешивать синхронный и асинхронный код - плохо.
    # https://loremflickr.com/cache/resized/65535_48847813606_da2a5de6bb_z_320_240_nofilter.jpg
    # filename = 'file-{}.jpeg'.format(int(time() * 1000))
    with open(filename, 'wb') as file:
        file.write(data)


async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        filename = response.url.parts[-1]
        write_image(data, filename)


async def async_main():
    url = 'https://loremflickr.com/320/240'
    tasks = []

    t0 = time()

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)
    print(time() - t0)


if __name__ == '__main__':
    main()
    asyncio.run(async_main())