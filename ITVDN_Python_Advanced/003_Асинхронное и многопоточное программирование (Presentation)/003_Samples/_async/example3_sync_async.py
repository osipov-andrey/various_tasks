import asyncio
from asyncio.coroutines import iscoroutine
import time


def sync_worker(number, divider):
    print('Sync Worker started with values: {} / {}'.format(number, divider))
    time.sleep(1)
    print(number / divider)


@asyncio.coroutine
def async_worker(number, divider):
    """
    Зачем писать свой декоратор, если в Python 3.5 уже он имеется в asyncio.
    """
    print('Async Worker started with values: {} / {}'.format(number, divider))
    yield from asyncio.sleep(3)
    print(number / divider)


# sync
sync_worker(30, 10)
sync_worker(30, 10)

# iscoroutine - позволяет проверить, является ли наша функция корутиной
# 1. случай - нет.
print(iscoroutine(sync_worker))
# 2. случай - да.
print(iscoroutine(async_worker(10, 2)))

# берем цикл событий и оборачиваем наши корутины в task-и для event loop
event_loop = asyncio.get_event_loop()
task_list = [
    event_loop.create_task(async_worker(30, 10)),
    event_loop.create_task(async_worker(50, 25)),
]
# создаем общую задачу, которая содержит в себе две подзадачи.
# Данная задача будет ждать завершения первых двух.
tasks = asyncio.wait(task_list)
# запускаем цикл событий до тех пор, пока не выполнятся все задачи.
event_loop.run_until_complete(tasks)
# закрываем цикл событий и программа завершается.
event_loop.close()
