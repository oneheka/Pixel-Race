import pygame
from pages.MainPage import MainPage

class Pygame:
    screen = pygame.display.set_mode((360, 660))
    pygame.display.set_caption('Niako Game')
    icon = pygame.image.load('assets/images/icon.png').convert_alpha()
    background = pygame.image.load('assets/images/bg.png').convert_alpha()
    background_y = 0
    state = 'Menu'
    

    def build(self):
        pygame.font.init()
        pygame.init()
        pygame.display.set_icon(self.icon)
        self.screen.blit(self.background, ((0, self.background_y)))

        while(bool(self.state)):
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()

            if(self.state == 'Menu'):
                MainPage(self.screen, self.background_y).render()
            
            self.screen.blit(self.background, ((0, self.background_y + 1000)))
            self.background_y -= 2
            if (self.background_y == -1000):
                self.background_y = 0

            

            pygame.display.update()
            pygame.time.Clock().tick(300)

Pygame().build()