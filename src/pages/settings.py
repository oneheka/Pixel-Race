import pygame

class Settings:
    isPlaying = False
    select = False
    
    def __init__(self, core):
        self.core = core
    
    def render(self, clicked):
        mouse = pygame.mouse.get_pos()

        self.core.setCarAnimation()
        self.core.window.blit(self.core.images.blur, (0, 0))

        self.core.window.blit(self.core.images.modal, (32, 200))

        self.core.window.blit(self.core.images.texts['sound'], (116, 262.5))
        if(self.isPlaying):
            toggle = self.core.window.blit(self.core.images.toggle['on'], (194, 257))
        else:
            toggle = self.core.window.blit(self.core.images.toggle['off'], (194, 257))
        
        if toggle.collidepoint(mouse) and clicked:
            self.isPlaying = not self.isPlaying
        
        self.core.window.blit(self.core.images.texts['choose_music'], (82, 314))

        if(self.select):
            y = 400
            select = self.core.window.blit(self.core.images.dropdown['open'], (50, 360.5))
            pygame.draw.rect(self.core.window, (10, 12, 15), (50, y-4, 260, 43 * len(self.core.sounds.array())), border_radius=8)
            for i in range(len(self.core.sounds.array())):
                btn = self.core.window.blit(self.core.images.block['active_song' if self.core.sounds.selected == i else 'song'], ((57, y)))
                self.core.window.blit(
                    self.core.fonts.render(
                        self.core.sounds.array()[i]['label']
                    ), (62, y+6)
                )
                y += 43
                if btn.collidepoint(mouse) and clicked:
                    if(self.isPlaying):
                        for j in range(len(self.core.sounds.array())):
                            self.core.sounds.array()[j]['file'].stop()
                        self.core.sounds.setSound(i)
                        self.core.sounds.array()[i]['file'].play(-1)
                        self.select = False
        else:
            select = self.core.window.blit(self.core.images.dropdown['close'], (50, 360.5))
        
        if select.collidepoint(mouse) and clicked:
            self.select = not self.select

        settings = self.core.window.blit(self.core.images.settings['close'], (305, 15))
        if settings.collidepoint(mouse) and clicked:
            if(self.core.page != 'menu'):
                self.core.page = 'menu'