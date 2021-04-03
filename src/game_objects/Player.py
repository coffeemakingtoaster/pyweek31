import pygame
import math
import time
from collections import defaultdict

from ..config import *
from ..superclasses import Actor
from . import Keycard


class Player(Actor.Actor):
    


    def __init__(self, logic, chests, collision, hiding_spots):
        super().__init__()
        self.logic = logic
        self.x = logic.player_spawn_point[0]
        self.y = logic.player_spawn_point[1]
        self.speed = PLAYER_SPEED
        self.inventory = defaultdict(lambda: 0)
        self.selected_item = None
        self.chests = chests
        self.rotation = 0
        self.coffee_start_time = 0
        self.collision = collision
        self.player_hitbox = pygame.Rect((0,0),(45,45))
        self.player_hitbox.center = (0,0)
        self.time_since_hidden = 0

        self.coinmode = False
        
        self.keypress_time = 0
        self.keypress_wait = 200
        
        self.inventory["coffee"] = 9999999
        self.inventory["jammer"] = 9999999
        self.inventory["donut"] = 9999999
        self.inventory["coin"] = 9999999

        self.has_moved = False
        self.hiding_spots = hiding_spots
        self.is_hidden = False
        
    
    def update(self):
        if not self.is_hidden:
            self.player_movement()
            self.player_interact()
            self.player_use_item()
        else:
            if pygame.key.get_pressed()[PLAYER_INTERACT] == True and time.time() - self.time_since_hidden > 1:
                self.is_hidden = False
                self.time_since_hidden = time.time()
        
    def player_movement(self):
        self.has_moved = True
        new_rotation = -1 
        x_movement = 0
        y_movement = 0      
        if pygame.key.get_pressed()[PLAYER_MOVE_RIGHT] == True:
            x_movement += self.speed
            if pygame.key.get_pressed()[PLAYER_MOVE_UP] == True:
                new_rotation = 315
            elif pygame.key.get_pressed()[PLAYER_MOVE_DOWN] == True:
                new_rotation = 225
            else:
                new_rotation = 270
                
        if pygame.key.get_pressed()[PLAYER_MOVE_LEFT] == True:
            x_movement -= self.speed            
            if pygame.key.get_pressed()[PLAYER_MOVE_UP] == True:
                new_rotation = 45
            elif pygame.key.get_pressed()[PLAYER_MOVE_DOWN] == True:
                new_rotation = 135
            else:
                new_rotation = 90
                
        if pygame.key.get_pressed()[PLAYER_MOVE_DOWN] == True:
            y_movement += self.speed
            if new_rotation == -1:
                new_rotation = 180         
                
        if pygame.key.get_pressed()[PLAYER_MOVE_UP] == True:
            y_movement -= self.speed
            if new_rotation == -1:
                new_rotation = 0 
        if new_rotation != -1:
            self.rotation = new_rotation
        
        move_vector = pygame.Vector2()
        move_vector.xy = x_movement,y_movement
        if move_vector.length() == 0:
            self.has_moved = False
            return
        move_vector.scale_to_length(self.speed)

        #print("player x:{} y:{}".format(self.x,self.y))
        #print("hitbox x:{} y:{}".format(self.player_hitbox.x - 25 ,self.player_hitbox.y - 25))
        
        self.player_hitbox.x += move_vector.x
        for blocker in self.collision:
            if self.player_hitbox.colliderect(blocker):
                self.player_hitbox.x -= move_vector.x
                move_vector.x = 0

        self.player_hitbox.y += move_vector.y
        for blocker in self.collision:
            if self.player_hitbox.colliderect(blocker):
                self.player_hitbox.y -= move_vector.y
                move_vector.y = 0

        if move_vector.x == move_vector.y == 0:
            self.has_moved = False
        
        self.x += move_vector.x
        self.y += move_vector.y
        self.player_hitbox.center = (self.x,self.y)
        
        #print("Player ", "x:" + str(self.x), "y: " + str(self.y))
        
    def player_interact(self):
        if pygame.key.get_pressed()[PLAYER_INTERACT] == True:
            #print("checking")
            closest_object = {"obj":None, "dist":10000, "type":None}
            for chest in self.chests:
                delta = (self.x - chest.x)**2
                if (delta) <=10000:
                    delta += (self.y - chest.y)**2
                    #print("valid chest found")
                    if (self.y - chest.y)**2 <=10000:
                        #print("valid chest found 2")
                        if delta<closest_object["dist"]:
                            closest_object["obj"] = chest
                            closest_object["dist"] = delta
                            closest_object["type"] = "chest"
            for spot in self.hiding_spots:
                if self.player_hitbox.colliderect(spot) and time.time() - self.time_since_hidden > 0.5:
                    self.time_since_hidden = time.time()
                    closest_object["obj"] = spot
                    closest_object["dist"] = None
                    closest_object["type"] = "hiding spot"
                    break
                
            if closest_object["obj"] is not None:
                if closest_object["type"] == "chest":
                    self.add_item_to_inventory(closest_object["obj"].open())
                elif closest_object["type"] == "hiding spot":
                    self.hide_player(closest_object)
                print(self.inventory)
    
    def hide_player(self, spot):
        self.is_hidden = True   
        self.x = spot["obj"].centerx 
        self.y = spot["obj"].centery 
        self.player_hitbox.center = (self.x, self.y)

                
    def player_use_item(self):
        self.use_coffee()
        self.use_coin()
        self.use_donut()
        self.use_jammer()
        
    def use_coffee(self):
        if pygame.key.get_pressed()[HOTKEY_1] == True and self.inventory["coffee"] > 0 and pygame.time.get_ticks() > self.keypress_time:
            self.keypress_time = pygame.time.get_ticks() + self.keypress_wait
            self.inventory["coffee"] -= 1
            self.logic.coffee.drink()
    
    def use_coin(self):
        if pygame.key.get_pressed()[HOTKEY_2] == True and pygame.time.get_ticks() > self.keypress_time:
            self.keypress_time = pygame.time.get_ticks() + self.keypress_wait
            if self.coinmode == False and self.inventory["coin"] > 0 and not self.logic.coin.is_active:
                self.coinmode = True
            elif self.coinmode == True:
                self.coinmode = False
            
        if self.coinmode == True and pygame.mouse.get_pressed()[0] == True and self.inventory["coin"] > 0:
            self.inventory["coin"] -= 1
            pointer_x = self.x - WINDOW_WIDHT / 2 + pygame.mouse.get_pos()[0]
            pointer_y = self.y - WINDOW_HEIGHT / 2 + pygame.mouse.get_pos()[1]
            self.logic.coin.throw(pointer_x, pointer_y)
            self.coinmode = False
            
    def use_donut(self):
        if pygame.key.get_pressed()[HOTKEY_3] == True and self.inventory["donut"] > 0 and pygame.time.get_ticks() > self.keypress_time:
            self.keypress_time = pygame.time.get_ticks() + self.keypress_wait
            self.inventory["donut"] -= 1
            self.logic.donut.place(self.x, self.y)
            
    def use_jammer(self):
        if pygame.key.get_pressed()[HOTKEY_4] == True and self.inventory["jammer"] > 0 and pygame.time.get_ticks() > self.keypress_time:
            self.keypress_time = pygame.time.get_ticks() + self.keypress_wait
            self.inventory["jammer"] -= 1
            self.logic.jammer.activate()
    
    def check_collide(self,x,y):
        hitbox = self.player_hitbox
        hitbox.x = self.player_hitbox.x + x      
        for blocker in self.collision:
            if hitbox.colliderect(blocker):
                return True
        hitbox.y = self.player_hitbox.y + y       
        for blocker in self.collision:
            if hitbox.colliderect(blocker):
                return True      
        return False       

    #call on item pickup    
    def add_item_to_inventory(self,item):
        self.inventory[item] = self.inventory[item] + 1
    
    #call on item drop/use
    def remove_item_to_inventory(self,item):
        self.inventory["item"] =self.inventory["item"] - 1

    #call on itemswitch
    def set_selected_item(self,item):
        if self.inventory["item"]>0:
            self.selected_item = item
        else:
            #print("item is not in the players inventory")
            raise 
