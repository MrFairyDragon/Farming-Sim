import numpy as np
from Tile import Tile


class Board:
    def __init__(self, posX, posY, SizeX, SizeY, main):
        self.__posX = posX
        self.__posY = posY
        self.__SizeX = SizeX
        self.__SizeY = SizeY
        self.main = main
        print(self.main)

        # Makes a 2D array with the type as the Tile class
        self.grid = np.ndarray(shape=(SizeX, SizeY), dtype=Tile)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j] = Tile(posX + i * 70, posY + j * 70, i, j, 'carrot', self.main)

    def getGridSize(self) -> []:
        return [self.__SizeX, self.__SizeY]