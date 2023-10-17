import pygame

class Window:
    self.width = 360
    self.height = 660

    def __init__(self):
        self.window = pygame.display.set_mode((self.width, self.height))