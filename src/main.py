import pygame

class Pygame:
    screen = pygame.display.set_mode((360, 660))
    pygame.display.set_caption('Niako Game')
    icon = pygame.image.load('assets/images/icon.png')
    state = 'Menu'
    

    def build(self):
        pygame.font.init()
        pygame.init()
        pygame.display.set_icon(self.icon)
        while(bool(self.state)):
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()

            pygame.display.update()

Pygame().build()