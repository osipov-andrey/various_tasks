import hashlib
from concurrent.futures import ThreadPoolExecutor

import tornado.gen
from tornado.ioloop import IOLoop
from tornado.process import cpu_count

# создаем pool потоков для вычислений, можно указать люое количество
pool = ThreadPoolExecutor(cpu_count())


def sync_highload_task(password):
    for i in range(100_000):
        password = hashlib.sha256(password).hexdigest().encode()
    return password

# используя декоратор, помечаем нашу функцию как корутину
@tornado.gen.coroutine
def make_password(password) -> str:
    # ожидаем результата из pool-а потоков и переключаемся на другую
    # до тех пор, пока не получим результат
    hashed_password = yield pool.submit(
        sync_highload_task,
        password.encode()
    )
    return hashed_password


@tornado.gen.coroutine
def test_cor():
    for i in range(1, 10):
        print('Sleep on {}'.format(i))
        # мы засыпаем и переключаемся на другую сопрограмму
        yield tornado.gen.sleep(i)
    return 2


@tornado.gen.coroutine
def multi():
    # ожидаем выполнения нескольких корутин с помощью gen.multi
    result = yield tornado.gen.multi([
        test_cor(),
        make_password('test_pass')
    ])
    print(result)


# запуск корутин в цикле событий - event loop
IOLoop.current().run_sync(multi)
