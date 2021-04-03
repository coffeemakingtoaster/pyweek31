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
        self.door_list.append(self.door_object(0,850,1100))
    
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
            collision.append(door.hitbox)                   
        return collision
            
    class door_object():
        def __init__(self, rotation, x, y):
            self.hitbox = self.calc_inital_hitbox(rotation, x, y)
            self.x = self.hitbox.x
            self.y = self.hitbox.y
            self.is_open = False
            self.default_rotation = rotation   
            self.time_since_open = 0
            self.old_hitbox_center = self.hitbox.center
            
        
        def calc_inital_hitbox(self, rotation, x, y):
            if rotation == 0 or rotation == 180:
                dimension = (4*3.125, 50)
            else:
                dimension = (50, 4*3.125)
            rect = pygame.Rect((0,0), dimension)
            w,h = dimension
            rect.center = (x,y)
            self.old_hitbox_dimensions = dimension
            return rect
        
        
        #this produces weird ass numbers on first open...
        #TODO: please fix          
        def open(self):               
            if time.time() - self.time_since_open < 1:
                return False
            print(self.hitbox.center) 
            self.time_since_open = time.time()
            if self.is_open:
                self.is_open = False
                self.hitbox.center = self.old_hitbox_center
                self.x = self.hitbox.x
                self.y = self.hitbox.y 
                width, height = self.old_hitbox_dimensions
                self.hitbox.width = width
                self.hitbox.height = height  
                return True
            self.is_open = True       
            if self.default_rotation == 180 or self.default_rotation == 0:
                x,y = self.hitbox.topleft
                self.hitbox.center = ((x + config.TILE_SIZE/2,y - (4*(config.TILE_SIZE/16))/2))
                height, width = self.old_hitbox_dimensions
                self.hitbox.width = width
                self.hitbox.height = height 
                self.x = self.hitbox.x
                self.y = self.hitbox.y
            else:
                x,y = self.hitbox.topright
                self.hitbox.center = ((x - config.TILE_SIZE/2,y + (4*(config.TILE_SIZE/16))/2))
                height,width = self.old_hitbox_dimensions
                self.hitbox.width = width
                self.hitbox.height = height 
                self.x = self.hitbox.x
                self.y = self.hitbox.y 
            return True
