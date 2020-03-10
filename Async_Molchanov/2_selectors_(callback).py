import socket
import selectors


selector = selectors.DefaultSelector()


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 8080))
    server_socket.listen()

    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)


def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print('Connection from ', addr)

    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)


def send_message(client_socket):

    request = client_socket.recv(4096)

    if request:
        response = 'Hello\n'.encode()
        client_socket.send(response)
    else:
        selector.unregister(fileobj=client_socket)
        client_socket.close()


def event_loop():
    while True:

        events = selector.select()  # [(key, events), ..]

        # SelectorKey - Named Tuple
        # fileobj
        # events
        # data

        for key in events:
            callback = key[0].data  # 'data=<function>' in selector.register()
            callback(key[0].fileobj)  # 'fileobj=<socket>' in selector.register()


if __name__ == '__main__':
    server()
    event_loop()
