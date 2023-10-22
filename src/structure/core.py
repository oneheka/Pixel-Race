from pages.settings import Settings
from pages.lose import Lose
from pages.game import Game
from pages.shop import Shop
from pages.menu import Menu
from structure.util import Util
import pygame

class Core(Util):
    window = pygame.display.set_mode((360, 660))
    page = 'menu'
    paused = False
    lastMetrs = 0
    lastStars = 0

    def __init__(self):
        pygame.init()
        self.load()
        self.pages = {
            'menu': Menu(self),
            'settings': Settings(self),
            'shop': Shop(self),
            'game': Game(self),
            'lose': Lose(self)
        }
    
    def setCarAnimation(self):
        self.window.blit(self.images.skins['eronary'], ((152, self.eronary_y + 1000)))
        self.window.blit(self.images.skins['walpuper'], ((28, self.walpuper_y + 1000)))
        self.window.blit(self.images.skins['aqua'], ((276, self.aqua_y + 1000)))
    
    def updatePlaying(self):
        if(self.sounds.isPlaying != self.pages['settings'].isPlaying):
            self.sounds.isPlaying = self.pages['settings'].isPlaying
            if(self.pages['settings'].isPlaying):
                self.sounds.active['file'].play(-1)
            else:
                self.sounds.active['file'].stop()

    def start(self):
        pygame.display.set_caption('Pixel Race')
        pygame.display.set_icon(self.images.logo)

        while True:
            self.window.blit(self.images.background, (0, 0))

            if(not self.paused):
                if(self.pages['game'].metrs > 0):
                    self.pages['game'].metrs += 1

            self.updatePlaying()
            self.updateCarAnimation()

            clicked = False

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicked = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.page == 'game':
                            if(not self.paused):
                                self.paused = True
                            elif(self.paused):
                                self.paused = False
                        elif self.page == 'lose':
                            self.pages['game'].startGame()
                            self.page = 'game'
  
            if(self.page in self.pages):
                self.pages[self.page].render(clicked)

            pygame.display.update()
            pygame.time.Clock().tick(300)