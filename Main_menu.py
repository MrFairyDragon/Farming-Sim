import pygame
from main import main


def StartTheGame():
    main()


class Main_menu:

    def __init__(self):
        self.__screen = pygame.display.set_mode((800, 600))
        self.__isInMenu = True
        self.__isPaused = False
        self.Widget1 = pygame.image.load('main_menu_assets/Multiplayer_Buttons.png')
        self.background = pygame.image.load('Sky_Skrr.png')
        self.font = pygame.font.Font('COMIC.TTF', 20)
        self.blue = (0, 0, 128)
        self.text = self.font.render('Play', True, self.blue)
        self.playCoordinates = (300, 280)
        self.Widget1Length = 190
        self.Widget1Height = 50
        self.mx = None
        self.my = None
        self.isRunning = True
        self.counter = 0
        self.isTrue = True

    def checkIfClicked(self):
        if self.mx >= self.playCoordinates[0]:
            if self.mx <= self.playCoordinates[0] + self.Widget1Length:
                if self.my >= self.playCoordinates[1]:
                    if self.my <= self.playCoordinates[1] + self.Widget1Height:
                        self.isRunning = False

    def main_menu(self):
        if self.isRunning:
            while self.isRunning:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.mx, self.my = pygame.mouse.get_pos()
                        self.checkIfClicked()
                self.__screen.blit(self.background, (0 + (1 * self.counter), 0))
                self.__screen.blit(self.Widget1, self.playCoordinates, (0, 142, self.Widget1Length, self.Widget1Height))
                self.__screen.blit(self.text, (377, 287))
                pygame.display.update()
                if self.isTrue:
                    self.counter += 1
                    if self.counter == 100:
                        self.isTrue = False
                if not self.isTrue:
                    self.counter -= 1
                    if self.counter == 0:
                        self.isTrue = True
            StartTheGame()

    def SelectTheScreen(self):
        if self.__isInMenu:
            self.main_menu()


Main_menu().SelectTheScreen()
