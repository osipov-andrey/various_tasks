from urllib import request

# получаем содержимое страницы по domain- в качестве порта будет использован 80
# Для казание другого порта используем запись вида: http://example:81.com
response = request.urlopen('http://example.com')

# печатаем информацию об http-ответе
print(response.status)
print(response.getcode())
print(response.msg)
print(response.reason)
# получаем заголовки в виде внутреннего объекта
print(response.headers)
# получаем словарь всех заголовков
print(response.getheaders())
# получение заголовка
print(response.headers.get('Content-Type'))
print(response.getheader('Content-Type'))
