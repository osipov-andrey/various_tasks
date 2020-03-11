import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(5)
# блокирующий режим, устанавливается для того, чтобы мы не блокировали
# интерпретатор по выхову accept/recv если у нас сеть простаивает.
# Принимает True / False.
sock.setblocking(False)

client, addr = sock.accept()
result = client.recv(1024)
client.close()

print('Message', result.decode('utf-8'))
