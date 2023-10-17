import pygame
from str.Window import Window

class Game:
    window = Window()

    def __init__(self):
        pygame.init()
    

    #def build():
        #pygame.display.set_icon(self.util.icon)

    def start(self):
        while True:
            pygame.display.update()
            pygame.time.Clock().tick(300)


Game().start()
