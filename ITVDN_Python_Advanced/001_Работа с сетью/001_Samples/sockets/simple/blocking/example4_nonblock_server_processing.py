import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(5)
# устанавливаем неблокирующий режим
sock.setblocking(False)

while True:
    try:
        # если в сети нет ожидающих клиентов, то попадаем в except socket.error
        client, addr = sock.accept()
    except socket.error:
        print('no clients')
    except KeyboardInterrupt:
        break
    else:
        # для данного клиента устанавливаем блокирующий режим.
        client.setblocking(True)
        result = client.recv(1024)
        client.close()
        print('Message', result.decode('utf-8'))
