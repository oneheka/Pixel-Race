import pygame

class Window:
    width = 360
    height = 660

    def __init__(self):
        self.window = pygame.display.set_mode((self.width, self.height))