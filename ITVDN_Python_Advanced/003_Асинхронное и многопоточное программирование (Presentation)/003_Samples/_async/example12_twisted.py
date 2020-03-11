from twisted.internet import reactor, defer


def resolve_deferred(deff, value):
    """
    Функция аналогична примеру example6_event_loop.py, где мы создавали футур,
    ожидая результата в одной корутине, а устанавливали ему результат в
    другой.
    """
    try:
        # callback аналогичен set_result
        deff.callback(value)
    except Exception as e:
        deff.errback(e)


def make_data(raw, timeout):
    print('make data called')
    # Используя фреймворк twisted, создаем deferred, он аналогичен Future.
    deferred = defer.Deferred()  # Future()
    # добавляем в цикл событий задачи к выполнению
    reactor.callLater(
        timeout,
        resolve_deferred,
        deferred,
        raw
    )  # Future.set_result
    return deferred


def pipe_1(result):
    print('Logging value: {}'.format(result))
    return result


def pipe_2(result):
    return result + 10


def pipe_3(result):
    return result * 2


def pipe_4(result):
    return 100 / result


def error_1(e):
    print('Error: {}'.format(e))


deferred = make_data(40, 2)
deferred.addCallback(pipe_1)
deferred.addCallback(pipe_2)
deferred.addCallback(pipe_1)
deferred.addCallback(pipe_3)
deferred.addCallback(pipe_1)
deferred.addCallback(pipe_4)
deferred.addCallbacks(pipe_1, error_1)

deferred = make_data(-10, 2)
deferred.addCallback(pipe_1)
deferred.addCallback(pipe_2)
deferred.addCallback(pipe_1)
deferred.addCallback(pipe_3)
deferred.addCallback(pipe_1)
deferred.addCallback(pipe_4)
deferred.addCallbacks(pipe_1, error_1)

# добавляем задачи остановки цикла событий через 4 сек.
reactor.callLater(4, reactor.stop)

print('Reactor is starting.')
# запускаем цикл событий
reactor.run()
print('Reactor is stopped.')
