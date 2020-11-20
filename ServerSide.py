import socket
from _thread import *


class ServerSide:

    def __init__(self):
        self.mousePos = (0, 0), (1, 1)
        self.currentPlayer = 0
        server = "192.168.0.48"
        port = 5555
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            mySocket.bind((server, port))
        except socket.error as e:
            str(e)

        mySocket.listen(5)
        print("Server Started")

        while True:
            connection, addr = mySocket.accept()
            print('Connected to :', addr[0], ':', addr[1], 'player:', self.currentPlayer)

            start_new_thread(self.thread, (connection, self.currentPlayer))
            self.currentPlayer += 1

    def read_pos(self, str):
        str = str.split(",")
        return int(str[0], int(str[1]))

    def make_pos(self, tup):
        return str(f'{tup[0]}, {tup[1]}')

    def thread(self, connection, player):
        connection.send(str.encode(self.make_pos(self.mousePos[player])))
        print("test")
        reply = ""
        while True:
            try:
                data = self.read_pos(connection.recv(2048))
                self.mousePos[player] = data
                reply = data.decode("utf-8")

                if not data:
                    print(f'Goodbye player{player}')
                else:
                    if player == 1:
                        reply = self.mousePos[0]
                    else:
                        reply = self.mousePos[1]
                    print("Received:", data)
                    print("Sending:", reply)

                connection.sendall(str.encode(self.make_pos(reply)))

            except:
                break

        print(f"Lost connection to player {player}")
        connection.close