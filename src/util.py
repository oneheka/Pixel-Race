import pygame
import os

class Util:
    def __init__(self):
        self.mainfont = pygame.font.Font('fonts/efnmacstyle8px.ttf', 20)
        self.buttons = [
            pygame.image.load('assets/images/buttons/playButton.png').convert_alpha(),
            pygame.image.load('assets/images/buttons/skinsButton.png').convert_alpha()
        ]
        self.icon = pygame.image.load('assets/images/icon.png').convert_alpha()
        self.background = pygame.image.load('assets/images/bg.png').convert_alpha()
        self.settingsBackground = pygame.image.load('assets/images/settings_bg.png').convert_alpha()
        self.darkerBackground = pygame.image.load('assets/images/darker_bg.png').convert_alpha()
        self.coins = pygame.image.load('assets/images/coins.png').convert_alpha()
        self.coin = pygame.image.load('assets/images/coin.png').convert_alpha()
        self.record = pygame.image.load('assets/images/record.png').convert_alpha()
        self.skins_page = [
                pygame.image.load('assets/images/skins_plate.png').convert_alpha(),
                pygame.image.load('assets/images/buttons/buyButton.png').convert_alpha(),
                pygame.image.load('assets/images/buttons/noBuyButton.png').convert_alpha(),
                pygame.image.load('assets/images/buttons/setButton.png').convert_alpha(),
                pygame.image.load('assets/images/buttons/leftArrow.png').convert_alpha(),
                pygame.image.load('assets/images/buttons/rightArrow.png').convert_alpha()
        ]
        self.settings = [
            pygame.image.load('assets/images/settings.png').convert_alpha(),
            pygame.image.load('assets/images/settings_exit.png').convert_alpha(),
            pygame.image.load('assets/images/settings_text.png').convert_alpha(),
            pygame.image.load('assets/images/buttons/toggle_on.png').convert_alpha(),
            pygame.image.load('assets/images/buttons/toggle_off.png').convert_alpha(),
            pygame.image.load('assets/images/music_choiser.png').convert_alpha(),
            pygame.image.load('assets/images/settings_text2.png').convert_alpha(),
            pygame.image.load('assets/images/select_opened.png').convert_alpha(),
            pygame.image.load('assets/images/buttons/song.png').convert_alpha(),
            pygame.image.load('assets/images/buttons/choosen_song.png').convert_alpha()
        ]
        self.skins = [
            pygame.image.load('assets/images/skins/eronaryCar.png').convert_alpha(),
            pygame.image.load('assets/images/skins/walpuperCar.png').convert_alpha(),
            pygame.image.load('assets/images/skins/aquaCar.png').convert_alpha(),
        ]
        #self.sounds = [
        #    pygame.mixer.Sound('assets/music/sound_1.mp3'),
        #    pygame.mixer.Sound('assets/music/sound_2.mp3'),
        #    pygame.mixer.Sound('assets/music/sound_3.mp3')
        #]

        self.sounds = []
        for filename in os.listdir('assets/music'):
            self.sounds.append(
                {
                    'name': (filename.split('.')[0]),
                    'file': pygame.mixer.Sound(f'assets/music/{filename}'),
                }
            )

    
    def getImage(self, name):
        if(name == 'Eronary'):
            return self.skins[0]
        elif(name == 'Walpuper'):
            return self.skins[1]
        else:
            return self.skins[2]