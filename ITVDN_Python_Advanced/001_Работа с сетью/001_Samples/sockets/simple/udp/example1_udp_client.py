# example 1 (UDP client socket )
import socket

# создаем UDP socket (IP)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# отправляем сообщение на `localhost:8888`
sock.sendto(b'Test message', ('localhost', 8888))
