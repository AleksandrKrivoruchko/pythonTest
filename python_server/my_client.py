
import socket
import threading

name = input("Input your nickname ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 55555))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf8')
            if not message:
                print(write())
                continue
            if message == "NICK":
                client.send(name.encode('utf8'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break


def write():
    mess = "{}: {}".format(name, input('w '))
    client.send(mess.encode('ascii'))
    return "OK"


receive()
