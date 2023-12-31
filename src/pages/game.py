import pygame
import random

class Game:
    added = 15
    car_x = 152
    car_y = 552
    coins = 0
    metrs = 0
    lastAdd = 10
    items = []
    speedY = 0

    def __init__(self, core):
        self.core = core
        self.staticItems = [
            {
                'id': 'coin',
                'file': core.images.coins['big'],
                'y': 0,
                'x': 0
            },
            {
                'id': 'car',
                'file': core.images.opponents[0],
                'y': 0,
                'x': 0
            },
            {
                'id': 'car',
                'file': core.images.opponents[1],
                'y': 0,
                'x': 0
            },
            {
                'id': 'car',
                'file': core.images.opponents[2],
                'y': 0,
                'x': 0
            }
        ]

    def render(self, events):
        if(not self.core.paused):
            self.handler()
        
        self.updtaeItems()
        self.speedometer()

        self.core.window.blit(self.core.images.stats, (16, 16))
        self.core.window.blit(
            self.core.fonts.render(
                str(self.getMetrs())+'m'
            ), (25, 26)
        )

        self.core.window.blit(self.core.images.stats, (16, 60))
        self.core.window.blit(self.core.images.coins['small'], (76, 68))
        self.core.window.blit(
            self.core.fonts.render(
                str(self.coins)
            ), (25, 70)
        )

        for i in self.core.config['skins']:
            if i['default'] == True:
                name = i['name'].lower()
                self.car_rect = self.core.images.getSkin(name).get_rect(topleft=(self.car_x, self.car_y))
                self.core.window.blit(
                    self.core.images.getSkin(name),
                    (self.car_x, self.car_y)
                )
    
    def speedometer(self):
        self.core.window.blit(self.core.images.speedometer, (256, 16))
        speed = self.core.fonts.render(self.formatSpeed())
        self.core.window.blit(
            speed, speed.get_rect(center=(303, 61))
        )
        pygame.draw.arc(
            self.core.window, (255, 69, 59), (256, 16, 96, 96),
            3.14 * 3 / 2, self.formulaSpeed(3.14) * 16 + (3.14 * 3 / 2), 10
        )


    def startGame(self):
        self.car_x = 152
        self.metrs = 1
        self.coins = 0
    
    def gameOver(self):
        self.core.sounds.others['CarDestroy'].play()
        self.core.lastStars = self.coins
        self.core.lastMetrs = self.getMetrs()
        self.core.config['coins'] += self.coins
        if(self.getMetrs() > self.core.config['record']):
            self.core.config['record'] = self.getMetrs()
            self.core.updateConfig(self.core.config)
        self.coins = 0
        self.metrs = 0
        self.speedY = 0
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
        if(100 > self.getMetrs()):
            return 1.5
        elif(250 > self.getMetrs()):
            return 2
        elif(500 > self.getMetrs()):
            return 2.5
        elif(750 > self.getMetrs()):
            return 3
        elif(1000 > self.getMetrs()):
            return 3.5
        elif(1250 > self.getMetrs()):
            return 4
        elif(1500 > self.getMetrs()):
            return 5
        elif(1750 > self.getMetrs()):
            return 6
        else:
            return 7
    
    def getMetrs(self):
        return round(self.metrs / self.added)
    
    def formulaSpeed(self, count):
        return self.getMetrs() / 10000 * count
    
    def getSpeed(self):
        self.speedY = self.formulaSpeed(self.core.config['skins'][self.core.selectSkin]['speed'])
        return self.speedY
    
    def formatSpeed(self):
        return round(self.speedY * 350)
    
    def updtaeItems(self):
        if(not self.core.paused):
            if(self.getMetrs() > self.lastAdd):
                count = random.randint(1, 2)
                ignore = []
                for i in range(count):
                    self.lastAdd += self.added
                    x = self.randomX(ignore)
                    ignore.append(x)
                    item = self.randomItem()
                    item['y'] = random.randint(-110, -80)
                    item['x'] = x
                    self.items.append(item)
        
        for item in self.items:
            if(not self.core.paused):
                item['y'] += (self.getY() + self.getSpeed())

            if(item['file'].get_rect(topleft=(item['x'], item['y'])).colliderect(self.car_rect)):
                if(item['id'] == 'coin'):
                    self.coins += 1
                    self.core.sounds.others['CoinCollect'].play()
                    self.items.remove(item)
                elif(item['id'] == 'car'):
                    self.gameOver()
                
            self.core.window.blit(item['file'], (item['x'], item['y']))