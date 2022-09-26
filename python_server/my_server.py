import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    clients = []
    nickname = []

    def handle(self):
        self.data = self.request.recv(1024).strip()

        if self.client_address[0] in self.clients:
            print("{} wrote:".format(self.client_address))
            print(self.data.decode('utf-8'))
            self.request.sendall(self.data)
        else:
            self.request.send(bytes("Input your nick", "utf-8"))
            self.clients.append(self.client_address[0])
            self.nickname.append(self.request.recv(1024).strip)
            self.request.send(self.nickname[0])


if __name__ == "__main__":
    host, port = "localhost", 9999
    with socketserver.TCPServer((host, port), MyTCPHandler) as server:
        server.serve_forever()
