import hashlib
from concurrent.futures import ThreadPoolExecutor

import tornado.ioloop
import tornado.web
import tornado.gen

# создаем pool из 5 потоков
pool = ThreadPoolExecutor(5)


def sync_highload_task(password):
    """
    Синхронная нагруженная, блокирующая функция
    """
    for i in range(9876565):
        password = hashlib.sha256(password).hexdigest().encode()
    return password


@tornado.gen.coroutine
def make_password(password) -> str:
    # отправляем в отдельный потом и ждем результата
    hashed_password = yield pool.submit(
        sync_highload_task,
        password.encode()
    )
    return hashed_password


class IndexHandler(tornado.web.RequestHandler):
    """
    Пример обработчика HTTP запроса.
    """

    @tornado.gen.coroutine
    def get(self):
        """
        Отмечаем наш обработчик как корутину, что позволит нам
        использовать yield.
        """
        value = self.get_query_argument('password', '')
        if value:
            # хэшируем пароль и дожидаемся ответа
            hashed_password = yield make_password(value)
            self.write('<h1>Hashed password: {}</h1>'.format(
                hashed_password.decode())
            )
        self.write(
            '<form>'
            '<input type="text" name="password" placeholder="Password"/>'
            '<input type="submit"/>'
            '</form>'
        )


def make_app():
    """
    Создаем приложение с urls, autoreload позволит перезгружать сервер
    по любому изменению файла.
    """
    url_handlers = [
        tornado.web.URLSpec(r'^/$', IndexHandler, name='index'),
    ]
    return tornado.web.Application(
        url_handlers,
        autoreload=True
    )


if __name__ == '__main__':
    app = make_app()
    # прослушиваем порт 8888
    app.listen(8888)
    print('started')
    tornado.ioloop.IOLoop.current().start()
