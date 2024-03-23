import pygame

class Menu:
    def __init__(self, core):
        self.core = core
    
    def render(self, events):
        hovered = False
        mouse = pygame.mouse.get_pos()

        self.core.setCarAnimation()
        self.core.window.blit(self.core.images.blur, (0, 0))
        
        self.core.window.blit(self.core.images.stats, (16, 16))
        self.core.window.blit(
            self.core.fonts.render(
                str(self.core.config['record'])+'m'
            ), (25, 26)
        )

        self.core.window.blit(self.core.images.stats, (16, 60))
        self.core.window.blit(self.core.images.coins['small'], (76, 68))
        self.core.window.blit(
            self.core.fonts.render(
                str(self.core.config['coins'])
            ), (25, 70)
        )

        self.core.window.blit(self.core.images.info_wrapper, (16, 588))
        if(self.core.selectFact != -1):
            self.core.window.blit(self.core.images.facts[self.core.selectFact], (16, 588))
        
        settings = self.core.components.settings(True, (305, 15))
        if settings.collidepoint(mouse):
            hovered = True
            if(events['clicked'] and self.core.page != 'settings'):
                    self.core.updatePage('settings')

        play = self.core.window.blit(self.core.images.buttons['play'], (90, 261))
        if play.collidepoint(mouse):
            hovered = True
            if(events['clicked'] and self.core.page != 'game'):
                    self.core.pages['game'].startGame()
                    self.core.updatePage('game')

        skin = self.core.window.blit(self.core.images.buttons['shop'], (90, 334))
        if skin.collidepoint(mouse):
            hovered = True
            if(events['clicked'] and self.core.page != 'shop'):
                self.core.updatePage('shop')
        
        return hovered
