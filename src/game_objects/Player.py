import pygame
from collections import defaultdict

from ..config import *
from ..superclasses import Actor

class Player(Actor.Actor):

    def __init__(self,chests):
        super().__init__()
        self.x = 0
        self.y = 0
        self.speed = 10
        self.inventory = defaultdict(lambda: 0)
        self.selected_item = None
        self.chests = chests
        self.orientation = [0,1]
        self.rotation = 0
    
    def update(self):
        self.player_movement()
        self.player_interact()
        
    def player_movement(self):
        new_rotation = -1       
        if pygame.key.get_pressed()[PLAYER_MOVE_RIGHT] == True:
            self.x += self.speed
            if pygame.key.get_pressed()[PLAYER_MOVE_UP] == True:
                new_rotation = 315
            elif pygame.key.get_pressed()[PLAYER_MOVE_DOWN] == True:
                new_rotation = 225
            else:
                new_rotation = 270
                
        if pygame.key.get_pressed()[PLAYER_MOVE_LEFT] == True:
            self.x -= self.speed            
            if pygame.key.get_pressed()[PLAYER_MOVE_UP] == True:
                new_rotation = 45
            elif pygame.key.get_pressed()[PLAYER_MOVE_DOWN] == True:
                new_rotation = 135
            else:
                new_rotation = 90
                
        if pygame.key.get_pressed()[PLAYER_MOVE_DOWN] == True:
            self.y += self.speed
            if new_rotation == -1:
                new_rotation = 180         
                
        if pygame.key.get_pressed()[PLAYER_MOVE_UP] == True:
            self.y -= self.speed
            if new_rotation == -1:
                new_rotation = 0 
        
        self.rotation = new_rotation

        #print("Player ", "x:" + str(self.x), "y: " + str(self.y))
        
    def player_interact(self):
        if pygame.key.get_pressed()[PLAYER_INTERACT] == True:
            print("checking")
            closest_object = {"obj":None, "dist":10000}
            for chest in self.chests:
                delta = (self.x - chest.x)**2
                # print(delta)
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

