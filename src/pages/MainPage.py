import pygame

class MainPage:
    def __init__(self, game):
        self.game = game

    def render(self, clicked):
        mouse = pygame.mouse.get_pos()
        
        self.game.screen.blit(self.game.util.skins[0], ((152, self.game.eronary_y + 1000)))
        self.game.screen.blit(self.game.util.skins[1], ((28, self.game.walpuper_y + 1000)))
        self.game.screen.blit(self.game.util.skins[2], ((276, self.game.aqua_y + 1000)))
        self.game.screen.blit(self.game.util.darkerBackground, ((0, 0)))
        self.game.screen.blit(self.game.util.record, ((15, 15)))
        self.game.screen.blit(self.game.util.coins, ((15, 66)))
        
        self.game.screen.blit(
            self.game.util.mainfont.render(
                str(self.game.config['record'])+'m', False, 'white'
            ), ((23, 23))
        )

        self.game.screen.blit(
            self.game.util.mainfont.render(
                str(self.game.config['coins']), False, 'white'
            ), ((23, 74))
        )

        settings = self.game.screen.blit(self.game.util.settings[0], ((305, 15)))
        if settings.collidepoint(mouse) and clicked:
            if(self.game.state != "Settings"):
                self.game.state = "Settings"
        self.game.screen.blit(self.game.util.buttons[0], ((90, 261)))
        skins = self.game.screen.blit(self.game.util.buttons[1], ((90, 334)))
        if skins.collidepoint(mouse) and clicked:
            if(self.game.state != "Skins"):
                self.game.state = "Skins"
