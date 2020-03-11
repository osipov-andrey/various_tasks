import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('', 8888))

sock.send(b'Test message')
result = sock.recv(64)
print('Response:', result)
sock.close()
