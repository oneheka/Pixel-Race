import pygame

class SkinsPage:
    def __init__(self, game):
        self.game = game
        self.mouse = pygame.mouse.get_pos()

    def render(self, clicked):
        self.game.screen.blit(self.game.util.skins[0], ((152, self.game.eronary_y + 1000)))
        self.game.screen.blit(self.game.util.skins[1], ((28, self.game.walpuper_y + 1000)))
        self.game.screen.blit(self.game.util.skins[2], ((276, self.game.aqua_y + 1000)))
        self.game.screen.blit(self.game.util.darkerBackground, ((0, 0)))
        self.game.screen.blit(self.game.util.skins_page[0], ((101, 200)))
        self.game.screen.blit(self.game.util.skins_page[1], ((132, 395)))
        self.game.screen.blit(self.game.util.skins_page[2], ((150, 265)))
        self.game.screen.blit(self.game.util.skins_page[3], ((186, 236)))
        self.game.screen.blit(self.game.util.skins_page[5], ((296, 306)))
        self.game.screen.blit(self.game.util.skins_page[4], ((16, 306)))
        self.game.screen.blit(self.game.util.skins_page[6], ((149, 238)))
        self.game.screen.blit(self.game.util.skins_page[7], ((132, 364)))

        settings = self.game.screen.blit(self.game.util.settings[1], ((305, 15)))
        if settings.collidepoint(self.mouse) and clicked:
            if(self.game.state != "Menu"):
                self.game.state = 'Menu'