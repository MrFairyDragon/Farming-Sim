import pygame
import numpy as np
from Grid import Grid
from Board import Board
from Chicken import Chicken
from Shop import Shop
from Cow import Cow
from network import network
from Node import Node
from Astar import Astar
from ClientSide import ClientSide
from ServerSide import ServerSide
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
        self.size = (800, 576)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Farming simulator")
        font = pygame.font.Font('Fonts/COMIC.TTF', 20)
        carryOn = True
        self.clock = pygame.time.Clock()
        self.counter = 0
        self.skyImg = pygame.image.load('Assets/Sky_Skrr.png')
        self.isTrue = True
        self.grid = Grid(self, 11, 10)
        self.astar = Astar()
        self.Agrid = Astar.make_grid(self.astar, self.grid.sizeX, self.grid.sizeY)
        self.Player = Player(self)
        # self.Player2 = Player(self)
        self.network = network()
        self.Player2mousePos = self.network.getMousePos()
        print(self.Player2mousePos)
        self.Player2mouseIsPressed = False
        # Defines Positions of self.farmland's and the self.size determined in tiles (posX, posY, self.sizeX,
        # self.sizeY)

        self.farmarray = [[1, 1, 3, 3],
                          [1, 5, 3, 3],
                          [5, 1, 3, 7]]
        # Makes the self.farmlands with the above positions and self.sizes

        self.farmland = np.ndarray(shape=(len(self.farmarray)), dtype=Board)
        for i in range(len(self.farmarray)):
            self.farmland[i] = Board(self.farmarray[i][0], self.farmarray[i][1], self.farmarray[i][2],
                                     self.farmarray[i][3], self, self.grid, i)

        self.test = Chicken(1, 5, self, self.farmland[1])
        self.test2 = Cow(5, 1, self, self.farmland[2])
        self.astar = Astar()
        self.shop = Shop(self)

        Agrid = Astar.make_grid(self.astar, self.grid.sizeX, self.grid.sizeY)
        # Agrid = Astar.make_grid(self.astar, self.grid.sizeX, self.grid.sizeY)

        for i in range(len(Agrid)):
            for j in range(len(Agrid[0])):
                # print (Agrid[i][j])
                node = Agrid[i][j]
                # print(Agrid[i][j])
                node.update_neighbors(Agrid)
        for i in range(len(self.Agrid)):
            for j in range(len(self.Agrid[0])):
                # print (self.Agrid[i][j])
                node = self.Agrid[i][j]
                # print(self.Agrid[i][j])
                node.update_neighbors(self.Agrid)
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
                    self.Player.setCounter2()
                    self.Player.setSwitch()
                    self.Player.setMove(self.Player.getMovement())
                    self.Player.setMove2()
                    print(self.Player.DetermineDirection(self.Player.getMove2()))

                # Is called whenever the mouse is pressed not whenever it's clicked
                Shop.clickAndDrag(self.shop)
                if not pygame.mouse.get_pressed()[0] and mousePressed:
                    mousePressed = False
                    self.grid.MouseClicked()
                elif pygame.mouse.get_pressed()[0] and not self.shop.isBuying:
                    mousePressed = True
            # Main Event loop end

            # This is the main loop the difference between this loop and the main event loop is that the other loop
            # only runs when a event is called (mouse movement, keys pressed, mouse clicked)

            # print(self.Player.getIndexCount2())
            # Draws everything on the screen
            self.BackgroundScroll()
            self.screen.blit(text, textRect)
            Player2mousePos = self.network.send(self.network.make_pos(pygame.mouse.get_pos()))
            #print(self.Player2mousePos)

            for k in range(len(self.farmarray)):
                for i in range(self.farmarray[k][2]):
                    for j in range(self.farmarray[k][3]):
                        self.farmland[k].board[i][j].grow()
                        self.farmland[k].board[i][j].draw()

            for i in range(len(self.sprinklerArray)):
                if not self.sprinklerArray[i] == None:
                    self.sprinklerArray[i].gadgetActivate()

            self.test.Walk()
            self.test2.Walk()
            self.Player.setScaleRatioFemale(2)
            Player.DrawCharacter(self.Player,
                                 self.screen,
                                 self.Player.getScaledUpCharacter(self.Player.female, self.Player.getScaleRatioFemale())
                                 , self.Player.setPos(300, 300), self.Player.getMove2(),
                                 self.Player.getCoordCropping(self.Player.getScaleRatioFemale(), self.Player.west),
                                 self.Player.getCoordCropping(self.Player.getScaleRatioFemale(), self.Player.north),
                                 self.Player.getCoordCropping(self.Player.getScaleRatioFemale(), self.Player.east),
                                 self.Player.getCoordCropping(self.Player.getScaleRatioFemale(), self.Player.south))

            self.grid.draw()
            self.shop.draw()
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
