from Chicken import Chicken
import pygame
from Sprinkler import Sprinkler


class Shop:

    def __init__(self, main):
        self.main = main
        self.__posX = self.main.size[0] - self.main.size[0] / 8
        self.__posY = 0
        self.__posOffset = 16
        self.__sizeX = self.main.size[0] / 8
        self.__sizeY = self.main.size[1]
        self.buying = None
        self.isBuying = False
        self.sprinklerCount = 0

        self.chickenImg = pygame.image.load('Choiken.gif')

    def draw(self):
        self.main.screen
        pygame.draw.rect(self.main.screen, [192, 192, 192], [self.__posX, self.__posY, self.__sizeX, self.__sizeY])

        #Chicken
        pygame.draw.rect(self.main.screen, [64, 64, 64], [self.__posX+self.__posOffset, self.__posY+(1 * self.__posOffset), 64, 64])
        self.chickenImg = pygame.transform.scale(self.chickenImg, (64, 64))
        self.main.screen.blit(self.chickenImg, (self.__posX+16, self.__posY+self.__posOffset))

        #Sprinkler
        pygame.draw.rect(self.main.screen, [0, 0, 255], [self.__posX + self.__posOffset,
                                                         self.__posY + 64 + (2 * self.__posOffset), 64, 64])
        font = pygame.font.Font('COMIC.TTF', 16)
        text = font.render(f'{self.sprinklerCount}/4', True, (0, 0, 0), None)
        textRect = text.get_rect()
        textRect.center = (self.__posX + self.__posOffset+16, self.__posY + 64 + (2 * self.__posOffset)+48)
        self.main.screen.blit(text, textRect)

        font = pygame.font.Font('COMIC.TTF', 16)
        text = font.render(f'10', True, (0, 0, 0), None)
        textRect = text.get_rect()
        textRect.center = (self.__posX + self.__posOffset + 48, self.__posY + 64 + (2 * self.__posOffset) + 48)
        self.main.screen.blit(text, textRect)

    def clickAndDrag(self):
        mousePosition = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0]:

            #Chicken
            if self.__posX+16 <= mousePosition[0] <= self.__posX+16+64 \
                    and self.__posY+16 <= mousePosition[1] <= self.__posY+16+64:
                    self.buying = "Chicken"
                    self.isBuying = True
                    print("bork")

            #Sprinkler
            if self.__posX + 16 <= mousePosition[0] <= self.__posX + 16 + 64 \
                    and self.__posY + 96 <= mousePosition[1] <= self.__posY + 96 + 64:
                        self.buying = "Sprinkler"
                        self.isBuying = True
                        print("drag")

        else:
            if self.isBuying:
                self.isBuying = False
                for k in range(len(self.main.farmarray)):
                    for i in range(self.main.farmarray[k][2]):
                        for j in range(self.main.farmarray[k][3]):
                            if self.main.farmarray[k][0] + (i * 70) <= mousePosition[0]\
                                    <= self.main.farmarray[k][0] + (i * 70) + 64 \
                                    and self.main.farmarray[k][1] + (j * 70) <= mousePosition[1]\
                                    <= self.main.farmarray[k][1] + (
                                    j * 70) + 64:
                                if self.buying == "Sprinkler":
                                    self.buySprinkler(self.main.farmland[k].grid[i][j], k)
                                    return


    def buySprinkler(self, farmland, k):
        if not farmland.islocked and not farmland.isHardLocked:
            if self.main.coins >= 10 and not self.sprinklerCount == 4:
                self.main.coins -= 10
                self.main.sprinklerArray[self.sprinklerCount] = Sprinkler(self.main.farmland[k], farmland, self.main)
                self.main.sprinklerArray[self.sprinklerCount].gadgetInitiate()
                self.sprinklerCount += 1
                print(self.sprinklerCount)
        self.buying = None