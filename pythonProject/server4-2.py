import asyncio

nicknames = {}
writers = []


def send_message(addr, data):
    i = 0
    for address in nicknames:
        if address == addr:
            i += 1
            continue
        try:
            writers[i].write(nicknames[addr] + data)
            i += 1
        except ConnectionError:
            print("Client suddenly closed, cannot send")
            return
        except IndexError:
            print(f'Index: {i}')
            print(writers)
            return


async def handle_connection(reader, writer):
    addr = writer.get_extra_info("peername")
    print("Connected by", addr)
    try:
        writer.write(b'Input your nickname\r\n')
    except ConnectionError:
        print("Client suddenly closed, cannot send")
        return
    try:
        data = await reader.read(512)
    except ConnectionError:
        print(f"Client suddenly closed while receiving from {addr}")
        return
    nicknames[addr] = data
    writers.append(writer)
    try:
        send_message(addr, b'joined\r\n')
        print(f'{data} joined!')
    except ConnectionError:
        print("Client suddenly closed, cannot send")
        return
    while True:
        try:
            data = await reader.read(1024)
            print(f'{nicknames[addr]} --> {data}')
        except ConnectionError:
            print(f"Client suddenly closed while receiving from {addr}")
            break
        if not data:
            break
        try:
            send_message(addr, data)
        except ConnectionError:
            print("Client suddenly closed, cannot send")
            break
    writers.remove(writer)
    writer.close()
    send_message(addr, b'leaved\r\n')
    del nicknames[addr]
    print("Disconnect by", addr)


async def main(host, port):
    server = await asyncio.start_server(handle_connection, host, port)
    async with server:
        print('Server starting...')
        await server.serve_forever()


host, port = "127.0.0.1", 55555

if __name__ == "__main__":
    asyncio.run(main(host, port))