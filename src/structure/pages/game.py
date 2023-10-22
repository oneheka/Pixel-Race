import pygame
import random

class Game:
    added = 15
    car_x = 152
    car_y = 552
    coins = 0
    metrs = 0
    lastAdd = 10
    car_rect = 0
    items = []

    def __init__(self, core):
        self.core = core
        self.staticItems = [
            {
                'id': 'coin',
                'file': core.images.coins['big'],
                'y': 0,
                'x': 32
            },
            {
                'id': 'car',
                'file': core.images.skins['walpuper'],
                'y': 0,
                'x': 144
            }
        ]

    def render(self, clicked):
        if(not self.core.paused):
            self.handler()
        
        self.updtaeItems()

        self.core.window.blit(self.core.images.stats, (15, 15))
        self.core.window.blit(
            self.core.fonts.render(
                str(round(self.metrs / self.added))+'m'
            ), ((22, 24))
        )

        self.core.window.blit(self.core.images.stats, (15, 66))
        self.core.window.blit(
            self.core.fonts.render(
                str(self.coins)
            ), ((22, 75))
        )
        self.core.window.blit(self.core.images.coins['small'], (74, 74))

        for i in self.core.config['skins']:
            if i['default'] == True:
                self.car_rect = self.core.images.getSkin(i['name'].lower()).get_rect(topleft=(self.car_x, self.car_y))
                self.core.window.blit(
                    self.core.images.getSkin(i['name'].lower()),
                    (self.car_x, self.car_y)
                )
        
    def startGame(self):
        self.car_x = 152
        self.metrs = 1
        self.coins = 0
    
    def gameOver(self):
        self.core.lastStars = self.coins
        self.core.lastMetrs = round(self.metrs / self.added)
        self.core.config['coins'] += self.coins
        if(round(self.metrs / self.added) > self.core.config['record']):
            self.core.config['record'] = round(self.metrs / self.added)
            self.core.updateConfig(self.core.config)
        self.coins = 0
        self.metrs = 0
        self.lastAdd = 10
        self.items = []
        self.core.updateConfig(self.core.config)
        if(self.core.page != "lose"):
            self.core.page = 'lose'
    
    def randomItem(self):
        return self.staticItems[random.randint(0, len(self.staticItems)-1)].copy()
    
    def randomX(self, ignore):
        x = list(filter(lambda n: n not in ignore, [ 32, 150, 274 ]))
        return x[random.randint(0, len(x)-1)]
        
    def handler(self):
        keys = pygame.key.get_pressed()
        if(not self.core.paused):
            if keys[pygame.K_LEFT] and self.car_x > 19:
                self.car_x -= 2
            elif keys[pygame.K_RIGHT] and self.car_x < 277:
                self.car_x += 2

    def getY(self):
        if(100 > round(self.metrs / self.added)):
            return 1.5
        elif(250 > round(self.metrs / self.added)):
            return 2
        elif(500 > round(self.metrs / self.added)):
            return 2.5
        elif(750 > round(self.metrs / self.added)):
            return 3
        elif(1000 > round(self.metrs / self.added)):
            return 3.5
        elif(1250 > round(self.metrs / self.added)):
            return 4
        elif(1500 > round(self.metrs / self.added)):
            return 5
        elif(1750 > round(self.metrs / self.added)):
            return 6
        else:
            return 7
    
    def updtaeItems(self):
        if(not self.core.paused):
            if(round(self.metrs / self.added) > self.lastAdd):
                count = random.randint(1, 2)
                ignore = []
                for i in range(count):
                    self.lastAdd += self.added
                    x = self.randomX(ignore)
                    ignore.append(x)
                    item = self.randomItem()
                    item['y'] = -80
                    item['x'] = x
                    self.items.append(item)
        
        for item in self.items:
            if(not self.core.paused):
                item['y'] += self.getY()

            if(item['file'].get_rect(topleft=(item['x'], item['y'])).colliderect(self.car_rect)):
                if(item['id'] == 'coin'):
                    self.coins += 1
                    self.items.remove(item)
                elif(item['id'] == 'car'):
                    self.gameOver()
                
            self.core.window.blit(item['file'], (item['x'], item['y']))
