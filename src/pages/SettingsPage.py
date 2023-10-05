import pygame

class SettingsPage:
    def __init__(self, game):
        self.game = game
        self.isPlaying = False
        self.select = False

    def render(self, clicked):
        mouse = pygame.mouse.get_pos()

        self.game.screen.blit(self.game.util.skins[0], ((152, self.game.eronary_y + 1000)))
        self.game.screen.blit(self.game.util.skins[1], ((28, self.game.walpuper_y + 1000)))
        self.game.screen.blit(self.game.util.skins[2], ((276, self.game.aqua_y + 1000)))
        self.game.screen.blit(self.game.util.darkerBackground, ((0, 0)))
        self.game.screen.blit(self.game.util.settingsBackground, ((32, 200)))
        self.game.screen.blit(self.game.util.settings[2], ((116, 262.5)))
        if(self.isPlaying):
            toggle = self.game.screen.blit(self.game.util.settings[3], ((194, 257)))
        else:
            toggle = self.game.screen.blit(self.game.util.settings[4], ((194, 257)))
        if(self.select):
            select_m = self.game.screen.blit(self.game.util.settings[7], ((50, 360.5)))
            for i in range(1, 3):
                plates = [
                    self.game.screen.blit(self.game.util.settings[8], ((57, 400))),
                    self.game.screen.blit(self.game.util.settings[8], ((57, 443))),
                    self.game.screen.blit(self.game.util.settings[8], ((57, 486))),
                ]
                plates[i]
        else:
            select_m = self.game.screen.blit(self.game.util.settings[5], ((50, 360.5)))
        self.game.screen.blit(self.game.util.settings[6], ((82, 311.5)))
        settings = self.game.screen.blit(self.game.util.settings[1], ((305, 15)))
        if settings.collidepoint(mouse) and clicked:
            if(self.game.state != "Menu"):
                self.game.state = 'Menu'
        
        if toggle.collidepoint(mouse) and clicked:
            self.isPlaying = not self.isPlaying
            
        if select_m.collidepoint(mouse) and clicked:
            self.select = not self.select
    
