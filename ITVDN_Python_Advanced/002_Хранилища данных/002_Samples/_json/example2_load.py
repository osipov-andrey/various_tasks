import json

json_data = '{"first_name": "Eugene"}'
# конвертация строки формата JSON в словарь (dict).
data = json.loads(json_data)
print(data)

with open('data/output.json', 'r') as f:
    # конвертация строки формата JSON, которая записана в файле в словарь.
    # упрощает работу с JSON файлами, чтобы не читать содержимое самому и не
    # передавать в json.loads, а выполнить эту операцию в рамках одной команды.
    data = json.load(f)
    print(data)
