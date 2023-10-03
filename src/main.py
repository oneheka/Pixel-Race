import pygame
from pages.MainPage import MainPage

class Pygame:
    screen = pygame.display.set_mode((360, 660))
    pygame.display.set_caption('Niako Game')
    icon = pygame.image.load('assets/images/icon.png').convert_alpha()
    background = pygame.image.load('assets/images/bg.png').convert_alpha()
    car = pygame.image.load('assets/images/buttons/playButton.png').convert_alpha()
    eronary_y = 0
    walpuper_y = 0
    state = 'Menu'
    

    def build(self):
        pygame.font.init()
        pygame.init()
        pygame.display.set_icon(self.icon)

        while(bool(self.state)):
            self.screen.blit(self.background, ((0, 0)))

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
            
            # self.screen.blit(self.car, ((0, self.background_y + 1000)))
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
                MainPage(self.screen, self.eronary_y, self.walpuper_y).render()

            pygame.display.update()
            pygame.time.Clock().tick(300)

Pygame().build()