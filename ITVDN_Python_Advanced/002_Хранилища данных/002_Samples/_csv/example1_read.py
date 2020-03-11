import csv

with open('data/example1.csv', 'r') as f:
    # передаем в reader файловый дескриптор
    reader = csv.reader(f)
    print('Line nums', reader.line_num)
    # печатаем dialect, который отвечает за правила парсинга CSV файла.
    print('Dialect', reader.dialect)
    # запускам цикл и итерируемся по каждой строке в CSV-файле
    for row in reader:
        print(row)
