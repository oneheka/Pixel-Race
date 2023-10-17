import pygame
import json
from pages.MainPage import MainPage
from pages.SkinsPage import SkinsPage
from pages.SettingsPage import SettingsPage
from pages.PlayPage import PlayPage
from pages.LosePage import LosePage
from util import Util

pygame.init()
class Game:
    screen = pygame.display.set_mode((360, 660))
    pygame.display.set_caption('Pixel Race')
    isPlaying = False
    eronary_y = 0
    walpuper_y = 0
    aqua_y = 0
    paused = False
    getSound = 0
    util = Util()
    state = 'Menu'
    lastMetrs = 0
    lastStars = 0

    def __init__(self):
        self.MainPage = MainPage(self)
        self.SkinsPage = SkinsPage(self)
        self.SettingsPage = SettingsPage(self)
        self.PlayPage = PlayPage(self)
        self.LosePage = LosePage(self)

        with open('src/config.json') as f:
            file_content = f.read()
            self.config = json.loads(file_content)
    
    def updateConfig(self, data):
        with open('src/config.json', 'w') as f:
            f.seek(0)
            json.dump(data, f)
            f.truncate()

    def updatePlaying(self):
        if(self.isPlaying != self.SettingsPage.isPlaying):
            self.isPlaying = self.SettingsPage.isPlaying
            if(self.SettingsPage.isPlaying):
                self.util.sounds[self.getSound]['file'].play(-1)
            else:
                self.util.sounds[self.getSound]['file'].stop()

    def build(self):
        pygame.display.set_icon(self.util.icon)

        while(bool(self.state)):
            self.screen.blit(self.util.background, ((0, 0)))
            clicked = False

            if(not self.paused):
                if(self.PlayPage.metrs > 0):
                    self.PlayPage.metrs += 1


            self.updatePlaying()

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicked = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.state == 'Play':
                        if(not self.paused):
                            self.paused = True
                        elif(self.paused):
                            self.paused = False


            self.setCarAnimation()
            
            if(self.state == 'Menu'):
                self.MainPage.render(clicked)
            elif(self.state == 'Settings'):
                self.SettingsPage.render(clicked)
            elif(self.state == 'Skins'):
                self.SkinsPage.render(clicked)
            elif(self.state == 'Play'):
                self.PlayPage.render()
            elif(self.state == 'Lose'):
                self.LosePage.render(clicked)
            
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
    

Game().build()