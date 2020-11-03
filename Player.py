import pygame
import numpy as np
from Astar import Astar


class Player:
    def DrawCharacter(self, screen, img, pos, getMovement,
                      sprite_sheetCroppingW,
                      sprite_sheetCroppingN,
                      sprite_sheetCroppingE,
                      sprite_sheetCroppingS):
        self.RenderAnimation(screen, img, pos, getMovement,
                             sprite_sheetCroppingW,
                             sprite_sheetCroppingN,
                             sprite_sheetCroppingE,
                             sprite_sheetCroppingS)

    def getMousePos(self):
        ans = []
        self.mx, self.my = pygame.mouse.get_pos()
        self.previousMovement.append((self.mx, self.my))
        return self.previousMovement

    def setCounter2(self):
        self.__counter2 += 1
        # print(self.__counter2)

    def getCounter2(self):
        return self.__counter2

    def setPos(self, a, b):
        self.startingPos = (a, b)
        if self.__counter2 == 0:
            return self.startingPos

    def MovementQueue(self):
        if self.getCounter2() <= 1:
            self.previousMovement2.append([int(self.startingPos[0] / 64), int(self.startingPos[1] / 64)])
            self.previousMovement2.append(self.translateMousePosToGridPos())
        self.previousMovement2.append(self.translateMousePosToGridPos())
        return self.previousMovement2[-3]

    def getMove2(self):
        ans = []
        ans2 = []
        for i in range(len(self.getMove())):
            for j in range(2):
                ans.append(self.getMove()[i][0][j])
        okay = np.asarray(ans)
        okay2 = okay * 64
        for n in range(1, len(okay2)):
            ans2.append((okay2[n-1], okay2[n]))
        ans3 = ans2[::2]
        ans3.reverse()
        return ans3
        # print(ans3)

    def getMovement(self):
        path = Astar.algorithm(self.main.astar, self.main.Agrid,
                               self.main.Agrid[self.MovementQueue()[0]]
                                              [self.MovementQueue()[1]],
                               self.main.Agrid[self.translateMousePosToGridPos()[0]]
                                              [self.translateMousePosToGridPos()[1]])
        ans = []
        for i in range(len(path)):
            ans.append([])
            pos = path[i].get_pos()
            for j in range(1):
                ans[i].append(pos)
        return ans

    def getMove(self):
        return self.__move

    def setMove(self, a):
        self.__move = a

    def translateMousePosToGridPos(self):
        ans = [int(self.getMousePos()[-1][0] / 64), int(self.getMousePos()[-1][1] / 64)]
        if ans[0] <= 10:
            return ans
        else:
            ans2 = [10, int(self.getMousePos()[-1][1] / 64)]
            return ans2

    def getScaledUpCharacter(self, img, scaleRatio):
        self.ScaleUp = pygame.transform.scale(img, (img.get_width() * scaleRatio, img.get_height() * scaleRatio))
        return self.ScaleUp

    def getCoordCropping(self, scaleRatio, direction):
        list1 = []
        list4 = []
        for i in range(len(direction)):
            list1.append(list(direction[i]))
        list2 = np.array(list1)
        list3 = list2 * scaleRatio
        for j in range(len(direction)):
            list4.append(tuple(list3[j]))
        return list4

    def setScaleRatioFemale(self, scaleRatioFemale):
        self.__scaleRatioFemale = scaleRatioFemale

    def getScaleRatioFemale(self):
        return self.__scaleRatioFemale

    def setIndexCounter(self, index):
        self.__indexCount = index

    def setSwitch(self, a):
        self.__switch = a

    def getSwitch(self):
        return self.__switch

    def setSwitch(self):
        self.__switch = True
        self.__indexCount2 = 0

    def getIndexCount2(self):
        return self.__indexCount2

    def RenderAnimation(self, screen, img, posTup, getMovement,
                        sprite_sheetCroppingW,
                        sprite_sheetCroppingN,
                        sprite_sheetCroppingE,
                        sprite_sheetCroppingS):
        t1 = pygame.time.get_ticks()
        dt = t1 - self.t0
        if self.__counter2 == 0:
            screen.blit(img, posTup, sprite_sheetCroppingW[self.__indexCount])
        if self.__counter2 >= 1:
            if self.__switch:
                for i in range(len(getMovement)):
                    screen.blit(img, getMovement[self.__indexCount2], sprite_sheetCroppingW[self.__indexCount])
                if self.__indexCount2 == len(getMovement)-1:
                    self.__switch = False
            if not self.__switch:
                screen.blit(img, getMovement[-1], sprite_sheetCroppingS[1])
        if dt >= 200:
            self.__indexCount += 1
            self.__indexCount2 += 1
            if self.__indexCount == len(sprite_sheetCroppingW):
                self.__indexCount = 0
            self.t0 = t1

    def __init__(self, main):
        self.main = main
        self.female = pygame.image.load('Assets/Pepper_publish.png')
        self.__scaleRatioFemale = None
        self.ScaleUp = pygame.transform.scale(self.female, (180, 128))
        self.__indexCount = 0
        self.t0 = pygame.time.get_ticks()
        self.mx = None
        self.my = None
        self.previousMovement = []
        self.previousMovement2 = []
        self.startingPos = (375, 130)
        self.__counter2 = 0
        self.__move = []
        self.__indexCount2 = 0
        self.__switch = True
        self.__Movement = 0

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
