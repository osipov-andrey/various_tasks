import psycopg2
from psycopg2 import errors

# with psycopg2.connect(database="mydb", user="andrey", password="andrey") as conn:
#     with conn.cursor() as cur:
#         #  1st transaction
#         cur.execute(
#             "CREATE TABLE users(id SERIAL PRIMARY KEY, name TEXT)"
#         )
#         conn.commit()
#         #  2nd transaction
#         cur.execute("INSERT INTO users(name) VALUES ('Elon Musk')")
#         conn.commit()

"""
Как сделать контекстный менеджер для транзакций:
"""

from psycopg2.extensions import STATUS_IN_TRANSACTION


class TransactionCtx:
    def __init__(self, connection):
        self.conn = connection

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Коммит, если была открыта транзакция и не было исключений
        в контексте
        """
        if self.conn.status == STATUS_IN_TRANSACTION:
            if exc_val:
                self.conn.rollback()  # Откат тразакции
            else:
                self.conn.commit()


# with psycopg2.connect(database="mydb", user="andrey", password="andrey") as conn:
#     with TransactionCtx(conn) as transaction:
#         with conn.cursor() as cur:
#             cur.execute('SELECT 1')
#             raise RuntimeError

"""
Точки сохранения в транзакциях.
SAVEPOINT позволяет откатить все команды, выполненные после неё,
и восстановить состояние на момент устанвоки этой точки
"""

# with psycopg2.connect(database="mydb", user="andrey", password="andrey") as conn:
#     with conn.cursor() as cur:
#         cur.execute("CREATE TABLE users(id ...)")
#         cur.execute("SAVEPOINT sp1")
#
#         try:
#             cur.execute("CREATE TABLE users(id ...)")
#         except psycopg2.errors.DatabaseError:
#             cur.execute("ROLLBACK TO SAVEPOINT sp1")
#
#         conn.commit()

"""
RETURNING
Позволяет получать данные из модифицируемых строк в 
процессе их обработки в запросах   INSERT, UPDATE, DELETE
"""

# query = "INSERT INTO users(name) VALUES ('John Silver') RETURNING users.*"
#
# with psycopg2.connect(database="mydb", user="andrey", password="andrey") as conn:
#     with conn.cursor() as cur:
#         cur.execute(query)
#         row = cur.fetchone()
#         print(row)
#         conn.commit()

"""
Возвращает весь набор измененных данных
"""

# query = "DELETE FROM users RETURNING users.*"
#
# with psycopg2.connect(database="mydb", user="andrey", password="andrey") as conn:
#     with conn.cursor() as cur:
#         cur.execute(query)
#         row = cur.fetchall()
#         print(row)
#         conn.commit()

"""
UPSERT: update or insert
можно совместить с RETURNING
"""

# with psycopg2.connect(database="mydb", user="andrey", password="andrey") as conn:
#     with conn.cursor() as cur:
#         cur.execute("""
#             CREATE TABLE domains(
#                 id SERIAL PRIMARY KEY, name TEXT UNIQUE, owner TEXT
#             )
#         """)
#         conn.commit()
#         cur.execute("""
#             INSERT INTO domains (name, owner) VALUES
#             ('example.com', 'John Travolta')
#         """)
#         cur.execute("""
#             INSERT INTO domains (name, owner) VALUES
#             ('example.com', 'Angelina Jolie')
#             ON CONFLICT (name) DO UPDATE SET owner = EXCLUDED.owner
#             RETURNING domains.*
#         """)
#
#         row = cur.fetchone()
#         print(row)
#         conn.commit()

"""
SELECT FOR UPDATE
Блокирует выбранные строки для изменения другими транзакицями,
до завершения текущей
"""

with psycopg2.connect(database="mydb", user="andrey", password="andrey") as conn:
    with conn.cursor() as cur:
        cur.execute(
            "SELECT * FROM domains WHERE name = %s FOR UPDATE",
            ('example.com',)
        )

        domain_id, name, *_ = cur.fetchone()
        print(domain_id, name)

        cur.execute(
            """
            UPDATE domains SET owner = %(owner)s
            WHERE id = %(domain_id)s
            """,
            {
                'owner': 'New Company Inc',
                'domain_id': domain_id
            }
        )
        conn.commit()