import math
import pygame
import random

from GameObject import GameObject


def rescale(X, A, B, C, D):
    newValue = ((float(X - A) / (B - A)) * (D - C)) + C
    return int(round(newValue))


class Tile:

    def __init__(self, posX, posY, gridX, gridY, name, main, farmindex):
        self.__sizeX = 64
        self.__sizeY = 64
        self.__posX = posX
        self.__posY = posY
        self.defaultPosX = posX
        self.defaultPosY = posY
        self.__gridX = gridX
        self.__gridY = gridY
        self.farmindex = farmindex

        self.__degree = -360
        self.__angle = -720

        self.name = name  # This is here because why not
        self.main = main
        self.shakeCount = 0

        self.time = 2000
        self.growTimer = self.time

        self.isOccupied = False
        self.isShaking = False
        self.isWatered = False
        self.isGrown = False
        self.animating = False

        self.islocked = True
        self.isHardLocked = True

    def drawRect(self, color):
        pygame.draw.rect(self.main.screen, color, [self.__posX, self.__posY, self.__sizeX, self.__sizeY])

    def drawTile(self, index, backgroundImg, foregroundImg ):
        grassImg = pygame.image.load(backgroundImg)
        grassImg = pygame.transform.scale(grassImg, [int(self.__sizeX), int(self.__sizeY)])
        carrotImg = pygame.image.load(foregroundImg)
        carrotImg = pygame.transform.scale(carrotImg, [int(self.__sizeX), int(self.__sizeY)])
        self.main.screen.blit(grassImg, (self.__posX, self.__posY))

        if index == 0:
            return
        elif index == 1:
            carrotImgChop = pygame.transform.chop(carrotImg, (0, 0, 0, rescale(self.growTimer, 0, self.time, 0, 64)))
            self.main.screen.blit(carrotImgChop, (self.__posX, (self.__posY + rescale(self.growTimer, 0, self.time,
                                                                                      0, 64))))
        elif index == 2:
            self.main.screen.blit(carrotImg, (self.__posX, self.__posY))

    def addText(self, text, textColor):
        font = pygame.font.Font('Fonts/COMIC.TTF', 20)
        text = font.render(text, True, textColor, None)
        textRect = text.get_rect()
        textRect.center = (self.__posX + (self.__sizeX / 2), self.__posY + (self.__sizeY / 2))
        self.main.screen.blit(text, textRect)

    # Draws the tile different depending on it's state
    def draw(self):
        if self.isHardLocked:
            self.drawRect([64, 64, 64])
            self.addText(f'{self.main.farmlandbuy}', (0, 0, 0))

        elif self.islocked:
            self.drawRect([192, 192, 192])
            self.addText(f'{self.main.tilebuy}', (0, 0, 0))

        elif self.isGrown:
            self.drawTile(2, 'Assets/Grass/Grass01.png', f'Assets/{self.name}.png')

        # Ready to be watered for the first time (Red)
        elif not self.isWatered and not self.isGrown and self.growTimer == self.time and not self.isOccupied:
            self.drawTile(0, 'Assets/Grass/Grass01.png', f'Assets/{self.name}.png')

        elif self.isWatered:
            self.drawTile(1, 'Assets/Grass/Grass01.png', f'Assets/{self.name}.png')

        elif self.isOccupied:
            self.drawTile(2, 'Assets/Grass/Grass01.png', f'Assets/{self.name}.png')

        # Ready to be watered again after it failed the tick method (yellow and blue)
        else:
            self.drawTile(1, 'Assets/Grass/Grass01.png', f'Assets/{self.name}.png')

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
            elif -720 <= self.__angle < -360:
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

    def hardUnlock(self):
        self.main.coins -= self.main.farmlandbuy
        self.main.farmlandbuy += 10
        for i in range(self.main.farmarray[self.farmindex][2]):
            for j in range(self.main.farmarray[self.farmindex][3]):
                self.main.farmland[self.farmindex].board[i][j].isHardLocked = False
        self.islocked = False

    def unlock(self):
        self.main.coins -= self.main.tilebuy
        self.main.tilebuy += 1
        self.islocked = False

    def harvest(self):
        self.isGrown = False
        self.main.coins += 1

    def water(self):
        if not self.isOccupied:
            self.isWatered = True

    def grow(self):
        if self.isWatered and not self.islocked and not \
                self.isHardLocked:

            # Checks if the timer is below 0
            if self.growTimer > 0:
                self.growTimer -= self.main.clock.get_time()

                # Gets a random number between 0 and 199
                f = random.randint(0, 200)
                if f == 30:
                    self.isWatered = False

            # Checks
            else:
                self.growTimer = self.time
                self.isWatered = False
                self.isGrown = True
                self.isShaking = True

        # Runs the animations all the time but they are only active
        # if there booleans are true (read line 98)
        self.shake(4, 120)
        self.animation(2, 40)
