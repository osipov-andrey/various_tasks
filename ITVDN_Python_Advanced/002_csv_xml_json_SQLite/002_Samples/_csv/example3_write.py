import csv

with open('data/output.csv', 'w') as f:
    # экранирование значений только по необходимости, если они содержат
    # символы, которые нарушают парсинг. Например: '"', ",", etc.
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
