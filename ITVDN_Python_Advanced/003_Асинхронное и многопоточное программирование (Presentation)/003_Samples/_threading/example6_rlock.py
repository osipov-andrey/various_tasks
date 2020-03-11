# DEAD LOCK
import threading


def producer():
    print('Set locking')
    with lock:
        # поток, взявший блокировку может взять её бесконечное количество раз.
        # но другой поток будет ждать
        with lock:
            print("It's great")
    print('Locking release!')


# пример аналогичен example5_lock.py, но решает проблему DEAD LOCK в рамках
# одного потока.
lock = threading.RLock()

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=producer)

task1.start()
task2.start()

task1.join()
task2.join()
