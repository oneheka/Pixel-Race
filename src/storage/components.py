class Components:
    def __init__(self, core):
        self.core = core

    def switcher(self, state, position):
        return self.core.window.blit(
            self.core.images.toggle['on' if state else 'off'],
            position
        )
    
    def settings(self, state, position):
        return self.core.window.blit(
            self.core.images.settings['open' if state else 'close'],
            position
        )