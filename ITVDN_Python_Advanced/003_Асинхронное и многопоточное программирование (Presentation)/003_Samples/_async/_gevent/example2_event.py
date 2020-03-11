import gevent
from gevent.event import Event


def waiter():
    print('I am waiting for event')
    # ожидание события с блокировкой дальнейшего исполнения кода функции
    event.wait()
    print('Waiter done')


def emitter():
    print('Emitter is sleeping')
    # засыпаем на 3 секунды
    gevent.sleep(3)
    # устанавливаем событие
    event.set()
    print('I kill endless task!')
    # останавливаем бесконечный greenlet принудилеьно
    endless_task.kill()


def endless():
    while True:
        print('Endless Task will be working forever!')
        gevent.sleep(2)


# создаем Event, который импортировали из модуля gevent.event
event = Event()

endless_task = gevent.spawn(endless)
jobs = [
    gevent.spawn(emitter),
    gevent.spawn(waiter),
    endless_task,
]


gevent.wait(jobs)
