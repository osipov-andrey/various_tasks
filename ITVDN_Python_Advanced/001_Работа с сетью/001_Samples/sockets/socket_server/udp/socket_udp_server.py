import socketserver


class EchoUDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # request содержит данные и сокет-клиент для коммуникации
        data, socket = self.request
        print('Address: {}'.format(self.client_address[0]))
        print('Data: {}'.format(data.decode()))
        socket.sendto(data, self.client_address)


if __name__ == '__main__':
    # используем оператор with для создания сервера на 0:8888 и запускаем
    # with гарантирует освобождение порта и корректное завершение работы
    # сервера- у класса реализован `__enter__` / `__exit__`.
    with socketserver.UDPServer(('0', 8888), EchoUDPHandler) as server:
        server.serve_forever()
