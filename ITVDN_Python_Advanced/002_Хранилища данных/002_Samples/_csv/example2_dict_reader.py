import csv

with open('data/example1.csv', 'r') as f:
    # аналогично вызову csv.reader(f)
    # но DictReader позволяем преобразовывать CSV строки в словари, для более
    # удобной работы на Python
    reader = csv.DictReader(f)
    print('Line nums', reader.line_num)
    print('Dialect', reader.dialect)
    for row in reader:
        print(row)
        # для обращения к конкретному столбцу строки используем обращение по
        # ключу `row['name'] --> row[0]`
