import pygame

class SkinsPage:
    def __init__(self, game):
        self.game = game
        self.page = 0

    def render(self, clicked):
        mouse = pygame.mouse.get_pos()

        self.game.screen.blit(self.game.util.skins[0], ((152, self.game.eronary_y + 1000)))
        self.game.screen.blit(self.game.util.skins[1], ((28, self.game.walpuper_y + 1000)))
        self.game.screen.blit(self.game.util.skins[2], ((276, self.game.aqua_y + 1000)))
        self.game.screen.blit(self.game.util.darkerBackground, ((0, 0)))

        self.game.screen.blit(self.game.util.coins, ((15, 15)))
        self.game.screen.blit(
            self.game.util.mainfont.render(
                str(self.game.config['coins']), False, 'white'
            ), ((23, 23))
        )

        skins = self.game.config['skins']

        self.game.screen.blit(self.game.util.skins_page[0], ((101, 200)))

        if(skins[self.page]['has']):
            if(skins[self.page]['default']):
                self.game.screen.blit(self.game.util.skins_page[6], ((132, 395)))
            else:
                setter = self.game.screen.blit(self.game.util.skins_page[3], ((132, 395)))
                if setter.collidepoint(mouse) and clicked:
                    for i in range(len(skins)):
                        if(skins[i]['default']):
                            self.game.config['skins'][i]['default'] = False
                    self.game.config['skins'][self.page]['default'] = True
                    self.game.updateConfig(self.game.config)
        else:
            if(skins[self.page]['cost'] > self.game.config['coins']):
                self.game.screen.blit(self.game.util.skins_page[2], ((132, 395)))
            else:
                buy = self.game.screen.blit(self.game.util.skins_page[1], ((132, 395)))
                if buy.collidepoint(mouse) and clicked:
                    self.game.config['skins'][self.page]['has'] = True
                    self.game.config['coins'] -= skins[self.page]['cost']
                    self.game.updateConfig(self.game.config)

        self.game.screen.blit(self.game.util.coin, ((186, 236)))
        self.game.screen.blit(
            self.game.util.getImage(skins[self.page]['name']),
            ((150, 265))
        )
        self.game.screen.blit(
            self.game.util.mainfont.render(
                str(skins[self.page]['cost']), False, 'white'
            ), ((149, 238))
        )
        name = self.game.util.mainfont.render(skins[self.page]['name'], False, 'white')
        self.game.screen.blit(
            name, name.get_rect(center=(self.game.screen.get_size()[0]/2, 370))
        )

        left = self.game.screen.blit(self.game.util.skins_page[4], ((16, 306)))
        if left.collidepoint(mouse) and clicked:
            self.left()

        right = self.game.screen.blit(self.game.util.skins_page[5], ((296, 306)))
        if right.collidepoint(mouse) and clicked:
            self.right()

        settings = self.game.screen.blit(self.game.util.settings[1], ((305, 15)))
        if settings.collidepoint(mouse) and clicked:
            if(self.game.state != "Menu"):
                self.game.state = 'Menu'

    def right(self):
        if(self.page + 1 >= len(self.game.config['skins'])):
            self.page = 0
        else:
            self.page += 1

    def left(self):
        if(0 > self.page - 1):
            self.page = len(self.game.config['skins']) - 1
        else:
            self.page -= 1