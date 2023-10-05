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
            y = 400
            select_m = self.game.screen.blit(self.game.util.settings[7], ((50, 360.5)))
            for i in range(len(self.game.util.sounds)):
                btn = self.game.screen.blit(self.game.util.settings[8 if self.game.getSound == i else 9], ((57, y)))
                self.game.screen.blit(
                    self.game.util.mainfont.render(
                        self.game.util.sounds[i]['name'], False, 'white'
                    ), ((62, y+4))
                )
                y += 43
                if btn.collidepoint(mouse) and clicked:
                    if(self.isPlaying):
                        for j in range(len(self.game.util.sounds)):
                            self.game.util.sounds[j]['file'].stop()
                        self.game.getSound = i
                        self.game.util.sounds[i]['file'].play()
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
    
