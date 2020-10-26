import numpy as np


class GameObject:
    def __init__(self, main, pixelPosX, pixelPosY, tile, length, height):
        self.posX = pixelPosX
        self.posY = pixelPosY
        self.sizeX = length
        self.sizeY = height
        self.tile = tile


