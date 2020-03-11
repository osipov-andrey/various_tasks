import socket


def parse_http_response(text_response):
    # разбиваем ответ на отдельные строки
    lines = text_response.split('\n')
    # разделяем строку статуса и загловки/контент
    status_raw, lines = lines[0], lines[1:]
    # разделяем строку статуса, разделяя protocol, status code, message
    # пример строки: `HTTP/1.1 200 OK`
    protocol, status_code, message = status_raw.split(' ')
    # запускаем цикл, для прохода по всем заголовкам и поиска строки контента
    empty_index = 1
    headers = {}
    for index, line in enumerate(lines):
        # удаляем все пустые символы \r и пробелы
        line = line.strip()
        line = line.strip('\r')
        # проверяем, явлется ли строка пустой
        if line == '':
            # если строка пустая, значит мы дошли до контента и нам надо
            # запомнить индекс с которого начинается контет и завершить цикл.
            empty_index = index
            break
        print(line)
        # в случае, если мы не дошли до контента, значит мы свё еще находимся
        # на блоке с заголовками- разбиваем заголовки по символу `:` и
        # созраняем в словарь название и значение заголовка.
        k, _, v = line.partition(':')
        headers.setdefault(k.strip(), v.strip())
    # индекс пустой строки - empty_index.
    # для взятия контекнта, надо использовать все нижележаие строки после
    # пустой -  empty_index + 1
    content = ''.join(lines[empty_index + 1:])
    # возвращаем ответ в виде кортежа:
    # (status_code: int, headers: dict, content: str)
    return int(status_code), headers, content


# создаем TCP-сокет (IP) и подключаемя к домену
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('example.com', 80))
content_items = [
    'GET / HTTP/1.1',
    'Host: example.com',
    'Connection: keep-alive',
    'Accept: text/html',
    '\n'
]
content = '\n'.join(content_items)
print('--- HTTP MESSAGE ---')
print(content)
print('--- END OF MESSAGE ---')
sock.send(content.encode())
result = sock.recv(10024)
# попытка вручную обработать ответ от http-сервера, распарсив заголовки и
# контент
status_code, headers, content = parse_http_response(result.decode())
print('Status Code: {}'.format(status_code))
print('Headers: {}'.format(headers))
print('Content:')
print(content)
