# example 1 (UDP client socket )
import socket

# создаем TCP сокет-клиент
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# подключаемся к 8888 порту
sock.connect(('127.0.0.1', 8080))
# отпарлвяем сообщение
sock.send(b'1 1')
recv = sock.recv(1024)
print(recv)

# # закрываем сокет-соединение
sock.close()
