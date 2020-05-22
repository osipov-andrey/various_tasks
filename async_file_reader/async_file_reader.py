"""
Скрипт для асинхронного чтения именений текстового файла
"""

import re
import asyncio
from aiofile import AIOFile, Reader
from asyncio.queues import Queue


class MyReader(Reader):
    """
    Класс возвращает асинхронный итератор,
    который возвращает данные из текстового файла.
    Если строки закончились - не бросает StopIteration, а ждет появления новых строк.
    """
    async def __anext__(self):

        while 1:
            chunk = await self.read_chunk()
            if not chunk:
                await asyncio.sleep(.1)
                continue
            return chunk


class LogStringFactory:
    """
    Асинхронная фабрика строк.
    Собирает получаемый текст в одну строку.
    Отрезает отдельные строки по символу '\n' и кладет их в очередь.
    """
    def __init__(self, output_queue: Queue):
        self.lock = asyncio.Lock()
        self.output_queue = output_queue
        self.raw_text: str = ""

    async def load_text(self, text):
        async with self.lock:
            self.raw_text += text
            await asyncio.sleep(0)

    async def generate_string(self):
        while 1:
            new_string_border = self.raw_text.find('\n')

            if new_string_border >= 0:
                async with self.lock:
                    # new_string = self.raw_text[:new_string_border]
                    # self.raw_text = self.raw_text[new_string_border+1:]

                    new_string, self.raw_text = self.raw_text.split('\n', 1)
                    await self.output_queue.put(new_string)

            else:
                await asyncio.sleep(.1)


async def log_reader(string_factory: LogStringFactory):
    """
    Открывает текстовый файл с помощью aiofile
    """
    async with AIOFile("BatchViewLog.txt", "r") as afp:
        reader = MyReader(afp, chunk_size=50)
        async for chunk in reader:
            # print(chunk.strip())
            await string_factory.load_text(chunk)


class LogMessageChecker:
    AP_pattern = '1-frmMain.AcceptParameters - Accept Parameters Called!'

    def __init__(self, queue: Queue):
        self.queue = queue

    async def check_subscribe(self):
        while 1:
            log_message = await self.queue.get()
            if self.AP_pattern in log_message:
                print('КНОПКА НАЖАТА')


async def printer(queue: Queue):
    while 1:
        message = await queue.get()
        print(message)


if __name__ == '__main__':
    strings_queue = Queue(maxsize=15)
    factory = LogStringFactory(strings_queue)
    log_checker = LogMessageChecker(strings_queue)

    loop = asyncio.get_event_loop()
    loop.create_task(log_reader(factory))
    loop.create_task(factory.generate_string())
    loop.create_task(log_checker.check_subscribe())
    loop.run_forever()