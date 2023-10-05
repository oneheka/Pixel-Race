import pygame

class PlayPage:
    def __init__(self, game):
        self.game = game
        self.car_x = 152

    def render(self):
        self.game.screen.blit(self.game.util.record, ((15, 15)))
        self.game.screen.blit(self.game.util.coins, ((15, 66)))
        
        self.handler()

        for i in self.game.config['skins']:
            if i['default'] == True:
                # print(i['name'])
                self.game.screen.blit(
                    self.game.util.getImage(i['name']),
                    ((self.car_x, 552))
                )   
        
    def handler(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.car_x > 19:
            self.car_x -= 2
        elif keys[pygame.K_RIGHT] and self.car_x < 277:
            self.car_x += 2
        