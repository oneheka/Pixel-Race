import pygame

class Util:
    def __init__(self):
        self.buttons = [
            pygame.image.load('assets/images/buttons/playButton.png').convert_alpha(),
            pygame.image.load('assets/images/buttons/skinsButton.png').convert_alpha()
        ]
        self.icon = pygame.image.load('assets/images/icon.png').convert_alpha()
        self.background = pygame.image.load('assets/images/bg.png').convert_alpha()
        self.settingsBackground = pygame.image.load('assets/images/settings_bg.png').convert_alpha()
        self.darkerBackground = pygame.image.load('assets/images/darker_bg.png').convert_alpha()
        self.coins = pygame.image.load('assets/images/coins.png').convert_alpha()
        self.record = pygame.image.load('assets/images/record.png').convert_alpha()
        self.settings = [
            pygame.image.load('assets/images/settings.png').convert_alpha(),
            pygame.image.load('assets/images/settings_exit.png').convert_alpha(),
            pygame.image.load('assets/images/settings_text.png').convert_alpha(),
            pygame.image.load('assets/images/buttons/toggle_on.png').convert_alpha(),
            pygame.image.load('assets/images/buttons/toggle_off.png').convert_alpha(),
            pygame.image.load('assets/images/music_choiser.png').convert_alpha(),
            pygame.image.load('assets/images/settings_text2.png').convert_alpha(),
        ]
        self.skins = [
            pygame.image.load('assets/images/skins/eronaryCar.png').convert_alpha(),
            pygame.image.load('assets/images/skins/walpuperCar.png').convert_alpha(),
            pygame.image.load('assets/images/skins/aquaCar.png').convert_alpha()
        ]
    