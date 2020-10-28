import pygame
import numpy as np
from Board import Board
from Chicken import Chicken
from Shop import Shop
from Node import Node
from Grid import Grid
from astar import astar
from GameObject import GameObject
import random
from Player import Player


class main:

    def __init__(self):
        pygame.init()
        mousePressed = False
        self.coins = 1000
        self.tilebuy = 1
        self.farmlandbuy = 20
        self.sprinklerArray = [None, None, None, None, None]
        self.Player = Player(self, (375, 130))
        self.size = (800, 576)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Farming simulator")
        font = pygame.font.Font('Fonts/COMIC.TTF', 20)
        carryOn = True
        self.clock = pygame.time.Clock()
        self.counter = 0
        self.skyImg = pygame.image.load('Assets/Sky_Skrr.png')
        self.isTrue = True
        self.grid = Grid(self, 10, 12)
        self.Player.setIndexCounter(0)
        # Defines Positions of self.farmland's and the self.size determined in tiles (posX, posY, self.sizeX,
        # self.sizeY)

        self.farmarray = [[64, 64, 3, 3],
                          [320, 64, 3, 7],
                          [64, 320, 3, 3]]
        self.farmland = np.ndarray(shape=(len(self.farmarray)), dtype=Board)
        # Makes the self.farmlands with the above positions and self.sizes
        for i in range(len(self.farmarray)):
            # print(i)
            self.farmland[i] = Board(self.farmarray[i][0], self.farmarray[i][1], self.farmarray[i][2],
                                     self.farmarray[i][3], self, self.grid, i)

        test = Chicken(self.screen, self.farmland[1], self)
        shop = Shop(self)
        self.astar = astar()
        Agrid = astar.make_grid(self.astar, self.grid.sizeX, self.grid.sizeY, self)
        for i in range(len(Agrid)):
            for j in range(len(Agrid)):
                node = Agrid[i][j]
                print(Agrid[i][j])
                node.update_neighbors(Agrid)
                # astar.algorithm(self.astar, Agrid, Agrid[1][1], Agrid[9][9])

        # Unlocks the first self.farmland and the first tile in the self.farmland
        for i in range(self.farmarray[0][2]):
            for j in range(self.farmarray[0][3]):
                self.farmland[0].board[i][j].isHardLocked = False
        self.farmland[0].board[0][0].islocked = False

        # -------- Main Program Loop -----------

        while carryOn:
            text = font.render(f'Coins: {self.coins}', True, (255, 255, 255), None)
            textRect = text.get_rect()
            textRect.center = (50, 25)
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    carryOn = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    astar.algorithm(self.astar, Agrid, Agrid[1][1], Agrid[self.Player.translateMousePosToGridPos()[0]]
                                                                         [self.Player.translateMousePosToGridPos()[1]])
                    print(self.Player.translateMousePosToGridPos())

                # Is called whenever the mouse is pressed not whenever it's clicked
                Shop.clickAndDrag(shop)
                if not pygame.mouse.get_pressed()[0] and mousePressed:
                    mousePressed = False
                    mousePos = pygame.mouse.get_pos()

                    # Runs trough all the tiles
                    self.grid.MouseClicked()

                # This is done to get a click instead of a press
                elif pygame.mouse.get_pressed()[0] and not shop.isBuying:
                    mousePressed = True
            # Main Event loop end

            # This is the main loop the difference between this loop and the main event loop is that the other loop
            # only runs when a event is called (mouse movement, keys pressed, mouse clicked)

            # Runs trough all tiles
            for k in range(len(self.farmarray)):
                for i in range(self.farmarray[k][2]):
                    for j in range(self.farmarray[k][3]):
                        self.farmland[k].board[i][j].grow()

            # Draws everything on the screen
            self.BackgroundScroll()
            self.screen.blit(text, textRect)

            for k in range(len(self.farmarray)):
                for i in range(self.farmarray[k][2]):
                    for j in range(self.farmarray[k][3]):
                        self.farmland[k].board[i][j].draw()

            for i in range(len(self.sprinklerArray)):
                if not self.sprinklerArray[i] == None:
                    self.sprinklerArray[i].gadgetActivate()
            test.drawChicken()
            test.chickenWalk()
            test.eatGrass()
            self.Player.setScaleRatioFemale(2)
            Player.DrawCharacter(self.Player,
                                 self.screen,
                                 self.Player.getScaledUpCharacter(self.Player.female, self.Player.getScaleRatioFemale())
                                 , self.Player.startingPos,
                                 self.Player.getWestCoordCropping(self.Player.getScaleRatioFemale(), self.Player.west),
                                 self.Player.getNorthCoordCropping(self.Player.getScaleRatioFemale(), self.Player.north),
                                 self.Player.getEastCoordCropping(self.Player.getScaleRatioFemale(), self.Player.east),
                                 self.Player.getSouthCoordCropping(self.Player.getScaleRatioFemale(), self.Player.south))

            shop.draw()

            self.grid.draw()

            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()

    def BackgroundScroll(self):
        self.screen.blit(self.skyImg, (0 + (1 * self.counter), 0))
        self.screen.blit(self.skyImg, (-self.size[0] + (1 * self.counter), 0))
        if self.isTrue:
            self.counter += 1
        if self.counter == 800:
            self.counter = 0
