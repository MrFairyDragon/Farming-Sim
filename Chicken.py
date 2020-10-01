import pygame

pygame.init()


# farmland[k].grid[0][0].__posX
# farmland[k].grid[0][0].__posY
class Chicken:
    def __init__(self, displayName: pygame.display, main):
        self.displayName = displayName
        self.main = main

        # create a surface object, image is drawn on it.
        self.image = pygame.image.load("Choiken.gif")
        self.bigImage = pygame.transform.scale(self.image, (55, 55))

    stepCounter: int = 0

    gridPlacementX: int = 0
    gridPlacementY: int = 0

    isTileCorrect: bool = False
    whichTile: int

    def drawChicken(self, posX, posY):
        self.displayName.blit(self.bigImage, (posX, posY))

    def chickenWalk(self):
        self.stepCounter += 1
        print(self.stepCounter)
        if self.stepCounter > 100:
            if self.whichTile == 1:
                if not self.main.farmland[0].grid[1][0].islocked:
                    self.gridPlacementX = 1
                    self.gridPlacementY = 0
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[2][0].islocked:
                    self.gridPlacementX = 2
                    self.gridPlacementY = 0
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[0][1].islocked:
                    self.gridPlacementX = 0
                    self.gridPlacementY = 1
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[1][1].islocked:
                    self.gridPlacementX = 1
                    self.gridPlacementY = 1
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[2][1].islocked:
                    self.gridPlacementX = 2
                    self.gridPlacementY = 1
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[0][2].islocked:
                    self.gridPlacementX = 0
                    self.gridPlacementY = 2
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[1][2].islocked:
                    self.gridPlacementX = 1
                    self.gridPlacementY = 2
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[2][2].islocked:
                    self.gridPlacementX = 2
                    self.gridPlacementY = 2
                    self.stepCounter = 0
                else:
                    self.gridPlacementX = 0
                    self.gridPlacementY = 0
            elif self.whichTile == 2:
                if not self.main.farmland[0].grid[2][0].islocked:
                    self.gridPlacementX = 2
                    self.gridPlacementY = 0
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[0][1].islocked:
                    self.gridPlacementX = 0
                    self.gridPlacementY = 1
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[1][1].islocked:
                    self.gridPlacementX = 1
                    self.gridPlacementY = 1
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[2][1].islocked:
                    self.gridPlacementX = 2
                    self.gridPlacementY = 1
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[0][2].islocked:
                    self.gridPlacementX = 0
                    self.gridPlacementY = 2
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[1][2].islocked:
                    self.gridPlacementX = 1
                    self.gridPlacementY = 2
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[2][2].islocked:
                    self.gridPlacementX = 2
                    self.gridPlacementY = 2
                    self.stepCounter = 0
                else:
                    self.gridPlacementX = 0
                    self.gridPlacementY = 0
            elif self.whichTile == 3:
                if not self.main.farmland[0].grid[0][1].islocked:
                    self.gridPlacementX = 0
                    self.gridPlacementY = 1
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[1][1].islocked:
                    self.gridPlacementX = 1
                    self.gridPlacementY = 1
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[2][1].islocked:
                    self.gridPlacementX = 2
                    self.gridPlacementY = 1
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[0][2].islocked:
                    self.gridPlacementX = 0
                    self.gridPlacementY = 2
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[1][2].islocked:
                    self.gridPlacementX = 1
                    self.gridPlacementY = 2
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[2][2].islocked:
                    self.gridPlacementX = 2
                    self.gridPlacementY = 2
                    self.stepCounter = 0
                else:
                    self.gridPlacementX = 0
                    self.gridPlacementY = 0
            elif self.whichTile == 4:
                if not self.main.farmland[0].grid[1][1].islocked:
                    self.gridPlacementX = 1
                    self.gridPlacementY = 1
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[2][1].islocked:
                    self.gridPlacementX = 2
                    self.gridPlacementY = 1
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[0][2].islocked:
                    self.gridPlacementX = 0
                    self.gridPlacementY = 2
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[1][2].islocked:
                    self.gridPlacementX = 1
                    self.gridPlacementY = 2
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[2][2].islocked:
                    self.gridPlacementX = 2
                    self.gridPlacementY = 2
                    self.stepCounter = 0
                else:
                    self.gridPlacementX = 0
                    self.gridPlacementY = 0
            elif self.whichTile == 5:
                if not self.main.farmland[0].grid[2][1].islocked:
                    self.gridPlacementX = 2
                    self.gridPlacementY = 1
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[0][2].islocked:
                    self.gridPlacementX = 0
                    self.gridPlacementY = 2
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[1][2].islocked:
                    self.gridPlacementX = 1
                    self.gridPlacementY = 2
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[2][2].islocked:
                    self.gridPlacementX = 2
                    self.gridPlacementY = 2
                    self.stepCounter = 0
                else:
                    self.gridPlacementX = 0
                    self.gridPlacementY = 0
            elif self.whichTile == 6:
                if not self.main.farmland[0].grid[0][2].islocked:
                    self.gridPlacementX = 0
                    self.gridPlacementY = 2
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[1][2].islocked:
                    self.gridPlacementX = 1
                    self.gridPlacementY = 2
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[2][2].islocked:
                    self.gridPlacementX = 2
                    self.gridPlacementY = 2
                    self.stepCounter = 0
                else:
                    self.gridPlacementX = 0
                    self.gridPlacementY = 0
            elif self.whichTile == 7:
                if not self.main.farmland[0].grid[1][2].islocked:
                    self.gridPlacementX = 1
                    self.gridPlacementY = 2
                    self.stepCounter = 0
                elif not self.main.farmland[0].grid[2][2].islocked:
                    self.gridPlacementX = 2
                    self.gridPlacementY = 2
                    self.stepCounter = 0
                else:
                    self.gridPlacementX = 0
                    self.gridPlacementY = 0
            elif self.whichTile == 8:
                if not self.main.farmland[0].grid[2][2].islocked:
                    self.gridPlacementX = 2
                    self.gridPlacementY = 2
                    self.stepCounter = 0
                else:
                    self.gridPlacementX = 0
                    self.gridPlacementY = 0

            else:
                self.gridPlacementX = 0
                self.gridPlacementY = 0
            self.stepCounter = 0

    def eatGrass(self):
        for i in range(3):
            for j in range(3):
                if self.gridPlacementX == i and self.gridPlacementY == j:
                    if self.main.farmland[0].grid[i][j].isGrown:
                        self.main.farmland[0].grid[i][j].animating = True
                        self.main.farmland[0].grid[i][j].isGrown = False
                        self.main.coins += 2

    def checkTile(self):
        for i in range(3):
            for j in range(3):
                if self.gridPlacementX == i and self.gridPlacementY == j:
                    self.isTileCorrect = True

                    if j == 0 and i == 0 and self.isTileCorrect:
                        self.whichTile = 1

                    elif j == 0 and i == 1 and self.isTileCorrect:
                        self.whichTile = 2

                    elif j == 0 and i == 2 and self.isTileCorrect:
                        self.whichTile = 3

                    elif j == 1 and i == 0 and self.isTileCorrect:
                        self.whichTile = 4

                    elif j == 1 and i == 1 and self.isTileCorrect:
                        self.whichTile = 5

                    elif j == 1 and i == 2 and self.isTileCorrect:
                        self.whichTile = 6

                    elif j == 2 and i == 0 and self.isTileCorrect:
                        self.whichTile = 7

                    elif j == 2 and i == 1 and self.isTileCorrect:
                        self.whichTile = 8

                    elif j == 2 and i == 2 and self.isTileCorrect:
                        self.whichTile = 9
        print(self.whichTile)
    # def checkUnlock(self):
    # self.main.farmland[0].grid[0][0].islocked
    # if self.main.farmland[0].grid[0][0].islocked
