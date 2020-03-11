import sqlite3


class RowSet:
    """
    Класс для реализации функционала собственной агрегационной функции.

    Пример:
        id, first_name, last_name
        1, f1, l1
        2, f2, l2
        3, f3, l3
        4, f4, l4
        5, f5, l5

    Запрос:
        SELECT row_set(first_name) AS result FROM users;

    Результат:
        f1;f2;f3;f4;f5
    """

    def __init__(self):
        # инициализируем контейнер
        self.rows = set()

    def step(self, value):
        # добавляем элемент в контейнер
        self.rows.add(value)

    def finalize(self):
        # завершение агрегации
        return ';'.join(self.rows)


conn = sqlite3.connect(':memory:')
# регистрируем наш класс для работы с нашей агрегационой функцией
conn.create_aggregate('row_set', 1, RowSet)

cur = conn.cursor()
cur.execute('CREATE TABLE users(first_name)')
cur.execute(
    """INSERT INTO users(first_name)
       VALUES ("Dmitry"),
              ("Eugene"),
              ("Viktor"),
              ("Nikita"),
              ("Eugene")
     """
)

# пробуем запуск агрегации по полю first_name- реультат будет конкатенация
# всех first_name в таблица
cur.execute('SELECT row_set(first_name) AS result FROM users')
results = cur.fetchall()
print(dict())
