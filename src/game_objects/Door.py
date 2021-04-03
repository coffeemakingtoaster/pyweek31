from ..superclasses import InteractiveObject
from .. import config

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
                        door = self.door_object(properties['rotation'],x,y)
                        self.door_list.append(door)   
        self.door_list.append(self.door_object(90,1000,1000))
    
    def update(self, player, guards):
        return_bool = False
        for door in self.door_list:
            if door.is_changing and (time.time() - door.time_since_open > 1) :
                door.is_changing = False
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
            collision.append(door.hitbox)                   
        return collision
            
    class door_object():
        def __init__(self, rotation, x, y):
            if rotation % 180 == 0:
                dimensions = (4*3.125,50)
            else:
                dimensions = (50,4*3.125)
            self.hitbox = pygame.Rect((x,y),dimensions)
            self.is_open = False
            self.is_changing = False
            self.x = x
            self.y = y
            self.rotation = rotation
            self.time_since_open = 0
            
            
               
        def open(self):               
            if time.time() - self.time_since_open < 1:
                return False
            self.time_since_open = time.time()
            if self.is_open:
                self.is_open = False
                self.is_changing = True 
                return True
            self.is_changing = True
            self.is_open = True       
            return True
