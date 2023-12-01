import pygame

class Lose:
    def __init__(self, core):
        self.core = core

    def render(self, clicked):
        mouse = pygame.mouse.get_pos()

        self.core.window.blit(self.core.images.blur, (0, 0))
        self.core.window.blit(self.core.images.modal, (32, 201))
        self.core.window.blit(self.core.images.texts['lose'], (78, 247))

        self.core.window.blit(
            self.core.fonts.render(
                'Проехали: ' + str(self.core.lastMetrs)+'m'
            ), (95, 296)
        )
        self.core.window.blit(
            self.core.fonts.render(
                'Собрал: ' + str(self.core.lastStars)
            ), (117, 331)
        )
        self.core.window.blit(self.core.images.coins['small'], (230, 330))

        menu = self.core.window.blit(self.core.images.buttons['menu'], (188, 380))
        if menu.collidepoint(mouse) and clicked:
            if(self.core.page != 'menu'):
                self.core.updatePage('menu')

        again = self.core.window.blit(self.core.images.buttons['again'], (76, 380))
        if again.collidepoint(mouse) and clicked:
            if(self.core.page != 'game'):
                self.core.pages['game'].startGame()
                self.core.updatePage('game')