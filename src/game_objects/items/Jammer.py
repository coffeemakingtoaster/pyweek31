from ...config import *
from ...superclasses import Item

class Jammer(Item.Item):
    def __init__(self, logic):
        super().__init__('jammer', logic)
        self.duration = ITEM_JAMMER_DURATION
    
    def activate(self):
        x = self.logic.player.x
        y = self.logic.player.y
        print(x, y)