import datetime
import json


class DateFormatEncoder(json.JSONEncoder):
    """
    Описываем класс для конвертации даты и времени в формат JSON,
    здесь используется свой собственный формат вида:
    {
        "value": "01/02/1990 12:57:31",
        "__date__": true
    }
    """

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return {
                'value': obj.strftime('%d/%m/%Y %H:%M:%S'),
                '__datetime__': True
            }
        elif isinstance(obj, datetime.date):
            return {
                'value': obj.strftime('%d/%m/%Y'),
                '__date__': True
            }
        # вызываем стандартную конвертацию, если obj не date или datetime
        return json.JSONEncoder.default(self, obj)


data = {
    'first_name': 'Eugene',
    'last_name': 'Petrov',
    'birthday': datetime.date(1986, 9, 29),
    'hired_at': datetime.datetime(2006, 9, 29, 12, 30, 5),
    'hobbies': [
        'guitar',
        'cars',
        'mountains',
        'adventures'
    ]
}

# используем ключевой аргумент `cls` со значением нашего класса.
# indent=4 - используется 4 пробела для форматирование JSON
json_data = json.dumps(data, cls=DateFormatEncoder, indent=4)
print(json_data)

with open('data/output.json', 'w') as f:
    json.dump(data, f, cls=DateFormatEncoder)


def as_date_datetime(dct):
    """
    Функция для обратной конвертации date и datetime из JSON во внутренние
    типы Python.

    {
        "value": "01/02/1990 12:57:31",
        "__date__": true
    }
    to datetime(1990, 2, 1, 12, 57, 31)

    и

    {
        "value": "01/02/1990",
        "__date__": true
    }
    to date(1990, 2, 1)
    """
    print(dct)
    if '__datetime__' in dct:
        return datetime.datetime.strptime(dct['value'], '%d/%m/%Y %H:%M:%S')
    if '__date__' in dct:
        return datetime.datetime.strptime(dct['value'], '%d/%m/%Y').date()
    return dct


with open('data/output.json', 'r') as f:
    # используем ключевой аргумент object_hook для передачи нашей функции
    data = json.load(f, object_hook=as_date_datetime)
    print(data)
