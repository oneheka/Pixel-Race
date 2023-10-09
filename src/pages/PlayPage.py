import pygame
import random

class PlayPage:
    def __init__(self, game):
        self.game = game
        self.car_x = 152
        self.car_y = 552
        self.coins = 0
        self.metrs = 0
        self.lastAdd = 10
        self.staticItems = [
            {
                'id': 'coin',
                'file': game.util.coin,
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
        self.game.screen.blit(self.game.util.record, ((15, 15)))
        self.game.screen.blit(self.game.util.coins, ((15, 66)))
        
        self.handler()
        self.updtaeItems()

        self.game.screen.blit(
            self.game.util.mainfont.render(
                str(round(self.metrs / 15))+'m', False, 'white'
            ), ((22, 24))
        )

        self.game.screen.blit(
            self.game.util.mainfont.render(
                str(self.coins), False, 'white'
            ), ((22, 75))
        )

        for i in self.game.config['skins']:
            if i['default'] == True:
                self.game.screen.blit(
                    self.game.util.getImage(i['name']),
                    ((self.car_x, self.car_y))
                )
    
    def startGame(self):
        self.car_x = 152
        self.metrs = 1
        self.coins = 0
    
    def gameOver(self):
        self.game.config['coins'] += self.coins
        if(round(self.metrs / 15) > self.game.config['record']):
            self.game.config['record'] = round(self.metrs / 15)
            self.game.updateConfig(self.game.config)
        self.coins = 0
        self.metrs = 0
        self.lastAdd = 10
        self.items = []
        self.game.updateConfig(self.game.config)
        if(self.game.state != "Menu"):
            self.game.state = 'Menu'
    
    def randomItem(self):
        return self.staticItems[random.randint(0, len(self.staticItems)-1)].copy()
    
    def randomX(self):
        x = [ 32, 150, 274 ]
        return x[random.randint(0, len(x)-1)]
        
    def handler(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.car_x > 19:
            self.car_x -= 2
        elif keys[pygame.K_RIGHT] and self.car_x < 277:
            self.car_x += 2
        elif keys[pygame.K_SPACE]:
            if(self.game.state != "Menu"):
                self.game.state = 'Menu'
    
    def getY(self):
        if(100 > round(self.metrs / 15)):
            return 1.5
        elif(250 > round(self.metrs / 15)):
            return 2
        elif(500 > round(self.metrs / 15)):
            return 2.5
        elif(750 > round(self.metrs / 15)):
            return 3
        else:
            return 3.5
    
    def updtaeItems(self):
        if(round(self.metrs / 15) > self.lastAdd):
            self.lastAdd += 15
            item = self.randomItem()
            item['y'] = 0
            item['x'] = self.randomX()
            self.items.append(item)
        
        for item in self.items:
            item['y'] += self.getY()
            
            if(self.car_x > item['x']-24 and item['x']+24 > self.car_x and item['y'] > self.car_y and self.car_y + 100 > item['y']):
                if(item['id'] == 'coin'):
                    self.coins += 1
                    self.items.remove(item)
                elif(item['id'] == 'car'):
                    self.gameOver()
                
            self.game.screen.blit(item['file'], ((item['x'], item['y'])))
            