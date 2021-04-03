from ...config import *
from ...superclasses import Item
from ..helper.Point import Point

class Coin(Item.Item):
    def __init__(self, logic):
        super().__init__('coin', logic)
        self.detection_radius = ITEM_COIN_DETECTION_RADIUS
        self.is_active = False
        self.x = 0
        self.y = 0
    
    def throw(self, center_x, center_y):
        # TODO: render coin on position?
        
        for guard in self.logic.enemies:
            if self.is_in_range(guard, center_x, center_y):
                if guard.check_vision():
                    guard.former_current_waypoint = guard.current_waypoint
                    guard.off_patrol_position = Point(guard.pos.x, guard.pos.y)
                    guard.waypoints.insert(guard.current_waypoint, guard.off_patrol_position)
                    guard.waypoints.insert(guard.current_waypoint, Point(center_x, center_y))
                    self.is_active = True
                    self.x = center_x
                    self.y = center_y
                    
    def is_in_range(self, actor, center_x, center_y):
        return pygame.math.Vector2(actor.pos.x - center_x, actor.pos.y - center_y).length() <= self.detection_radius
    
    def collection_handling(self):
        if self.is_active:
            for guard in self.logic.enemies:
                if guard.pos.x <= self.x + 10 and guard.pos.x >= self.x - 10 and guard.pos.y <= self.y + 10 and guard.pos.y >= self.y - 10:
                    self.is_active = False
                    for guard in self.logic.enemies:
                        if self.is_in_range(guard, self.x, self.y):
                            if guard.check_vision():
                                pass