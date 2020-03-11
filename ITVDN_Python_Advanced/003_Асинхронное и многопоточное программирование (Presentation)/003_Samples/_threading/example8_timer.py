import os
import threading


def exec_watcher():
    # запускаем функцию print_files каждые 5 секунд в отдельном потоке
    timer = threading.Timer(5.0, print_files)
    timer.start()


def print_files():
    for i in os.listdir('.'):
        print(i)
    exec_watcher()


exec_watcher()
