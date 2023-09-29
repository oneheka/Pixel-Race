import pygame

class Pygame:
    screen = pygame.display.set_mode((512, 512))
    state = 'Menu'

    def build(self):
        pygame.font.init()
        pygame.init()

        while(bool(self.state)):
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()

            pygame.display.flip()

Pygame().build()