import pygame
import math


def rescale(X, A, B, C, D):
    newValue = ((float(X - A) / (B - A)) * (D - C)) + C
    return int(round(newValue))


class Tile:

    def __init__(self, posX, posY, name, main):
        self.__sizeX = 64
        self.__sizeY = 64
        self.__posX = posX
        self.__posY = posY
        self.defaultPosX = posX
        self.defaultPosY = posY
        self.name = name
        self.main = main
        self.__degree = -360
        self.__angle = -360
        self.shakeCount = 0

        self.isShaking = False
        self.isWatered = False
        self.isGrown = False
        self.islocked = True
        self.time = 2000
        self.growTimer = self.time
        self.animating = False
        self.isHardLocked = True
        self.font = pygame.font.Font('COMIC.TTF', 20)
        print(self.main)

    def draw(self):
        if self.isHardLocked:
            pygame.draw.rect(self.main.screen, [64, 64, 64], [self.__posX, self.__posY, self.__sizeX, self.__sizeY])
            text = self.font.render(f'{self.main.farmlandbuy}', True, (0, 0, 0), (64, 64, 64))
            textRect = text.get_rect()
            textRect.center = (self.__posX+(self.__sizeX/2), self.__posY+(self.__sizeY/2))
            self.main.screen.blit(text, textRect)
        elif self.islocked:
            pygame.draw.rect(self.main.screen, [192, 192, 192], [self.__posX, self.__posY, self.__sizeX, self.__sizeY])
            text = self.font.render(f'{self.main.tilebuy}', True, (0, 0, 0), (192, 192, 192))
            textRect = text.get_rect()
            textRect.center = (self.__posX+(self.__sizeX/2), self.__posY+(self.__sizeY/2))
            self.main.screen.blit(text, textRect)
        elif self.isGrown:
            pygame.draw.rect(self.main.screen, [0, 255, 0], [self.__posX, self.__posY, self.__sizeX, self.__sizeY])

        elif not self.isWatered and not self.isGrown and self.growTimer == self.time:
            pygame.draw.rect(self.main.screen, [255, 0, 0], [self.__posX, self.__posY, self.__sizeX, self.__sizeY])

        elif self.isWatered:
            pygame.draw.rect(self.main.screen, [0, 255, 0], [self.__posX, self.__posY, self.__sizeX, self.__sizeY])
            pygame.draw.rect(self.main.screen, [0, 0, 255], [self.__posX, self.__posY, self.__sizeX,
                                                          rescale(self.growTimer, 0, self.time, 0, self.__sizeY)])

        else:
            pygame.draw.rect(self.main.screen, [255, 255, 0], [self.__posX, self.__posY, self.__sizeX, self.__sizeY])
            pygame.draw.rect(self.main.screen, [0, 0, 255], [self.__posX, self.__posY, self.__sizeX,
                                                          rescale(self.growTimer, 0, self.time, 0, self.__sizeY)])

    def animation(self, scale, speed):
        if self.animating:
            if 0 <= self.__degree < 360:
                self.__posX += -math.sin(math.radians(self.__degree)) * scale
                self.__posY += -math.sin(math.radians(self.__degree)) * scale
                self.__sizeX += math.sin(math.radians(self.__degree)) * 2 * scale
                self.__sizeY += math.sin(math.radians(self.__degree)) * 2 * scale
                self.__degree += speed
            elif -360 <= self.__degree < 0:
                self.__posX += -math.sin(math.radians(self.__degree) - math.pi) * scale
                self.__posY += -math.sin(math.radians(self.__degree) - math.pi) * scale
                self.__sizeX += math.sin(math.radians(self.__degree) - math.pi) * 2 * scale
                self.__sizeY += math.sin(math.radians(self.__degree) - math.pi) * 2 * scale
                self.__degree += speed

            else:
                self.animating = False
                self.__sizeX = 64
                self.__sizeY = 64
                self.__posX = self.defaultPosX
                self.__posY = self.defaultPosY
                self.__degree = -360

    def shake(self, scale, speed):
        if self.isShaking:
            print(self.__angle)
            if 0 <= self.__angle < 360:
                self.__posX += math.sin(math.radians(self.__angle)) * scale
                self.__posY += math.sin(math.radians(self.__angle)) * scale
                self.__angle += speed
            elif -360 <= self.__angle < 0:
                self.__posX -= math.sin(math.radians(self.__angle)) * scale
                self.__posY += math.sin(math.radians(self.__angle)) * scale
                self.__angle += speed
            elif -720 <= self.__angle < 360:
                self.__posX += math.sin(math.radians(self.__angle)) * scale
                self.__posY -= math.sin(math.radians(self.__angle)) * scale
                self.__angle += speed
            elif 360 <= self.__angle < 720:
                self.__posX -= math.sin(math.radians(self.__angle)) * scale
                self.__posY -= math.sin(math.radians(self.__angle)) * scale
                self.__angle += speed
            elif self.shakeCount == 2:
                self.__posX = self.defaultPosX
                self.__posY = self.defaultPosY
                self.__angle = -720
                self.shakeCount = 0
                self.isShaking = False
            else:
                self.__angle = -720
                self.shakeCount += 1
