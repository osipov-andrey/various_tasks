import json

import urllib3

HOST = '127.0.0.1:8000'


def get_url(path):
    return 'http://{host}{path}'.format(host=HOST, path=path)


def issue_url(pk):
    return get_url('/api/issues/{id}/'.format(id=pk))


issues_url = get_url('/api/issues/')
login_url = get_url('/api/auth/login/')
logout_url = get_url('/api/auth/logout/')

# создаем `PoolManager` для кеширования, испоьзуя
# num_pools - количество соединений, которые будут кешироваться.
# стоить отметить, что requests использует тот же `urllib3` pool manager.
pool = urllib3.PoolManager(num_pools=4)

response = pool.request('GET', issues_url)
print(response)

login_credentials = {'username': 'test_user', 'password': 'test_pass'}
# отправляем POST-запрос на login_url используя pool manager
response = pool.request('POST', login_url, fields=login_credentials)

# копируем cookies из заголовка (используем явное имя заголовка)
cookie = response.headers['Set-Cookie']

# отправляем GET запрос добавляя полученные cookies к запросу.
response = pool.request('GET', issues_url, headers={'Cookie': cookie})
parsed_data = json.loads(response.data.decode())
print(parsed_data)

# попытка передачи файла (читаем с диска и пытаемся передать на сервер)
with open('example7_urllib3.py', 'r') as f:
    content = f.read()

print('File content', content)
# формируем данные для запроса
data = {'text_file': ('example.txt', content, 'text/plain')}
response = pool.request('POST', issues_url, fields=data,
                        headers={'Cookie': cookie})
print(response.status)
print(response.data)

# передаем данные в формате json на сервер методом POST.
login_credentials = json.dumps({
    'username': 'test_user',
    'password': 'test_pass'
}).encode()
response = pool.request('POST', login_url, body=login_credentials,
                        headers={'Content-Type': 'application/json'})
print(response.data)
print(cookie)
cookie = response.headers['Set-Cookie']
