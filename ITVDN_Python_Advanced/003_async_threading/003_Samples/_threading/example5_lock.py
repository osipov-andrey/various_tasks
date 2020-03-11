# DEAD LOCK
import threading


def producer():
    print('Set locking')
    # берем блокировку
    with lock:
        print('done')
        # попытка взять блокировку в рамках текущего потока дает нам DEAD LOCK
        # Из данной блокировки накак не выйти, так как мы ожидаем завершения
        # самого себя, чтобы взять блокировку- блокировка никогда не
        # освободится.
        # Актуально даже в рамках одного потока
        with lock:
            print("It's great")
    print('Locking release!')


# блокировка, позволяющая отметитьк акой участок кода атомарным.
lock = threading.Lock()
# __enter__ => lock.acquire()
# __exit__ => lock.release()

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=producer)

task1.start()
task2.start()

task1.join()
task2.join()
