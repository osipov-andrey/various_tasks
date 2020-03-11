import sqlite3


# функция конвертации значения
def upper_word(raw):
    return raw.upper()


conn = sqlite3.connect(':memory:')
# регистрируем нашу функция, чтобы использовать её в SQL запросе
conn.create_function('upper1', 1, upper_word)
cur = conn.cursor()

cur.execute('CREATE TABLE users(first_name char(20))')
cur.execute(
    'INSERT INTO users(first_name) VALUES ("Eugene"),("Dmitry"),("Viktor")'
)
# тестируем нашу функцию
cur.execute('SELECT upper1(first_name) FROM users')
row = cur.fetchone()
print(row)
