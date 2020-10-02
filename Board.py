import numpy as np
from Tile import Tile


class Board:
    def __init__(self, posX, posY, SizeX, SizeY, main, farmindex):
        self.__posX = posX
        self.__posY = posY
        self.__SizeX = SizeX
        self.__SizeY = SizeY
        self.main = main
        self.farmindex = farmindex
        # print(self.main)

        # Makes a 2D array with the type as the Tile class
        self.grid = np.ndarray(shape=(SizeX, SizeY), dtype=Tile)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j] = Tile(posX + i * 70, posY + j * 70, i, j, 'Carrot', self.main, self.farmindex)

    def getGridSize(self) -> []:
        return [self.__SizeX, self.__SizeY]

    def getNextFreeTile(self, startPos) -> Tile:

        freeTile: Tile = self.grid[startPos[0], startPos[1]]
        found = False

        posX = startPos[0]
        posY = startPos[1]

        while not found:
            posX += 1
            if posX == self.__SizeX:
                posX = 0
                posY += 1
                if posY == self.__SizeY:
                    posY = 0

            if not self.grid[posX, posY].islocked and not self.grid[posX, posY].isOccupied:
                freeTile = self.grid[posX, posY]
                found = True

            if posX == startPos[0] and posY == startPos[1]:
                break

        return freeTile
