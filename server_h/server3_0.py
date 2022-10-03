import types
import socket
import select
from collections import namedtuple

Session = namedtuple('Session', ['address', 'file'])

sessions = {}
callback = {}
generators = {}
nicknames = {}


def reactor(host, port):
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(5)

    sessions[sock] = None
    print(f'Server up, running, and waiting for call on {host}:{port}')

    try:
        while True:
            ready_to_read, _, _ = select.select(sessions, [], [], 0.1)
            for conn in ready_to_read:
                if conn is sock:
                    conn, cli_address = sock.accept()
                    connect(conn, cli_address)
                    continue

                try:
                    line = sessions[conn].file.readline()
                except UnicodeDecodeError:
                    pass
                if line:
                    callback[conn](conn, line.rstrip())
                else:
                    disconnect(conn)
                    break
    finally:
        sock.close()


def connect(conn, cli_address):
    sessions[conn] = Session(cli_address, conn.makefile())

    gen = process_request(conn)
    generators[conn] = gen
    callback[conn] = gen.send(None)


def disconnect(conn):
    del nicknames[conn]
    gen = generators.pop(conn)
    gen.close()
    sessions[conn].file.close()
    conn.close()

    del sessions[conn]
    del callback[conn]
   


def send_mess(conn, line):
    for socket in nicknames:
        if socket is conn:
            continue
        socket.sendall(bytes(f'{nicknames[conn]}:\r\n{line}\r\n', 'utf-8'))


async def process_request(conn):
    try:

        conn.sendall(bytes('Input your nickname\r\n', 'utf-8'))
        answer = await readline()
        nicknames[conn] = answer
        send_mess(conn, 'joined!')
        print(
            f'Received connection from {nicknames[conn]} {sessions[conn].address}')
        conn.sendall(bytes(f'<welcome: {nicknames[conn]}>\r\n', 'utf-8'))
        while True:
            try:
                line = await readline()
            except:
                return
            if line == 'q':
                conn.sendall(bytes(
                    f'{nicknames[conn]}: {sessions[conn].address} connection closed\r\n',
                    'utf-8'))
                send_mess(conn, f'{nicknames[conn]} leaved!')
                return
            send_mess(conn, line)

            print(f'{nicknames[conn]} --> {line}')
    finally:
        try:
            print(f'{nicknames[conn]} {sessions[conn].address} leaved')
        except:
            print("Error")


@types.coroutine
def readline():
    def inner(conn, line):
        gen = generators[conn]
        try:
            callback[conn] = gen.send(line)
        except StopIteration:
            disconnect(conn)

    line = yield inner
    return line


if __name__ == '__main__':
    host = "127.0.0.1"
    port = 55555
    reactor(host, port)
