import csv


class CustomDialect(csv.Dialect):
    """
    Создание собственно диалекта, который позволяет нам описать правила для
    чтения и записи файла.
    Удобный механизм, если вы используете собственные правила обработки CSV,
    которые можно сгруппировать в диалект.
    """
    quoting = csv.QUOTE_ALL
    quotechar = "*"
    delimiter = "!"
    lineterminator = '\n'


# регистрация диалекта, чтобы он был доступен во время создания reader/writer.
csv.register_dialect('tester', CustomDialect)

with open('data/output.csv', 'w') as f:
    # два варианта передачи диалекта
    # 2. передача класса диалекта
    # writer = csv.writer(f, dialect=CustomDialect)
    # 2. передача имени диалекта, который ма заранее зарегистрировали с этим
    # же именем.
    writer = csv.writer(f, dialect='tester')
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
