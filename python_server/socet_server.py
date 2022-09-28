import types
import socket
import select
from operator import mul
from functools import reduce
from collections import namedtuple
from sqlite3 import connect

Session = namedtuple('Session', ['address', 'file'])

sessions = {}
callback = {}
generators = {}


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
    gen = generators.pop(conn)
    gen.close()
    sessions[conn].file.close()
    conn.close()

    del sessions[conn]
    del callback[conn]


async def process_request(conn):
    print(f'Received connection from {sessions[conn].address}')
    mode = 'sum'

    try:
        conn.sendall(b'<welcome: starting in sum mode>\n')
        while True:
            line = await readline(conn)
            if line == 'quit':
                conn.sendall(b'connection closed\r\n')
                return

            if line == 'sum':
                conn.sendall(b'<switching to sum mode>\r\n')
                mode = 'sum'
                continue
            if line == 'product':
                conn.sendall(b'<switching to product mode>\r\n')
                mode = 'product'
                continue

            print(f'{sessions[conn].address} --> {line}')
            try:
                nums = list(map(int, line.split(',')))
            except ValueError:
                conn.sendall(
                    b'ERROR Enter only integers separated by commas\n'
                )
                continue

            if mode == 'sum':
                conn.sendall(b'Sum of input numbers: %a\r\n' %
                             str(sum(nums)))
            else:
                conn.sendall(b'Product of input numbers: %a\r\n' % str(
                    reduce(mul, nums, 1)))
    finally:
        print(f'{sessions[conn].address} quit')


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
    # addr = (host, port)
    # socket_list = []
    # nickname_list = []
    reactor(host, port)
