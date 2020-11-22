import socket
from _thread import *
import time
from NetPlayer import NetPlayer
import NetMessageCodes
import pygame
import keyboard
import traceback

class NetServer:

    class Client:

        ID = 0
        connection = None
        mousePos = (0, 0)
        clientPlayer = None
        screen = None

        def __init__(self, main):

            self.clientPlayer = NetPlayer(main)

            self.screen = main.screen

        def DrawPlayer(self):


            self.clientPlayer.DrawCharacter(self.screen,
                                            self.clientPlayer.getScaledUpCharacter(self.clientPlayer.female, self.clientPlayer.getScaleRatioFemale()),
                                            self.clientPlayer.setPos(300, 300),
                                            self.clientPlayer.getMove2(),
                                            self.clientPlayer.getCoordCropping(self.clientPlayer.getScaleRatioFemale(), self.clientPlayer.west),
                                            self.clientPlayer.getCoordCropping(self.clientPlayer.getScaleRatioFemale(), self.clientPlayer.north),
                                            self.clientPlayer.getCoordCropping(self.clientPlayer.getScaleRatioFemale(), self.clientPlayer.east),
                                            self.clientPlayer.getCoordCropping(self.clientPlayer.getScaleRatioFemale(), self.clientPlayer.south))

    gameClients = []

    def __init__(self, main):
        self.main = main
        self.mousePos = (0, 0), (1, 1)
        self.clientIDcounter = 0
        #server = "192.168.0.48"
        #server = '192.168.0.103'
        server = '127.0.0.1'
        port = 5555
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            mySocket.bind((server, port))
        except socket.error as e:
            str(e)

        print("let's listen")
        mySocket.listen(5)
        print("Server Started")

        start_new_thread(self.waitForConnections, (mySocket,))


    def waitForConnections(self, mySocket):
        while True:
            connection, addr = mySocket.accept()
            print('Connected to :', addr[0], ':', addr[1], 'player:', self.clientIDcounter)

            start_new_thread(self.thread, (connection, self.clientIDcounter))
            self.clientIDcounter += 1

    def read_pos(self, string):
        string = str(string)
        print(string)
        readStr = string.split(",")
        return (int(readStr[0]), int(readStr[1]))

    def make_pos(self, tup):
        return str(f'{tup[0]}, {tup[1]}')

    def processClientMessage(self, message, client):
        message = str(message)
        message = message.split('\'')[1]
        #print(f"Converted and trimmed: {message}")
        messageContents = message.split('_')

        func = self.switcher.get(messageContents[0])
        func(self, messageContents[1], client)

    def processCharacterPos(self, message, client):

        message = message.replace('[', '')
        message = message.replace(']', '')
        message = message.replace('(', '')
        message = message.replace(')', '')
        message = message.replace(' ', '')

        positionArray = []
        messagePositions = message.split(",")
        for i in range(0, len(messagePositions), 2):
            positionArray.append([(int(messagePositions[i]), int(messagePositions[i+1]))])

        print(f"Restructured array: {positionArray}")
        client.clientPlayer.setMove(positionArray)

        client.clientPlayer.setCounter2()
        client.clientPlayer.setSwitch()
        client.clientPlayer.setMove2()

    def processBuyTile(self, message, client):
        print(f"PlayerBuyTile: {message}")

    def processPlaceSprinkler(self, message, client):
        print(f"PlayerPlaceSprinkler: {message}")

    switcher = {
        NetMessageCodes.PlayerMovement: processCharacterPos,
        NetMessageCodes.PlayerBuyTile: processBuyTile,
        NetMessageCodes.PlayerPlaceSprinkler: processPlaceSprinkler
    }

    def thread(self, connection, ID):

        clientPlayer = self.Client(self.main)
        self.gameClients.append(clientPlayer)

        clientPlayer.ID = ID
        clientPlayer.connection = connection
        clientPlayer.connection.send(str.encode(self.make_pos(clientPlayer.mousePos)))

        while True:
            try:
                print("Waiting for data from client: {}".format(time.time()))
                data = clientPlayer.connection.recv(2048)
                clientPlayer.connection.send(str.encode("Received"))

                #print(f"Received data: {data}")

                self.processClientMessage(data, clientPlayer)

                #reply = "Thank you"
                #print(f"Reply message: {reply}")

                #if not data:
                #    print(f'Goodbye player{clientPlayer}')
                #else:
                #    print("Received:", data)
                #    print("Sending:", reply)



            except Exception as e:
                print(f"Connection error: {traceback.format_exc()}")
                break

        self.gameClients.remove(clientPlayer)
        print(f"Lost connection to player {clientPlayer}: {time.time()}")
        connection.close