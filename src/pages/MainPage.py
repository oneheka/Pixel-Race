import pygame

class MainPage:
    def __init__(self, main, eronary_y, walpuper_y):
        self.main = main
        self.eronary_y = eronary_y
        self.walpuper_y = walpuper_y

    def render(self):
        buttonPlay = pygame.image.load('assets/images/buttons/playButton.png').convert_alpha()
        buttonSkins = pygame.image.load('assets/images/buttons/skinsButton.png').convert_alpha()
        darker_bg = pygame.image.load('assets/images/darker_bg.png').convert_alpha()
        eronary = pygame.image.load('assets/images/skins/eronaryCar.png').convert_alpha()
        walpuper = pygame.image.load('assets/images/skins/walpuperCar.png').convert_alpha()
        stars = pygame.image.load('assets/images/stars.png').convert_alpha()
        record = pygame.image.load('assets/images/record.png').convert_alpha()

        self.main.blit(walpuper, ((28, self.walpuper_y + 1000)))
        self.main.blit(eronary, ((152, self.eronary_y + 1000)))
        self.main.blit(darker_bg, ((0, 0)))
        self.main.blit(record, ((15, 15)))
        self.main.blit(stars, ((15, 66)))
        self.main.blit(buttonPlay, ((90, 261)))
        self.main.blit(buttonSkins, ((90, 334)))
        