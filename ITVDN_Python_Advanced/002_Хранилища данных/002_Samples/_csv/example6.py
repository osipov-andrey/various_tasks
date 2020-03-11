import csv

# создаем экземпляр класса Sniffer для дальнейшего использовании при
# сканировании структур файлов
sniffer = csv.Sniffer()
dialect = None

# попытка прочитать файл без указания конкретного диалекта, но файл содержит
# нестандартные правила, что приведт к некорректности чтения.
# Некоторые столбцы вовсе будут объеденины и данные будут прочтены неверно.
with open('data/undefined_dialect.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# попытка открыть файл и просканировать его содержимое на определение диалекта
# с помощью Sniffer.
with open('data/undefined_dialect.csv', 'r') as f:
    content = f.read()
    # можно отдавать кусок файла, не обязательно весь целиком,
    # всё зависит от размера файла и порции данных, по которой sniffer сможет
    # определить диалект.
    dialect = sniffer.sniff(content)

# выводим полученный результат, чтобы убедиться, что разделители и
# экранирование корректно вычислены
print(dialect.delimiter, dialect.doublequote, dialect.quoting)

# успешное чтение файла CSV с использованием вычисленного диалекта.
with open('data/undefined_dialect.csv', 'r') as f:
    reader = csv.reader(f, dialect=dialect)
    for row in reader:
        print(row)
