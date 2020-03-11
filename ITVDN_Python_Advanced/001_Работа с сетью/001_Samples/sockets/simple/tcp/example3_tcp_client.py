# example 1 (UDP client socket )
import socket

# создаем TCP сокет-клиент
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# подключаемся к 8888 порту
sock.connect(('', 8888))
# отпарлвяем сообщение
sock.send(b'Test message')
# закрываем сокет-соединение
sock.close()
