from ...config import *
from ...superclasses import Item
import time, threading

class Jammer(Item.Item):
    def __init__(self, logic):
        super().__init__('jammer', logic)
        self.duration = ITEM_JAMMER_DURATION
    
    def activate(self):
        self.logic.soundHelper.play_tickless_sfx(self.logic.assets["sounds"]["jammer"], 0)
        x = self.logic.player.x
        y = self.logic.player.y
        for guard in self.logic.enemies:
            guard.ray_length = ITEM_JAMMER_RAY_LENGTH
        threading.Timer(self.duration, self.reset).start()
          
    def reset(self):
        for guard in self.logic.enemies:
            guard.ray_length = GUARD_SIGHT_LENGTH