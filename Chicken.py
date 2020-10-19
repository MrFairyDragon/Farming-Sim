import pygame
import Board
import Tile
import random

pygame.init()


# farmland[k].grid[0][0].__posX
# farmland[k].grid[0][0].__posY
class Chicken:
    def __init__(self, displayName: pygame.display, farmland: Board, main):
        self.displayName = displayName
        self.main = main

        # create a surface object, image is drawn on it.
        self.image = pygame.image.load("Assets/Choiken.gif")
        self.bigImage = pygame.transform.scale(self.image, (55, 55))

        self.myLand = farmland
        self.myTile = farmland.board[0, 0]

    chickenChillTime: int = 100
    chickenChillTimer: int = 0
    keepingTrackTimer: int = 0

    myLand: Board = None
    myTile: Tile = None

    def drawChicken(self):
        self.displayName.blit(self.bigImage, (self.myTile.defaultPosX, self.myTile.defaultPosY))

    def chickenWalk(self):
        self.chickenChillTimer += random.randint(1, 4)
        if self.chickenChillTimer > self.chickenChillTime:

            self.myTile.isOccupied = False
            myNewTile: Tile = self.myLand.getNextFreeTile(self.myTile.getGridIndexes())
            self.myTile = myNewTile
            self.myTile.isOccupied = True

            self.chickenChillTimer = 0


    def eatGrass(self):
        if self.myTile.isGrown:
            self.myTile.animating = True
            self.myTile.isGrown = False
            self.main.coins += 2


    # def checkUnlock(self):
    # self.main.farmland[0].grid[0][0].islocked
    # if self.main.farmland[0].grid[0][0].islocked
