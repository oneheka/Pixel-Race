from storage.sound import Sound
from storage.image import Image
from storage.font import Font
import json

class Util:
    _config = {}
    _configDir = 'assets/config.json'
    storage = {
        'image': Image(),
        'sound': Sound(),
        'font': Font()
    }
    eronary_y = 0
    walpuper_y = 0
    aqua_y = 0

    def load(self):
        self.storage['image'].load()
        self.storage['sound'].load()
        self.storage['font'].load()
        self._config = self.getConfig()
        
    @property
    def config(self):
        if(str(self._config) == '{}'):
            self._config = self.getConfig()
        
        return self._config
    
    @property
    def images(self):
        return self.storage['image']
    
    @property
    def sounds(self):
        return self.storage['sound']

    @property
    def fonts(self):
        return self.storage['font']
    
    def getConfig(self):
        with open(self._configDir) as f:
            file_content = f.read()
            return json.loads(file_content)
    
    def updateConfig(self, config):
        with open(self._configDir, 'w') as f:
            f.seek(0)
            json.dump(config, f)
            f.truncate()
    
    def updateCarAnimation(self):
        self.eronary_y -= 2
        if (-1100 > self.eronary_y):
            self.eronary_y = 0
            
        if (self.eronary_y > -342):
            if(self.walpuper_y > -2):
                self.walpuper_y = 1
        if(self.walpuper_y != 0):
            self.walpuper_y -= 2
        if (-1100 > self.walpuper_y):
            self.walpuper_y = 0
            
    
        if (self.walpuper_y > -391):
            if(self.aqua_y > -2):
                self.aqua_y = 1
        if(self.aqua_y != 0):
            self.aqua_y -= 2
        if(-1100 > self.aqua_y):
            self.aqua_y = 0