import gevent


def task():
    print('Gevent sleep')
    gevent.sleep(1)
    print('Gevent finished')


# помещаем функцию в гринлеты
jobs = [
    gevent.spawn(task),
    gevent.spawn(task),
    gevent.spawn(task)
]

# блокируем дальнейшую работу программы и дожидаемся выполнения всех гринлетов
gevent.joinall(jobs)
