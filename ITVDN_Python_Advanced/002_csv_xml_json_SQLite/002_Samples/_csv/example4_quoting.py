import csv

# экранирование всех ячеек файла
quoting = csv.QUOTE_ALL

with open('data/output.csv', 'w') as f:
    # используем DictWriter для более удобной работы с данными
    # он позволяет работать со строками как со словарем, общаясь к значениям
    # по ключам (названием колонок)
    writer = csv.DictWriter(
        f,
        fieldnames=['first_name', 'last_name', 'age'],
        quoting=quoting
    )

    writer.writeheader()
    # запись также проихводится с использованием словарей в качестве строк
    # с данными, что является более интуитивно, нежели просто плоский список
    writer.writerow({
        'first_name': 'Ivan',
        'last_name': 'Petrov @ ll, Test',
        'age': 20
    })
    writer.writerow({
        'first_name': 'Dmitry',
        'last_name': 'Sidorov',
        'age': 30
    })
    writer.writerow({
        'first_name': 'Alexey',
        'last_name': 'Ivanov',
        'age': 30
    })
