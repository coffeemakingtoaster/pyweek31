from ..superclasses import InteractiveObject

import pygame
import pytmx
import time

class Door_Container(InteractiveObject.InteractiveObject):

    def __init__(self, map):
        super().__init__()
        self.door_list = []
        self.map = map
        self.get_doors()
       
    def get_doors(self):
        for layer in self.map.visible_layers:
            if isinstance(layer, pytmx.TiledObjectGroup):
                # access collision object
                for collision_object in layer:
                    properties = collision_object.__dict__
                    if properties["name"] == "'door'":
                        x = properties['x'] * (config.TILE_SIZE/16)
                        y = properties['y'] * (config.TILE_SIZE/16)
                        width = properties['width'] * (config.TILE_SIZE/16)
                        height = properties['height'] * (config.TILE_SIZE/16)
                        door = self.door_object(properties['rotation'],pygame.Rect(x, y, width, height))
                        self.door_list.append(door)   
        self.door_list.append(self.door_object(90,pygame.Rect(1000, 1000, 50, 50)))    
    
    def update(self, player, guards):
        return_bool = False
        for door in self.door_list:
            if door.hitbox.colliderect(player.player_hitbox):
                return_bool = door.open()
            else:
                for guard in guards:
                    if door.hitbox.colliderect(guard.hitbox): 
                        return_bool = door.open()
                        break
        
        return return_bool
                    
    
    def add_closed_doors(self, collision):
        for door in self.door_list:
            if not door.is_open:         
                collision.append(door.hitbox)
        return collision
            
    class door_object():
        def __init__(self, rotation, rect):
            self.x = rect.x
            self.y = rect.y
            self.is_open = False
            self.default_rotation = rotation
            self.hitbox = rect
            self.time_since_open = 0
            
        def open(self):         
            if time.time() - self.time_since_open < 1:
                return False
            self.time_since_open = time.time()
            if self.is_open:
                self.is_open = False
                return True
            self.is_open = True 
            return True
