import socket

class network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.48"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.MousePos = self.connect()

    def getMousePos(self):
        return self.MousePos

    def connect(self):
        try:
            self.client.connect(self.addr)
            data = self.client.recv(2048).decode()
            print(data)
            return data
        except:
            pass

    def read_pos(self, str):
        str = str.split(",")
        return int(str[0], int(str[1]))

    def make_pos(self, tup):
        return str(f'{tup[0]}, {tup[1]}')

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)
