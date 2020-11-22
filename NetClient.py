import socket
import NetMessageCodes

class NetClient:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.server = "192.168.0.48"
        #self.server = '192.168.0.103'
        self.server = '127.0.0.1'
        self.port = 5555
        self.addr = (self.server, self.port)
        self.connect()

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

    def set_pos(self, position):
        print(f"Sending position to server: {position}")
        self.send(f"{NetMessageCodes.PlayerMovement}_{position}")

    def send(self, data):
        try:
            sendString = str.encode(data)
            print(f"Sending message to server: {data} --> {sendString}")
            self.client.send(sendString)
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)