import json

data = {
    'first_name': 'Eugene',
    'last_name': 'Petrov',
    'age': 35,
    'hobbies': [
        'guitar',
        'cars',
        'mountains',
        'adventures'
    ]
}

# конвертация словаря в строку формата JSON
json_data = json.dumps(data)
print(json_data)

# конвертация словаря в строку формата JSON и записью данного текста в файл.
with open('data/output.json', 'w') as f:
    # передаем словарь (что хотим сконвертировать в JSON) и файловый дескриптор
    # (куда ходим записать)
    json.dump(data, f)
