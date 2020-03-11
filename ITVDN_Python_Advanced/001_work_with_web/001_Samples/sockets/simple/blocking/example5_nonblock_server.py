import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(5)
# sock.setblocking(True)
# есть возможность установить время ожидания в блокирующем режиме в
# количество секунд.
# sock.settimeout(5)

# sock.settimeout(0) идентичен sock.blocking(False)
# sock.settimeout(0)  # ->  sock.blocking(False)

# sock.settimeout(None) идентичен sock.blocking(True)
sock.settimeout(None)  # ->  sock.blocking(True)

try:
    client, addr = sock.accept()
except socket.error:
    print('No connections')
# если по истечению N секунд мы получаем исключение socket.timeout
# except socket.timeout:
#     print('timed out')
else:
    result = client.recv(1024)
    client.close()
    print('Message', result.decode('utf-8'))
