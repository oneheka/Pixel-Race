import pygame

class Font:
    def load(self):
        self.fonts = {
            'main': pygame.font.Font('assets/fonts/efnmacstyle8px.ttf', 24)
        }

    def render(self, text, color = 'white'):
        return self.fonts['main'].render(str(text), False, color)