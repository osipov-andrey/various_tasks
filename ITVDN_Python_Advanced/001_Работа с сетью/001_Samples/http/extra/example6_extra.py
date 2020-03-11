import json

import requests
from requests.adapters import HTTPAdapter

HOST = '127.0.0.1:8000'


def get_url(path):
    return 'http://{host}{path}'.format(host=HOST, path=path)


issues_url = get_url('/api/issues/')
login_url = get_url('/api/auth/login/')
logout_url = get_url('/api/auth/logout/')


def issue_url(pk):
    return get_url('/api/issues/{id}/'.format(id=pk))


# get issues (error)
# запрашиваем http://127.0.0.1:8000/api/issues/ как неавторизованный
# пользователь
response = requests.get(issues_url)
print(response.status_code)
# `response.json()` - преобразует формат JSON в словарь.
print(response.json())

# попытка авторизоваться, используя уже имеющиеся login/password
# test_user/test_pass уже созданы, поэтому мы можем их использовать.
data = {'username': 'test_user', 'password': 'test_pass'}
headers = {'Content-Type': 'application/json'}
# выполняем запрос и проверяем ответ- мы авторизованы, в случае корректных
# username, password
response = requests.post(login_url, data=json.dumps(data), headers=headers)
print(response.status_code)
print(response.json())

# копируем cookies из ответа.
# сервер использует cookies для хранения `sessionid`, который также хранится
# на сервере. С помощью данной cookie сервер может определить, авторизован ли
# пользователь с данным `sessionid`.
# `sessionid` становится авторизованным после обращения к `login_url`.
cookies = response.cookies

# передаем cookies в последующие запросы, чтобы сервер воспринимал нас как
# пользователя `test_user`.
response = requests.get(issues_url, cookies=cookies)
print(response.status_code)
print(response.json())

# попытка создать новую заметку на сервере с пустым телом запроса, используя
# POST запрос с авторизованным `sessionid` в cookies.
response = requests.post(issues_url, cookies=cookies)
# Так как мы не передаем данных для создания заметки (name, description,
# due_date), то сервер вернет статус 400 и не создаст заметку.
print(response.status_code)
print(response.json())

# подготавливаем данные для отправки на сервер
issue_data = {'name': 'Buy Python Book',
              'due_date': '2009-02-11',
              'description': 'We have to buy a Python book!!!'}

# создаем заметку на сервере.
response = requests.post(issues_url, data=json.dumps(issue_data),
                         headers=headers, cookies=cookies)
# собираем данные из ответа сервера в dict, использую метод `resp.json()`
created_issue = response.json()
print(response.status_code)
print(created_issue)

# обновление имени заметки, без изменения других полей, используем меод PATCH
new_data = {'name': 'Fixed name'}
response = requests.patch(issue_url(created_issue['id']),
                          data=json.dumps(new_data), headers=headers,
                          cookies=cookies)
print(response.status_code)
print(response.json())

# удаление заметки с сервера по её `id`.
response = requests.delete(issue_url(created_issue['id']), cookies=cookies)
print(response.status_code)
# print(response.json())

# SESSION EXAMPLE
# Для более простой схемы работы и без постоянной передачи cookies используем
# механизм сессия в библиотеке requests.
# cookies автоматически будут прокидываться при каждом запросе.

# авторизуемся и пытаемся проделать всё те же действия, но с request.Session.
data = {'username': 'test_user', 'password': 'test_pass'}
headers = {'Content-Type': 'application/json'}
# создаем экземпляр `Session`
session = requests.Session()

response = session.post(login_url, data=json.dumps(data), headers=headers)
print(response.status_code)
print(response.json())

# мы всё также можем взять cookies из сессии (сделаем это для примера)
cookies = response.cookies

# выполняем те же дейсвия, но в рамках сессии.
# Сессия будет хранить в себе cookies и обновлять их, если сервер их изменит.
# а при каждом запросе в рамках экземпляра Session cookies будут передаваться
# автоматически.

# получаем список заметок
response = session.get(issues_url)
print(response.status_code)
print(response.json())

# создание заметки с ошибкой, что данные не были переданы
# (error: ошибка данных - 400)
response = session.post(issues_url)
print(response.status_code)
print(response.json())

# POOL MANAGER

# сохранение подключений и переиспольщование их
# pool_maxsize - максимальный размер pool-а, за который нельзя выйти.
# pool_block - блокирующий режим (True | False).
# pool_connections - количество кешируемых содинений
# если pool_block == True - мы не сможем выйти за пределы maxsize, и будем
# вынуждены ждать, пока не осовободится содеинение (мы будем как бы в очереди
# на использование содинения из кэша)
# пример:
# HTTPAdapter(pool_maxsize=100, pool_block=True, pool_connections=10)
# Максимальное количество соединений 100, с блокирующим режимом и 10-ю
# кешируемыми соединениями.
# Если количество содинений будет 140, то 40 из них будет ждать в очереди,
# пока какое-нибудь из 100 содинений не освободится.

adapter = HTTPAdapter(pool_maxsize=10, pool_block=True, pool_connections=10)
session = requests.Session()
# для https кешируем соединения
session.mount('http://', adapter=adapter)
session.post(issues_url)
