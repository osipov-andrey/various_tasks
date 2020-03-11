import threading
import time


def producer():
    time.sleep(10)
    print('Product found!')
    # устанавливаем событий
    product.set()
    # очищаем событие
    product.clear()


def consumer():
    print('product wait')
    # ожидаем события ровно столько, пока не вызовется product.set в любом из
    # потоков
    product.wait()
    print('Product exists!')


# создаем событие, которое будем использовать в потока- ожидать и устанавливать
# создадим блокировку потока до появления события product
product = threading.Event()

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=consumer)

task1.start()
task2.start()

task1.join()
task2.join()
