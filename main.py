import pygame
from Board import Board
from Chicken import Chicken
import random


class main:

    def __init__(self):
        pygame.init()
        mousePressed = False

        self.coins = 0
        self.tilebuy = 1
        self.farmlandbuy = 20

        size = (800, 600)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Farming simulator")
        font = pygame.font.Font('COMIC.TTF', 20)
        carryOn = True
        clock = pygame.time.Clock()

        # Defines Positions of farmland's and the size determined in tiles (posX, posY, sizeX, sizeY)
        farmarray = [[size[0] / 10, size[1] / 10, 3, 3],
                     [size[0] / 2, size[1] / 10, 3, 7],
                     [size[0] / 10, size[1] / 2, 3, 3]]

        # Makes the farmlands with the above positions and sizes
        farmland = [Board(farmarray[0][0], farmarray[0][1], farmarray[0][2], farmarray[0][3], self),
                    Board(farmarray[1][0], farmarray[1][1], farmarray[1][2], farmarray[1][3], self),
                    Board(farmarray[2][0], farmarray[2][1], farmarray[2][2], farmarray[2][3], self)]
        self.farmland = farmland
        test = Chicken(self.screen, self)
        # Unlocks the first farmland and the first tile in the farmland
        for i in range(farmarray[0][2]):
            for j in range(farmarray[0][3]):
                farmland[0].grid[i][j].isHardLocked = False
        farmland[0].grid[0][0].islocked = False

        # -------- Main Program Loop -----------
        while carryOn:
            text = font.render(f'self.Coins: {self.coins}', True, (255, 255, 255), (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (50, 50)

            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    carryOn = False

                # Is called whenever the mouse is pressed not whenever it's clicked
                if not pygame.mouse.get_pressed()[0] and mousePressed == True:
                    mousePressed = False
                    mousePos = pygame.mouse.get_pos()

                    # Runs trough all the tiles
                    for k in range(len(farmarray)):
                        for i in range(farmarray[k][2]):
                            for j in range(farmarray[k][3]):

                                # Mouse clicks on tile
                                if farmarray[k][0] + (i * 70) <= mousePos[0] <= farmarray[k][0] + (i * 70) + 64 \
                                        and farmarray[k][1] + (j * 70) <= mousePos[1] <= farmarray[k][1] + (
                                        j * 70) + 64:

                                    # Tile is hard locked
                                    if farmland[k].grid[i][j].isHardLocked and self.coins >= self.farmlandbuy:
                                        self.coins -= self.farmlandbuy
                                        self.farmlandbuy += 10

                                        for w in range(farmarray[k][2]):
                                            for q in range(farmarray[k][3]):
                                                farmland[k].grid[w][q].isHardLocked = False

                                    # Tile is locked
                                    elif farmland[k].grid[i][j].islocked and self.coins >= self.tilebuy \
                                            and not farmland[k].grid[i][j].isHardLocked:
                                        self.coins -= self.tilebuy
                                        self.tilebuy += 1
                                        farmland[k].grid[i][j].islocked = False

                                    # Tile is grown
                                    elif farmland[k].grid[i][j].isGrown:
                                        farmland[k].grid[i][j].animating = True
                                        farmland[k].grid[i][j].isGrown = False
                                        self.coins += 1

                                    # Tile is watered
                                    elif not farmland[k].grid[i][j].isWatered:
                                        print(i, j)
                                        farmland[k].grid[i][j].animating = True
                                        farmland[k].grid[i][j].isWatered = True

                # This is done to get a click instead of a press
                elif pygame.mouse.get_pressed()[0]:
                    mousePressed = True

            # Main Event loop end

            # This is the main loop the difference between this loop and the main event loop is that the other loop
            # only runs when a event is called (mouse movement, keys pressed, mouse clicked)

            # Runs trough all tiles
            for k in range(len(farmarray)):
                for i in range(farmarray[k][2]):
                    for j in range(farmarray[k][3]):

                        # Checks if the tiles is watered and not locked
                        if farmland[k].grid[i][j].isWatered and not farmland[k].grid[i][j].islocked and not \
                                farmland[k].grid[i][j].isHardLocked:

                            # Checks if the timer is below 0
                            if farmland[k].grid[i][j].growTimer > 0:
                                farmland[k].grid[i][j].growTimer -= clock.get_time()

                                # Gets a random number between 0 and 199
                                f = random.randint(0, 200)
                                if f == 30:
                                    farmland[k].grid[i][j].isWatered = False

                            # Checks
                            else:
                                farmland[k].grid[i][j].growTimer = farmland[k].grid[i][j].time
                                farmland[k].grid[i][j].isWatered = False
                                farmland[k].grid[i][j].isGrown = True
                                farmland[k].grid[i][j].isShaking = True

                        # Runs the animations all the time but they are only active
                        # if there booleans are true (read line 88)
                        farmland[k].grid[i][j].shake(4, 80)
                        farmland[k].grid[i][j].animation(1, 20)

            # Draws everything on the screen
            self.screen.fill([0, 0, 0])
            skyImg = pygame.image.load('Sky_Skrr.png')
            self.screen.blit(skyImg, (0, 0))
            self.screen.blit(text, textRect)
            for k in range(len(farmarray)):
                for i in range(farmarray[k][2]):
                    for j in range(farmarray[k][3]):
                        farmland[k].grid[i][j].draw()
            test.drawChicken(farmland[0].grid[test.gridPlacementX][test.gridPlacementY].defaultPosX,
                             farmland[0].grid[test.gridPlacementX][test.gridPlacementY].defaultPosY)
            test.chickenWalk()
            test.eatGrass()
            pygame.display.flip()

            clock.tick(60)

        pygame.quit()
