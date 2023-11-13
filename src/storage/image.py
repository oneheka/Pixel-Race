import pygame
import os

class Image:
    def load(self):
        self.logo = pygame.image.load('assets/images/Logo.png').convert_alpha()
        self.background = pygame.image.load('assets/images/Background.png').convert_alpha()
        self.blur = pygame.image.load('assets/images/Blur.png').convert_alpha()
        self.modal = pygame.image.load('assets/images/Modal.png').convert_alpha()
        self.stats = pygame.image.load('assets/images/Stats.png').convert_alpha()
        self.speedometer = pygame.image.load('assets/images/Speedometer.png').convert_alpha()
        self.skin_background = pygame.image.load('assets/images/SkinBackground.png').convert_alpha()
        self.toggle = {
            'on': pygame.image.load('assets/images/toggle/On.png').convert_alpha(),
            'off': pygame.image.load('assets/images/toggle/Off.png').convert_alpha()
        }
        self.settings = {
            'open': pygame.image.load('assets/images/Settings.png').convert_alpha(),
            'close': pygame.image.load('assets/images/Exit.png').convert_alpha()
        }
        self.coins = {
            'small': pygame.image.load('assets/images/coins/Small.png').convert_alpha(),
            'big': pygame.image.load('assets/images/coins/Big.png').convert_alpha()
        }
        self.buttons = {
            'play': pygame.image.load('assets/images/button/Play.png').convert_alpha(),
            'shop': pygame.image.load('assets/images/button/Shop.png').convert_alpha(),
            'again': pygame.image.load('assets/images/button/Again.png').convert_alpha(),
            'apply': pygame.image.load('assets/images/button/Apply.png').convert_alpha(),
            'buy': pygame.image.load('assets/images/button/Buy.png').convert_alpha(),
            'expensive': pygame.image.load('assets/images/button/Expensive.png').convert_alpha(),
            'menu': pygame.image.load('assets/images/button/Menu.png').convert_alpha(),
            'selected': pygame.image.load('assets/images/button/Selected.png').convert_alpha()
        }
        self.texts = {
            'sound': pygame.image.load('assets/images/text/Sound.png').convert_alpha(),
            'night': pygame.image.load('assets/images/text/Night.png').convert_alpha(),
            'lose': pygame.image.load('assets/images/text/Lose.png').convert_alpha(),
            'choose_music': pygame.image.load('assets/images/text/ChooseMusic.png').convert_alpha()
        }
        self.skins = {
            'eronary': pygame.image.load('assets/images/skins/Eronary.png').convert_alpha(),
            'aqua': pygame.image.load('assets/images/skins/Aqua.png').convert_alpha(),
            'walpuper': pygame.image.load('assets/images/skins/Walpuper.png').convert_alpha(),
            'rider_blade': pygame.image.load('assets/images/skins/RiderBlade.png').convert_alpha()
        }
        self.dropdown = {
            'open': pygame.image.load('assets/images/MusicDropdownOpen.png').convert_alpha(),
            'close': pygame.image.load('assets/images/MusicDropdownClose.png').convert_alpha()
        }
        self.block = {
            'song': pygame.image.load('assets/images/block/ChooseSong.png').convert_alpha(),
            'active_song': pygame.image.load('assets/images/block/ActiveSong.png').convert_alpha()
        }
        self.arrows = {
            'left': pygame.image.load('assets/images/arrow/Left.png').convert_alpha(),
            'right': pygame.image.load('assets/images/arrow/Right.png').convert_alpha()
        }
        self.asphalt = {
            'day': pygame.image.load('assets/images/asphalt/Day.png').convert_alpha(),
            'night': pygame.image.load('assets/images/asphalt/Night.png').convert_alpha()
        }
        self._loadOpponents()
        
    
    def getSkin(self, name):
        return self.skins[name]
    
    def _loadOpponents(self):
        self.opponents = []
        for filename in os.listdir('assets/images/opponents'):
            self.opponents.append(
                pygame.image.load(f'assets/images/opponents/{filename}').convert_alpha(),
            )