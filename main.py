import pygame
from Board import Board
import random


class main:

    def __init__(self):
        pygame.init()
        mousePressed = False
        coins = 0
        self.tilebuy = 1
        self.farmlandbuy = 20
        size = (800, 600)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Farming simulator")
        farm = [size[0] / 10, size[1] / 10, 3, 3]
        farm2 = [size[0] / 2, size[1] / 10, 3, 7]
        farm3 = [size[0] / 10, size[1] / 2, 3, 3]
        farmarray = [farm, farm2, farm3]
        farmland = [Board(farm[0], farm[1], farm[2], farm[3], self),
                    Board(farm2[0], farm2[1], farm2[2], farm2[3], self),
                    Board(farm3[0], farm3[1], farm3[2], farm3[3], self)]
        for i in range(farmarray[0][2]):
            for j in range(farmarray[0][3]):
                farmland[0].grid[i][j].isHardLocked = False
        farmland[0].grid[0][0].islocked = False
        font = pygame.font.Font('COMIC.TTF', 20)
        carryOn = True
        clock = pygame.time.Clock()
        # -------- Main Program Loop -----------
        while carryOn:
            text = font.render(f'Coins: {coins}', True, (255, 255, 255), (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (50, 50)

            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    carryOn = False

                if not pygame.mouse.get_pressed()[0] and mousePressed == True:
                    mousePressed = False
                    mousePos = pygame.mouse.get_pos()
                    for k in range(len(farmarray)):
                        for i in range(farmarray[k][2]):
                            for j in range(farmarray[k][3]):
                                if farmarray[k][0] + (i * 70) <= mousePos[0] <= farmarray[k][0] + (i * 70) + 64 \
                                        and farmarray[k][1] + (j * 70) <= mousePos[1] <= farmarray[k][1] + (
                                        j * 70) + 64:
                                    if farmland[k].grid[i][j].isHardLocked and coins >= self.farmlandbuy:
                                        coins -= self.farmlandbuy
                                        self.farmlandbuy += 10
                                        for w in range(farmarray[k][2]):
                                            for q in range(farmarray[k][3]):
                                                farmland[k].grid[w][q].isHardLocked = False
                                        farmland[k].grid[0][0].isLocked = False
                                    elif farmland[k].grid[i][j].islocked and coins >= self.tilebuy \
                                            and not farmland[k].grid[i][j].isHardLocked:
                                        coins -= self.tilebuy
                                        self.tilebuy += 1
                                        farmland[k].grid[i][j].islocked = False
                                    elif farmland[k].grid[i][j].isGrown:
                                        farmland[k].grid[i][j].animating = True
                                        farmland[k].grid[i][j].isGrown = False
                                        coins += 1
                                    elif not farmland[k].grid[i][j].isWatered:
                                        print(i, j)
                                        farmland[k].grid[i][j].animating = True
                                        farmland[k].grid[i][j].isWatered = True
                elif pygame.mouse.get_pressed()[0]:
                    mousePressed = True

            # Main Event loop end
            for k in range(len(farmarray)):
                for i in range(farmarray[k][2]):
                    for j in range(farmarray[k][3]):
                        if farmland[k].grid[i][j].isWatered and not farmland[k].grid[i][j].islocked and not \
                        farmland[k].grid[i][j].isHardLocked:
                            if farmland[k].grid[i][j].growTimer > 0:
                                farmland[k].grid[i][j].growTimer -= clock.get_time()
                                f = random.randint(0, 200)
                                print(f)
                                if f == 30:
                                    farmland[k].grid[i][j].isWatered = False
                            else:
                                farmland[k].grid[i][j].growTimer = farmland[k].grid[i][j].time
                                farmland[k].grid[i][j].isWatered = False
                                farmland[k].grid[i][j].isGrown = True
                                farmland[k].grid[i][j].isShaking = True
                        farmland[k].grid[i][j].animation(1, 20)
                        farmland[k].grid[i][j].shake(4, 80)

            self.screen.fill([0, 0, 0])
            self.screen.blit(text, textRect)
            for k in range(len(farmarray)):
                for i in range(farmarray[k][2]):
                    for j in range(farmarray[k][3]):
                        farmland[k].grid[i][j].draw()

            pygame.display.flip()

            clock.tick(60)

        pygame.quit()


main()
