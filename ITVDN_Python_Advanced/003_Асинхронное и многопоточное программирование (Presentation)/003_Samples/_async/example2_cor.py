import functools


def is_divider(number):
    print("Coroutine started")
    while True:
        # принимаем значение в сопрограмму через yield
        value = yield
        if number % value == 0:
            print(value)


# создание корутины
cor = is_divider(100)
# запуск корутины и выполнение вычислений в теле while
# программа останавливается на yield
cor.send(None)
# передаем число для вычислений одной итерации, для присвоения value
cor.send(11)
cor.send(18)
cor.send(20)
# закрывает корутину
cor.close()


def coroutine(func):
    """
    Декоратор для автоматического запуска корутины, чтобы не выполнять
    cor.send(None).
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        # запускаем и возвращаем корутину
        res.send(None)
        return res

    return wrapper


@coroutine
def is_divider_cor(number):
    print("Coroutine started")
    while True:
        value = yield
        if number % value == 0:
            print(value)


cor = is_divider_cor(100)
# нет необходимости делать шаг `cor.send(None)`, так как он описан в декораторе
cor.send(10)
cor.send(10)
cor.send(10)
cor.close()
