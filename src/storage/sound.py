import pygame
import os

class Sound:
    _cache = []
    _selected = 0
    isPlaying = False

    def load(self):
        for filename in os.listdir('assets/music'):
            self._cache.append(
                {
                    'label': filename.split('.')[0],
                    'file': pygame.mixer.Sound(f'assets/music/{filename}')
                }
            )
        
    def array(self):
        return self._cache
    
    def setSound(self, index):
        if bool(self._cache[index]):
            self._selected = index
            return self._cache[index]
        else:
            return False
    
    @property
    def selected(self):
        return self._selected
    
    @property
    def active(self):
        return self._cache[self._selected]