import pygame

class MainPage:
    def __init__(self, main, bg_y):
        self.main = main
        self.bg_y = bg_y

    def render(self):
        buttonPlay = pygame.image.load('assets/images/buttons/playButton.png').convert_alpha()
        buttonSkins = pygame.image.load('assets/images/buttons/skinsButton.png').convert_alpha()
        darker_bg = pygame.image.load('assets/images/darker_bg.png').convert_alpha()
        
        self.main.blit(darker_bg, ((0, 0)))
        self.main.blit(buttonPlay, ((90, 261)))
        self.main.blit(buttonSkins, ((90, 334)))
        