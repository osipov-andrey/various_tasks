import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b'Get time', ('127.0.0.1', 8888))
current_time, client_address = sock.recvfrom(1024)
print(current_time.decode('utf-8'))