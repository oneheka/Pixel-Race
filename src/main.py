import pygame
import json
from pages.MainPage import MainPage
from pages.SkinsPage import SkinsPage
from pages.SettingsPage import SettingsPage
from util import Util

pygame.init()
class Game:
    screen = pygame.display.set_mode((360, 660))
    pygame.display.set_caption('Niako Game')
    eronary_y = 0
    walpuper_y = 0
    aqua_y = 0
    util = Util()
    state = 'Menu'

    def __init__(self):
        self.MainPage = MainPage(self)
        self.SkinsPage = SkinsPage(self)
        self.SettingsPage = SettingsPage(self)
        with open('src/config.json') as f:
            file_content = f.read()
            self.config = json.loads(file_content)

    def build(self):
        pygame.display.set_icon(self.util.icon)

        while(bool(self.state)):
            self.screen.blit(self.util.background, ((0, 0)))

            clicked = False

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = True
            
            self.setCarAnimation()

            if(self.state == 'Menu'):
                self.MainPage.render(clicked)
            elif(self.state == 'Settings'):
                self.SettingsPage.render(clicked)
            elif(self.state == 'Skins'):
                self.SkinsPage.render(clicked)
            
            pygame.display.update()
            pygame.time.Clock().tick(300)

    def setCarAnimation(self):
        self.eronary_y -= 2
        if (-1100 > self.eronary_y):
            self.eronary_y = 0
            
        if (self.eronary_y > -342):
            if(self.walpuper_y > -2):
                self.walpuper_y = 1
        if(self.walpuper_y != 0):
            self.walpuper_y -= 2
        if (-1100 > self.walpuper_y):
            self.walpuper_y = 0
            
    
        if (self.walpuper_y > -391):
            if(self.aqua_y > -2):
                self.aqua_y = 1
        if(self.aqua_y != 0):
            self.aqua_y -= 2
        if(-1100 > self.aqua_y):
            self.aqua_y = 0
    
    def updateState(self, state):
        self.state = state

Game().build()