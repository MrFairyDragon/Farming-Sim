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

    def MouseClicked(self):
        self.main.mousePos = pygame.mouse.get_pos()
        for k in range(len(self.main.farmarray)):
            for i in range(self.main.farmarray[k][2]):
                for j in range(self.main.farmarray[k][3]):

                    # Mouse clicks on tile
                    if (self.main.farmarray[k][0] * 64) + (i * 64) <= self.main.mousePos[0] <= (self.main.farmarray[k][0] * 64) + (
                            i * 64) + 64 \
                            and (64 * self.main.farmarray[k][1]) + (j * 64) <= self.main.mousePos[1] <= (64 * self.main.farmarray[k][1]) + (
                            j * 64) + 64:

                        self.main.farmland[k].board[i][j].animating = True

                        # Tile is hard locked
                        if self.main.farmland[k].board[i][j].isHardLocked and self.main.coins >= self.main.farmlandbuy:
                            self.main.farmland[k].board[i][j].hardUnlock()

                        # Tile is locked
                        elif self.main.farmland[k].board[i][j].islocked and self.main.coins >= self.main.tilebuy \
                                and not self.main.farmland[k].board[i][j].isHardLocked:
                            self.main.farmland[k].board[i][j].unlock()

                        # Tile is grown
                        elif self.main.farmland[k].board[i][j].isGrown:
                            self.main.farmland[k].board[i][j].harvest()

                        # Tile is watered
                        elif not self.main.farmland[k].board[i][j].isWatered:
                            self.main.farmland[k].board[i][j].water()

    def draw(self):
        for x in range(len(self.grid[0])):
            for y in range(len(self.grid)):
                pygame.draw.line(self.main.screen, [128, 128, 128], [x * 64, 0], [x * 64, self.main.size[1]])
                pygame.draw.line(self.main.screen, [128, 128, 128], [0, y * 64], [self.main.size[0] - 96, y * 64])