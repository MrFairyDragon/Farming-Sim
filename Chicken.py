import pygame
from Tile import Tile
from Board import Board

pygame.init()

#farmland[k].grid[0][0].__posX
#farmland[k].grid[0][0].__posY
class Chicken:
    def __init__(self,displayName: pygame.display, main):
        self.displayName = displayName
        self.main = main

        # create a surface object, image is drawn on it.
        self.image = pygame.image.load("Choiken.gif")
        self.bigImage = pygame.transform.scale(self.image, (55, 55))

    stepCounter = 0

    gridPlacementX = 0
    gridPlacementY = 0

    def drawChicken(self, posX ,posY):
        self.displayName.blit(self.bigImage, (posX, posY))

    def chickenWalk(self):
        self.stepCounter += 1

        if   self.stepCounter < 100:
             self.gridPlacementX = 0

        elif self.stepCounter > 100 and self.stepCounter < 200:
             self.gridPlacementX = 1

        elif self.stepCounter > 200 and self.stepCounter < 300:
             self.gridPlacementX = 2

        elif self.stepCounter == 300:
             self.gridPlacementX = 0
             self.stepCounter   = 0
             self.gridPlacementY += 1

             if self.gridPlacementY == 3:
                 self.gridPlacementY = 0

    def eatGrass(self):
        if self.gridPlacementX == 0 and self.gridPlacementY == 0:
            if self.main.farmland[0].grid[0][0].isGrown:
                self.main.farmland[0].grid[0][0].animating = True
                self.main.farmland[0].grid[0][0].isGrown = False
                self.main.coins += 2







