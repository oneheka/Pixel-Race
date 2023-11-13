import pygame

class Menu:
    def __init__(self, core):
        self.core = core
    
    def render(self, clicked):
        mouse = pygame.mouse.get_pos()

        self.core.setCarAnimation()
        self.core.window.blit(self.core.images.blur, (0, 0))
        
        self.core.window.blit(self.core.images.stats, (15, 15))
        self.core.window.blit(
            self.core.fonts.render(
                str(self.core.config['record'])+'m'
            ), (22, 24)
        )

        self.core.window.blit(self.core.images.stats, (15, 66))
        self.core.window.blit(self.core.images.coins['small'], (74, 74))
        self.core.window.blit(
            self.core.fonts.render(
                str(self.core.config['coins'])
            ), (22, 74)
        )
        
        settings = self.core.components.settings(True, (305, 15))
        if settings.collidepoint(mouse) and clicked:
            if(self.core.page != 'settings'):
                self.core.page = 'settings'

        play = self.core.window.blit(self.core.images.buttons['play'], (90, 261))
        if play.collidepoint(mouse) and clicked:
            if(self.core.page != 'game'):
                self.core.pages['game'].startGame()
                self.core.page = 'game'

        skin = self.core.window.blit(self.core.images.buttons['shop'], (90, 334))
        if skin.collidepoint(mouse) and clicked:
            if(self.core.page != 'shop'):
                self.core.page = 'shop'

