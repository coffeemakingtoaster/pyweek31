from ...config import *
from ...superclasses import Item
from ..helper.Point import Point

import time, threading

class Coin(Item.Item):
    def __init__(self, logic):
        super().__init__('coin', logic)
        self.logic = logic
        self.detection_radius = ITEM_COIN_DETECTION_RADIUS
        self.is_active = False
        self.is_rendered = False
        self.render_duration = ITEM_COIN_RENDER_DURATION
        self.x = 0
        self.y = 0
    
    def throw(self, center_x, center_y):
        self.x = center_x
        self.y = center_y
        self.is_rendered = True
        guard_in_range = False

        if not self.is_active:
            self.logic.soundHelper.play_tickless_sfx(self.logic.assets["sounds"]["coin"], 0)
        for guard in self.logic.enemies:
            if self.is_in_range(guard, center_x, center_y):
                if guard.check_vision_to_point(Point(center_x, center_y)):
                    guard.former_current_waypoint = guard.current_waypoint
                    guard.off_patrol_position = Point(guard.pos.x, guard.pos.y)
                    guard.waypoints.insert(guard.current_waypoint, guard.off_patrol_position)
                    guard.waypoints.insert(guard.current_waypoint, Point(center_x, center_y))
                    self.is_active = True
                    guard_in_range = True
                    
        if guard_in_range == False:       
            threading.Timer(self.render_duration, self.stop_render).start()
        
    def is_in_range(self, actor, center_x, center_y):
        return pygame.math.Vector2(actor.pos.x - center_x, actor.pos.y - center_y).length() <= self.detection_radius
        
    def stop_render(self):
        self.is_rendered = False
