import numpy as np


class GameObject:
    def __init__(self, gridPosX, gridPosY, main):
        self.gridPosX = gridPosX
        self.gridPosY = gridPosY
        self.posX = gridPosX*64
        self.posY = gridPosY*64
        self.main = main

    def getGridPos(self):
        return self.gridPosX, self.gridPosY

    def getPos(self):
        return self.posX, self.posY


