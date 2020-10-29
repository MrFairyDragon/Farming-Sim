import pygame
import numpy as np


class Player:
    def DrawCharacter(self, screen, img, pos,
                      sprite_sheetCroppingW,
                      sprite_sheetCroppingN,
                      sprite_sheetCroppingE,
                      sprite_sheetCroppingS):
        self.RenderAnimation(screen, img, pos,
                             sprite_sheetCroppingW,
                             sprite_sheetCroppingN,
                             sprite_sheetCroppingE,
                             sprite_sheetCroppingS)

    def getMousePos(self):
        self.mx, self.my = pygame.mouse.get_pos()
        self.previousMovement.append((self.mx, self.my))
        return self.previousMovement[-1]

    def translateMousePosToGridPos(self):
        ans = [round(self.getMousePos()[0] / 64), round(self.getMousePos()[1] / 64)]
        return ans

    def getScaledUpCharacter(self, img, scaleRatio):
        self.ScaleUp = pygame.transform.scale(img, (img.get_width() * scaleRatio, img.get_height() * scaleRatio))
        return self.ScaleUp

    def getWestCoordCropping(self, scaleRatio, westCoordinates):
        list1 = []
        list4 = []
        for i in range(len(self.west)):
            list1.append(list(westCoordinates[i]))
        list2 = np.array(list1)
        list3 = list2 * scaleRatio
        for j in range(len(self.west)):
            list4.append(tuple(list3[j]))
        return list4

    def getNorthCoordCropping(self, scaleRatio, northCoordinates):
        list1 = []
        list4 = []
        for i in range(len(self.north)):
            list1.append(list(northCoordinates[i]))
        list2 = np.array(list1)
        list3 = list2 * scaleRatio
        for j in range(len(self.north)):
            list4.append(tuple(list3[j]))
        return list4

    def getEastCoordCropping(self, scaleRatio, eastCoordinates):
        list1 = []
        list4 = []
        for i in range(len(self.east)):
            list1.append(list(eastCoordinates[i]))
        list2 = np.array(list1)
        list3 = list2 * scaleRatio
        for j in range(len(self.east)):
            list4.append(tuple(list3[j]))
        return list4

    def getSouthCoordCropping(self, scaleRatio, southCoordinates):
        list1 = []
        list4 = []
        for i in range(len(self.south)):
            list1.append(list(southCoordinates[i]))
        list2 = np.array(list1)
        list3 = list2 * scaleRatio
        for j in range(len(self.south)):
            list4.append(tuple(list3[j]))
        return list4

    def setScaleRatioFemale(self, scaleRatioFemale):
        self.__scaleRatioFemale = scaleRatioFemale

    def getScaleRatioFemale(self):
        return self.__scaleRatioFemale

    def setIndexCounter(self, index):
        self.__indexCount = index

    def movement(self):
        pass

    def RenderAnimation(self, screen, img, posTup,
                        sprite_sheetCroppingW,
                        sprite_sheetCroppingN,
                        sprite_sheetCroppingE,
                        sprite_sheetCroppingS):
        t1 = pygame.time.get_ticks()
        dt = t1 - self.t0
        screen.blit(img, posTup, sprite_sheetCroppingW[self.__indexCount])
        if dt >= 200:
            # astar.algorithm(self.astar, Agrid, Agrid[1][1], Agrid[2][2])
            self.__indexCount += 1
            if self.__indexCount == len(sprite_sheetCroppingW):
                self.__indexCount = 0
            self.t0 = t1

    def __init__(self, main, startingPos):
        self.main = main
        self.female = pygame.image.load('Assets/Pepper_publish.png')
        self.__scaleRatioFemale = None
        self.ScaleUp = pygame.transform.scale(self.female, (180, 128))
        self.__indexCount = 0
        self.t0 = pygame.time.get_ticks()
        self.mx = None
        self.my = None
        self.previousMovement = []
        self.startingPos = startingPos

        self.west = [(6, 100, 12, 28),
                     (30, 99, 12, 29),
                     (54, 100, 12, 29),
                     (30, 99, 12, 29)]

        self.north = [(3, 3, 18, 29),
                      (27, 2, 18, 30),
                      (51, 3, 18, 29),
                      (27, 2, 18, 30)]

        self.east = [(6, 35, 12, 29),
                     (30, 35, 12, 29),
                     (54, 36, 12, 28),
                     (30, 35, 12, 29)]

        self.south = [(3, 67, 18, 29),
                      (27, 66, 18, 30),
                      (51, 67, 18, 29),
                      (27, 66, 18, 30)]
