import os
import gevent
from gevent.event import Event


def reader(file_name='2_2_events.txt'):
    while True:
        print('Try to open...')
        try:
            with open(file_name, 'r', encoding='UTF-8') as file:
                content = file.read()
                print('Try to read...')
                if content.count('Wow!'):
                    print(f'File {file_name} is opened!')
                    file.close()
                    event.set()
                    break
                else:
                    gevent.sleep(5)
        except FileNotFoundError:
            gevent.sleep(5)


def deleter(file_name=r'2_2_events.txt'):
    event.wait()
    print(f'{file_name} is deleted!')
    os.remove(file_name)


event = Event()

jobs = [
    gevent.spawn(reader),
    gevent.spawn(deleter),
]

gevent.wait(jobs)