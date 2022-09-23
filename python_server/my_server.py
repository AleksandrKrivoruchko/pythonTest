import socket
import threading

host = "127.0.0.1"
port = 55555
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nick_names = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.revc(1024)
            if not message:
                break
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nick_name = nick_names[index]
            broadcast("{} left!".format(nick_name).encode('utf8'))
            nick_names.remove(nick_name)
            break


def receive():
    while True:
        client, address = server.accept()
        print("Connected which {}".format(str(address)))

        client.send("NICK".encode('utf8'))
        nick_name = client.recv(1024).decode('utf8')
        nick_names.append(nick_name)
        clients.append(client)

        print("Nickname is {}".format(nick_name))
        broadcast("{} joined!".format(nick_name).encode('utf8'))
        client.send("Connected to server!".encode('utf8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server is listening...")
receive()
