import math
import pygame


def rescale(X, A, B, C, D):
    newValue = ((float(X - A) / (B - A)) * (D - C)) + C
    return int(round(newValue))


class Tile:

    def __init__(self, posX, posY, gridX, gridY, name, main):
        self.__sizeX = 64
        self.__sizeY = 64
        self.__posX = posX
        self.__posY = posY
        self.defaultPosX = posX
        self.defaultPosY = posY
        self.__gridX = gridX
        self.__gridY = gridY

        self.grassImg = pygame.image.load('Grass/Grass01.png')
        self.grassImg = pygame.transform.scale(self.grassImg, (64, 64))

        self.carrotImg = pygame.image.load('Carrot.png')

        self.name = name  # This is here because why not
        self.main = main
        self.__degree = -360
        self.__angle = -360
        self.shakeCount = 0

        self.time = 2000
        self.growTimer = self.time

        self.isShaking = False
        self.isWatered = False
        self.isGrown = False
        self.animating = False

        self.islocked = True
        self.isHardLocked = True

        self.font = pygame.font.Font('COMIC.TTF', 20)

    # Draws the tile different depending on it's state
    def draw(self):

        # Hard locked
        if self.isHardLocked:
            pygame.draw.rect(self.main.screen, [64, 64, 64], [self.__posX, self.__posY, self.__sizeX, self.__sizeY])
            text = self.font.render(f'{self.main.farmlandbuy}', True, (0, 0, 0), (64, 64, 64))
            textRect = text.get_rect()
            textRect.center = (self.__posX + (self.__sizeX / 2), self.__posY + (self.__sizeY / 2))
            self.main.screen.blit(text, textRect)

        # Locked
        elif self.islocked:
            pygame.draw.rect(self.main.screen, [192, 192, 192], [self.__posX, self.__posY, self.__sizeX, self.__sizeY])
            text = self.font.render(f'{self.main.tilebuy}', True, (0, 0, 0), (192, 192, 192))
            textRect = text.get_rect()
            textRect.center = (self.__posX + (self.__sizeX / 2), self.__posY + (self.__sizeY / 2))
            self.main.screen.blit(text, textRect)

        # Grown
        elif self.isGrown:
            pygame.draw.rect(self.main.screen, [0, 255, 0], [self.__posX, self.__posY, self.__sizeX, self.__sizeY])

        # Ready to be watered for the first time (Red)
        elif not self.isWatered and not self.isGrown and self.growTimer == self.time:
            self.main.screen.blit(self.grassImg, (self.__posX, self.__posY))

        # Watered
        elif self.isWatered:
            pygame.draw.rect(self.main.screen, [0, 255, 0], [self.__posX, self.__posY, self.__sizeX, self.__sizeY])
            pygame.draw.rect(self.main.screen, [0, 0, 255], [self.__posX, self.__posY, self.__sizeX,

                                                             # Scales the growth timer from 0 and 2000
                                                             # to a number between 0 and 64
                                                             rescale(self.growTimer, 0, self.time, 0, self.__sizeY)])

        # Ready to be watered again after it failed the tick method (yellow and blue)
        else:
            pygame.draw.rect(self.main.screen, [255, 255, 0], [self.__posX, self.__posY, self.__sizeX, self.__sizeY])
            pygame.draw.rect(self.main.screen, [0, 0, 255], [self.__posX, self.__posY, self.__sizeX,

                                                             # Scales the growth timer from 0 and 2000
                                                             # to a number between 0 and 64
                                                             rescale(self.growTimer, 0, self.time, 0, self.__sizeY)])

    # Animation click
    def animation(self, scale, speed):
        if self.animating:

            # Makes the square bigger and the back to original size
            if 0 <= self.__degree < 360:
                self.__posX += -math.sin(math.radians(self.__degree)) * scale
                self.__posY += -math.sin(math.radians(self.__degree)) * scale
                self.__sizeX += math.sin(math.radians(self.__degree)) * 2 * scale
                self.__sizeY += math.sin(math.radians(self.__degree)) * 2 * scale
                self.__degree += speed

            # Makes the square smaller and then back to original size
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

    # Animation Shake
    def shake(self, scale, speed):

        # Makes the square move in all directions (NV, NE, SV, SE)
        if self.isShaking:
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

            # Once done 2 times it stops (Change the shake count to more then 2 for more shaking)
            elif self.shakeCount == 2:
                self.__posX = self.defaultPosX
                self.__posY = self.defaultPosY
                self.__angle = -720
                self.shakeCount = 0
                self.isShaking = False

            # Repeat's the cycle goes to all the corners again
            else:
                self.__angle = -720
                self.shakeCount += 1

    def getGridIndexes(self) -> []:
        return [self.__gridX, self.__gridY]