import threading
import time


def handler(started=0, finished=0):
    result = 0
    for i in range(started, finished):
        result += i
    print('Value: ', result)


params = {'finished': 2 ** 26}

# предварительное создание потока, который будет выполнять функцию handler,
# с ключевыми аргументами params.
task = threading.Thread(target=handler, kwargs=params)
started_at = time.time()
print('RESULTS 1')
# запускаем поток на выполнение
task.start()
# присоединяем поток к текущему- то есть мы как бы синхронизируем второй поток,
# дожидаясь от него результата
task.join()
print('Time: {}'.format(time.time() - started_at))

started_at = time.time()
print('RESULTS 2')
handler(**params)
print('Time: {}'.format(time.time() - started_at))
