#!/usr/bin/env python3.7

import asyncio
from inspect import getmembers, isfunction
import solvers

solvers_dict = {o[0]: o[1] for o in getmembers(solvers) if isfunction(o[1])}


async def data_decode(data):
    try:
        parsed_msg = data.decode().split()
    except Exception as e:
        message = "Error {}".format(e)
    else:
        print(parsed_msg)
        message = await solvers_dict[parsed_msg[0]](parsed_msg[1:]) \
            if len(parsed_msg) >= 1 \
               and parsed_msg[0] in solvers_dict \
            else "E wrong parsed command {}".format(parsed_msg)
    return message


async def handle_echo(reader, writer):
    while not reader.at_eof():
        message = await data_decode(
            await reader.readline()
        )

        addr = writer.get_extra_info('peername')

        print(f"Received {message!r} from {addr!r}")

        print(f"Send: {message!r}")
        writer.write((str(message) + "\n").encode('utf-8'))#data)
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
