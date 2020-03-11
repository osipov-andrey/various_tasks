import socketserver


class EchoTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # self.request содержит сокет клиента, чтобы мы могли отправитьему
        # сообщение обратно (надо учитывай, что клиент должен уметь принимать
        # сообщения, отправив ему обратно сообщение, вовсе не значит, что он
        # сразу его обработает- надо иметь данный фукнционал)
        data = self.request.recv(1024).strip()
        print('Address: {}'.format(self.client_address[0]))
        print('Data: {}'.format(data.decode()))
        self.request.sendall(data)


if __name__ == '__main__':
    # аналогичный пример TCP-сервера и использования оператора with..
    with socketserver.TCPServer(('', 8888), EchoTCPHandler) as server:
        server.serve_forever()
