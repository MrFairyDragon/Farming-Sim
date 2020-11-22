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

        def __init__(self, main):

            self.clientPlayer = NetPlayer(main)

        def DrawPlayer(self, screen):


            self.clientPlayer.DrawCharacter(screen,
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
            connection.send(str.encode("Connection verified"))

            start_new_thread(self.thread, (connection, self.clientIDcounter))
            self.clientIDcounter += 1

    def drawPlayers(self, screen):
        for client in self.gameClients:
            client.DrawPlayer(screen)

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

    def processMovement(self, message, client):

        messageTrim = message.replace('[', '')
        messageTrim = messageTrim.replace(']', '')
        messageTrim = messageTrim.replace('(', '')
        messageTrim = messageTrim.replace(')', '')
        messageTrim = messageTrim.replace(' ', '')

        positionArray = []
        messagePositions = messageTrim.split(",")
        #print(messagePositions)
        for i in range(0, len(messagePositions), 2):
            positionArray.append([(int(messagePositions[i]), int(messagePositions[i+1]))])

        #print(f"Restructured array: {positionArray}")
        client.clientPlayer.setMove(positionArray)

        client.clientPlayer.setCounter2()
        client.clientPlayer.setSwitch()
        client.clientPlayer.setMove2()

        for otherClient in self.gameClients:
            if otherClient.ID != client.ID:
                #print(f"Tell other users about movement: {otherClient.ID}")
                sendMessage = f"{NetMessageCodes.PlayerMovement}_{messageTrim}_{client.ID}"
                otherClient.connection.send(str.encode(sendMessage))

    def processBuyTile(self, message, client):
        print(f"PlayerBuyTile: {message}")

    def processPlaceSprinkler(self, message, client):
        print(f"PlayerPlaceSprinkler: {message}")

    switcher = {
        NetMessageCodes.PlayerMovement: processMovement,
        NetMessageCodes.PlayerBuyTile: processBuyTile,
        NetMessageCodes.PlayerPlaceSprinkler: processPlaceSprinkler,
    }

    def thread(self, connection, ID):

        clientPlayer = self.Client(self.main)
        clientPlayer.ID = ID
        clientPlayer.connection = connection

        #If other players are already connected we want to tell the new user about them
        if len(self.gameClients) > 0:
            playerList = ""

            for client in self.gameClients:
                #Also tell the other users about the new guy
                client.connection.send(str.encode(f"{NetMessageCodes.PlayerAdd}_{clientPlayer.ID}"))
                playerList += f"{client.ID}-"

            clientPlayer.connection.send(str.encode(f"{NetMessageCodes.PlayerAddMultiple}_{playerList}"))

        self.gameClients.append(clientPlayer)

        while True:
            try:
                print(f"Waiting for data from client: {clientPlayer.ID}")
                data = clientPlayer.connection.recv(2048)
                if str(data) == NetMessageCodes.MessageReceivedByte:
                    print(f"Received confirmation from client: {clientPlayer.ID}")
                    continue

                clientPlayer.connection.send(str.encode(NetMessageCodes.MessageReceived))

                #print(f"Received data: {data}")

                self.processClientMessage(data, clientPlayer)

            except Exception as e:
                print(f"Connection error: {traceback.format_exc()}")
                break

        self.gameClients.remove(clientPlayer)
        self.ClientDisconnected(clientPlayer.ID)
        print(f"Lost connection to player {clientPlayer}: {time.time()}")

        connection.close

    def ClientDisconnected(self, clientID):

        #We removed the client so we don't need to check while looping
        for client in self.gameClients:
            try:
                client.connection.send(str.encode(f"{NetMessageCodes.PlayerRemove}_{clientID}"))
            except:
                pass