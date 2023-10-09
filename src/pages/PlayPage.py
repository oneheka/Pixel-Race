import pygame
import random

class PlayPage:
    added = 15

    def __init__(self, game):
        self.game = game
        self.car_x = 152
        self.car_y = 552
        self.coins = 0
        self.metrs = 0
        self.lastAdd = 10
        self.car_rect = 0
        self.staticItems = [
            {
                'id': 'coin',
                'file': self.game.util.coin,
                'y': 0,
                'x': 32
            },
            {
                'id': 'car',
                'file': self.game.util.skins[0],
                'y': 0,
                'x': 144
            }
        ]
        self.items = []

    def render(self):
        self.handler()
        self.updtaeItems()

        self.game.screen.blit(self.game.util.record, ((15, 15)))
        self.game.screen.blit(self.game.util.coins, ((15, 66)))
        
        self.game.screen.blit(
            self.game.util.mainfont.render(
                str(round(self.metrs / self.added))+'m', False, 'white'
            ), ((22, 24))
        )

        self.game.screen.blit(
            self.game.util.mainfont.render(
                str(self.coins), False, 'white'
            ), ((22, 75))
        )
    
        for i in self.game.config['skins']:
                if i['default'] == True:
                    self.car_rect = self.game.util.getImage(i['name']).get_rect(topleft=(self.car_x, self.car_y))
                    self.game.screen.blit(
                        self.game.util.getImage(i['name']),
                        ((self.car_x, self.car_y))
                    )
        
    def startGame(self):
        self.car_x = 152
        self.metrs = 1
        self.coins = 0
    
    def gameOver(self):
        self.game.lastStars = self.coins
        self.game.lastMetrs = round(self.metrs / self.added)
        self.game.config['coins'] += self.coins
        if(round(self.metrs / self.added) > self.game.config['record']):
            self.game.config['record'] = round(self.metrs / self.added)
            self.game.updateConfig(self.game.config)
        self.coins = 0
        self.metrs = 0
        self.lastAdd = 10
        self.items = []
        self.game.updateConfig(self.game.config)
        if(self.game.state != "Lose"):
            self.game.state = 'Lose'
    
    def randomItem(self):
        return self.staticItems[random.randint(0, len(self.staticItems)-1)].copy()
    
    def randomX(self, ignore):
        x = list(filter(lambda n: n not in ignore, [ 32, 150, 274 ]))
        return x[random.randint(0, len(x)-1)]
        
    def handler(self):
        keys = pygame.key.get_pressed()
        if(not self.game.paused):
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
        if(not self.game.paused):
            if(round(self.metrs / self.added) > self.lastAdd):
                count = random.randint(1, 2)
                ignore = []
                for i in range(count):
                    self.lastAdd += self.added
                    x = self.randomX(ignore)
                    ignore.append(x)
                    item = self.randomItem()
                    item['y'] = 0
                    item['x'] = x
                    self.items.append(item)
        
        for item in self.items:
            item['y'] += self.getY()
            if(item['file'].get_rect(topleft=(item['x'], item['y'])).colliderect(self.car_rect)):
                if(item['id'] == 'coin'):
                    self.coins += 1
                    self.items.remove(item)
                elif(item['id'] == 'car'):
                    self.gameOver()
                
            self.game.screen.blit(item['file'], ((item['x'], item['y'])))
            