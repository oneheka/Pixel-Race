import pygame

class Shop:
    page = 0

    def __init__(self, core):
        self.core = core
    
    def render(self, clicked, scrolled):
        mouse = pygame.mouse.get_pos()
        
        self.core.setCarAnimation()
        self.core.window.blit(self.core.images.blur, (0, 0))
        
        self.core.window.blit(self.core.images.stats, (15, 15))
        self.core.window.blit(self.core.images.coins['small'], (74, 23))
        self.core.window.blit(
            self.core.fonts.render(
                str(self.core.config['coins'])
            ), (22, 23)
        )
        
        settings = self.core.components.settings(False, (305, 15))
        if settings.collidepoint(mouse) and clicked:
            if(self.core.page != 'menu'):
                self.core.updatePage('menu')

        self.core.window.blit(self.core.images.skin_wrapper, (101, 200))

        skins = self.core.config['skins']
        if(skins[self.page]['has']):
            if(skins[self.page]['default']):
                self.core.window.blit(self.core.images.buttons['selected'], (132, 399))
            else:
                setter = self.core.window.blit(self.core.images.buttons['apply'], (132, 399))
                if setter.collidepoint(mouse) and clicked:
                    for i in range(len(skins)):
                        if(skins[i]['default']):
                            self.core.config['skins'][i]['default'] = False
                    self.core.config['skins'][self.page]['default'] = True
                    self.core.selectSkin = self.page
                    self.core.updateConfig(self.core.config)
        else:
            if(skins[self.page]['cost'] > self.core.config['coins']):
                self.core.window.blit(self.core.images.buttons['expensive'], (132, 399))
            else:
                buy = self.core.window.blit(self.core.images.buttons['buy'], (132, 399))
                if buy.collidepoint(mouse) and clicked:
                    self.core.config['skins'][self.page]['has'] = True
                    self.core.config['coins'] -= skins[self.page]['cost']
                    self.core.updateConfig(self.core.config)

        self.core.window.blit(self.core.images.coins['small'], (186, 231))
        self.core.window.blit(
            self.core.fonts.render(
                str(skins[self.page]['cost'])
            ), (149, 233)
        )
        
        self.core.window.blit(
            self.core.images.getSkin(skins[self.page]['name'].lower()),
            (150, 261)
        )

        name = self.core.fonts.render(skins[self.page]['name'])
        self.core.window.blit(
            name, name.get_rect(center=(self.core.window.get_size()[0]/2, 380))
        )

        left = self.core.window.blit(self.core.images.arrows['left'], (16, 306))
        if left.collidepoint(mouse) and clicked:
            self.left()

        right = self.core.window.blit(self.core.images.arrows['right'], (296, 306))
        if right.collidepoint(mouse) and clicked:
            self.right()
        
    def right(self):
        if(self.page + 1 >= len(self.core.config['skins'])):
            self.page = 0
        else:
            self.page += 1

    def left(self):
        if(0 > self.page - 1):
            self.page = len(self.core.config['skins']) - 1
        else:
            self.page -= 1