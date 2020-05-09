import json
import psycopg2
from psycopg2.extras import DictCursor, NamedTupleCursor, RealDictCursor

with psycopg2.connect(database="mydb", user="andrey", password="andrey") as conn:
    cur = conn.cursor()
    # cur = conn.cursor(name='somename')
    # Специальный объект в PostgreSQL (создается командой DECLARE).
    # Может получать результаты запроса по частям и двигаться по результатам вперед-назад.

    cur.execute("SELECT * FROM city")
    data = cur.fetchall()
    print(data)

with psycopg2.connect(database="mydb", user="andrey", password="andrey") as conn:
    """ с курсором на стороне сервера """
    with conn.cursor(name='example') as cur:
        # by default: 2000
        cur.itersize = 1  # по сколько строк забирать из БД
        cur.execute("SELECT * FROM generate_series(1, 999)")

        for row in cur:
            print(row)
            break

with psycopg2.connect(database="mydb", user="andrey", password="andrey") as conn:
    """ Перемещение курсора на стороне сервера """
    with conn.cursor(name='example') as cur:
        cur.itersize = 1
        cur.execute("SELECT * FROM generate_series(1, 5)")

        print(cur.fetchall())

        # cur.scroll(1, mode='absolute')
        cur.scroll(-6)

        print(cur.fetchall())

with psycopg2.connect(database="mydb", user="andrey", password="andrey") as conn:
    """ 
    DictCursor - позволяет обращаться к контейнеру с данными 
    по индексам
    """
    with conn.cursor(cursor_factory=DictCursor) as cur:
        cur.execute("SELECT * FROM generate_series(1, 999) as col")
        row = cur.fetchone()  # {psycorg2.extras.DictRow} [1]
        print(row[0])  # {int} 1
        print(row['col'])  # {int} 1 /
        print(json.dumps(row))  # {str} '[1]'

with psycopg2.connect(database="mydb", user="andrey", password="andrey") as conn:
    """ 
    NamedTupleCursor - позволяет обращаться к контейнеру с данными 
    по названию столбцов
    """
    with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute("SELECT * FROM generate_series(1, 999) as col")
        row = cur.fetchall()  # {psycorg2.extras.DictRow} [1]
        print(row[0])  # {int} 1
        print(row[0].col)  # {int} 1 /
        print(json.dumps(row[0]))  # {str} '[1]'
