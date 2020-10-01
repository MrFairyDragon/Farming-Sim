import pygame
from Board import Board
from Chicken import Chicken
from Shop import Shop
import random


class main:

    def __init__(self):
        pygame.init()
        mousePressed = False

        self.coins = 1000
        self.tilebuy = 1
        self.farmlandbuy = 20
        self.sprinklerArray = [None, None, None, None, None]

        self.size = (800, 600)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Farming simulator")
        font = pygame.font.Font('COMIC.TTF', 20)
        carryOn = True
        self.clock = pygame.time.Clock()

        # Defines Positions of self.farmland's and the self.size determined in tiles (posX, posY, self.sizeX,
        # self.sizeY)
        self.farmarray = [[self.size[0] / 10, self.size[1] / 10, 3, 3],
                     [self.size[0] / 2, self.size[1] / 10, 3, 7],
                     [self.size[0] / 10, self.size[1] / 2, 3, 3]]

        # Makes the self.farmlands with the above positions and self.sizes
        self.farmland = [Board(self.farmarray[0][0], self.farmarray[0][1], self.farmarray[0][2], self.farmarray[0][3], self, 0),
                    Board(self.farmarray[1][0], self.farmarray[1][1], self.farmarray[1][2], self.farmarray[1][3], self, 1),
                    Board(self.farmarray[2][0], self.farmarray[2][1], self.farmarray[2][2], self.farmarray[2][3], self, 2)]

        test = Chicken(self.screen, self)
        shop = Shop(self)
        # Unlocks the first self.farmland and the first tile in the self.farmland
        for i in range(self.farmarray[0][2]):
            for j in range(self.farmarray[0][3]):
                self.farmland[0].grid[i][j].isHardLocked = False
        self.farmland[0].grid[0][0].islocked = False

        # -------- Main Program Loop -----------
        while carryOn:
            text = font.render(f'Coins: {self.coins}', True, (255, 255, 255), None)
            textRect = text.get_rect()
            textRect.center = (50, 25)

            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    carryOn = False

                # Is called whenever the mouse is pressed not whenever it's clicked
                Shop.clickAndDrag(shop)
                if not pygame.mouse.get_pressed()[0] and mousePressed == True and shop.buying == None:
                    mousePressed = False
                    mousePos = pygame.mouse.get_pos()


                    # Runs trough all the tiles
                    for k in range(len(self.farmarray)):
                        for i in range(self.farmarray[k][2]):
                            for j in range(self.farmarray[k][3]):

                                # Mouse clicks on tile
                                if self.farmarray[k][0] + (i * 70) <= mousePos[0] <= self.farmarray[k][0] + (i * 70) + 64 \
                                        and self.farmarray[k][1] + (j * 70) <= mousePos[1] <= self.farmarray[k][1] + (
                                        j * 70) + 64:

                                    self.farmland[k].grid[i][j].animating = True

                                    # Tile is hard locked
                                    if self.farmland[k].grid[i][j].isHardLocked and self.coins >= self.farmlandbuy:
                                        self.farmland[k].grid[i][j].hardUnlock()

                                    # Tile is locked
                                    elif self.farmland[k].grid[i][j].islocked and self.coins >= self.tilebuy \
                                            and not self.farmland[k].grid[i][j].isHardLocked:
                                        self.farmland[k].grid[i][j].unlock()

                                    # Tile is grown
                                    elif self.farmland[k].grid[i][j].isGrown:
                                        self.farmland[k].grid[i][j].harvest()

                                    # Tile is watered
                                    elif not self.farmland[k].grid[i][j].isWatered:
                                        self.farmland[k].grid[i][j].water()

                # This is done to get a click instead of a press
                elif pygame.mouse.get_pressed()[0] and shop.isBuying == False:
                    mousePressed = True

            # Main Event loop end

            # This is the main loop the difference between this loop and the main event loop is that the other loop
            # only runs when a event is called (mouse movement, keys pressed, mouse clicked)

            # Runs trough all tiles
            for k in range(len(self.farmarray)):
                for i in range(self.farmarray[k][2]):
                    for j in range(self.farmarray[k][3]):
                        self.farmland[k].grid[i][j].grow()

            # Draws everything on the screen
            self.screen.fill([0, 0, 0])
            self.skyImg = pygame.image.load('Sky_Skrr.png')
            self.screen.blit(self.skyImg, (0, 0))
            self.screen.blit(text, textRect)

            for k in range(len(self.farmarray)):
                for i in range(self.farmarray[k][2]):
                    for j in range(self.farmarray[k][3]):
                        self.farmland[k].grid[i][j].draw()

            for i in range(len(self.sprinklerArray)):
                if not self.sprinklerArray[i] == None:
                    self.sprinklerArray[i].gadgetActivate()
            test.drawChicken(self.farmland[0].grid[test.gridPlacementX][test.gridPlacementY].defaultPosX,
                             self.farmland[0].grid[test.gridPlacementX][test.gridPlacementY].defaultPosY)
            test.checkTile()
            test.chickenWalk()
            test.eatGrass()
            shop.draw()
            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()
