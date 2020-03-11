import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 255.255.255.255
sock.bind(('127.0.0.1', 8888))
# указываем очередь в 5 соединений, количество клиентов, которые смогут
# подключиться к серверу одновременно.
sock.listen(5)
# устанавливаем, чтобы смогли отправлять широковещательные пакеты на несколько
# адресов, например 255.255.255.255.
# Тогда мы отправим сообщение на несколько клиентов одновременно-
# называется широковещательным. Исключаем возможность ошибки, чтобы мы не
# отправляли сообщение случайно.
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# устанавливаем, чтобы смогли переиспользовать данные socket без интервалов
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# берем клиента и его адрес
client, addr = sock.accept()
result = client.recv(1024)
client.close()

print('Message', result.decode('utf-8'))
