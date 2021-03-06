#!/usr/bin/env python3.7

import asyncio
import solvers

solvers_dict = {
    'ping': solvers.ping,
    'cat': solvers.cat_file,
    'sum': solvers.sum_items,
    'sleep': solvers.sleep_secs,
    'set': solvers.set_item,
    'get': solvers.get_item
}


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

        writer.write((str(message) + "\n").encode('utf-8'))
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
