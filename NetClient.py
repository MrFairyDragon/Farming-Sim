import socket
import NetMessageCodes
from _thread import *
import traceback
import time
from NetPlayer import NetPlayer


class NetClient:
    netPlayers = []
    messagesToServer = []

    class OtherPlayer:
        ID = -1
        NetPlayer = None

        def __init__(self, main, ID):
            self.ID = int(ID)
            self.NetPlayer = NetPlayer(main)

    def __init__(self, main):
        self.main = main
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.server = "192.168.0.48"
        # self.server = '192.168.0.103'
        self.server = '127.0.0.1'
        self.port = 5555
        self.addr = (self.server, self.port)

        print("Connecting to server")
        try:
            self.connection = self.socket.connect(self.addr)
            data = self.socket.recv(2048).decode()

            start_new_thread(self.listenToServer, ("Filler",))
            start_new_thread(self.messageQueueToServer, ("Filler",))

        except Exception as e:
            print(f"Connecting failed: {traceback.format_exc()}")

    def drawPlayers(self, screen):
        for player in self.netPlayers:
            player.NetPlayer.DrawCharacter(screen,
                                 player.NetPlayer.getScaledUpCharacter(player.NetPlayer.female, player.NetPlayer.getScaleRatioFemale()),
                                 player.NetPlayer.setPos(300, 300),
                                 player.NetPlayer.getMove2(),
                                 player.NetPlayer.getCoordCropping(player.NetPlayer.getScaleRatioFemale(), player.NetPlayer.west),
                                 player.NetPlayer.getCoordCropping(player.NetPlayer.getScaleRatioFemale(), player.NetPlayer.north),
                                 player.NetPlayer.getCoordCropping(player.NetPlayer.getScaleRatioFemale(), player.NetPlayer.east),
                                 player.NetPlayer.getCoordCropping(player.NetPlayer.getScaleRatioFemale(), player.NetPlayer.south))

    def read_pos(self, str):
        str = str.split(",")
        return int(str[0], int(str[1]))

    def make_pos(self, tup):
        return str(f'{tup[0]}, {tup[1]}')

    def set_pos(self, movement):

        # Do not send empty data to the server
        if str(movement) == "[]":
            return

        print(f"Sending movement to server: {movement}")
        self.sendToServer(f"{NetMessageCodes.PlayerMovement}_{movement}")

    def processServerMessage(self, message):
        message = str(message)
        message = message.split('\'')[1]
        print(f"Converted and trimmed: {message}")
        messageContents = message.split('_')

        func = self.switcher.get(messageContents[0])
        func(self, messageContents)

    def processMovement(self, messageContents):

        messageTrim = messageContents[1].replace('[', '')
        messageTrim = messageTrim.replace(']', '')
        messageTrim = messageTrim.replace('(', '')
        messageTrim = messageTrim.replace(')', '')
        messageTrim = messageTrim.replace(' ', '')

        positionArray = []
        messagePositions = messageTrim.split(",")
        print(messagePositions)
        for i in range(0, len(messagePositions), 2):
            positionArray.append([(int(messagePositions[i]), int(messagePositions[i + 1]))])

        print(f"Add movement of player: {int(messageContents[2])}")
        for otherPlayer in self.netPlayers:
            print(f"{otherPlayer.ID} == {int(messageContents[2])}")
            if otherPlayer.ID == int(messageContents[2]):
                print(f"Update movement of player: {messageContents[2]}")
                otherPlayer.NetPlayer.setMove(positionArray)

                otherPlayer.NetPlayer.setCounter2()
                otherPlayer.NetPlayer.setSwitch()
                otherPlayer.NetPlayer.setMove2()
                break

    def processBuyTile(self, messageContents):
        print(f"PlayerBuyTile: {messageContents}")

    def processPlaceSprinkler(self, messageContents):
        print(f"PlayerPlaceSprinkler: {messageContents}")

    def processPlayerAdd(self, messageContents):
        self.netPlayers.append(self.OtherPlayer(self.main, messageContents[1]))
        print(f"PlayerAdd {messageContents}")

    def processPlayerAddMultiple(self, messageContents):
        for netPlayerID in messageContents[1].split('-'):
            if(netPlayerID == ''):
                continue
            self.netPlayers.append(self.OtherPlayer(self.main, netPlayerID))
        print(f"PlayerAddMultiple {messageContents}")

    def processPlayerRemove(self, messageContents):
        print(f"PlayerRemove {messageContents}")

    switcher = {
        NetMessageCodes.PlayerMovement: processMovement,
        NetMessageCodes.PlayerBuyTile: processBuyTile,
        NetMessageCodes.PlayerPlaceSprinkler: processPlaceSprinkler,
        NetMessageCodes.PlayerAdd: processPlayerAdd,
        NetMessageCodes.PlayerAddMultiple: processPlayerAddMultiple,
        NetMessageCodes.PlayerRemove: processPlayerRemove
    }

    def sendToServer(self, message):
        self.messagesToServer.append(message)

    def messageQueueToServer(self, filler):

        while True:
            while len(self.messagesToServer) == 0:
                time.sleep(0.01)

            try:
                for message in self.messagesToServer:
                    sendString = str.encode(message)
                    print(f"Sending message to server: {sendString}")
                    self.socket.send(sendString)

                self.messagesToServer.clear()
            except socket.error as e:
                print(e)

    def listenToServer(self, filler):
        print("Listen thread started")
        while True:
            try:
                print("Waiting for data from server")
                data = self.socket.recv(2048)
                if str(data) == NetMessageCodes.MessageReceivedByte:
                    print("Received confirmation from server")
                    continue
                print(f"{str(data)} --- {NetMessageCodes.MessageReceived}")
                self.socket.send(str.encode(NetMessageCodes.MessageReceived))

                self.processServerMessage(data)

            except Exception as e:
                print(f"Connection error: {traceback.format_exc()}")
