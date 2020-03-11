# example 1 (UDP server socket)
import socket

# создаем UDP-сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# резервируем порт 8888
sock.bind(('', 8888))
# читаем 1024 байт
result = sock.recv(1024)
print('Message', result.decode('utf-8'))
# закрываем сокет
sock.close()
