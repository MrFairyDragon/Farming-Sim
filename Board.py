import numpy as np
import pygame
from Tile import Tile


class Board:
    def __init__(self, posX, posY, SizeX, SizeY, main, grid, farmindex):
        self.__posX = posX
        self.__posY = posY
        self.__SizeX = SizeX
        self.__SizeY = SizeY
        self.main = main
        self.grid = grid
        self.farmindex = farmindex
        # print(self.main)

        # Makes a 2D array with the type as the Tile class
        self.board = np.ndarray(shape=(SizeX, SizeY), dtype=Tile)
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.board[i][j] = Tile(posX + i * 64, posY + j * 64, i, j, 'Carrot', self.main, self.farmindex)
                self.grid.grid[i][j] = Tile(posX + i * 64, posY + j * 64, i, j, 'Carrot', self.main, self.farmindex)

    def getGridSize(self) -> []:
        return [self.__SizeX, self.__SizeY]

    def getNextFreeTile(self, startPos) -> Tile:

        freeTile: Tile = self.board[startPos[0], startPos[1]]
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

            if not self.board[posX, posY].islocked and not self.board[posX, posY].isOccupied:
                freeTile = self.board[posX, posY]
                found = True

            if posX == startPos[0] and posY == startPos[1]:
                break

        return freeTile
