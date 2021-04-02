from ...config import *
from ...superclasses import Item

class Coin(Item.Item):
    def __init__(self, logic):
        super().__init__('coin', logic)
        self.detection_radius = ITEM_COIN_DETECTION_RADIUS
    
    def throw(self, center_x, center_y):
        # TODO: render coin on position?
        
        for guard in self.logic.enemies:
            if (guard.pos.x - center_x)^2 + (guard.pos.y - center_y)^2 <= self.detection_radius^2:
                # set guards waypoint to center_x and center_y
                print(center_x, center_y, guard.pos.x, guard.pos.y)
    
    def collected(self):
        # TODO: delete waypoints from guard's paths
        pass