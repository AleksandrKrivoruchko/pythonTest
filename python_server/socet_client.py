import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("127.0.0.1", 55555))
sock.sendall('Hello, Habr!'.encode('utf-8'))
data = sock.recv(1024)
print(data.decode('utf-8'))
sock.close()
