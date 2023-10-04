import pygame

class SettingsPage:
    def __init__(self, game):
        self.game = game

    def render(self):
        self.game.screen.blit(self.game.util.skins[0], ((152, self.game.eronary_y + 1000)))
        self.game.screen.blit(self.game.util.skins[1], ((28, self.game.walpuper_y + 1000)))
        self.game.screen.blit(self.game.util.skins[2], ((276, self.game.aqua_y + 1000)))
        self.game.screen.blit(self.game.util.darkerBackground, ((0, 0)))
        self.game.screen.blit(self.game.util.settingsBackground, ((32, 200)))
        self.game.screen.blit(self.game.util.settings[1], ((305, 15)))

        