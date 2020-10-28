import numpy as np
import pygame
from GameObject import GameObject


class Grid:
    def __init__(self, main, sizeX, sizeY):
        self.main = main
        self.sizeX = sizeX
        self.sizeY = sizeY

        self.grid = np.ndarray(shape=[self.sizeX, self.sizeY], dtype=GameObject)

        for x in range(len(self.grid)):
            for y in range(len(self.grid[0])):
                self.grid[x][y] = None

    def draw(self):
        for x in range(len(self.grid[0])):
            for y in range(len(self.grid)):
                pygame.draw.line(self.main.screen, [128, 128, 128], [x * 64, 0], [x * 64, self.main.size[1]])
                pygame.draw.line(self.main.screen, [128, 128, 128], [0, y * 64], [self.main.size[0] - 96, y * 64])