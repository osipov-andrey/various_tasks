import asyncio


async def business_logic(message):

    message = message.split()
    message = [int(i) for i in message]
    result = sum(message)
    return str(result)


async def handle_echo(reader, writer):
    while True:
        data = await reader.read(100)
        message = data.decode()

        if message == 'close':
            print("Close the client socket")
            writer.close()
            break

        addr = writer.get_extra_info('peername')
        print(f"Received {message} from {addr}")

        response = await business_logic(message)

        print(f"Send: {response}")
        writer.write(response.encode())
        await writer.drain()

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, '127.0.0.1', 8080, loop=loop)
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()