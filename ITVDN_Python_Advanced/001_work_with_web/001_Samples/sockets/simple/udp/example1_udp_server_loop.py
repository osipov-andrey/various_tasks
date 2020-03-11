# example 1 (UDP server socket)
import socket

# IP UDP-сокет сервер
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 8888))

# бесконечный цикл для постоянного чтения данных, без остановки сервера
while True:
    try:
        result = sock.recv(1024)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        print('Message', result.decode('utf-8'))
