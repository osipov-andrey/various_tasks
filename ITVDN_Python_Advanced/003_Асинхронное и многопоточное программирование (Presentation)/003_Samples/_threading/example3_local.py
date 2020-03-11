import threading

# количсетво активных потоков
print(threading.active_count())
# текущий поток
current = threading.current_thread()
# имя текущего потока
print(current.getName())
# проверка состояния потока- жив или нет
print(current.is_alive())
# что произойдет, если попробуем еще раз его запустить
try:
    # поток может быть запущен лишь раз
    current.start()
except RuntimeError as e:
    # получаем исключение, так как основной поток итак работает
    print('ERROR: {error}'.format(error=e))
current.setName('SuperThread')
print(current.getName())

# на самом деле setName, getName - это просто старый интерфейс.
# В реальных задачах вы смело можете работаь напрямую с атрибутом name
current.name = 'SuperThread1'
print(current.name)
print(current.getName())

# вывод всех запущенных и живых трэдов
print(threading.enumerate())

# Напишем пример для демонстрации потокобезопасного хранилища данных.
thread_data = threading.local()
thread_data.value = 5


def print_results():
    """
    Выполняя данную функцию в разных потоках мы заметим, что хранилище
    действительно имеет различные значения в рамках каждого потока- отсюда и
     название потокобезопасного хранилища.
    :return:
    """
    print(threading.current_thread())
    print('Result: {}'.format(thread_data.value))


def counter(started, to_value):
    print(hasattr(thread_data, 'value'))
    thread_data.value = started
    for i in range(to_value):
        thread_data.value += 1
    print_results()


# запускаем потоки, в которых меняем значение thread_data.value
task1 = threading.Thread(target=counter, args=(0, 10), name='Task1')
task2 = threading.Thread(target=counter, args=(100, 3), name='Task2')
task1.name = 'task1'
task2.name = 'task2'

task1.start()
task2.start()

print_results()

task1.join()
task2.join()
print_results()
