import pygame

class SkinsPage:
    def __init__(self, game):
        self.game = game
        self.mouse = pygame.mouse.get_pos()

    def render(self, clicked):
        self.game.screen.blit(self.game.util.darkerBackground, ((0, 0)))
        settings = self.game.screen.blit(self.game.util.settings[1], ((305, 15)))
        if settings.collidepoint(self.mouse) and clicked:
            if(self.game.state != "Menu"):
                self.game.state = 'Menu'