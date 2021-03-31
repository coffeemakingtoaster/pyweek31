import pygame
import time
from threading import Timer


from collections import defaultdict

from ..config import *
from ..superclasses import Actor

class Player(Actor.Actor):

    def __init__(self,chests):
        super().__init__()
        self.x = 0
        self.y = 0
        self.speed = PLAYER_SPEED
        self.inventory = defaultdict(lambda: 0)
        self.selected_item = None
        self.chests = chests
        self.rotation = 0
        self.coffee_start_time = 0
        
    
    def update(self):
        self.player_movement()
        self.player_interact()
        self.player_use_item()
        
    def player_movement(self):
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
        
        self.rotation = new_rotation
        
        move_vector = pygame.Vector2()
        move_vector.xy = x_movement,y_movement
            
        if move_vector.length() > self.speed:
            print("normalizing")   
            move_vector.scale_to_length(self.speed)
            self.x += move_vector.x
            self.y += move_vector.y
            return
        self.x += x_movement
        self.y += y_movement
        

        #print("Player ", "x:" + str(self.x), "y: " + str(self.y))
        
    def player_interact(self):
        if pygame.key.get_pressed()[PLAYER_INTERACT] == True:
            print("checking")
            closest_object = {"obj":None, "dist":10000}
            for chest in self.chests:
                delta = (self.x - chest.x)**2
                print(delta)
                if (delta) <=10000:
                    delta += (self.y - chest.y)**2
                    print("valid chest found")
                    if (self.y - chest.y)**2 <=10000:
                        print("valid chest found 2")
                        if delta<closest_object["dist"]:
                            closest_object["obj"] = chest
                            closest_object["dist"] = delta
            if closest_object["obj"] is not None:
                self.add_item_to_inventory(closest_object["obj"].open())
                print(self.inventory)
                
    def player_use_item(self):
        used_item = None
        
        if  time.time() - self.coffee_start_time > ITEM_COFFEE_DURATION and self.speed==ITEM_COFFEE_SPEED:
            self.speed = PLAYER_SPEED
            print("coffee has worn off")
        if pygame.key.get_pressed()[HOTKEY_1] == True:
            used_item = "coffee"
            
        if used_item is None:
            return
        
        print(self.inventory["coffee"])
        if used_item == "coffee" and self.inventory["coffee"]>0 and not self.speed==ITEM_COFFEE_SPEED:
            print(self.inventory["coffee"])
            print("Now using {}".format(used_item))           
            self.inventory["coffee"] -=1
            self.speed = ITEM_COFFEE_SPEED
            self.coffee_start_time = time.time()        
            
            

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
            print("item is not in the players inventory")
            raise 
