import numpy as np
from Tile import Tile


class Board:
    def __init__(self, posX, posY, SizeX, SizeY):
        self.__posX = posX
        self.__posY = posY
        self.__SizeX = SizeX
        self.__SizeY = SizeY

        self.grid = np.ndarray(shape=(SizeX, SizeY), dtype=Tile)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j] = Tile(i, j, 'carrot')
