import json
from http import server


class CustomHandler(server.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(400)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"CSV UPLOADING")

    def do_POST(self):
        self.send_response(200)
        self.send_header('content-type', 'application/json')
        self.send_header('Server', 'CoolServer')
        self.end_headers()
        self.wfile.write(json.dumps({'result': True}).encode())

    def do_PUT(self):
        self.send_response(200)
        self.send_header('content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'PUT request\n')

    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()


server_address = ('', 8888)
# создаем экземпляр сервера, передавая данные IP/Port, которые будут
# использованы для соединения. Также передаем класс, описанный для обработки
# запросов к серверу
httpd = server.HTTPServer(server_address, CustomHandler)
# запускаем сервер, которые будет слушать сокет на 8888 порту и принимать
# http-запросы, а после приема передавать в класс CustomHandler в зависимости
# от типа запроса GET, POST, PUT, ...
httpd.serve_forever()
