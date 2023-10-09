import pygame

class LosePage:
    def __init__(self, game):
        self.game = game

    def render(self, clicked):
        mouse = pygame.mouse.get_pos()

        self.game.screen.blit(self.game.util.skins[0], ((152, self.game.eronary_y + 1000)))
        self.game.screen.blit(self.game.util.skins[1], ((28, self.game.walpuper_y + 1000)))
        self.game.screen.blit(self.game.util.skins[2], ((276, self.game.aqua_y + 1000)))
        self.game.screen.blit(self.game.util.darkerBackground, ((0, 0)))
        self.game.screen.blit(self.game.util.lose_page[0], ((32, 201)))
        self.game.screen.blit(self.game.util.lose_page[1], ((78, 247)))
        again = self.game.screen.blit(self.game.util.lose_page[2], ((76, 380)))
        menu = self.game.screen.blit(self.game.util.lose_page[3], ((188, 380)))
        self.game.screen.blit(
            self.game.util.mainfont.render(
                'Проехали: ' + str(self.game.lastMetrs)+'m', False, 'white'
            ), ((95, 296))
        )
        self.game.screen.blit(
            self.game.util.mainfont.render(
                'Собрал : ' + str(self.game.lastStars), False, 'white'
            ), ((117, 331))
        )
        self.game.screen.blit(self.game.util.coin, ((230, 330)))
        if menu.collidepoint(mouse) and clicked:
            if(self.game.state != "Menu"):
                self.game.state = "Menu"
        if again.collidepoint(mouse) and clicked:
            if(self.game.state != "Play"):
                self.game.state = "Play"
                self.game.PlayPage.startGame()

