import pygame
import json

class SkinsPage:
    def __init__(self, game):
        self.game = game
        self.mouse = pygame.mouse.get_pos()
        self.page = 0
        with open('src/config.json') as f:
            file_content = f.read()
            self.config = json.loads(file_content)


    def render(self, clicked):
        self.game.screen.blit(self.game.util.skins[0], ((152, self.game.eronary_y + 1000)))
        self.game.screen.blit(self.game.util.skins[1], ((28, self.game.walpuper_y + 1000)))
        self.game.screen.blit(self.game.util.skins[2], ((276, self.game.aqua_y + 1000)))
        self.game.screen.blit(self.game.util.darkerBackground, ((0, 0)))

        skins = self.config['skins']

        self.game.screen.blit(self.game.util.skins_page[0], ((101, 200)))
        self.game.screen.blit(self.game.util.skins_page[1], ((132, 395)))
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
        self.game.screen.blit(
            self.game.util.mainfont.render(
                skins[self.page]['name'], False, 'white'
            ), ((132, 364))
        )

        left = self.game.screen.blit(self.game.util.skins_page[2], ((16, 306)))
        if left.collidepoint(self.mouse) and clicked:
            self.left()

        right = self.game.screen.blit(self.game.util.skins_page[3], ((296, 306)))
        if right.collidepoint(self.mouse) and clicked:
            self.right()

        settings = self.game.screen.blit(self.game.util.settings[1], ((305, 15)))
        if settings.collidepoint(self.mouse) and clicked:
            if(self.game.state != "Menu"):
                self.game.state = 'Menu'

    def right(self):
        if(self.page + 1 >= len(self.config['skins'])):
            self.page = 0
        else:
            self.page += 1

    def left(self):
        if(0 > self.page - 1):
            self.page = len(self.config['skins']) - 1
        else:
            self.page -= 1