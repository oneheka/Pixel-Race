import pygame
from pages.MainPage import MainPage
from util import Util

class Game:
    screen = pygame.display.set_mode((360, 660))
    pygame.display.set_caption('Niako Game')
    eronary_y = 0
    walpuper_y = 0
    util = Util()
    state = 'Menu'
    

    def build(self):
        pygame.font.init()
        pygame.init()
        pygame.display.set_icon(self.util.icon)

        while(bool(self.state)):
            self.screen.blit(self.util.background, ((0, 0)))

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
            
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

            if(self.state == 'Menu'):
                MainPage(self).render()

            pygame.display.update()
            pygame.time.Clock().tick(300)

Game().build()