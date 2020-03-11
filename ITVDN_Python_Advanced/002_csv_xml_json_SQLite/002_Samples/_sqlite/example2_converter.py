import json
import sqlite3


# пишем свой адантер, который преобразует словарь в текст формата JSON
def adapt_json(data):
    return json.dumps(data)


# пишем свой конвертер, который преобразует текст формата JSON в словарь
# действие обратное адаптеру
def convert_json(raw):
    return json.loads(raw)


# conn = sqlite3.connect(":memory:")
# cur = conn.cursor()
#
# cur.execute('CREATE TABLE test(p json)')
# cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 1, 'ppp': 10},))
# cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 2, 'ppp': 11},))
# cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 3, 'ppp': 12},))
# cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 4, 'ppp': 13},))
# cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 5, 'ppp': 14},))
# cur.execute('SELECT * FROM test')
# row = cur.fetchone()
#
# conn.close()


# регистрируем адаптер и конвертер.
# определчем поведения для конвертации в двух направлениях
# 1. из языка Python в базу данных
# 2. из базы данных SQLite в типы данных Python (в нашем случае dict)
sqlite3.register_adapter(dict, adapt_json)
sqlite3.register_converter('json', convert_json)

# определяем базу данных в оперативной памяти
conn = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES)
cur = conn.cursor()

# создаем таблицу с нашим типом данных и пробуем вставить dict
cur.execute('CREATE TABLE test(p json)')
cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 1, 'ppp': 10},))
cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 2, 'ppp': 11},))

# берем первую запись и проверяем работу нашего адаптера и конвертера
cur.execute('SELECT * FROM test')
record = cur.fetchone()
print(type(record[0]))
