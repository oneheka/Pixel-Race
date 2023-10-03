import pygame

class MainPage:
    def __init__(self, main):
        self.main = main

    def render(self):
        self.main.fill('red')