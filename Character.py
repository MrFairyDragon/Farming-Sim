import pygame
import sys
from GameServer import main


def StartTheGame():
    main()


def MovementControl():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass


class Character:

    def __init__(self):
        self.__screen = self.main.screen
        self.__isInMenu = True
        self.__isPaused = False
        self.Widget1 = pygame.image.load('Assets/Multiplayer_Buttons.png')
        self.background = pygame.image.load('Assets/Sky_Skrr.png')
        # self.background = pygame.transform.scale(self.background, self.size)
        self.font = pygame.font.Font('Fonts/COMIC.TTF', 20)
        self.blue = (0, 0, 128)
        self.text = self.font.render('Play', True, self.blue)
        self.playCoordinates = (300, 280)
        self.girlAnimation = (360, 130)
        self.Widget1Length = 190
        self.Widget1Height = 50
        self.mx = None
        self.my = None
        self.isRunning = True
        self.counter = 0
        self.indexCount = 0
        self.isTrue = True
        self.spriteSheet = pygame.image.load('Assets/Pepper_publish.png')
        self.scaleUp = pygame.transform.scale(self.spriteSheet, (540, 384))
        self.spriteList = [(3 * 3, 3 * 3, 18 * 3, 29 * 3),
                           (27 * 3, 2 * 3, 18 * 3, 30 * 3),
                           (51 * 3, 3 * 3, 18 * 3, 29 * 3),
                           (27 * 3, 2 * 3, 18 * 3, 30 * 3),
                           (6 * 3, 35 * 3, 12 * 3, 29 * 3),
                           (30 * 3, 35 * 3, 12 * 3, 29 * 3),
                           (54 * 3, 36 * 3, 12 * 3, 28 * 3),
                           (30 * 3, 35 * 3, 12 * 3, 29 * 3),
                           (3 * 3, 67 * 3, 18 * 3, 29 * 3),
                           (27 * 3, 66 * 3, 18 * 3, 30 * 3),
                           (51 * 3, 67 * 3, 18 * 3, 29 * 3),
                           (27 * 3, 66 * 3, 18 * 3, 30 * 3),
                           (6 * 3, 100 * 3, 12 * 3, 28 * 3),
                           (30 * 3, 99 * 3, 12 * 3, 29 * 3),
                           (54 * 3, 100 * 3, 12 * 3, 29 * 3),
                           (30 * 3, 99 * 3, 12 * 3, 29 * 3)]

        self.relative = None
        self.west = [(6 * 3, 100 * 3, 12 * 3, 28 * 3),
                     (30 * 3, 99 * 3, 12 * 3, 29 * 3),
                     (54 * 3, 100 * 3, 12 * 3, 29 * 3),
                     (30 * 3, 99 * 3, 12 * 3, 29 * 3)]

        self.north = [(3 * 3, 3 * 3, 18 * 3, 29 * 3),
                      (27 * 3, 2 * 3, 18 * 3, 30 * 3),
                      (51 * 3, 3 * 3, 18 * 3, 29 * 3),
                      (27 * 3, 2 * 3, 18 * 3, 30 * 3)]

        self.east = [(6 * 3, 35 * 3, 12 * 3, 29 * 3),
                     (30 * 3, 35 * 3, 12 * 3, 29 * 3),
                     (54 * 3, 36 * 3, 12 * 3, 28 * 3),
                     (30 * 3, 35 * 3, 12 * 3, 29 * 3)]

        self.south = [(3 * 3, 67 * 3, 18 * 3, 29 * 3),
                      (27 * 3, 66 * 3, 18 * 3, 30 * 3),
                      (51 * 3, 67 * 3, 18 * 3, 29 * 3),
                      (27 * 3, 66 * 3, 18 * 3, 30 * 3)]

        self.previousMovement = []

        self.switch = True
        self.t0 = pygame.time.get_ticks()

        self.clock = pygame.time.Clock()

    # list2 = [item[0] for item in self.previousMovement]

    def CheckRelativeCoordinates(self):
        self.mx, self.my = pygame.mouse.get_pos()
        self.previousMovement.append((self.mx, self.my))
        list2 = [item[0] for item in self.previousMovement]
        list3 = list2[-1]
        list4 = [item[1] for item in self.previousMovement]
        list5 = list4[-1]
        print(self.previousMovement[-1])
        b = self.mx - list3
        a = self.my - list3
        if b > list3:
            self.__screen.blit(self.scaleUp, (self.mx, self.my), self.east[self.indexCount])
            self.indexCount += 1
            if self.indexCount == len(self.spriteList):
                self.indexCount = 0
        if a < list3:
            self.__screen.blit(self.scaleUp, (self.mx, self.my), self.west[0])
            self.indexCount += 1
            if self.indexCount == len(self.spriteList):
                self.indexCount = 0
        if b < list5:
            self.__screen.blit(self.scaleUp, (self.mx, self.my), self.south[0])
            self.indexCount += 1
            if self.indexCount == len(self.spriteList):
                self.indexCount = 0
        if b > list5:
            self.__screen.blit(self.scaleUp, (self.mx, self.my), self.north[0])
            self.indexCount += 1
            if self.indexCount == len(self.spriteList):
                self.indexCount = 0

    def checkIfClicked(self):
        if self.mx >= self.playCoordinates[0]:
            if self.mx <= self.playCoordinates[0] + self.Widget1Length:
                if self.my >= self.playCoordinates[1]:
                    if self.my <= self.playCoordinates[1] + self.Widget1Height:
                        self.isRunning = False

    def RenderAnimation(self):
        self.__screen.blit(self.scaleUp, (375, 130), self.spriteList[self.indexCount])
        self.indexCount += 1
        if self.indexCount == len(self.spriteList):
            self.indexCount = 0

    # used for reference only
    def main_menu(self):
        if self.isRunning:
            while self.isRunning:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.CheckRelativeCoordinates()
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                self.__screen.fill(255)
                self.mx, self.my = pygame.mouse.get_pos()
                t1 = pygame.time.get_ticks()
                dt = t1 - self.t0
                self.CheckRelativeCoordinates()
                pygame.display.update()
                self.clock.tick(60)
                if self.isTrue:
                    self.counter += 1
                if self.counter == 800:
                    self.counter = 0
            StartTheGame()

    def SelectTheScreen(self):
        if self.__isInMenu:
            self.main_menu()


p = Character()
p.SelectTheScreen()
