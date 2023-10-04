import pygame

class MainPage:
    def __init__(self, game):
        self.game = game
        self.mouse = pygame.mouse.get_pos()

    def render(self):
        self.game.screen.blit(self.game.util.skins[0], ((152, self.game.eronary_y + 1000)))
        self.game.screen.blit(self.game.util.skins[1], ((28, self.game.walpuper_y + 1000)))
        self.game.screen.blit(self.game.util.skins[2], ((276, self.game.aqua_y + 1000)))
        self.game.screen.blit(self.game.util.darkerBackground, ((0, 0)))
        self.game.screen.blit(self.game.util.record, ((15, 15)))
        self.game.screen.blit(self.game.util.coins, ((15, 66)))
        a = self.game.screen.blit(self.game.util.settings[0], ((305, 15)))
        # if pygame.mouse.get_pressed()[0] and a.collidepoint(self.mouse):
        #     if(self.game.state != "Settings"):
        #         self.game.state = "Settings"
        self.game.screen.blit(self.game.util.buttons[0], ((90, 261)))
        self.game.screen.blit(self.game.util.buttons[1], ((90, 334)))
