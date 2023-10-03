class MainPage:
    def __init__(self, screen):
        self.screen = screen

    def render(self):
        print(self)
        self.screen.fill('black')