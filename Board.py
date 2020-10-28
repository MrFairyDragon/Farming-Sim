import numpy as np
import pygame
from GameObject import GameObject
from Tile import Tile


class Board:
    def __init__(self, gridPosX, gridPosY, SizeX, SizeY, main, grid, farmindex):
        self.gridPosX = gridPosX
        self.gridPosY = gridPosY
        self.SizeX = SizeX
        self.SizeY = SizeY
        self.main = main
        self.grid = grid
        self.farmindex = farmindex
        # print(self.main)

        # Makes a 2D array with the type as the Tile class
        self.board = np.ndarray(shape=(SizeX, SizeY), dtype=GameObject)
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                temptile = grid.grid[self.gridPosX+i][self.gridPosY+j] = Tile(i+gridPosX, j+gridPosY, self.main, 'Carrot', self.farmindex, i, j)
                self.board[i][j] = temptile

    def getGridSize(self) -> []:
        return [self.SizeX, self.SizeY]

    def getNextFreeTile(self, startPos) -> Tile:

        freeTile: Tile = self.board[startPos[0], startPos[1]]
        found = False

        posX = startPos[0]
        posY = startPos[1]

        while not found:
            posX += 1
            if posX == self.SizeX:
                posX = 0
                posY += 1
                if posY == self.SizeY:
                    posY = 0

            if not self.board[posX, posY].islocked and not self.board[posX, posY].isOccupied:
                freeTile = self.board[posX, posY]
                found = True

            if posX == startPos[0] and posY == startPos[1]:
                break

        return freeTile
