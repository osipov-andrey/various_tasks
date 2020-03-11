import sqlite3

conn = sqlite3.connect('db.sqlite3')
conn.execute(
    """CREATE TABLE "users" (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           first_name,
           last_name,
           birthday
   )""")
conn.execute("""
        insert into users(id, first_name, last_name, birthday)
        VALUES (1, "Eugene", "Hatsko", "09-11-1992"),
               (2, "Dmitry", "Ivanov", "01-09-1993")
   """)

# определяем способ работы с строками результата
# в данном случае используем встроенный класс Row,
# аналогичный интерфейс как у dict
conn.row_factory = sqlite3.Row
users = conn.execute('SELECT * FROM "users"').fetchall()

user = users[0]
print(user.keys())
print(user['id'], user['iD'])
print(user['first_name'], user['first_NAME'], user['FIRST_NAME'])
