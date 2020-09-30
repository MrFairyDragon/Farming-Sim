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
        self.font = pygame.font.Font('COMIC.TTF', 20)
        self.blue = (0, 0, 128)
        self.text = self.font.render('Play', True, self.blue)
        self.playCoordinates = (300, 280)
        self.mx = None
        self.my = None
        self.isRunning = True

    def checkIfClicked(self):
        if self.mx >= self.playCoordinates[0]:
            if self.mx <= self.playCoordinates[0] + 190:
                if self.my >= self.playCoordinates[1]:
                    if self.my <= self.playCoordinates[1] + 50:
                        self.isRunning = False

    def main_menu(self):
        if self.isRunning:
            while self.isRunning:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.mx, self.my = pygame.mouse.get_pos()
                        self.checkIfClicked()
                self.__screen.blit(self.Widget1, self.playCoordinates, (0, 142, 190, 50))
                self.__screen.blit(self.text, (377, 287))
                pygame.display.update()
            StartTheGame()

    def SelectTheScreen(self):
        if self.__isInMenu:
            self.main_menu()


Main_menu().SelectTheScreen()
