import uvloop
import asyncio


def fibonacci(n):
    if n <= 2:
        return 2
    return fibonacci(n-1) + fibonacci(n-2)


async def handle_connection(client_reader, client_writer):
    while True:
        data = (await client_reader.readline()).decode("utf-8")

        result = fibonacci(int(data))
        client_writer.write(str(result).encode('utf-8'))

        await client_writer.drain()


if __name__ == "__main__":
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)

    server = asyncio.start_server(handle_connection,
                                  host='localhost', port='25000',
                                  loop=loop)

    loop.run_until_complete(server)
    loop.run_forever()
