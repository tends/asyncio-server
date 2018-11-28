#!/usr/bin/env python3.7

import asyncio


async def handle_echo(reader, writer):
    while not reader.at_eof():
        data = await reader.readline()
        try:
            message = data.decode()
        except Exception as e:
            message = "Error {}".format(e)

        addr = writer.get_extra_info('peername')

        print(f"Received {message!r} from {addr!r}")

        print(f"Send: {message!r}")
        writer.write(data)
        await writer.drain()

    print("Close the connection")
    writer.close()


async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
