import pygame
from Sprinkler import Sprinkler


class Shop:

    def __init__(self, main):
        self.main = main
        self.__posX = self.main.grid.sizeX * 64
        self.__posY = 0
        self.__posOffset = 16
        self.__sizeX = self.main.size[0] -96
        self.__sizeY = self.main.size[1]
        self.buying = None
        self.isBuying = False
        self.sprinklerCount = 0

        self.chickenImg = pygame.image.load('Assets/Chicken.png')
        self.sprinklerImg = pygame.image.load('Assets/Sprinkler.png')
        self.grassImg = pygame.image.load('Assets/Grass/Grass01.png')

    def draw(self):
        pygame.draw.rect(self.main.screen, [192, 192, 192], [self.__posX, self.__posY, self.__sizeX, self.__sizeY])

        # Chicken
        pygame.draw.rect(self.main.screen, [64, 64, 64],
                         [self.__posX + self.__posOffset, self.__posY + (1 * self.__posOffset), 64, 64])
        self.grassImg = pygame.transform.scale(self.grassImg, (64, 64))
        self.main.screen.blit(self.grassImg, (self.__posX + 16, self.__posY + self.__posOffset))
        self.chickenImg = pygame.transform.scale(self.chickenImg, (64, 64))
        self.main.screen.blit(self.chickenImg, (self.__posX + 16, self.__posY + self.__posOffset))

        # Sprinkler
        pygame.draw.rect(self.main.screen, [0, 0, 255], [self.__posX + self.__posOffset,
                                                         self.__posY + 64 + (2 * self.__posOffset), 64, 64])
        self.grassImg = pygame.transform.scale(self.grassImg, (64, 64))
        self.main.screen.blit(self.grassImg,
                              (self.__posX + self.__posOffset, self.__posY + 64 + (2 * self.__posOffset)))
        self.sprinklerImg = pygame.transform.scale(self.sprinklerImg, (64, 64))
        self.main.screen.blit(self.sprinklerImg,
                              (self.__posX + self.__posOffset, self.__posY + 64 + (2 * self.__posOffset)))
        font = pygame.font.Font('Fonts/COMIC.TTF', 16)
        text = font.render(f'{self.sprinklerCount}/4', True, (0, 0, 0), None)
        textRect = text.get_rect()
        textRect.center = (self.__posX + self.__posOffset + 16, self.__posY + 64 + (2 * self.__posOffset) + 48)
        self.main.screen.blit(text, textRect)

        font = pygame.font.Font('Fonts/COMIC.TTF', 16)
        text = font.render(f'10', True, (0, 0, 0), None)
        textRect = text.get_rect()
        textRect.center = (self.__posX + self.__posOffset + 48, self.__posY + 64 + (2 * self.__posOffset) + 48)
        self.main.screen.blit(text, textRect)

        # Sell icon
        pygame.draw.rect(self.main.screen, [64, 64, 64],
                         [self.__posX + self.__posOffset, self.__posY + (1 * self.__posOffset), 64, 64])
        self.grassImg = pygame.transform.scale(self.grassImg, (64, 64))
        self.main.screen.blit(self.grassImg,
                              (self.__posX + self.__posOffset, self.__posY + (2 * 64) + (3 * self.__posOffset)))
        self.chickenImg = pygame.transform.scale(self.chickenImg, (64, 64))
        self.main.screen.blit(self.chickenImg,
                              (self.__posX + self.__posOffset, self.__posY + (2 * 64) + (3 * self.__posOffset)))
        pygame.draw.rect(self.main.screen, [64, 64, 64],
                         [self.__posX + self.__posOffset, self.__posY + (2 * 64) + (3 * self.__posOffset), 64, 64])

    def clickAndDrag(self):
        mousePosition = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0]:

            # Chicken
            if self.__posX + 16 <= mousePosition[0] <= self.__posX + 16 + 64 \
                    and self.__posY + 16 <= mousePosition[1] <= self.__posY + 16 + 64:
                self.buying = "Chicken"
                self.isBuying = True
                print("bork")

            # Sprinkler
            if self.__posX + 16 <= mousePosition[0] <= self.__posX + 16 + 64 \
                    and self.__posY + 96 <= mousePosition[1] <= self.__posY + 96 + 64:
                self.buying = "Sprinkler"
                self.isBuying = True
                print("drag")

            # Sell
            if self.__posX + 16 <= mousePosition[0] <= self.__posX + 16 + 64 \
                    and self.__posY + 160 <= mousePosition[1] <= self.__posY + 160 + 64:
                print("Heyf")
                self.buying = "Sell"
                self.isBuying = True


        else:
            if self.isBuying:
                self.isBuying = False
                for k in range(len(self.main.farmarray)):
                    for i in range(self.main.farmarray[k][2]):
                        for j in range(self.main.farmarray[k][3]):
                            if (self.main.farmarray[k][0] * 64) + (i * 64) <= mousePosition[0] <= (self.main.farmarray[k][0] * 64) + (
                                    i * 64) + 64 \
                                    and (64 * self.main.farmarray[k][1]) + (j * 64) <= mousePosition[1] <= (
                                    64 * self.main.farmarray[k][1]) + (j * 64) + 64:
                                if self.buying == "Sprinkler":
                                    print("Buy")
                                    self.buySprinkler(self.main.farmland[k].board[i][j], k)
                                    return
                                elif self.buying == "Sell":
                                    print("Sell")
                                    self.sell(self.main.farmland[k].board[i][j], k)
                                    return
            return

    def buySprinkler(self, farmland, k):
        if not farmland.islocked and not farmland.isHardLocked and not farmland.isOccupied:
            if self.main.coins >= 10 and not self.sprinklerCount == 4:
                for i in range(len(self.main.sprinklerArray)):
                    if self.main.sprinklerArray[i] is None:

                        #Needs position
                        self.main.sprinklerArray[i] = Sprinkler(farmland.getGridPos()[0], farmland.getGridPos()[1], self.main, self.main.farmland[k], farmland)
                        self.main.sprinklerArray[i].gadgetInitiate()
                        self.sprinklerCount += 1
                        self.main.coins -= 10
                        farmland.isOccupied = True
                        farmland.name = 'Sprinkler'
                        for j in range(len(self.main.sprinklerArray)):
                            print(self.main.sprinklerArray[j])
                        return
        self.buying = None

    def sell(self, farmland, k):
        if farmland.isOccupied and not farmland.islocked and not farmland.isHardLocked:
            if farmland.name == 'Sprinkler':
                for i in range(len(self.main.sprinklerArray)):
                    if self.main.sprinklerArray[i] is not None:
                        tileLocation = self.main.sprinklerArray[i].getTileLocation()
                        farmlandLocation = farmland.getGridIndexes()
                        if tileLocation == farmlandLocation:
                            self.main.sprinklerArray[i] = None
                            farmland.name = 'Carrot'
                            farmland.isOccupied = False
                            self.main.coins += 5
                            self.sprinklerCount -= 1
                            for j in range(len(self.main.sprinklerArray)):
                                print(self.main.sprinklerArray[j])
        self.buying = None

