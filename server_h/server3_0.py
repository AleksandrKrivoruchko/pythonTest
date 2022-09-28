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
    sock.setblocking(0)

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

                line = sessions[conn].file.readline()
                if line:
                    callback[conn](conn, line.rstrip())
                else:
                    disconnect(conn)
    finally:
        sock.close()


def connect(conn, cli_address):
    sessions[conn] = Session(cli_address, conn.makefile())

    gen = process_request(conn)
    generators[conn] = gen
    callback[conn] = gen.send(None)


def disconnect(conn):
    nicknames.pop(conn)
    gen = generators.pop(conn)
    gen.close()
    sessions[conn].file.close()
    conn.close()

    del sessions[conn]
    del callback[conn]


def send_mess(conn, line):
    for name in nicknames:
        name.sendall(bytes(f'{nicknames[conn]}:\n {line}\r\n', 'utf-8'))


async def process_request(conn):
    conn.sendall(b'Input your nickname\n')
    answer = await readline(conn)
    nicknames[conn] = answer
    send_mess(conn, 'joined!')
    print(
        f'Received connection from {nicknames[conn]} {sessions[conn].address}')
    try:
        conn.sendall(b'<welcome: %a>\n' % nicknames[conn])
        while True:
            line = await readline(conn)
            if line == 'q':
                conn.sendall(b'%a: %a connection closed\r\n' %
                             (nicknames[conn], sessions[conn].address))
                return
            send_mess(conn, line)

            print(f'{nicknames[conn]} --> {line}')

    finally:
        send_mess(conn, f'{nicknames[conn]} leaved!')
        print(f'{nicknames[conn]} {sessions[conn].address} leaved')


@types.coroutine
def readline(conn):
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
