from ...config import *
from ...superclasses import Item

class Donut(Item.Item):
    def __init__(self, logic):
        super().__init__('donut', logic)
        self.duration = ITEM_DONUT_DURATION
        
    def place(self, x, y):
        # TODO: render coin on position?
        # self.collision_rect = pygame.Rect(x, y, width, height)
        pass
        
    # def is_colliding(self):
        # for guard in self.logic.enemies:
            