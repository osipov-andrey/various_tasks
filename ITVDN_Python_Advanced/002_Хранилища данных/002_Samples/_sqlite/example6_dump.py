import os
import sqlite3

conn = sqlite3.connect(':memory:')
conn.execute(
    """CREATE TABLE "users" (
           id INTEGER PRIMARY KEY,
           first_name VARCHAR(30) NOT NULL,
           last_name VARCHAR(30),
           birthday VARCHAR(30)
   )""")
conn.execute("""
        INSERT INTO users(id, first_name, last_name, birthday)
        VALUES (1, "Eugene", "Hatsko", "09-11-1992"),
               (2, "Dmitry", "Ivanov", "01-09-1993")
   """)

with open('dump.sql', 'w') as f:
    # собираем дамп и сохраняем в файл- чистый SQL код.
    for line in conn.iterdump():
        f.write('%s\n' % line)
        print('{}\n'.format(line))
