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

        self.core.window.blit(self.core.images.texts['sound'], (116, 243))
        if(self.isPlaying):
            toggleSound = self.core.window.blit(self.core.images.toggle['on'], (194, 241))
        else:
            toggleSound = self.core.window.blit(self.core.images.toggle['off'], (194, 241))

        if toggleSound.collidepoint(mouse) and clicked:
            self.isPlaying = not self.isPlaying

        self.core.window.blit(self.core.images.texts['night'], (116, 294))
        if(self.core.config['theme'] == 'night'):
            toggleNight = self.core.window.blit(self.core.images.toggle['on'], (194, 290))
        else:
            toggleNight = self.core.window.blit(self.core.images.toggle['off'], (194, 290))
        
        if toggleNight.collidepoint(mouse) and clicked:
            self.core.config['theme'] = 'day' if self.core.config['theme'] == 'night' else 'night'
            self.core.updateConfig(self.core.config)

        self.core.window.blit(self.core.images.texts['choose_music'], (82, 345))

        if(self.select):
            y = 425
            select = self.core.window.blit(self.core.images.dropdown['open'], (50, 385))
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
            select = self.core.window.blit(self.core.images.dropdown['close'], (50, 385))
        
        if select.collidepoint(mouse) and clicked:
            self.select = not self.select

        settings = self.core.window.blit(self.core.images.settings['close'], (305, 15))
        if settings.collidepoint(mouse) and clicked:
            if(self.core.page != 'menu'):
                self.select = False
                self.core.page = 'menu'