from GameObject import GameObject
from Board import Board
from Tile import Tile
import random


class Animal(GameObject):

    def __init__(self, gridPosX, gridPosY, main, farmland):
        super().__init__(gridPosX, gridPosY, main)
        # create a surface object, image is drawn on it.
        self.myLand = farmland
        self.myTile = farmland.board[0, 0]


    chickenChillTime: int = 100
    chickenChillTimer: int = 0
    keepingTrackTimer: int = 0

    myLand: Board = None
    myTile: Tile = None


    def chickenWalk(self):
        self.chickenChillTimer += random.randint(1, 4)
        if self.chickenChillTimer > self.chickenChillTime:
            self.myTile.isOccupied = False
            self.myTile.name = "Carrot"
            myNewTile: Tile = self.myLand.getNextFreeTile(self.myTile.getGridIndexes())
            self.myTile = myNewTile
            self.myTile.name = self.getTexture()
            self.myTile.isOccupied = True

            self.chickenChillTimer = 0
            self.eatGrass()


    def eatGrass(self):
        if self.myTile.isGrown:
            self.myTile.animating = True
            self.myTile.isGrown = False
            self.main.coins += 2

    def getTexture(self):
        return "Chicken"