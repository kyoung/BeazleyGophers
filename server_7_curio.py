from curio import run, tcp_server


def fibonacci(n):
    if n <= 2:
        return 2
    return fibonacci(n-1) + fibonacci(n-2)


async def handle_connection(client, addr):
    while True:
        data = await client.recv(100000)
        result = fibonacci(int(data))
        await client.sendall(data)


if __name__ == "__main__":
    run(tcp_server('', 25000, handle_connection))
