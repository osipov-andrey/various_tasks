from twisted.internet import reactor, protocol, endpoints
from twisted.internet.protocol import connectionDone


class ProcessClient(protocol.Protocol):

    def __init__(self, server):
        self.server = server

    def connectionMade(self):
        print('Client connected...')
        self.server.concurrentClientCount += 1

    def connectionLost(self, reason=connectionDone):
        self.server.concurrentClientCount -= 1

    def dataReceived(self, data: str):
        data = data.strip()
        print('Data: ', data)
        self.transport.write(data)


class Server(protocol.Factory):
    commands = ('init', 'send', 'get', 'close')

    def __init__(self):
        self.concurrentClientCount = 0
        self.database = {}

    def buildProtocol(self, addr):
        return ProcessClient(self)


server = endpoints.serverFromString(reactor, 'tcp:8888')
server.listen(Server())
reactor.run()
